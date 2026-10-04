# Cone Derivation Ledger v14.005 — Frozen P4 Source-Six-Plane Admissibility and Partition-Invariance Guardrail

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [N] corrected fail-closed N=192 frozen-P4/source-six-plane replay; [N] small principal-angle mismatch against the high-precision resonance four-plane; [N] positive complement floors preserved; [D] exact capacity invariance under a complete protected/complement split; [G] equality of frozen/ideal capacities is therefore not an alignment certificate; [O] promote the frozen P4 carrier to the M3999/4000 midpoint and certify only complement positivity plus the source-aligned scalar crossing.
**Parents:** v14.003–004, v13.982, v13.988.
**Research commits:** 563a1cb6a68a8f9462c7f3f7eeba578b444e8283, 87e9a40c43150b3eded95985a82083aecff9e484.
**Workflow commits:** 04be492d78057c7efc9ec673c05cd67ce07935e1, 3ea7091cfe09d43fad3325a34cb70a5a6ff1afbb.
**Collision check:** immediately before this write, live HEAD was 5468cc6bc7a9997f48063a270c071b0c3e869df9 and no current v14.005 ledger file was present.

---

## 1. CI repair before interpretation

The first frozen-P4 workflow run looked green because the shell pipeline did not use pipefail, while the Python process actually stopped inside mpmath on a multi-right-hand-side LU call.

Two repairs were made before interpreting any numerical result:

1. solve the complement coupling columns one right-hand side at a time;
2. make the workflow fail closed with set -o pipefail.

The repaired run completed successfully and uploaded the full result artifact.

---

## 2. Frozen P4 versus high-precision resonance four-plane [N]

At the N=192 source-faithful checkpoint, compare:

- the four-column frozen P4 carrier restricted to the same tail modes;
- the high-precision normalized-resonance four-plane used in the v14.003 capacity producer.

### Even parity

Principal-angle cosines:

\[
(1.0,\ 0.9999999999999993,\ 0.9999999999999175,\ 0.9999898115648197).
\]

The maximum principal angle is

\[
\boxed{0.2586376481^\circ}.
\]

### Odd parity

Principal-angle cosines:

\[
(0.9999999999999997,\ 0.9999999999999994,\ 0.9999999999714115,\ 0.9999441252030359).
\]

The maximum principal angle is

\[
\boxed{0.6056861340^\circ}.
\]

Thus the already-frozen P4 carrier is numerically very close to the independently generated high-precision resonance four-plane in both parities.

---

## 3. Complement floors [N]

Using the two low source-active coordinate directions together with the frozen P4 tail plane gives a six-dimensional protected space.

The Euclidean orthogonal complement remains positive at N=192.

### Even

\[
\boxed{\lambda_{\min}(D_{Q,\mathrm{frozen}})=0.1711671054661427}.
\]

For the ideal resonance plane:

\[
\lambda_{\min}(D_{Q,\mathrm{ideal}})=0.1711688786911413.
\]

### Odd

\[
\boxed{\lambda_{\min}(D_{Q,\mathrm{frozen}})=0.5508927121025952}.
\]

For the ideal resonance plane:

\[
\lambda_{\min}(D_{Q,\mathrm{ideal}})=0.5508677648412738.
\]

The stiff-complement geometry is therefore essentially unchanged by replacing the high-precision generated plane with the frozen P4 carrier.

---

## 4. Exact partition-invariance guardrail [D]

The replay also reports exactly the same full source energy and capacity for the frozen and ideal protected spaces.

That equality is not evidence that the two four-planes are close.

Let P and Q be any complete orthogonal decomposition, and write

\[
T=
\begin{pmatrix}
A&E^*\\
E&D
\end{pmatrix},
\qquad
f=\binom{f_P}{f_Q}.
\]

If D is invertible, exact Schur elimination gives

\[
f^*T^{-1}f
=
f_Q^*D^{-1}f_Q
+
g^*S^{-1}g,
\]

with

\[
S=A-E^*D^{-1}E,
\qquad
g=f_P-E^*D^{-1}f_Q.
\]

The left-hand side is basis independent.

Therefore any two complete protected/complement splittings that are eliminated exactly must return the same full source energy and capacity.

Hence

\[
\boxed{
\mathcal C_{\mathrm{frozen}}=\mathcal C_{\mathrm{ideal}}
}
\]

is an algebraic invariance statement, not an alignment test.

The actual admissibility evidence is:

1. small principal angles;
2. preservation of a positive stiff-complement floor;
3. successful isolation of the same six near-dangerous directions.

---

## 5. Decision

The frozen P4 carrier is accepted as the leading theorem-scale candidate for the four resonance directions.

This is not yet a proof that it is valid at M3999/4000 or in the infinite problem.

The next gate must test the same fixed carrier at the theorem-scale cutoff, without regenerating the basis.

Specifically use

\[
P=
\operatorname{span}\{e_1,e_2\}
\oplus
\operatorname{Ran}Z_{P4}^{\mathrm{frozen}}
\]

restricted to modes at or below 3999 in even parity and 4000 in odd parity.

Then certify or diagnose:

1. positivity of the complement;
2. the joint protected/source Schur reduction;
3. source alignment;
4. the scalar crossing s-alpha beta^2;
5. residual quality in the joint complement solve.

Do not use equality of reconstructed full capacities as a carrier-quality metric.

---

## 6. Result

At N=192 the frozen P4 carrier tracks the ideal resonance four-plane within

\[
\boxed{0.259^\circ\ \text{even},\qquad 0.606^\circ\ \text{odd}}
\]

and preserves essentially the same stiff-complement floors.

This is sufficient to justify a theorem-scale frozen-carrier test.

It does not itself certify the M3999/4000 split.

---

HANDOFF
target: sandbox
type: audit
parent: v14.005
status: open
action: Independently audit the frozen-P4 basis-freezing decision, especially the partition-invariance guardrail and whether the principal-angle/complement-floor evidence is sufficient to justify testing the same frozen carrier at M3999/4000 without regenerating a new basis.
deliverable: theorem-or-obstruction
constraints: Do not use equality of reconstructed capacities as evidence of subspace alignment; keep the N=192 diagnostic distinct from theorem-scale and infinite-tail certification.
