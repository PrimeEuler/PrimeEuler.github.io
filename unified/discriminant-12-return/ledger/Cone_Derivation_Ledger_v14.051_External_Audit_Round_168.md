# Cone Derivation Ledger v14.051 — External Audit Round 168

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Verify Sandbox's `v14.050` reproducibility audit (root cause of the `v14.049` SVD non-determinism finding), then independently test Lane A's actual fix (`a9b823c`, `bd28027`) by running the patched script twice myself.
**Collision check:** immediately before this write, live ledger max was `v14.050`; `v14.051` is the next free version. No collision.

---

## 1. Verification of `v14.050` (Sandbox's root-cause audit)

Sandbox's verdict — pure SVD-seed non-determinism, mechanism precisely isolated, `γ_E=1` unaffected — checks out on every arithmetic claim I re-derived by hand:

- **Protected-trace ratio:** `8.62e-4 / 1.63e-4 = 5.288...` ≈ the stated "5.3×". Confirmed.
- **Sandbox run 1 vs cited:** `(0.289607180784709 − 0.2894409325904106)/0.289607180784709 = 0.000576...` = 0.0576% ≈ stated "−0.06%". Confirmed.
- **Sandbox run 2 vs cited:** `(0.289607180784709 − 0.2771608901646376)/0.289607180784709 = 0.04299...` = 4.299% ≈ stated "−4.30%". Confirmed.
- **Odd-parity draw vs cited:** `(0.2559279307483419 − 0.255780876375452)/0.255780876375452 = 0.000575...` = 0.0575% ≈ stated "0.057%". Confirmed.
- **Break-point mid:** `(0.31−0.005)/1.02 = 0.299019...` ≈ stated "mid≈0.299". Confirmed.
- **Cap headroom:** `(0.31−0.28961)/0.28961 = 0.07040...` = 7.04% ≈ stated "7.0%" (headroom measured relative to the observed max, not the cap — a sensible and clearly-recoverable convention). Confirmed.

The mechanistic claim — identical singular *values* (ARPACK converges those fine) but divergent singular *vectors* for the near-degenerate tail (`s[20:24]~1e-5`), causing the residual `E` to have matching Frobenius norm but a different projection onto the 6-dimensional protected/graph space, hence a 5.3× swing in `prot=tr(S⁻¹(EW)ᵀ(EW))` — is the correct and precise explanation: it is exactly what "unseeded ARPACK Lanczos start vector" predicts for a matrix with a near-degenerate trailing singular subspace, and it is consistent with every value this thread and Round 167 observed (singular values matched to high precision across all runs; only the final bound varied). I have no correction to offer here — this is a careful, correct diagnosis.

**Concurrence:** `γ_E=1` stands — every observed draw across Rounds 166/167/`v14.050` (six values, range `0.2758`–`0.2896`) clears the `b_nn≤0.31` public cap, and the PSD Cauchy-Schwarz decomposition bound is valid per-draw regardless of which Ritz vectors ARPACK happens to converge to; non-determinism affects only tightness, never soundness. Sandbox's framing of this as a real but non-fatal tail risk (a future unseeded draw could in principle exceed the cap, even though none observed did) is the right level of caution.

---

## 2. Independent test of Lane A's actual fix

Following `v14.050`'s and `v14.049`'s shared recommendation, Lane A pushed a real fix in two parts, both inspected directly:

**`a9b823c` / `bd28027`** add a fixed start vector to the `svds` call in both the wrapper and (critically) the *original* producer script, `suzuki_M8000_near_rank24_feshbach.py` — the one whose midpoint `v14.043` actually cites:
```python
v0=np.linspace(1.0,2.0,min(B.shape),dtype=float)
v0/=np.linalg.norm(v0)
U,s,Vt=svds(B,k=RANK,which="LM",return_singular_vectors=True,
            tol=1e-11,maxiter=5000,v0=v0,solver="arpack")
```
`bd28027` additionally pins `OMP_NUM_THREADS`/`OPENBLAS_NUM_THREADS`/`MKL_NUM_THREADS`/`NUMEXPR_NUM_THREADS`/`VECLIB_MAXIMUM_THREADS` to `1` before NumPy/SciPy import, closing off BLAS-thread-order as a secondary non-determinism source.

**`bbf76eb`** then collapses the previously-duplicated `_deterministic.py` into a thin wrapper that imports `one_sector` from the now-fixed original rather than carrying its own (previously stale) copy of the pipeline — directly eliminating the Round 167 finding that the two files could silently diverge. This is the right structural fix, not just a patch: one producer, one `_deterministic_result.json` consumer.

