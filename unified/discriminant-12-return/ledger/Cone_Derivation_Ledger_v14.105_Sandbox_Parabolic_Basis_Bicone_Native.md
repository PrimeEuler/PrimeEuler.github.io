# Cone Derivation Ledger v14.105 — Sandbox: Parabolic Basis Is Bicone-Native (A_z,L_z Eigenbasis)

**Date:** 2026-10-07
**Track:** Sandbox (Jeremy)
**Status:** Framing clarification strengthening v14.099. Nothing published.
**Parents:** v14.099, v14.101, v14.104.

---

## 1. The point (Jeremy)

The parabolic basis functions $|n_1n_2m\rangle$ used in v14.099's
$|C|/a_0$ derivation can be derived from the cone itself --- the whole
thing is parabolic slices.

## 2. Why it holds

The Stark exploration (sandbox) showed: the simultaneous
$(A_z,L_z)$ eigenbasis **is** the parabolic basis, with
$A_z=J_z-K_z$ the Stark operator built directly from the bicone's
$su(2)\oplus su(2)$ ($J$ on cone 1, $K$ on cone 2).

Hence $|n_1n_2m\rangle$ are **algebraic eigenstates of the cone's
$so(4)$** --- not Schrödinger solutions imported from elsewhere.
Their position-space forms coincide with the parabolic-coordinate
Schrödinger solutions, but the *basis itself* is cone-native:
diagonalizing $(A_z,L_z)$ on the bicone yields the parabolic states
with no differential equation solved.

## 3. What this changes vs. v14.101

v14.101 (audit) correctly noted the parabolic *wavefunctions*
$\psi_{n_1n_2m}(\xi,\eta,\phi)$ satisfy Schrödinger's equation, and
cautioned against "zero Schrödinger input" as a paper claim. That
caution stands for the *functions*.

This entry records the stronger structural fact: the *states*
$|n_1n_2m\rangle$ are defined by the bicone algebra
($(A_z,L_z)$ eigenvalues), independent of any wave equation. The
coincidence of their $\xi\eta\phi$-forms with Schrödinger solutions
is a consequence of the $so(4)$ dynamical symmetry, not an input.
The paper wording adopted: "the parabolic basis is the bicone's
$(A_z,L_z)$ eigenbasis; the matrix element follows in the natural
parabolic $SO(4,2)$ representation, with no spherical radial solution
and no Gordon/hypergeometric integral."

## 4. Verdict

Framing strengthened, no numerics altered. The $|C|/a_0=256/(243\sqrt2)$
derivation in v14.099 now rests on cone-native algebraic states
throughout: bicone ladder algebra ($\sqrt3$ form) $\times$ bicone
$(A_z,L_z)$ eigenbasis (parabolic scale). Credit to Jeremy for the
bicone construction and this observation.

---
*Sandbox exploratory. Per-item Jeremy authorization 2026-10-07 ("tell the ledger that too").*
