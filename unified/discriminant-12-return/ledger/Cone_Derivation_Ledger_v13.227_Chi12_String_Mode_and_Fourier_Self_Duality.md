# Cone Derivation Ledger v13.227 — chi12 String Mode and Fourier Self-Duality

Date: 2026-09-04
Status: EXACT NEW RESULT + INTERPRETIVE MODEL — research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README and the current `master` tree were re-fetched. The tip remained

`dcd00ed913ff984d89124185a96c371877624433`

with v13.226 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry therefore extends the reconciled branch without overwriting newer work.

## 1. The distinguished 12-position pattern

On the modulus-12 carrier

\[
U(12)=\{1,5,7,11\}\cong V_4,
\]

the primitive quadratic character of discriminant 12 is

\[
\chi_{12}(1)=+1,\qquad
\chi_{12}(5)=-1,\qquad
\chi_{12}(7)=-1,\qquad
\chi_{12}(11)=+1,
\]

and it vanishes on nonunits. In particular,

\[
\boxed{
1,5,6,7,11
\quad\mapsto\quad
+1,-1,0,-1,+1.
}
\]

Thus the midpoint `6` is flanked by the two negative character positions `5,7`, while the reflected outer pair `1,11` carries the positive sign.

## 2. Generator interpretation of 5 and 7

The residues `5` and `7` form a generating pair for the Klein four group:

\[
5^2\equiv7^2\equiv1\pmod{12},
\qquad
5\cdot7\equiv11\pmod{12}.
\]

Hence

\[
\boxed{U(12)=\langle5,7\rangle=\{1,5,7,11\}.}
\]

This generating pair is not algebraically unique — any two distinct nonidentity elements generate `V_4` — but `5,7` are geometrically distinguished because they are the nearest unit residues to the midpoint `6`:

\[
5=6-1,\qquad7=6+1.
\]

The group roles are therefore

\[
1=\text{identity},\qquad
5,7=\text{chosen symmetric generators},\qquad
11=5\cdot7.
\]

## 3. Exact fixed-sum Cone realization

On the fixed-sum shell

\[
x+y=12,
\]

Paper A coordinates give

\[
T=6,
\qquad
X=\frac{x-y}{2}.
\]

Using the reflected factor pair

\[
(x,y)=(r,12-r),
\]

we obtain

\[
\boxed{X=r-6}
\]

and

\[
\boxed{Y^2=r(12-r)=36-X^2.}
\]

For the distinguished residues,

\[
\begin{array}{c|ccccc}
r&1&5&6&7&11\\
\hline
X=r-6&-5&-1&0&1&5\\
\chi_{12}(r)&+1&-1&0&-1&+1
\end{array}
\]

so the character pattern becomes the exact symmetric Cone pattern

\[
\boxed{
X=-5,-1,0,1,5
\quad\mapsto\quad
+1,-1,0,-1,+1.
}
\]

Equivalently,

\[
|X|=5\mapsto+1,
\qquad
|X|=1\mapsto-1,
\qquad
X=0\mapsto0.
\]

This is a theorem-level arithmetic/geometric identification on the `x+y=12` slice.

## 4. Reflection and generator-swap guardrail

There are two related but distinct symmetries.

### 4.1 Additive reflection about the midpoint

The string/Cone reflection is

\[
r\mapsto12-r\equiv-r\pmod{12}.
\]

On `U(12)` this is multiplication by `11`:

\[
1\leftrightarrow11,
\qquad
5\leftrightarrow7.
\]

Because

\[
\chi_{12}(11)=+1,
\]

we have

\[
\boxed{\chi_{12}(12-r)=\chi_{12}(r).}
\]

Thus the real quadratic character is even under the midpoint reflection.

### 4.2 Klein-group generator swap

The abstract automorphism of `V_4` that fixes `1,11` and exchanges `5,7` is different from the additive midpoint reflection, because the latter also exchanges `1,11`.

Under the generator-swap automorphism, the two characters `chi_{-4}` and `chi_{-3}` are exchanged, while `chi_12=chi_{-4}chi_{-3}` is fixed.

