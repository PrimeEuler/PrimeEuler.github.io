# Cone Derivation Ledger v13.892 — Sandbox: Quantization Exploration (Map, Not Flag)

**Date:** 2026-10-01
**Track:** Sandbox (our Lane B exploratory track)
**Status:** [I]/[O] exploratory throughout; [N] pilot numerics; [D] where noted
**Authorization:** Jeremy, 2026-10-01 ("yes both")
**Predecessors:** v13.891 (selector derived); Road 2 / Suzuki (background main line)

---

## Question

Jeremy: "could this spring be our Hilbert–Pólya operator?" We have a
CLASSICAL system (compression spring) with zero FREQUENCIES. H-P needs a
SELF-ADJOINT OPERATOR with zero EIGENVALUES. This entry maps the
quantization territory — five directions explored, none claiming the
operator.

## Direction 1: Berry–Keating, discrete [I]/[O]

Genuine resonance: Σ_{n≤E} d(n) ~ E log E matches the BK Weyl law — our
divisor dynamics on hyperbolas xy=n is the discrete cousin of BK's xp=E.
But inherits the known regularization wall (continuous spectrum,
cutoff-dependence). Does not break it.

## Direction 2: Trace formula [I]/[O]

Structurally the correct framework (geometric side ↔ spectral side).
New observation: in the twisted explicit formula, χ(p)^k is a **holonomy**
— a flat line bundle over the primes. This is v13.887's "two selection
axes" in trace-formula language: geometry stages WHERE, the character's
holonomy selects WHICH SPECTRUM. Does not construct H (inverse problem).

## Direction 3: Koopman [I]/[O]

The Cayley-transform route (unitary → self-adjoint) is formally correct
but **circular** (U defined from the data it would explain). The
non-circular Ruelle/Mayer transfer-operator route is real mathematics
but yields *Selberg* zeros, not Riemann. **Ruled out as a proof route.**
Mayer numerics proposed only as method validation.

## Direction 4: Suzuki bridge — FRONT-RUNNER [N]/[I]

Pilot numerics: prime-sum-only anchored kernels are **indefinite** for
both Λ-weights (48 negative eigenvalues) and indicator-weights (49
negatives) on (−6,6). The **archimedean term is load-bearing** — the
primes alone do not carry positivity. Consistent with Suzuki's
architecture (his g(t) needs the full archimedean + prime structure).

Blocked on: a Lerch-term bracketing ambiguity in Suzuki's text and F(t)
series convergence (|t|<π). Specified as the concrete next step, not a
refutation. (Suzuki's exact screw extracted from 2606.09096v2.pdf,
including the pole term −4(e^{t/2}+e^{−t/2}−2) whose omission sank
v13.881.)

**Honest caveat:** even indicator-positivity would NOT inherit Suzuki's
RH-equivalence theorem — it would need a new theorem. This feeds Road 2;
it does not replace it.

## Direction 5: Positivity [D]/[I]

d(gcd(m,n)) is positive-definite [D] (Gram matrix via d = 1∗1) — but no
known link to zeros. Proposed as cheap numerics, likely negative,
valuably so. The compression-Weil-criterion idea has a **broken logical
implication** (b≤Λ pointwise ⟹ nothing for quadratic forms) — **ruled
out**.

## Ranked next steps [O]

1. **Suzuki stability test** — implement full g(t), calibrate PSD on Λ
   (must hold by Suzuki's theorem), test indicator weights,
   θ-interpolate tracking the smallest eigenvalue. Fully specified
   protocol. **Launched as follow-up.**
2. Twisted Weil formula as holonomy / flat-bundle Hilbert space.
3. Mayer transfer-operator numerics vs Selberg zeros (method validation).
4. gcd-kernel spectrum numerics.
5. Discrete BK finite-section (expect cutoff-dependence).

## Debugging note [N]

An early interpolation bug (non-monotonic |t| grid into np.interp)
produced spuriously PSD kernels; caught via row-constancy check, fixed
with sorted-unique grid. Recorded in the exploration doc so it is not
repeated.

## Files (sandbox)

- `~/workspace/d12/lane_b/sandbox/runs/20260930-divisor-tension/quantization_exploration.md`
  (16KB, full math, [D]/[N]/[I]/[O] labels, ranked next steps)

---

**Creed check:** The cone selects frequencies (derived, v13.891). The
OPERATOR that would make them eigenvalues is not constructed here — this
is a map of five routes with one front-runner (Suzuki bridge) and two
ruled out (Koopman-proof, compression-Weil). The spring is the classical
limit; H-P remains the quantization. Shown honestly; no flag planted.
