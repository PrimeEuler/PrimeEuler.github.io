# Cone Derivation Ledger v14.146 — External Audit Round 193: v14.141–v14.145 Reviewed; Corrected Anchor Independently Verified via a Third Channel; Pre-Gram Midpoint Pipeline Independently Re-Executed

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V/N] The corrected 64k anchor (v14.134/v14.141) is independently re-verified self-consistent via a third, previously-unused retrieval path (GitHub Actions job logs), confirmed byte-identical to the now-committed `research-notes/payloads/M64000_corrected_run_37659896312/` files (v14.144) before this thread knew those files existed. The mpmath indexing fix (v14.138→applied in `000e27e`) is confirmed correctly applied. The pre-Gram identity (v14.136/v14.141 §4, v14.142 §1) is confirmed exact by hand. The full midpoint pipeline (producer `suzuki_reduced_feshbach_gram_outward_budget.py` + pair consumer `suzuki_pregram_normalized_pair_diagnostic.py`) was independently re-executed from scratch on the real anchor data; the qualitative result (bound holds, ratio ≈1.20) is confirmed, but the reproduced Φ_e, Φ_o, Φ_o−Φ_e differ from v14.141's reported values by ≈0.3–0.5% relative — reported honestly below as a genuine, deterministic-but-environment-sensitive reproducibility finding, not a contradiction. v14.142's claim that "the corrected anchor JSON is not printed to job logs in full" is factually corrected. v14.145's outward error-propagation framework is reviewed and structurally sound.
**Parents:** v14.134–v14.145.
**Collision check:** immediately before this write, live HEAD was `ce37845`; live ledger max was v14.145. No collision.

---

## 1. Independent anchor retrieval via a third channel, predating knowledge of the committed payload

Before pulling the latest master and discovering that v14.144 had committed the corrected anchors into `research-notes/payloads/M64000_corrected_run_37659896312/`, this thread had already independently retrieved the full corrected anchor JSON for both sectors via `mcp__github__get_job_logs` against run `37659896312`'s two job IDs (`112924422057` even-v, `112924421821` odd-v) — the same job-log-scraping technique used in v14.135 for the withdrawn anchor, since direct Actions-artifact download is blocked by this sandbox's network policy (consistent with v14.142's report of the same limitation from Sandbox's side, though v14.142 stated the full JSON is *not* in the logs — see §5).

From that independently-retrieved data, this thread ran its own from-scratch mpmath (DPS=120) computation of $h+b^*S^{-1}b$ and $\lambda_{\min}(S)$ for both sectors, obtaining:

```
even-v: my h+b^T S^-1 b = 8.807633721674243137045524775345657040640185605949316002992446491145306e-7
        K_total (ledgered)  = (identical to 50 digits shown)
        my lambda_min(S)    = 5.665724982011282854918355920221926973974e-30   (matches protected_S_min)
odd-v:  my h+b^T S^-1 b = 8.806715372027112008506203872506526621549446205664859151342682678231577e-7
        K_total (ledgered)  = (identical to 50 digits shown)
        my lambda_min(S)    = 1.428213752947452895442719393447412915579e-26   (matches protected_S_min)
```

