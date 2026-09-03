# Cone Derivation Ledger v13.172 — Continuous Resolution and mod-1/m Refinement

**Status:** Exact continuation of v13.171  
**Date:** 2026-09-03  
**Scope:** General mod-`1/m` quantization, continuous resolution parameter, and the exact continuous-scale extension of Paper A's gnomons.

## Audit convention

- **[S]** source-established
- **[D]** exact derived
- **[N-cert]** rigorous finite numerical/computer-assisted
- **[I]** interpretation
- **[O]** open
- **[Audit]** correction / limitation

---

## 1. General residue at mesh `1/m`

For any real `m>0` and any real `z`, define the mesh quantizer

\[
Q_m(z)=\frac1m\lfloor mz\rfloor
\]

and the corresponding remainder

\[
R_m(z)=z-Q_m(z).
\]

Equivalently,

\[
\boxed{
R_m(z)=z\bmod \frac1m
= z-\frac1m\lfloor mz\rfloor
=\frac{\{mz\}}m.
}
\]

Hence

\[
\boxed{
z=Q_m(z)+R_m(z)
}
\]

with

\[
\boxed{
0\le R_m(z)<\frac1m.
}
\]

For `m=2`, this is exactly remainder mod `1/2=0.5`:

\[
R_2(z)=z\bmod \frac12.
\]

**[D] Mesh-remainder theorem.** The previously observed mod-`0.5` correction is the `m=2` member of the exact family `mod 1/m`.

The normalized intra-cell phase is

\[
\boxed{
\phi_m(z)=mR_m(z)=\{mz\}\in[0,1).
}
\]

Thus all mesh levels share a common unit phase variable even though the physical cell width is `1/m`.

---

## 2. Apply the residue to Paper A's gnomon arm

Paper A's continuous one-sided gnomon arm is

\[
\boxed{
g_n(u)=\frac{n-u^2}{u}=\frac nu-u,
\qquad 1\le u\le\sqrt n.
}
\]

At mesh `1/m`, the physical arm length resolved by the grid is

\[
Q_m(g_n(u))
=\frac1m\lfloor m g_n(u)\rfloor.
\]

Therefore

\[
\boxed{
g_n(u)
=\frac1m\lfloor m g_n(u)\rfloor
+\left(g_n(u)\bmod\frac1m\right).
}
\]

Since v13.171 proved

\[
g_n(u)=2X_u,
\]

where `X_u` is the Cone horizontal coordinate of the row-parabola / divisor-hyperbola crossing,

\[
\boxed{
2X_u
=\frac1m\lfloor 2mX_u\rfloor
+\left(2X_u\bmod\frac1m\right).
}
\]

**[D]** The `mod 1/m` remainder is exactly the unresolved sub-cell horizontal displacement of the crossing at resolution `1/m`.

This makes the modular correction geometric rather than merely algebraic.

---

## 3. Relation to reciprocal / harmonic quantization

For any positive `u`,

\[
\frac nu
=\frac1m\left\lfloor\frac{mn}{u}\right\rfloor
+\left(\frac nu\bmod\frac1m\right).
\]

Equivalently,

\[
\boxed{
\frac1m\left\lfloor\frac{mn}{u}\right\rfloor
=\frac nu-\left(\frac nu\bmod\frac1m\right).
}
\]

Thus every reciprocal term admits a resolution-`m` decomposition into a lattice-resolved part and a mod-`1/m` defect.

For integer sampling `u=k`, summing gives

\[
\boxed{
\frac1m\sum_{k=1}^n\left\lfloor\frac{mn}{k}\right\rfloor
=nH_n-
\sum_{k=1}^n
\left(\frac nk\bmod\frac1m\right).
}
\]

For `m=1`, this reduces to the standard fractional-part identity

\[
D(n)=nH_n-\sum_{k=1}^n\left\{\frac nk\right\}.
\]

For `m=2`, the correction is exactly a sum of mod-`0.5` remainders.

**[D]** The mod-`0.5` formula and the ordinary mod-`1` divisor correction belong to one exact mod-`1/m` family.

**[Audit]** For `m>1`, the left side above is a refined reciprocal-floor sum; it is not the ordinary divisor summatory function `D(n)` unless `m=1`.

---

## 4. Can `m` be continuous?

Yes, algebraically and geometrically. The definitions

\[
Q_m(z)=\frac1m\lfloor mz\rfloor,
\qquad
R_m(z)=\frac{\{mz\}}m
\]

make sense for every real

\[
\boxed{m>0}.
\]