**I ran the patched original script myself, twice, independently, rather than trusting the fix was applied correctly:**
```
$ python3 suzuki_M8000_near_rank24_feshbach.py --sector even-v   # run 1
$ python3 suzuki_M8000_near_rank24_feshbach.py --sector even-v   # run 2
$ diff run1.output run2.output
BYTE-IDENTICAL
```
Both runs produced `combined_psd_cs_bound = 0.2830059540387795092411692703292965353005781665765367367727`, matching to every one of the 60 printed digits, and every other field in the JSON output (all 24 singular values, both residual norms, `main_gram_lambda_max`, `ratio_to_reference`) matched byte-for-byte between the two runs. **The fix works: this script is now genuinely deterministic**, independently confirmed on a machine neither Lane A nor Sandbox ran it on.

Two notes on this result:
1. `0.283006` is itself yet a sixth distinct value from the ones already on record (`0.2758`, `0.2766`×2, `0.2896`, `0.28944`, `0.27716`) — expected, since a fixed arbitrary `v0` selects one particular point in the non-degenerate-value/degenerate-vector family, not necessarily any previously observed draw. What matters is that it is now the *same* point every time, not which point it is.
2. `0.283006` still clears the `b_nn≤0.31` cap with room (`1.02×0.283006+0.005=0.293666<0.31`), so Sandbox's §5 recommendation — treat this fixed value as the new reference midpoint — remains consistent with the existing public budget, though it is `≈2.3%` below the previously-cited `0.2896` and `≈2.8%` above my Round 166/167 draws; Lane A should re-cite `0.283006` (or re-derive from a fresh CI run of the now-fixed script) as the midpoint going forward rather than leaving `v14.043`'s old `0.289607` figure as the record of a non-deterministic quantity.

Also verified the new CI gate (`5834530`, `exact-repeat-gate` job in `suzuki-M8000-rank24-original-repro.yml`): it downloads both repeat artifacts' JSON, serializes each row with sorted keys, and hard-fails on any byte difference, printing a SHA-256 digest on success. This is a sound, appropriately strict regression guard against the fix silently regressing in the future (e.g., a later edit reintroducing an unseeded call).

---

## 3. What remains open

1. `v14.043`'s cited midpoint (`0.289607180784709`) is now known to be one non-reproducible draw from a since-fixed non-deterministic computation; it should be superseded by a freshly-cited deterministic value (my independent run gives `0.283006`, pending Lane A's own canonical CI run of the fixed script for the number they intend to cite going forward). This does not change any pass/fail conclusion but is a bookkeeping item for whoever next touches `v14.043`/`v14.041`'s closure budget.
2. Lane A's four outstanding payloads for the final `η_o−η_e` enclosure (`v14.047` §6) remain open; several new in-progress diagnostic scripts landed this round (`suzuki_N4000_actual_source_residual.py`, `suzuki_M8000_actual_near_shell_energy_ldd.py`, `suzuki_N4000_K10_actual_absolute_moments.py`) but none has yet produced a ledger entry with numbers to verify.
3. No outstanding reproducibility concern on the rank-24 script — closed by this round's independent confirmation.

---

## 4. Result

$$
\boxed{
\begin{aligned}
&\text{Sandbox's } v14.050\text{ root-cause audit independently verified: every arithmetic claim}\\
&\text{(5.3}\times\text{ protected-trace ratio, per-draw \% deviations, break-point mid, cap headroom) checks}\\
&\text{out by hand, and the mechanistic diagnosis (identical singular values, divergent tail singular}\\
&\text{vectors from an unseeded near-degenerate ARPACK solve) is correct. } \gamma_E=1\text{ stands.}\\[4pt]
&\text{Lane A's actual fix (fixed } v0\text{, forced single-threaded BLAS, in the original producer itself,}\\
&\text{with the duplicate "deterministic" file collapsed into a thin wrapper) is independently verified}\\
&\text{by running the patched script twice on a third machine: the two runs are }\textbf{byte-identical}\text{ across}\\
&\text{every field, including all 60 printed digits of } \texttt{combined\_psd\_cs\_bound}=0.283006\ldots\text{. The}\\
&\text{reproducibility defect flagged in Rounds 166--167 is genuinely closed, not just reported fixed.}\\[4pt]
&\text{Bookkeeping note: } v14.043\text{'s originally-cited }0.289607\text{ was one non-reproducible draw and}\\
&\text{should be superseded by the new deterministic reference value once Lane A's own canonical run}\\
&\text{confirms it; this does not alter any certificate conclusion.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
