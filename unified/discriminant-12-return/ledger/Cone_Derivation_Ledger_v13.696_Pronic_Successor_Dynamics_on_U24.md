# Cone Derivation Ledger v13.696 — Pronic Successor Dynamics on U(24): Exact Eight-Cycle and Affine Obstruction

Date: 2026-09-23

Status labels: **[S]** source/audit-established, **[D]** exact derived, **[N]** obstruction/negative result, **[I]** interpretation.

## 1. Synchronization

Immediately before this write the live head was v13.695 External Audit Round 79, commit \`851764570e5e2dfe300a90b4ccdb48f67db011d8\`. Round 79 independently reverified v13.690–694, including the exact equality
\[
\{r:r^2\equiv1\pmod{24}\}=U(24).
\]

This checkpoint tests whether pronic index evolution supplies a canonical D12/Pell-like dynamics on that carrier.

## 2. Admissible pronic indices and exact carrier order [D]

Let
\[
P_m=m(m+1),\qquad r_m=2m+1.
\]
The admissibility condition
\[
6\mid P_m
\]
is equivalent to
\[
m\not\equiv1\pmod3.
\]

Modulo \(12\), the admissible indices are
\[
\boxed{m=0,2,3,5,6,8,9,11.}
\]
Their doubled completed radii modulo \(24\) are
\[
\boxed{
r_m=1,5,7,11,13,17,19,23.
}
\]
Thus one period of the admissible pronic sequence traverses every element of \(U(24)\) exactly once.

Define \(S\) to mean “advance to the next admissible pronic index,” wrapping modulo \(12\). Then
\[
\boxed{
1\to5\to7\to11\to13\to17\to19\to23\to1.
}
\]
Therefore \(S\) is an exact 8-cycle permutation of the finite carrier.

The gaps in \(m\) alternate
\[
\boxed{+2,+1,+2,+1,+2,+1,+2,+1}
\]
and hence the corresponding additive changes in \(r=2m+1\) alternate
\[
\boxed{+4,+2,+4,+2,+4,+2,+4,+2}
\]
before modular wrap.

## 3. Binary-coordinate form [D]

Using v13.530's fixed coordinates
\[
r(a,b,c)=5^a7^b(-1)^c,
\]
the eight-cycle is
\[
\boxed{
000\to100\to010\to110\to111\to011\to101\to001\to000.
}
\]

The first four states are the fixed-sign \(V_4\):
\[
000,100,010,110
\leftrightarrow
1,5,7,11.
\]
The next four are its signed lifts:
\[
111,011,101,001
\leftrightarrow
13,17,19,23.
\]

Thus the pronic successor traverses one four-state sheet and then the other, but its crossing between sheets occurs at
\[
11\to13=-11,
\]
not by applying the arithmetic sign generator uniformly at every state.

## 4. It is not multiplication by a fixed U(24) element [N]

Every nonidentity element of \(U(24)\cong C_2^3\) has order \(2\). Therefore translation by multiplication with a fixed \(g\in U(24)\),
\[
r\mapsto gr,
\]
has cycles of length at most \(2\).

Since \(S\) has order \(8\),
\[
\boxed{
S\text{ is not multiplication by any fixed }g\in U(24).
}
\]

Thus the pronic index flow is not the native group-translation dynamics of the carrier.

## 5. It is not an affine F2^3 map in the established coordinates [N]

Suppose
\[
S(v)=Mv+t
\]
with \(M\in GL_3(\mathbf F_2)\).

From
\[
S(000)=100
\]
we obtain
\[
t=100.
\]
Then
\[
S(100)=010
\]
forces
\[
M(100)=110,
\]
and
\[
S(010)=110
\]
forces
\[
M(010)=010.
\]

Affine linearity would therefore give
\[
S(110)
=M(100)+M(010)+t
=110+010+100
=000.
\]
But the exact pronic successor gives
\[
S(110)=111.
\]
Contradiction.

Hence
\[
\boxed{
S\notin AGL(3,2)
}
\]
for the already-established \(U(24)\cong\mathbf F_2^3\) structure.

This is stronger than saying the step sizes are irregular: the successor is not an affine symmetry of the audited character-dual carrier.

## 6. Character behavior along the cycle [D]

Using v13.530,
\[
\chi_{-3}=\psi_{100},\qquad
\chi_{-4}=\psi_{010},\qquad
\chi_{12}=\psi_{110},\qquad
\sigma=\psi_{001},
\]
with \(v=(a,b,c)\), so
\[
\chi_{-3}=(-1)^a,\quad
\chi_{-4}=(-1)^b,\quad
\chi_{12}=(-1)^{a+b},\quad
\sigma=(-1)^c.
\]

Along
\[
000,100,010,110,111,011,101,001
\]
the \(\chi_{12}\) signs are
\[
\boxed{
+,-,-,+,+,-,-,+,
}
\]
while the signed-sheet character is
\[
\boxed{
+,+,+,+,-,-,-,-.
}
\]

Thus the eight-cycle contains a four-step sheet block, but the Pell time-orientation character \(\chi_{12}\) oscillates in the two-minus/two-plus pattern
\[
+--++--+.
\]

[N] Consequently the pronic successor itself is not the previously established Pell time-orientation action. It orders states on the same carrier but does not implement the \(\chi_{12}\) Galois/Pell action.

## 7. What *is* canonical about the successor [D/I]

Although \(S\) is not a group or affine action, it is canonical from the ordered pronic index line:

1. increment \(m\);
2. omit the ramified class \(m\equiv1\pmod3\);
3. map by \(r=2m+1\);
4. reduce modulo \(24\).

This produces the unique increasing-residue traversal
\[
1,5,7,11,13,17,19,23
\]
within the chosen period \(0\le m<12\).

[I] Thus there are two distinct structures on the same eight-state set:

- **multiplicative/character structure:** \(U(24)\cong C_2^3\), with character dual and cone reflections;
- **ordered pronic successor:** an 8-cycle inherited from the integer index line after deleting the ramified \(m\equiv1\pmod3\) states.

They should not be conflated.

## 8. Relation to D12 return [I/N]

The result strengthens the finite-carrier identification but blocks one tempting stronger claim.

[D] The pronic half-integer construction selects exactly the same eight states as the D12 \(U(24)\) carrier.

[N] The elementary successor \(m\mapsto\) next admissible \(m\) does **not** reproduce the carrier group law, an affine \(F_2^3\) symmetry, or the established \(\chi_{12}\) Pell time-orientation action.

[I] Therefore any genuine dynamical bridge from pronics to the Pell return must use more than raw index succession. Natural candidates are the centered quadratic/RMS operation, the rapidity coordinate, or a nonlinear permutation conjugacy carrying additional geometric data.

## 9. Next exact target

The strongest remaining candidate is the centered RMS/Casimir cell:
\[
35\mid36\mid37
\quad\leadsto\quad
11\mid0\mid1\pmod{12}.
\]
Test whether the transformation from the completed-pronic pair
\[
\{5,7\}=\chi_{12}^{-1}(-1)
\]
to the RMS/geometric pair
\[
\{11,1\}=\chi_{12}^{-1}(+1)
\]
is itself expressible by an established cone operation (product, half-turn, reflection, norm, or character duality), and whether that operation matches the known Pell orientation reversal more faithfully than the pronic successor does.
