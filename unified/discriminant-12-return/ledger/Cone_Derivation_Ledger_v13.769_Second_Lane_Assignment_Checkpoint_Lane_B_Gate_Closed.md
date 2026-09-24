# Cone Derivation Ledger v13.769 — Second Lane Assignment Checkpoint: Lane B Gate Closed

Date: 2026-09-24

Author: external audit session (Claude Sonnet 5), by request of the project owner. Supersedes v13.760 where the two disagree; read this entry first.

Synchronization: live head checked immediately before write is v13.768 (External Audit Round 95, commit `de0fda3`). No collision.

## 0. Why this checkpoint exists

Lane B's original gate (v13.760 B.2, itself inherited from v13.736) is now closed — proven, not merely explored. This is a natural pause point for both lanes: Lane B needs a new, well-scoped target, and Lane A's status is worth restating cleanly after a batch of negative-but-useful results. Read this before starting new work in either lane.

---

## LANE B — Norm-Quotient / Idele-Class Representation

### B.0 The original gate is closed. Result: negative, and permanent.

`v13.731`'s prime-power Hilbert space (`\mathcal H_{\rm fin}=\bigoplus_p\ell^2(\mathbb N_{\ge1})`, `H_{\rm fin}e_{p,k}=k\log p\,e_{p,k}`) can **never** be unitarily identified with the canonical trivial-`C_{\mathbb Q}^1` sector `\mathcal H_{\rm norm}=L^2(\mathbb R,dr)`, `H_{\rm norm}=-i\partial_r` (v13.767, audited Round 95). The proof is elementary and airtight: unitary equivalence preserves spectral type; `H_{\rm fin}` has pure point spectrum, `H_{\rm norm}` has purely absolutely continuous spectrum. **Do not reopen this question.** No future construction of `\mathcal H_{\rm norm}` or of a "better" intertwiner can overturn it — the obstruction is about spectral type, not about the specific construction used.

### B.1 What replaced it — established, do not re-derive

- The exact centered finite-place trace: `\langle\mu_{\rm Weil}^{\rm fin},\phi\rangle=\mathrm{Tr}[A_{\rm fin}e^{-H_{\rm fin}/2}(\phi(H_{\rm fin})+\phi(-H_{\rm fin}))]` (v13.763, audited Round 94).
- The full common trace `\mathfrak T_{\rm common}=τ_{∞/0}-\mathrm{Tr}_{\rm fin}[\cdots]=\langle\mathscr W_S,\phi\rangle`, unifying the archimedean/origin package and the finite-place trace into one functional equal to Lane A's already-audited common Suzuki–Weil current (v13.767 §2–4, audited Round 95).
- The distributional replacement bridge: `U(\mu_s)=-\zeta'/\zeta(s+iH_{\rm norm})` for `\Re s>1`, obtained by functional calculus on `H_{\rm norm}` rather than by unitary identification of eigenbases (v13.767 §8, audited Round 95). This is the correct object to build on.

### B.2 The proposed next question — legitimate, but scope it correctly

The natural next question, as the source thread itself framed it, is:

\[
\boxed{
\text{Can }\mathfrak T_{\rm common}\text{ be derived directly as the regularized orbital/fixed-point trace}
}
\]
\[
\boxed{
\text{of a canonical action on the full adèle-class space }\mathbb A/\mathbb Q^\times\text{, rather than assembled from local factors?}
}
\]

This is a real and interesting question, but it is **not** a well-posed single gate the way B.2 (now closed) was. It is, in substance, Alain Connes' adele-class-space trace-formula program (Connes 1999, with 25 years of subsequent literature — Connes–Consani, Meyer's adelic BC-system work, and others) — an actively studied, still-open research direction, not a computation that collapses to a scalar estimate. Treat it accordingly:

1. **This is a research-scope target, not an incremental gate.** Do not expect it to close in a handful of entries the way the finite-place trace or the eta-positivity proof did.
2. **Anchor every claim to the actual literature.** If this direction is pursued, cite the specific construction being used (Connes' original trace formula or a specific named refinement) precisely, the way Lane A anchors claims to Suzuki's paper page-by-page. Unanchored claims of "reproducing" the adelic trace will not be accepted as established without that comparison — this auditor will check against the cited source, not just internal consistency.
3. **Watch for a specific failure mode.** The stated goal ("would close the remaining gap without contradicting the continuous-spectrum result") is coherent as written — it asks for a *different kind of object* (an orbital trace combining continuous and discrete data), not a reopening of the unitary-identification question. But if any future entry produces something that amounts to "`H_{\rm fin}` is, after all, essentially the norm-line generator," that is the exact claim B.0 already rules out, and will be flagged as such regardless of how it is dressed up.
4. **A smaller, more tractable fallback exists if the full adelic construction proves too heavy:** stay within the already-established "local adelic orbit data → norm pushforward → distributional group-algebra action" picture (v13.767 §8–9) and try to characterize *which* class of test functions or regularizations make that pushforward canonical, rather than reconstructing the whole trace formula from a geometric action from scratch.

---

## LANE A — Screw/Helix–Weil–Hermite–Biehler Program

### A.0 Status update since v13.760

Four candidate shortcuts to Schur nonresonance have now been ruled out by direct, correct argument (not by omission):
1. Bulk coercivity of `\mathcal L_A` alone (v13.761, Round 93) — controls magnitude, not phase.
2. Identification of the new feedback Fredholm determinants with Suzuki's genuine HB boundary-extension determinant (v13.765, Round 95) — no established intertwiner between source/trace feedback and boundary-condition perturbation.
3. Coupling homotopy `t\mathcal F_{\pm,A}` (v13.766, Round 95) — exactly affine, adds no leverage beyond the original scalar question.
4. Pointwise sign of Suzuki's explicit basepoint kernels (v13.766, Round 95) — the Green term `N(0,y)` provably changes sign at `|y|=A(1-1/\sqrt3)`, ruling out a pointwise-positivity argument.

Lane B's finite-place trace closure (`\mathscr W_{S,\rm fin}=-\mu_{\rm Weil}^{\rm fin}`) is confirmed **not** to bear on this question either (v13.765 §8, v13.766 §9) — the two lanes' recent results are consistent but do not solve each other's problems.

### A.1 The load-bearing open item, unchanged in substance, now sharply bounded

\[
\boxed{M_{00}>-1,\qquad M_{1x}>-1}
\]
(equivalently `|M_{00}|,|M_{1x}|<1` as a stronger sufficient form). This is now confirmed to require genuinely new information, not further formal rearrangement. v13.766 §8 lists the accurate remaining routes:
- quantitative norm/coercivity estimates strong enough to force `|M|<1`;
- a positive-compatible energy-space Riesz representation of the trace functionals `\ell_{0,A},\ell_{1,A}` (distinct from the general Banach-duality bound already established);
- direct numerical/rigorous finite-`A` evaluation of `M_{00},M_{1x}`, followed by an analytic asymptotic argument;
- an as-yet-unproved intertwiner identifying the feedback operator with a protected extension determinant.

No route is preferred a priori; pick whichever is most tractable given available tools.

---

## 1. Coordination rules (unchanged from v13.760)

Check the live ledger and latest audit round before starting. Import established results rather than re-deriving them. Label new cross-lane algebra `[X]` only after both source facts are independently established. Keep RH, Hilbert–Pólya, and unproved positivity explicitly open. On version collision, earlier UTC commit keeps the number.

---

**Checkpoint conclusion.** Lane B's original question has a real, proven, negative answer — a genuine result, not a stall. Its next step is open-ended and should be scoped as research rather than as a gate, with literature anchoring required. Lane A's open item is unchanged in substance but now much better characterized: four plausible shortcuts are closed off, and the remaining routes are concrete and enumerable rather than vague.