**Audit guardrail:** do not identify midpoint reflection, group translation by `11`, and generator-swap automorphism as the same map. They agree on the exchange `5<->7` but act differently on the identity/product pair.

## 5. Connection to the half-integer/pronic level

For factor separation `d`, let

\[
y=x+d.
\]

Then

\[
X=-\frac d2,
\]

and the Cone identity gives

\[
\boxed{
xy+\frac{d^2}{4}
=\left(\frac{x+y}{2}\right)^2.
}
\]

For `d=1`,

\[
\boxed{n(n+1)+\frac14=\left(n+\frac12\right)^2,}
\]

so the pronic sequence shifted by `1/4` is exactly the half-integer-square sequence. This is the `|X|=1/2` level.

The distinguished generator pair `(5,7),(7,5)` has separation `d=2`, hence

\[
|X|=1,
\]

which is the next transverse half-lattice level after the pronic/half-integer-square collision.

## 6. Exact 12-point Fourier self-duality

The vibrating-string language becomes mathematically spectral once `chi_12` is regarded as a 12-periodic function extended by zero off the units.

Define the unnormalized discrete Fourier transform

\[
\widehat\chi_{12}(m)
=
\sum_{r\bmod12}
\chi_{12}(r)e^{2\pi i mr/12}.
\]

Because `chi_12` is a primitive real quadratic character of conductor `12`, its Gauss-sum identity gives

\[
\widehat\chi_{12}(m)
=\tau(\chi_{12})\chi_{12}(m).
\]

Direct evaluation at `m=1` gives

\[
\tau(\chi_{12})
=
 e^{2\pi i/12}
-e^{10\pi i/12}
-e^{14\pi i/12}
+e^{22\pi i/12}
=2\sqrt3
=\sqrt{12}.
\]

Therefore

\[
\boxed{
\widehat\chi_{12}(m)=\sqrt{12}\,\chi_{12}(m).
}
\]

This is an exact Fourier eigenvector statement.

Hence the sparse node pattern

\[
\boxed{(+1,-1,-1,+1)\text{ on }\{1,5,7,11\}}
\]

reappears, up to the scalar `sqrt(12)`, in frequency space on the same four residue positions. All nonunit Fourier modes vanish.

This is the strongest rigorous realization so far of the user's vibrating-string intuition: the discriminant-12 character is simultaneously a sparse position-space pattern and an eigenmode of the 12-point discrete Fourier transform.

## 7. Interpretation and limits

It is now justified to call `chi_12` a discrete 12-node Fourier mode in the precise DFT sense. The sign pattern

\[
+1,-1,0,-1,+1
\]

on the distinguished reflected positions is exact, and the same primitive character reproduces itself under the 12-point Fourier transform.

However, the phrase **prime harmonic generation** remains interpretive unless a dynamical wave operator or physical Hamiltonian is specified. The exact theorem presently established is Fourier self-duality of the primitive quadratic character, not a literal vibrating-string dynamics.

## 8. Immediate consequence for the continuing program

The new exact bridge is

\[
\boxed{
\text{Cone midpoint geometry}
\longleftrightarrow
\chi_{12}\text{ sign pattern}
\longleftrightarrow
\text{12-point Fourier eigenmode}.
}
\]

Together with v13.225 and v13.226, the branch now contains three compatible structures:

\[
\boxed{
U(12)\cong V_4
\xrightarrow{\text{characters}}
\chi_{12}
\xrightarrow{\mathrm{DFT}_{12}}
\sqrt{12}\,\chi_{12},
}
\]

\[
\boxed{
5,7\text{ as symmetric V4 generators about }6,
}
\]

and

\[
\boxed{
U(24)\cong C_2^3
\text{ as the two-sheeted prime-admissible lift.}
}
\]

The next high-value audit is to compare this exact 12-point Fourier eigenmode with the `H_4` character transform and then with the `H_8` Walsh transform on `U(24)`, asking whether the mod-24 sheet bit factors cleanly from the existing discriminant-12 mode.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.