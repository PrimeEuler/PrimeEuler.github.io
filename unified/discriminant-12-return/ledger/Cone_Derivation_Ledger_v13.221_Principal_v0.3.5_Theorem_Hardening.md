# Cone Derivation Ledger v13.221 — Principal v0.3.5 Theorem Hardening

Date: 2026-09-04
Project root: `unified/discriminant-12-return/`

## Purpose

Implement the theorem-packaging hardening identified by the ground-up audit in
v13.220 without changing the mathematical content of the discriminant-12
return chain.  v0.3.4 remains the preceding audited publication snapshot; the
new source is `papers/Discriminant_12_Return_v0.3.5.tex`.

## Ground-up audit input

The v13.220 audit found no theorem-breaking defect in v0.3.4.  It identified
four theorem-hardening improvements:

1. promote the finite-field trace / XOR identity into the main theorem;
2. give the `n=11` narrow-class / Artin result an explicit proposition;
3. replace the bare imported residue-field identification with a direct local
   proof of `O_K/P_2 ~= F_4`;
4. state the full signed three-dimensional Lorentz boost explicitly, including
   `Y'=Y`.

## v0.3.5 source changes

Source creation commit:

`fe5b1d35bee463ec198612179fff40da89e94db1`

### 1. Signed Cone boost made explicit

From

`x' = lambda x`, `y' = lambda^{-1} y`, `lambda=2+sqrt(3)`,

v0.3.5 now states the equivalent full signed Cone action

`X' = 2X + sqrt(3) T`,
`Y' = Y`,
`T' = sqrt(3) X + 2T`.

Thus each signed sheet is preserved separately, as is `Y^2=xy`.

### 2. Direct residue-field proof

In the cyclotomic quotient by

`P_2 = p_2 O_{K_12}`,

one has `2=0` and `1+sqrt(3)=0`, hence `sqrt(3)=1` in characteristic two.
Using

`sqrt(3)=zeta+zeta^{-1}`

gives

`zeta^2+zeta+1=0`.

Since `X^2+X+1` is irreducible over `F_2`, this yields directly

`O_{K_12}/P_2 ~= F_2[omega]/(omega^2+omega+1) ~= F_4`,

with `omega=bar(zeta)` of order three.

This strengthens self-containment while preserving the carrier guardrail:
this quotient is not the same ring as `p_2/2p_2`.

### 3. Trace / XOR promoted into the main theorem

The main theorem now includes

`bar(q_12) = Tr_{F_4/F_2}`

under the explicitly stated additive identification

`f_1 -> 1`, `f_2 -> omega^2`.

Equivalently, in Boolean/Pell coordinates,

`Tr(epsilon_1 omega + epsilon_2 omega^2) = epsilon_1 XOR epsilon_2`.

This is now theorem content rather than only a later interpretive conclusion.

### 4. `n=11` result packaged as a proposition

v0.3.5 adds an explicit proposition proving

`N(1+2sqrt(3))=-11`,

`[p_11]=[p_2]`

in the narrow ideal class group, and

`Art_{K_12/F}(p_11)=T_11`,

where `T_11` is complex conjugation over `F=Q(sqrt(3))`.

The companion statement

`T_11 <-> J`

remains explicitly a representation correspondence, not literal equality
between different categories.

## Build / CI synchronization

New build script:

`papers/build_discriminant12_v0.3.5.sh`

creation commit:

`9e70013e038b3d00d6f26f840dfd0bc3364fc111`

The build preserves the v0.3.4 publication safeguards:

- paper-owned figure generators only;
- staged remapping of historical generic figure names;
- isolated build directory;
- `TEXINPUTS` begins with `.` so the staged source is compiled rather than the
  original paper path;
- Paper A figure assets are not overwritten.

Workflow `.github/workflows/build-discriminant12-paper.yml` was synchronized in
commit:

`af22422552e16ea3bb88c1fae4f916944cddd398`

It now watches/builds v0.3.5 and will publish
`papers/Discriminant_12_Return_v0.3.5.pdf` if CI succeeds.

## Status

At this checkpoint:

**v0.3.5 theorem hardening is complete at source level.**

Publication promotion remains conditional on successful CI compilation and
subsequent README synchronization.  Until that confirmation, v0.3.4 remains
the active audited publication baseline.