At noninteger `m`, however, `m` should no longer be called a denominator. It is better interpreted as a **resolution**, **mesh density**, or **dilation parameter**.

The mesh width

\[
\boxed{h=\frac1m}
\]

can therefore vary continuously through all positive real values.

**[D] Continuous-resolution extension.** Quantization and mod-`1/m` remainder have a canonical real-parameter extension to all `m>0`.

---

## 5. Two possible continuous meshes

A subtlety appears when `m` is not an integer.

### Origin-anchored mesh

The direct lattice

\[
\frac1m\mathbb Z
\]

is defined for all real `m>0`, but if `m` is noninteger then the point `1` is generally not on the lattice.

For Paper A, whose bounded divisor region begins exactly at `x,y=1`, this moves the sampled lower boundary to the first mesh point above `1`.

### Boundary-anchored mesh

To preserve Paper A's exact boundary for every real `m>0`, define instead

\[
\boxed{
\Lambda_m=1+\frac1m\mathbb Z_{\ge0}.
}
\]

Then `1` is always a grid point and the spacing is still exactly `1/m`.

For integer `m`, the two descriptions agree on the positive region `x\ge1`:

\[
1+\frac1m\mathbb Z_{\ge0}
=
\left\{\frac a m:a=m,m+1,m+2,\ldots\right\}.
\]

**[D]** The boundary-anchored mesh is the canonical continuous-`m` extension of Paper A's original `x,y\ge1` lattice geometry.

---

## 6. Exact continuous-`m` gnomon formula

Use the boundary-anchored mesh

\[
u_j=1+\frac jm,
\qquad j=0,1,2,\ldots
\]

for arbitrary real `m>0`.

The diagonal gnomon levels satisfying `u_j\le\sqrt n` are

\[
0\le j\le\left\lfloor m(\sqrt n-1)\right\rfloor.
\]

At level `u_j`, the continuous arm length is still

\[
g_n(u_j)=\frac n{u_j}-u_j.
\]

Because the arm is sampled in steps of size `1/m`, the number of points beyond the diagonal vertex is

\[
\left\lfloor m g_n(u_j)\right\rfloor.
\]

Therefore define

\[
\boxed{
\mathscr D_n(m)
=
\sum_{j=0}^{\lfloor m(\sqrt n-1)\rfloor}
\left[
2\left\lfloor
m\left(\frac n{1+j/m}-(1+j/m)\right)
\right\rfloor+1
\right],
\qquad m>0.
}
\]

This formula is meaningful for every positive real `m`.

For every positive integer `m`, it agrees exactly with the fractional Paper-A count `D_m^*(n)` from v13.171.

In particular,

\[
\boxed{\mathscr D_n(1)=D(n).}
\]

**[D] Continuous-resolution gnomon theorem.** Paper A's integer gnomon count sits inside a one-real-parameter family of exact lattice counts indexed by resolution `m>0`.

---

## 7. What continuity of `m` does and does not mean

Although the parameter `m` is continuous, the count

\[
\mathscr D_n(m)
\]

is integer-valued and therefore cannot vary smoothly.

As `m` changes, jumps occur when either

\[
m(\sqrt n-1)
\]

crosses an integer and a new diagonal level enters, or when one of the quantities

\[
m g_n\left(1+\frac jm\right)
\]

crosses an integer and an arm gains or loses a lattice point.

Hence `m` defines a **continuous scale flow whose observable count is a staircase**.

**[I]** This is analogous to moving a continuous measuring scale past a fixed geometry: the ruler spacing changes continuously, while the number of resolved cells changes only at threshold events.

**[Audit]** Continuous `m` does not make the divisor count itself a continuous function. It continuously deforms the quantizer; the floor operation still produces discrete jumps.

---

## 8. The modular phase as `m` flows

For fixed real `z>0`,

\[
\phi_m(z)=\{mz\}
\]

is the normalized sub-cell phase.

Its discontinuities occur at

\[
\boxed{m=\frac{k}{z}},
\qquad k\in\mathbb Z_{>0},
\]

exactly when `mz` becomes an integer and the point lands on a mesh boundary.

The physical remainder is

\[
R_m(z)=\frac{\phi_m(z)}m,
\]

so

\[
0\le R_m(z)<\frac1m.
\]

Therefore

\[
\boxed{
\lim_{m\to\infty}R_m(z)=0
}
\]

for every fixed `z`.

Thus continuous resolution gives a precise interpolation between finite-cell modular defects and the continuum limit.

---

## 9. Cone form of the continuous scale flow

At the `u`-row / `xy=n` crossing,

