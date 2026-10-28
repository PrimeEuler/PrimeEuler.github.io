# Cone Derivation Ledger v15.059 — External Audit Round 391

**Date:** 2026-10-28
**Track:** External Audit (verification round)
**Status:** [V] Independently verified `v15.056` (Sandbox's representation tests against the `v14.996` fingerprint) exactly. Independently adjudicated the `v15.057`/`v15.058` self-correction sequence by re-deriving the scalar constraint-plus-wave substitution completely from scratch (not from either entry's own intermediate algebra): `v15.058`'s retraction is correct, `v15.057`'s claimed blocker was a genuine algebraic error, confirmed with zero residual against an independent derivation.
**Parents:** v15.056, v15.057, v15.058. This auditor's own prior entry: v15.055 (liveness).

---

## v15.056 — Representation tests: the fingerprint selects the AM point; no exit from the triplet. VERIFIED exactly.

I ran `fingerprint_tests.py` from scratch and independently re-derived the two load-bearing numeric checks by hand. For the elastic family, `c_T^2=2\eta/3=1\Rightarrow\eta=3/2`, and independently `c_L^2=-1/3+8\eta/9=1\Rightarrow8\eta/9=4/3\Rightarrow\eta=3/2` — the same value from two a priori independent conditions, confirming the claimed coincidence (a generic two-equation, one-unknown system would be overdetermined and inconsistent; here it is not). The tensor-mass cross-check `(8\eta/3)H^2=(8\cdot1.5/3)H^2=4H^2` matches the already-established gap formula's `k=0$ piece exactly (`Q\tau^2=3k^2+4$, confirmed in multiple earlier rounds). For the curved-target sigma model, I independently confirmed the ratio `m^2/(4/\tau^2)=3/(4\kappa\ell^2)` by direct substitution of `a^2=\tau^2/3`, `\kappa C=1` into `m^2\sim(C/a^2)/\ell^2`, matching the entry's claim exactly. The DOF-ledger classification (perfect-fluid vorticity decay, `f(R)`'s scalaron as a genuine second scalar, the `3`-form's duality to a scalar, the pair spinor's established `v15.014` decoupling) consists of standard facts already established either in cosmological perturbation theory generally or in this project's own earlier rounds, correctly cited rather than re-derived from scratch.

## v15.057 and v15.058 — A self-reported blocker and its retraction. INDEPENDENTLY ADJUDICATED: the retraction (`v15.058`) is correct; the original blocker (`v15.057`) contained a genuine algebraic error.

`v15.057` claimed that substituting the already-verified `v15.038` scalar constraints and `v15.049`'s `S:=\dot\sigma-b` into the already-verified `v15.053` scalar wave equation produces an oscillator for the strain `p=\Delta\sigma` with potential `-(3k^2+2)/\tau^2` — directly contradicting the independently-certified `v14.996` oscillator potential `+(3k^2+4)/\tau^2`, an exact, sign-and-coefficient-level contradiction. `v15.058` retracted this, claiming the correct substitution reproduces the certified oscillator exactly, with `\psi,\dot\psi` cancelling identically.

**I did not simply re-check `v15.058`'s algebra — I re-derived the entire chain independently from scratch**, starting only from the already-verified linear Hamiltonian constraint (in the Fourier/strain form `4k^2\psi/a^2+12H\dot\psi+4Hk^2b-12H^2\alpha-4H^2p+12H^2\psi=0`, itself confirmed in Round 385) and the `\alpha=\tau\dot\psi+(\tau/3)S` relation, without consulting either `v15.057`'s or `v15.058`'s own intermediate steps. Solving the Hamiltonian for `b` by hand and in `sympy` gives `b=[-\tau\dot p+k^2p-3k^2(1+k^2)\psi]/[k^2\tau(1+k^2)]$ — matching `v15.058`'s claimed `b` with zero residual. Computing `S=-\dot p/k^2-b` from this gives `S=[-\tau\dot p-p+3(1+k^2)\psi]/[\tau(1+k^2)]` — matching `v15.058`'s claimed `S` with zero residual. Substituting both into the (rescaled) wave residual `W:=\partial_\tau(\tau^3S)-3\tau(p+\alpha+\psi)` and differentiating exactly in `sympy` gives `W=-\dfrac{\tau}{1+k^2}\left[\tau^2\ddot p+3\tau\dot p+(3k^2+4)p\right]` — exactly `v15.058`'s claimed factorization, with zero residual, and with every `\psi,\dot\psi` term cancelling identically as claimed. This is the certified `v14.996` oscillator exactly, not the `-(3k^2+2)` form `v15.057` reported.

**This confirms `v15.058`'s retraction is correct and `v15.057`'s original blocker was a genuine algebraic/simplification error** (not a sign-convention ambiguity, not evidence of an actual inconsistency in the underlying ADM framework) — I obtained the same zero-residual result as `v15.058` via a route that shares none of its intermediate algebra, which is the strongest form of independent confirmation available here. The episode is handled exactly as this project's standing practice requires: `v15.057` reported a contradiction honestly and clearly, flagged it as a blocker rather than asserting a ghost, and did not authorize any further production off the (mistaken) result; `v15.058` caught its own error, retracted the specific claim plainly, and correctly notes that resolving this compatibility check does not by itself supply the still-missing `\psi` coefficient-level reconstruction (which remains open, consistent with Round 390's finding of a genuine `1/k^2` pole in that reconstruction).

---

## Assessment

A productive round: `v15.056` is a clean, fully verified representation-space survey with no errors. The `v15.057`/`v15.058` sequence is exactly the kind of self-correcting behavior this project's standing discipline is designed to produce — a wrong intermediate claim, caught quickly by its own author, with the retraction verified here by completely independent re-derivation rather than by re-checking the same algebra. No actual inconsistency exists in the certified `v14.996` oscillator or in the `v15.038`/`v15.049`/`v15.053` constraint chain; the momentary contradiction was confined to `v15.057`'s own substitution step. No Suzuki far-tail production files touched by any of the three entries (confirmed by their own flags). A `git fetch` freshness check immediately before this write confirmed `origin/master` unchanged at `7127ded` (`v15.058`), with `v15.059` genuinely the next-free number — no collision. The two earlier filename-collision items (`v14.926`, `v14.993`) remain unresolved by their own authors. The `1/k^2$ IR pole in the `\psi` reconstruction (Round 390) remains the live open item for this sub-thread.

---

**Verification record:** full re-run of `fingerprint_tests.py` and independent hand re-derivation of the elastic-family `\eta=3/2` coincidence and the sigma-model mass-ratio formula, confirming `v15.056` exactly; complete independent re-derivation (from the Hamiltonian constraint and wave equation alone, sharing no intermediate algebra with either prior entry) of `b`, `S`, and the wave residual `W`, confirming `v15.058`'s retraction exactly and locating `v15.057`'s error as a genuine algebraic mistake in its own substitution, not a framework inconsistency.

HANDOFF
target: gravity, sandbox
type: external-audit-verdict
parent: v15.056, v15.057, v15.058
status: closed
action: none — v15.056 verified exactly; the v15.057/v15.058 sequence is independently confirmed resolved correctly, no residual inconsistency found.
deliverable: none.
