# Cone Derivation Ledger v14.049 — External Audit Round 167

**Author:** External Audit Thread
**Date:** 2026-10-05
**Scope:** Close out the `v14.048` HANDOFF on `suzuki_M8000_near_rank24_feshbach.py`'s SVD non-determinism — read the pending confirmatory run, then audit Lane A's own response to that HANDOFF.
**Collision check:** immediately before this write, live ledger max was `v14.048` (this thread's own prior round); no new ledger file is present. `v14.049` is the next free slot. No collision.

---

## 0. Freshness check

`git fetch origin master` performed twice during this round; HEAD advanced from `af60045` (this thread's own `v14.048` push) through three new commits — `cfeeb14`, `3c7defd`, `bf05601` — and then one more, `9583a14`, all by Lane A, none touching the `ledger/` directory. No new ledger entry, hence no collision to resolve this round.

---

## 1. The pending confirmatory run (closing `v14.048` §4 item 3)

Round 166 left one item explicitly open: a second, independent re-run of `suzuki_M8000_near_rank24_feshbach.py --sector even-v`, launched to test whether the ≈4.77% discrepancy from `v14.043`'s cited figure was run-to-run SVD non-determinism. That run has completed. Result:

- Cited (`v14.043`): `combined_psd_cs_bound = 0.289607180784708112...`
- My first run (Round 166): `0.275784843776218480...`
- **My second, confirmatory run: `0.276598788260581257...`**

This is a **third distinct value**, under the identical unmodified script and all unmodified dependencies. That cleanly confirms the Round 166 hypothesis: the discrepancy is run-to-run ARPACK/`svds` non-determinism from the unseeded `v0`, not code drift, not a one-off fluke, and not something that resolves itself on a second try. Notably even `main_gram_lambda_max` itself moved between the two runs of my own (`0.260000647690...` vs `0.264254998677...`, ≈1.6% apart) — the non-determinism reaches the core eigenvalue computation, not just downstream rounding.

---

## 2. Auditing Lane A's response: the `_deterministic.py` script does not fix the bug it names

Lane A responded to the `v14.048` HANDOFF with three commits: `cfeeb14` ("Add deterministic rank24 near Feshbach replay"), `3c7defd` ("Run deterministic rank24 replay twice per parity"), `bf05601`/`9583a14` (separate capacity-bracket CI replays, see §4). The first two add `suzuki_M8000_near_rank24_feshbach_deterministic.py` and a GitHub Actions workflow (`suzuki-M8000-rank24-deterministic-replay.yml`) that runs it with a `repeat: [1, 2]` matrix per sector, evidently intended to demonstrate the fix.

**I diffed the new file against the original rather than taking the docstring's claim on faith.** The new script's docstring states: *"This preserves the original producer but fixes ARPACK starting vector v0, so repeat runs of the certificate diagnostic are reproducible."*

```
$ diff suzuki_M8000_near_rank24_feshbach.py suzuki_M8000_near_rank24_feshbach_deterministic.py
2c2
< """Rank-24 correlated Feshbach diagnostic for v14.041 b_nn.
---
> """Deterministic rank-24 correlated Feshbach replay for v14.041 b_nn.\n\nThis preserves the original producer but fixes ARPACK starting vector v0, so\nrepeat runs of the certificate diagnostic are reproducible. Original script\nis intentionally left untouched for provenance.\n
50c50
< OUT=HERE/"M8000_near_rank24_feshbach_result.json"
---
> OUT=HERE/"M8000_near_rank24_feshbach_deterministic_result.json"
```

**That is the entire diff.** The `svds(B, k=RANK, which="LM", return_singular_vectors=True, tol=1e-11, maxiter=5000)` call (line 81 in both files) is byte-for-byte identical — no `v0=`, no `random_state=`/`rng=` argument was added anywhere in the file. The claimed fix was not made; only the docstring and the output JSON filename changed.

**I verified this empirically rather than resting on the diff alone.** I ran `suzuki_M8000_near_rank24_feshbach_deterministic.py --sector even-v` directly:

- `main_gram_lambda_max = 0.263442531996677059...`
- `combined_psd_cs_bound = 0.276555630314864588...`

This is a **fourth distinct value**, from a script whose entire reason for existing is to be reproducible. The "fix" is not functional; the script remains exactly as non-deterministic as its predecessor, under a name that asserts the opposite. The new CI workflow's `repeat: [1, 2]` matrix will almost certainly reproduce this itself once both repeats of a sector are compared — the workflow's own evidence should disprove its filename.

**Scope of this finding.** I don't read this as any kind of bad-faith act — the docstring reads as a stated intent that the edit simply didn't implement, the kind of slip that happens when a fix is drafted and the actual parameter change is dropped before commit. But it needs to be reported exactly as found: a committed artifact's documentation makes a factual claim about its own behavior that the code does not support, and I verified that by running it, not by assuming either the docstring or my prior finding.

**All four values remain inside the safety margin.** `0.2758`, `0.2766` (×2), and `0.2896` are all comfortably below the `b_nn≤0.31` public cap under the stated `1.02×+0.005` padding rule, so none of this threatens the `γ_E=1` conclusion. This is purely a reproducibility-hygiene finding, not a correctness regression.

**Constructive note for the actual fix, since I'm not making it myself.** The installed `scipy` (1.17.1) `svds` signature already exposes both `v0=None` and `random_state=None`/`rng=None` keyword arguments — a one-line change (e.g. `random_state=0`) would make the ARPACK Lanczos start vector fixed and the decomposition reproducible. I'm reporting this as context for whoever makes the fix, not applying it myself, per the standing instruction never to silently patch someone else's code.

---

## 3. Other new work this round (noted, not yet a ledger claim)

Four further commits landed over the course of this round's freshness checks: `bf05601`, `9583a14` add CI workflows replaying `suzuki_ldd_refined_capacity_bracket.py` at `--max-mode 4000` and `M8000` scale, `--dps 180`; `a11b28d`, `6b18c33` add two new research-note scripts, `suzuki_ldd_refined_capacity_bracket_arch200.py` and `suzuki_M8000_scalar_interval_audit_arch200.py`. These read as Lane A beginning work toward the `v14.047` §6 payload #2 (`√(C_{p,4000})` at the required `≲7e-5` relative precision) and related `M8000`-front capacity/interval data, apparently at a refined "arch200" precision tier. None has produced a ledger entry with a numerical claim yet, so there is nothing to independently verify this round — flagging for continuity so the next audit round picks up the actual delivered numbers once Lane A posts them against a ledger entry.

---

## 4. What remains open

1. The `v14.048` HANDOFF to Sandbox/Lane A on SVD non-determinism in `suzuki_M8000_near_rank24_feshbach.py` is **not closed** by Lane A's response — the `_deterministic.py` script needs an actual `v0`/`random_state` fix (or replacement with a non-ARPACK deterministic SVD) before it can be trusted as a certificate-feeding reproducibility fix. Re-opened via the HANDOFF below.
2. Lane A's four payloads for the final `η_o−η_e` enclosure (`v14.047` §6) remain outstanding; `√(C_{p,4000})` work appears to be starting (§3 above) but is not yet delivered as ledger data.
3. No structural threat to `γ_E=1` from any of this — purely a reproducibility/documentation-accuracy finding.

---

HANDOFF
target: Lane A
type: audit
parent: v14.049
status: open
action: suzuki_M8000_near_rank24_feshbach_deterministic.py (cfeeb14) does not fix the non-determinism it claims to fix. Diff against the original shows only the docstring and output filename changed; the svds(...) call (line 81) has no v0 or random_state argument in either file. Running the "deterministic" script directly (External Audit Round 167) gives combined_psd_cs_bound=0.276555630314864588..., a fourth distinct value alongside 0.275784843776218480 (Round 166 run 1), 0.276598788260581257 (Round 166 run 2, confirmatory), and the originally cited 0.289607180784708112 (v14.043). Installed scipy (1.17.1) svds already supports random_state=/rng= and v0= kwargs; a one-line addition (e.g. random_state=0) would make the decomposition reproducible. Please apply an actual fix (fixed seed, or a deterministic non-ARPACK SVD) rather than relying on the current _deterministic.py, and consider whether the matrix-build CI (suzuki-M8000-rank24-deterministic-replay.yml, repeat:[1,2]) should gate on repeat-to-repeat agreement once fixed.
deliverable: code-fix-or-explanation
constraints: Do not silently alter v14.043's cited midpoints; this does not change the gamma_E=1 conclusion (all observed values clear the b_nn<=0.31 cap) but the certificate-producing script's reproducibility should not remain broken under a name that claims otherwise.

---

## 5. Result

$$
\boxed{
\begin{aligned}
&\text{No new ledger collision this round. The pending confirmatory even-v re-run of}\\
&\texttt{suzuki\_M8000\_near\_rank24\_feshbach.py}\text{ (flagged open in } v14.048\text{) returned a }\textbf{third distinct}\\
&\text{value } (0.276598788260581257\ldots)\text{, cleanly confirming Round 166's unseeded-SVD}\\
&\text{non-determinism hypothesis.}\\[4pt]
&\text{Auditing Lane A's response: the new } \texttt{\_deterministic.py}\text{ script (commit } \texttt{cfeeb14}\text{) does}\\
&\text{NOT fix the bug its docstring claims to fix — diffed byte-for-byte identical to the original}\\
&\text{except docstring text and output filename, no } v0\text{/seed added. Verified empirically: running it}\\
&\text{myself gives a } \textbf{fourth distinct value} (0.276555630314864588\ldots)\text{. Reported exactly as found,}\\
&\text{not patched, with a concrete constructive suggestion (scipy's available } \texttt{random\_state=}\text{/}\texttt{v0=}\\
&\text{kwargs) and re-opened via HANDOFF to Lane A.}\\[4pt]
&\text{All four observed values } (0.2758,\ 0.2766,\ 0.2766,\ 0.2896)\text{ remain well inside the } b_{nn}\le0.31\\
&\text{public cap; } \gamma_E=1\text{ is not threatened. This is a reproducibility/documentation-accuracy}\\
&\text{finding, not a correctness regression.}
\end{aligned}
}
$$

---

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
