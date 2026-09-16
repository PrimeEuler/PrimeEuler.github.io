# Cone Derivation Ledger v13.504 — χ12 Bridge Coordination After the Mod-24 Audit

## Scope

Synchronize the χ12 prime-phase/Suzuki bridge lane with v13.500–v13.503 before continuing the nonlinear q=5/q=7 Schur-interaction calculation. This entry is deliberately a coordination checkpoint, not a new numerical result.

The mod-12 cone realization is retained as an exact geometric realization of the unit-core label. The cone U(24) double cover is **not** used as a Suzuki input: v13.502 and v13.503 have now ruled out that identification, first at mod 24 and then for every even 2-adic stratum.

---

## 1. Common arithmetic coordinate retained [D]

For a Suzuki index write
\[
k=2^a3^b u,\qquad (u,6)=1.
\]
The reusable common coordinate between the cone/character side and the Suzuki valuation side is
\[
\boxed{(a,b;\ u\bmod12)},\qquad u\bmod12\in U(12)=\{1,5,7,11\}.
\]

The roles are distinct:

- `(a,b)` records ramified valuation/scale information at 2 and 3;
- `u mod 12` records the unramified V4 unit-core class;
- the four real characters `1, chi_-4, chi_-3, chi_12` are the H4/Fourier coordinates of that unit core;
- the AM-GM cone points
  \[
  (X_r,Y_r,T_r)=((r-1)/2,\sqrt r,(r+1)/2),\qquad r\in U(12),
  \]
  are a geometric realization of the same four labels.

This is the structural object to carry forward. Raw mod-24 unit-group membership is not.

---

## 2. What v13.501–v13.503 do and do not contribute [Audit]

Retained:

1. `U(24)=U(12) x C2` is an exact audited double cover.
2. Its cone coordinate realization has sheet map `(X,T)->(X+6,T+6)`.
3. This is useful as a geometric picture of the algebraic lift.

Guardrails:

1. The `(X,T)` translation is automatic in the `(r,1)` family from `T-X=1`; it is not an independently discovered cone dynamics.
2. Suzuki's first even stratum `{2,10,14,22} mod 24` is disjoint from `U(24)`.
3. More generally, on `v_2(k)=a>=1`, the exact recovery modulus is `M_a=12*2^a`, but the raw residues `2^a r` are never units modulo `M_a`.
4. Therefore no `U(24)`, `U(48)`, ... cone-unit double cover is to be inserted into the Suzuki operator merely because the same V4 labels reappear after stripping ramified factors.

So the bridge lane is now explicitly
\[
\boxed{
\text{Pell/character orientation}
\to u\bmod12\text{ phase label}
\to \text{authentic Suzuki source}
\to dS_q,D^2S_{q,q'}
\to N^T(\cdot)N
\to \text{terminal spectral geometry?}
}
\]
with the question mark retained until a downstream, control-resistant invariant exists.

---

## 3. Active numerical target inherited from v13.496 [N]

The first-order q=5/q=7 alignment
\[
C_{5,7}=0.9873520060523864
\]
was stable under cutoff/solve/step tests but failed the preregistered source-background gate. In particular the alignment changes strongly as the canonical source background is enlarged.

The active diagnostic is therefore the already-committed

`research-notes/suzuki_chi12_q5_q7_mixed_schur_derivative.py`

(commit `5867934753d0fe12cbeece6bda7651255216e11a`).

It separates two nonlinear effects that must not be conflated:

- the q=7 self-Hessian along the path turning q=7 into the Q=5 background,
  \[
  \frac{d}{dt}B_7(t)=N^T D^2S[x_7,x_7]N;
  \]
- the mixed q=5/q=7 Hessian,
  \[
  \boxed{H_{57}=N^TD^2S[x_5,x_7]N}.
  \]

The purpose is to determine whether the Q=5 -> Q=7 axis reversal is quantitatively explained by nonlinear Schur interactions, and whether any residual unit-core/chi12 organization remains after those interactions are accounted for.

---

## 4. Promotion rule [Audit]

Do not compare to the frozen v13.471 terminal direction until the nonlinear interaction diagnostic is stable and yields a background-resistant residual observable.

A useful bridge signal must survive all of:

1. source-faithful propagation;
2. finite-difference / analytic or cancellation-free derivative agreement;
3. M/cutoff stability;
4. source-background variation or an explicit Hessian correction that explains it;
5. ramified controls;
6. only then, comparison with an independently frozen terminal direction.

No exact-kernel, critical-line, RH, or GRH claim follows from any current result.

## Coordination note

Live ledger checked immediately before this write. v13.503 was current; v13.504 was free. This entry records the lane and the negative mod-24 result so parallel threads do not reintroduce the cone U(24) double cover as a Suzuki mechanism.