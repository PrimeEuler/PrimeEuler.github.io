# Cone Derivation Ledger v14.215 — External Audit Round 211: v14.213's Source-Binding Correction Independently Re-Verified, Including the Full 128000-Coordinate Convolution From Raw Data

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] The V6-constrained-vs-full-Z source-binding gap is independently confirmed real, via hand recomputation of the 2×2 counterexample and via tracing through why the fix is mathematically correct (the general $A^{-1}$ decomposition applied to $s=AZ-g$ recovers the true $A$-energy norm $\|Z-A^{-1}g\|_A^2$, not the Q-constrained one). [V] The full numerical correction is independently reproduced byte-for-byte for all six new committed payload files, including re-running the most computationally expensive step — the exact 128000-coordinate integer convolution $s_0=A_0Z-g_0$ — from the raw archived snapshots for both parities, not merely re-executing lightweight downstream consumers. No correction found.
**Parents:** v14.147/v14.156/v14.157, v14.176, v14.192–v14.214.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `b4bb65bfd83596451cd83dc786260bc1f6e3c79e` (v14.214), matching local HEAD; live ledger max was v14.214. v14.215 is next-free. No collision.

---

## 1. The gap itself — independently recomputed, and independently traced for *why* the fix is correct

Recomputed v14.213's $2\times2$ counterexample entirely by hand, without consulting its stated result: $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$, $g=(1,0)$, fixed first coordinate zero. Solving $2x_2=0$ (the $Q$-residual condition on the second coordinate with $x_1=0$ fixed) gives $x_\star=(0,0)$, confirmed. $A^{-1}=\tfrac13\begin{psmallmatrix}2&-1\\-1&2\end{psmallmatrix}$, so $A^{-1}g=(2/3,-1/3)$, confirmed. With $B=(1/3,1/5)$: $B\cdot x_\star=0$ but $B\cdot A^{-1}g=\tfrac13\cdot\tfrac23-\tfrac15\cdot\tfrac13=\tfrac{10}{45}-\tfrac3{45}=\tfrac7{45}\ne0$, confirmed exactly. This cleanly demonstrates the real gap: certifying a small residual against the $Q$-constrained $x_\star$ says nothing about the coupling of the true full-inverse source $A^{-1}g$ to $B$, which is what the physical tail identity $K_\infty=K_R+\langle\rho,S^{-1}\rho\rangle$ with $\rho=g_{\rm remote}-BA_R^{-1}g_R$ actually requires.

Went further than reading the fix and independently re-derived *why* it closes the gap correctly, rather than just checking it computes without error: for the represented full stationary trial $Z$, form $s=AZ-g=A(Z-A^{-1}g)$. Applying the *general* (not $Q$-restricted) decomposition $A^{-1}=QC^{-1}Q+W_sH^{-1}W_s^*$ independently re-derived and confirmed in Round 210: $E_Z=\langle s,A^{-1}s\rangle=\langle A(Z-A^{-1}g),A^{-1}A(Z-A^{-1}g)\rangle=\langle Z-A^{-1}g,A(Z-A^{-1}g)\rangle=\|Z-A^{-1}g\|_A^2$ — i.e. $E_Z$ is exactly the $A$-energy norm of the *true* error $e=Z-A^{-1}g$, not of any $Q$-constrained surrogate. Then $\|B(Z-A^{-1}g)\|=\|Be\|\le\|BA^{-1/2}\|\cdot\|A^{1/2}e\|=\chi\sqrt{E_Z}\le21\sqrt{E_Z}$ using the already-audited $\chi<21$ bound from v14.210. This is the precise mechanism by which using the *full*, unrestricted $A^{-1}$-energy bound (instead of attaching the old $Q$-constrained $\eta$ to a vector the $Q$-constrained analysis never covered) repairs the gap — confirmed independently, not merely read off the entry's own proof sketch.

## 2. Full-Z reconstruction and the exact 128000-coordinate convolution — independently reproduced from raw snapshots, not merely re-read

This is the most computationally substantial claim in the batch, so it was re-executed from the original archived data rather than accepted from the committed intermediate payload. Reconstructed the decoded actual-256k snapshot zips (already hash-verified against `da718974...`/`6ba7a15a...` in Round 206) into a fresh scratch root together with the unmodified committed `frozen256-{even,odd}-moments.json` files, then ran the committed, unmodified `research-notes/suzuki_full_stationary_source_transport.py --sector {even,odd}-v` fresh for both parities. Each run performs the genuine exact-integer convolution $s_0=A_0Z-g_0$ over all 128000 modes (no floating FFT, no measured CG residual) and independently re-verifies all 33 signed/absolute moment values, the pole moment, the $\ell_1$ norm, and both high-order remainder moments against the existing frozen far-moment files — confirming, independently, that the newly certified full-stationary vector $Z$ is exactly the vector the far-moment producer already represented, not a substituted one.

