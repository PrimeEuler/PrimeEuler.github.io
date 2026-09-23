# Cone Derivation Ledger v13.694 — The Pronic mod-24 Root Carrier Is Exactly U(24)

Date: 2026-09-23

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[N]** limitation.

## 1. Synchronization and question

Immediately before this write the live head was v13.693, commit \`bc8ddfc7b80c387020bd561a2c120eedd3aaae96\`; no v13.694 collision was present.

Question: compare the pronic half-integer condition
\[
r^2\equiv1\pmod{24}
\]
with the independently established v13.530 carrier
\[
U(24)=\{\pm1,\pm5,\pm7,\pm11\}\cong C_2^3.
\]

## 2. Set equality: the two carriers are literally identical [D]

For any residue \(r\bmod24\),
\[
r^2\equiv1\pmod{24}
\]
implies \(r\) is coprime to \(24\), hence \(r\in U(24)\).

Conversely, every unit modulo \(24\) is odd and not divisible by \(3\). Therefore
\[
r^2\equiv1\pmod8
\]
for odd \(r\), and
\[
r^2\equiv1\pmod3
\]
for \(3\nmid r\). By CRT,
\[
r^2\equiv1\pmod{24}.
\]

Hence
\[
\boxed{
\{r\bmod24:r^2\equiv1\pmod{24}\}
=
U(24).
}
\]

Explicitly,
\[
\boxed{
\{1,5,7,11,13,17,19,23\}
=
\{\pm1,\pm5,\pm7,\pm11\}.
}
\]

So this is not merely an isomorphic eight-state set: it is the exact same subset of \(\mathbb Z/24\mathbb Z\).

## 3. Group law: the root carrier is the same C2^3 [D]

If \(r^2=s^2=1\pmod{24}\), then
\[
(rs)^2\equiv1\pmod{24},
\]
so the root set is closed under multiplication. Every element is its own inverse:
\[
r^{-1}=r.
\]
There are eight elements, hence
\[
\boxed{
R_{24}:=\{r:r^2=1\pmod{24}\}
=
U(24)
\cong C_2^3.
}
\]

Using the already-established v13.530 basis
\[
r(a,b,c)=5^a7^b(-1)^c,
\]
the pronic-root carrier inherits exactly the same binary coordinates:
\[
\begin{array}{c|c}
000&1\\
100&5\\
010&7\\
110&11\\
001&23=-1\\
101&19=-5\\
011&17=-7\\
111&13=-11.
\end{array}
\]

No new choice of isomorphism is required.

## 4. Every U(24) state has a pronic half-integer lift [D]

Let \(r\) be any odd representative of a state in \(U(24)\). Put
\[
m=\frac{r-1}{2}.
\]
Then
\[
P_m=m(m+1)=\frac{r^2-1}{4}.
\]
Since \(r^2\equiv1\pmod{24}\),
\[
6\mid P_m.
\]
Moreover,
\[
P_m+\frac14=\frac{r^2}{4},
\]
so
\[
\boxed{
\sqrt{P_m+\frac14}=\frac{|r|}{2}
}
\]
for the positive square root, while the signed doubled completion is \(\pm r\).

Thus each signed \(U(24)\) state is represented by a pronic completion
\[
\boxed{
r=\pm2\sqrt{P_m+\frac14}.
}
\]

The sign is important: the positive square root alone gives a positive representative, whereas v13.530's third \(C_2\) coordinate is the arithmetic sign \(r\mapsto-r\).

## 5. Quotient to U(12): exactly the sign-forgetting projection [D]

Reduction modulo \(12\)
\[
\pi:U(24)\to U(12)
\]
pairs
\[
1\leftrightarrow13,\quad
5\leftrightarrow17,\quad
7\leftrightarrow19,\quad
11\leftrightarrow23.
\]

In v13.530 binary coordinates this quotient forgets one signed lift direction (equivalently identifies the two mod-24 lifts of each mod-12 unit). Therefore
\[
|U(24)|=8\longrightarrow |U(12)|=4
\]
is precisely the two-sheet-to-one reduction already suggested by v13.693.

[N] The pairings under reduction mod 12 are not identical to the notation \(\{\pm1,\pm5,\pm7,\pm11\}\) viewed as ordinary integer sign pairs; e.g. \(1\) and \(13\) have the same mod-12 image, while \(-1=23\) maps to \(11\). Thus one must distinguish “mod-24 lift sheet” from literal integer negation when describing the quotient.

## 6. Character dual: automatically the same dual C2^3 [D]

Because the pronic-root group is literally \(U(24)\), its character group is literally the same
\[
\widehat{U(24)}\cong C_2^3
\]
used in v13.530.

With the established binary pairing
\[
B(v,w)=ap+bq+cs\pmod2,
\qquad
\psi_v(w)=(-1)^{B(v,w)},
\]
the full dual table remains
\[
1,\quad
\chi_{-3},\quad
\chi_{-4},\quad
\chi_{12},\quad
\sigma,\quad
\sigma\chi_{-3},\quad
\sigma\chi_{-4},\quad
\sigma\chi_{12}.
\]

Therefore the pronic-root carrier does not merely have a character group of the same abstract type. It carries the exact previously audited character-dual structure after the identity
\[
R_{24}=U(24)
\]
is made.

## 7. Cone C2^3 intertwiner transfers without modification [D]

v13.530 established the basis-compatible isomorphism
\[
\Phi:U(24)\overset\sim\longrightarrow
\langle R_X,R_Y,S_T\rangle
\]
with
\[
\Phi(5^a7^b(-1)^c)=R_X^aR_Y^bS_T^c.
\]

Since \(R_{24}=U(24)\), the pronic-root carrier inherits exactly the same map:
\[
\boxed{
r=5^a7^b(-1)^c
\longmapsto
R_X^aR_Y^bS_T^c.
}
\]

In particular,
\[
5\leftrightarrow R_X,\qquad
7\leftrightarrow R_Y,\qquad
11\leftrightarrow R_XR_Y,
\]
and the signed half of the carrier adds the sheet-reversal coordinate \(S_T\) according to the existing v13.530 convention.

The previous canonicity guardrail remains unchanged: only the \(\chi_{-4}\leftrightarrow R_Y\) leg has the stronger intrinsic cyclotomic-complex justification; the full three-axis assignment is an explicit compatible intertwiner, not a newly proved basis-free canonical one.

## 8. CRT explanation of why 24 appears [D]

The equality is structural:
\[
24=8\cdot3,\qquad (8,3)=1.
\]

The half-integer completion produces an odd integer \(r=2m+1\). Every odd square obeys
\[
r^2\equiv1\pmod8.
\]
The additional condition
\[
6\mid m(m+1)
\]
is exactly the condition that \(r\not\equiv0\pmod3\), hence
\[
r^2\equiv1\pmod3.
\]
CRT then gives
\[
r^2\equiv1\pmod{24}.
\]

Thus the modulus \(24\) is not an accidental enlargement of \(12\): it is the natural modulus that simultaneously records the dyadic half-integer square condition (mod \(8\)) and the discriminant-12 unramified condition at \(3\).

[I] This supplies a precise arithmetic reason that the half-lattice completion naturally lifts the four-state \(U(12)\) carrier to an eight-state \(U(24)\) carrier.

## 9. Relation to the central 6,12 pronics [D]

For
\[
P_2=6,\qquad P_3=12,
\]
the completed doubled radii are
\[
r_2=5,\qquad r_3=7.
\]
These are exactly the first two nontrivial positive generators used in v13.530:
\[
5=(1,0,0),\qquad7=(0,1,0).
\]
Their product is
\[
5\cdot7=35\equiv11\pmod{24},
\]
so
\[
11=(1,1,0).
\]

Therefore the central consecutive-pronic pair generates the entire fixed-sign Klein four
\[
\boxed{
\langle5,7\rangle=\{1,5,7,11\},
}
\]
and adjoining the independent sign lift \(-1\) generates
\[
\boxed{
\langle5,7,-1\rangle=U(24)\cong C_2^3.
}
\]

Under the v13.530 cone map, this is
\[
\boxed{
\langle5,7\rangle
\leftrightarrow
\langle R_X,R_Y\rangle
}
\]
within a fixed cone sheet, while the sign generator supplies the third sheet-reversal direction.

## 10. Gate result

\[
\boxed{\textbf{PASS: }r^2\equiv1\pmod{24}\textbf{ defines exactly }U(24),\textbf{ element-for-element and with the same multiplication law.}}
\]

\[
\boxed{\textbf{PASS: the pronic half-integer carrier therefore inherits the exact previously audited character-dual }C_2^3\textbf{ structure.}}
\]

\[
\boxed{\textbf{PASS: the central pronics }6,12\textbf{ give the established generators }5,7,\textbf{ whose product is }11.}
\]

\[
\boxed{\textbf{PASS: adjoining the signed completion gives the eighth-state direction and the full }U(24)\cong C_2^3\textbf{ carrier.}}
\]

This closes the question at the finite-carrier level: the pronic mod-24 root carrier and the v13.530 \(U(24)\) carrier are not merely related; they are the same finite group.

## 11. Next controlled question

The remaining nontrivial issue is no longer carrier identity. It is dynamical/canonical structure:

- Does the pronic index evolution \(m\mapsto m+1\), after restriction to admissible \(6\mid m(m+1)\), induce any canonical walk or affine action on this \(C_2^3\)?
- Does the RMS \(35|36|37\) completion select the already-established \(\chi_{12}\) axis in a way compatible with the v13.530 cone half-turn and Pell time orientation?
- Can the signed square-root choice be identified intrinsically with the existing arithmetic-sign coordinate \(\sigma\), rather than merely by the compatible v13.530 basis convention?