\[
2X_u=g_n(u).
\]

Hence the normalized phase of that crossing is

\[
\boxed{
\phi_m(u)=\{2mX_u\}.
}
\]

The physical unresolved displacement is

\[
\boxed{
\rho_m(u)=2X_u\bmod\frac1m
=\frac{\{2mX_u\}}m.
}
\]

A crossing is exactly resolved by the `1/m` mesh iff

\[
\boxed{2mX_u\in\mathbb Z.}
\]

Thus continuous variation of `m` sweeps each fixed crossing through an infinite sequence of exact-resolution events

\[
\boxed{m=\frac{k}{2X_u}}
\]

for integers `k>0` when `X_u>0`.

**[D]** The continuous scale parameter converts the floor geometry into a family of exact phase-locking conditions.

---

## 10. Continuum limit survives continuous `m`

The proof in v13.171 used integer `m`, but the boundary-anchored continuous family has the same limiting mesh width `1/m`.

Therefore, as real `m\to\infty`,

\[
\boxed{
\frac{\mathscr D_n(m)}{m^2}
\longrightarrow
n\log n-n+1.
}
\]

The reason is unchanged: the mesh becomes uniformly fine, the total floor defect is lower order than `m^2`, and the gnomon sum converges to

\[
2\int_1^{\sqrt n}\left(\frac nu-u\right)du.
\]

**[D]** The continuum area is independent of whether the refinement parameter approaches infinity through integers or through arbitrary positive real values.

---

## 11. Arithmetic meaning is special at integer/rational scales

For integer `m`, the mesh points are rational with common denominator `m`, and the scaled factor relation

\[
ab=nm^2
\]

has its ordinary integer arithmetic meaning.

For noninteger `m`, that denominator interpretation is lost. In particular, the boundary-anchored mesh points

\[
1+\frac jm
\]

need not be rational.

Therefore continuous `m` preserves the **geometry and quantization mechanism**, but not the same finite arithmetic interpretation at every scale.

**[Audit]** Keep two layers distinct:

- integer `m`: arithmetic fractional-grid refinement;
- real `m>0`: continuous resolution/quantization flow.

The integer scales are distinguished arithmetic slices of the larger real-parameter family.

---

## 12. New synthesis

The results now fit into the exact hierarchy

\[
\boxed{
\text{continuous profile }g_n(u)=2X_u
}
\]

\[
\boxed{
\downarrow\quad \text{resolution }m>0
}
\]

\[
\boxed{
Q_m(g_n(u))
=\frac1m\lfloor 2mX_u\rfloor
}
\]

plus the modular defect

\[
\boxed{
R_m(g_n(u))
=2X_u\bmod\frac1m.
}
\]

At integer `m`, this is a rational fractional lattice. At `m=2`, the defect is mod `0.5`. At arbitrary real `m`, it is a continuously varying scale quantizer. As `m\to\infty`, the physical modular defect vanishes.

**[I]** This suggests that the project's mod-`0.5` observation is not isolated: it may be the first visible nontrivial arithmetic slice of a continuous scale/phase structure already implicit in Paper A's floor gnomons.

---

## 13. Next investigations

### [D] Immediate consequences to exploit

1. Every gnomon crossing carries a phase `phi_m(u)={2mX_u}`.
2. Exact grid alignment occurs at `2mX_u in Z`.
3. Integer `m` selects rational arithmetic refinements from the continuous scale family.
4. The physical defect is bounded by one cell width and vanishes as `m->infinity`.

### [O] High-value next tests

1. Test whether the previously observed half-cell tangent-circle configurations correspond to phase values `0`, `1/2`, or another distinguished `phi_m`.
2. Determine whether the cumulative phase sum

\[
\sum_u\{2mX_u\}
\]

has a clean relation to the refined `nH_n` correction.
3. Study the jump set of `mathscr D_n(m)` as a function of continuous `m` and ask whether its threshold curves recover the same parabolas/circles visible in Paper A.
4. Compare the boundary-anchored continuous mesh with the origin-anchored arithmetic mesh at integer scales and quantify their divergence away from integer `m`.

### Publication guardrails

1. Do not call noninteger `m` a denominator; call it a resolution or mesh-density parameter.
2. Do not claim `mathscr D_n(m)` is continuous; it is an integer-valued staircase driven by a continuous scale.
3. Do not transfer the integer factorization identity `ab=nm^2` unchanged to arbitrary boundary-anchored real `m`.
4. Treat phase-locking language as an exact quantization statement, not as evidence of a physical quantum system unless a separate model establishes that interpretation.