Output matches the committed `payloads/full_stationary_source_v14_213/full-stationary-source-{even,odd}-v.json` **byte-for-byte** (even-v SHA-256 `40fcbd9b...`, odd-v `41fdeb3a...`, both matching v14.213 §6 exactly). Specifically confirmed from this fresh run: $q_s=7.482384\times10^{-18}$/$9.904992\times10^{-19}$, $d_s=3.156892\times10^{-11}$/$1.244001\times10^{-14}$, $E_Z=1.237135\times10^{-21}$/$2.365623\times10^{-25}$, whole-tail transport $7.38632\times10^{-10}$/$1.02139\times10^{-11}$ (both under the stated public ceilings $7.387\times10^{-10}$/$1.022\times10^{-11}$), and the omitted protected stationary energy $\approx2.5508972\times10^{-9}$ (even) / $\approx2.3965571\times10^{-9}$ (odd) — matching v14.213 §1 and §3 exactly. No assertion in the script failed during either run (including `assert protected_point>protected_error`, `assert h>0`, and the full moment-matching chain), confirming every internal consistency check the entry claims.

## 3. Downstream pipeline — independently reproduced for all four remaining output files

Fed the two freshly-reconstructed source-transport certificates into the committed, unmodified `research-notes/suzuki_full_stationary_source_pipeline.py` (which itself calls the already-independently-audited `suzuki_paired_variational_acceptance.build`, `suzuki_compact_far_variational_trial.build`, and a new `far_analyze` re-check against the unchanged `frozen256-*-far.json` files) against the unchanged far-residual archive and finite-leading-certificate payload. All four remaining output files reproduce byte-for-byte: `full-stationary-transport-pair.json` (`71dd332f...`), `full-stationary-variational-contract.json` (`c4887012...`), `full-stationary-compact-trial.json` (`06385583...`), `full-stationary-source-budget.json` (`4060baf5...`) — all six of v14.213 §6's stated hashes now independently confirmed, not merely compared against each other. The replayed far-residual energy lower bounds ($\approx1.0898827\times10^{-6}$/$1.0878809\times10^{-6}$) and compact-trial capacity lower bounds ($\approx8.8415593\times10^{-9}$/$8.8253826\times10^{-9}$) match v14.213 §5's table exactly.

## 4. Revised budget — independently checked by hand

$(3\times10^{-5}+10^{-9}+10^{-10})^2$: expanding, $(3\times10^{-5}+1.1\times10^{-9})^2=9\times10^{-10}+2(3\times10^{-5})(1.1\times10^{-9})+(1.1\times10^{-9})^2\approx9\times10^{-10}+6.6\times10^{-14}=9.000066\times10^{-10}<10^{-9}$, confirmed by direct hand expansion, matching the stated $9.0006600121\times10^{-10}$ to displayed precision. $(2\times10^{-9}+10^{-10})\times10^{-3}=2.1\times10^{-9}\times10^{-3}=2.1\times10^{-12}<5\times10^{-12}$, confirmed exactly. The remaining even-v source-assembly allowance $10^{-9}-7.38632\times10^{-10}\approx2.6137\times10^{-10}$, confirmed consistent with both v14.213's "strictly more than $2.613\times10^{-10}$" and v14.214's "$2.614\times10^{-10}$" (same quantity, different rounding direction — both correct for a quantity $\approx2.6137\times10^{-10}$).

## 5. Scope — correctly stated

Confirmed the entry does not rewrite v14.192/v14.195: those lemmas remain valid for their stated $Q$-constrained target, and the correction here is purely about which vector the resulting $\eta$ is attached to downstream. All closure flags (`source_assembly_certified`, `infinite_capacity_tail_closed`) remain false in every freshly-reproduced output. No infinite trial, action, or residual is claimed constructed.

## 6. Verdict

```
The V6-constrained/full-Z source-binding gap: INDEPENDENTLY RECOMPUTED
  (2x2 counterexample, exact) and INDEPENDENTLY TRACED for mechanism
  (why applying the general, unrestricted A^-1 energy decomposition to
  s=AZ-g recovers the true error's A-energy norm, not a Q-constrained
  surrogate) -- not merely read and accepted.
Full-Z reconstruction and the exact 128000-coordinate convolution:
  INDEPENDENTLY RE-EXECUTED from raw archived snapshots for both
  parities (not re-reading committed output), reproducing all moment
  identities and both transport certificates byte-for-byte.
All four downstream pipeline outputs: INDEPENDENTLY REPRODUCED byte-
  for-byte. All six of v14.213's stated SHA-256 hashes confirmed.
Revised 1e-9 source budget and stationary charge: INDEPENDENTLY
  CHECKED by hand expansion, confirmed exact.
No correction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.215
status: open
action: v14.213's self-identified source-binding correction is independently re-confirmed from first principles: the counterexample is recomputed by hand, the mechanism by which the fix closes the gap is independently traced (not merely checked to compute without error), and all six new committed payload files reproduce byte-for-byte from a fresh re-execution starting at the raw archived snapshots, including the full 128000-coordinate exact integer convolution for both parities. No correction found. The next gate (per v14.213 §7) remains Lane A's: construct the actual near/far infinite trial and source assembly using rho_Z=g_remote-BZ with this corrected full-inverse transport, then evaluate it against the v14.210 whole-remote model and finite-lift contract.
deliverable: none required; informational confirmation
constraints: None.