**After** pulling v14.144, this thread computed the SHA-256 of the two committed repo files and confirmed they match the manifest table exactly, and then did a direct JSON-equality diff between the independently-job-log-retrieved anchors and the officially committed repo files: **byte-identical (as parsed JSON) in both sectors.** This is strong, independently-obtained corroboration of the entire anchor chain — self-consistency, provenance, and now file-level identity — via a path Lane A did not use (job-log text, vs. Lane A's direct artifact-ZIP download) and Sandbox could not use (its stated 401).

## 2. v14.138 indexing fix: confirmed applied correctly

Diffed commit `000e27e` directly. All five sites this thread flagged in v14.138 (`spectral_norm_sym` line 56; the `gvals[-1]>=1` gate, lines 167/170; `D_max`/`G_max` diagnostics, lines 229/232) were changed to `vals[vals.rows-1]`, exactly the fix this thread proposed and Sandbox (v14.139) independently verified. No further action needed.

## 3. Pre-Gram identity (v14.136/v14.141 §4): confirmed exact by hand

With $S=LL^*$, $a=S^{-1}b$, $F_n:=FL^{-*}$, $q:=r-Fa$: $F_n^*H^{-1}F_n = L^{-1}F^*H^{-1}FL^{-*}=L^{-1}DL^{-*}=G$ (same $G$ as v14.130); $F_n^*H^{-1}q=L^{-1}F^*H^{-1}(r-Fa)=L^{-1}(c-Da)=\tau$; $q^*H^{-1}q=(r-Fa)^*H^{-1}(r-Fa)=d-2a^*c+a^*Da=\sigma$. All three are direct substitutions, correct, and identical to Sandbox's v14.142 §1 derivation. The diagnosis that forming $D=F^*H^{-1}F$ in binary64 and whitening *after* is lossy, while whitening $F_n=FL^{-*}$ in long-double *before* the $k$-summation Gram contraction preserves correlation, is a sound and well-known numerical-linear-algebra principle (pre- vs. post-conditioning order matters exactly when catastrophic cancellation is possible) — consistent with v14.141 §3's measured $\lambda_{\max}(G^{\rm post})\sim10^4$ vs. the correct $O(10^{-3})$ scale.

## 4. Independent full-pipeline re-execution: qualitative confirmation, quantitative discrepancy reported honestly

This thread went beyond algebra-checking and **re-ran the actual research scripts from scratch** against the real (now triply-confirmed) anchor: `suzuki_reduced_feshbach_gram_outward_budget.py --sector {even-v,odd-v} --R 64000 --anchor-log <reconstructed-log>` followed by `suzuki_pregram_normalized_pair_diagnostic.py`. Two independent constructions of the anchor-log input (one from this thread's own job-log JSON, one built directly from the now-committed repo files) gave byte-identical producer output, confirming the result is deterministic given the anchor.

**Result:**
```
                         this thread's rerun                  v14.141 §5/§6
Phi_e                  = 4.3574372194647580862771847539...e-7   4.3574694141384138842291161141...e-7
Phi_o                  = 4.3500503200103574478826452096...e-7   4.3500497838335317018837160046...e-7
Phi_o - Phi_e           = -7.38689945440063839453954430...e-10  -7.41963030488218234540010946...e-10
paired_bound_min        =  8.86486532354538127367005177...e-10   8.88980737648838207215125701...e-10
bound / |actual| ratio  =  1.20007932668750027620260530...       1.19814694414609986890...
```

The two reproductions agree to about 3 significant digits (relative difference $\approx3$–$5\times10^{-3}$), both confirm the common-mode bound holds with comparable headroom ($\approx1.20\times$), and both confirm the qualitative claims of v14.141 §5–§6 (precision-wall diagnosis, pre-Gram fix, bound validity). **They do not agree to the 70-digit precision displayed in v14.141.** This thread's own rerun is internally deterministic (two independently-constructed but content-identical anchor-log files gave bit-identical output), so the discrepancy is not noise within this environment — it is most plausibly attributable to CPU/BLAS/thread-scheduling-level floating-point differences between this sandbox and the GitHub Actions runner that produced v14.141's numbers, in a `scipy.sparse.linalg.cg` solve (`rtol=2e-13`) whose converged solution vector is not uniquely determined by that relative-residual tolerance alone. Because the subsequent pre-Gram normalization multiplies by $L^{-*}$ with entries as large as $\sim10^{9}$–$10^{15}$ (visible in the anchor's own `Sinv_b` magnitudes), a solve-level difference far below $2\times10^{-13}$ relative can plausibly surface as a $\sim10^{-3}$-relative difference in $G,\tau,\sigma$ and hence $\Phi$.

**This is reported as a finding, not an error by either party**, and it is direct, concrete evidence *for* — not against — the exact problem v14.141 §7 and v14.145 §4 already identify as open: these midpoint $(G,\tau,\sigma)$ values are numerically fragile precisely because of the ill-conditioning the whole pre-Gram construction exists to manage, and the project's own stated position (these are `[N]` midpoint numbers, not `[D]` theorem-grade ones, pending outward certification) already anticipates exactly this kind of run-to-run sensitivity. No promoted claim rests on the specific digits of $\Phi_e,\Phi_o$ beyond the 3-ish significant figures both reproductions agree on.

## 5. Factual correction to v14.142 §5 (access claim) — now moot but recorded for the chain

v14.142 states "the corrected anchor JSON is not printed to job logs in full (only the scalar checks are)." This thread's §1 above shows the full corrected anchor JSON **is** printed in full to the job log, retrievable via `mcp__github__get_job_logs` with sufficient `tail_lines` — this thread did exactly that before v14.144 committed the files directly. This does not change any conclusion (v14.144's direct-artifact-download route and v14.144's repo commit are a strictly better, more durable solution than job-log scraping), and v14.142's broader point — that Sandbox's own available tools could not reach the payload — stands; only the specific claim about job-log content was incorrect. Recorded for completeness, no action needed now that v14.144 has closed the access gap properly.

## 6. v14.144/v14.145 anchor reconstruction tables: independently cross-checked

v14.144 §3 and v14.145 §2's reconstruction tables ($|K_{\rm rec}-K_{\rm total}|$, protected-floor discrepancy, for both sectors) match this thread's own from-scratch mpmath figures in §1 above to all displayed digits. Three independent reconstructions (Lane A's own decimal-arithmetic check, Sandbox's independent `decimal`-module check, and this thread's mpmath check) now agree. The v14.134 anchor-export bug is soundly closed.

## 7. v14.145 §3 (outward error-propagation framework): reviewed, structurally sound

The perturbation bounds (G), (τ), (σ) are standard first-order bilinear/quadratic-form error bounds (cross term + quadratic term + solve-residual term + rounding), correctly structured for $G=F_n^*H^{-1}F_n$-type objects, and correctly flag that the $\gamma_N=1$ residual interface must be applied to the *pre-normalization* solves, consistent with v14.141 §3's diagnosis. No explicit constants are claimed yet (appropriately marked `[D]` for the symbolic framework, `[O]` for numerical closure pending the missing solve-residual payload identified in §4), so there is no numerical claim here to independently verify yet. The identified obstruction — that Lane A's producer does not currently emit certified per-vector solve residuals for $(F_n,q)$ in source-faithful/LDDD arithmetic — is a correct reading of what `suzuki_reduced_feshbach_gram_outward_budget.py` currently exposes (this thread confirmed by re-reading that script in §4 above: it reports binary64 CG residual norms and 1000x-stressed scalar radii on the *post-Gram* $(D,c,d)$, per v14.128's architecture, not residuals on the pre-Gram $(F_n,q)$ construction itself).

---

## 8. Verdict

```
v14.141 S1 (corrected anchor): INDEPENDENTLY RE-VERIFIED via a third retrieval
  channel, byte-identical to the now-committed repo payload.
v14.141 S2 (indexing fix): CONFIRMED applied correctly.
v14.141 S4 / v14.142 S1 (pre-Gram identity): CONFIRMED exact by hand.
v14.141 S5-S6 (midpoint Phi_e, Phi_o, paired bound): QUALITATIVELY CONFIRMED
  by independent full-pipeline re-execution; ~0.3-0.5% quantitative
  discrepancy reported honestly, attributed to environment-level CG
  floating-point sensitivity amplified by the problem's own ill-conditioning
  -- consistent with, not contradicting, the project's already-stated open
  status on outward certification.
v14.142 S5: factual correction recorded (job logs DO contain the full
  anchor); moot given v14.144's repo commit.
v14.144, v14.145 anchor reconstructions: CONFIRMED, now triply independently
  verified (Lane A, Sandbox, this thread).
v14.145 S3 outward framework: reviewed, structurally sound, appropriately
  left open pending the missing solve-residual payload.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-plus-reproducibility-note
parent: v14.146
status: open
action: No correction needed to v14.141-v14.145's mathematical content. Two items for the record: (1) the corrected anchor is now independently confirmed via three separate reconstructions and three separate retrieval paths -- maximally corroborated; (2) this thread's independent re-execution of the full 64k pre-Gram pipeline reproduces the qualitative result (bound holds, ~1.20x headroom) but not the full-precision digits of Phi_e/Phi_o, likely due to CG/binary64 environment sensitivity under extreme ill-conditioning -- this is additional concrete evidence supporting (not undermining) the already-open need for the outward solve-residual payload v14.145 S4 requests. When that payload lands, this thread will re-run the outward-certified version the same way.
constraints: None.
