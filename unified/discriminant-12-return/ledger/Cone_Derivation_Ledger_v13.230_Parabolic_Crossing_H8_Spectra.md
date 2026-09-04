# Cone Derivation Ledger v13.230 — Parabolic-Crossing H8 Spectra

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.226/v13.229; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`0f3c5a544b8196e0cec38591e930cc5f856506c4`

with v13.229 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry therefore extends the reconciled branch without overwriting newer work.

## 1. Crossing masks on the eight-state carrier

Use the ordered mod-24 carrier

\[
U(24)=(1,5,7,11,13,17,19,23).
\]

For a sieve prime `q>=5` and block index `k`, define the crossing mask

\[
C_q(k;r)=
\begin{cases}
1,&q\mid(24k+r),\\
0,&q\nmid(24k+r),
\end{cases}
\qquad r\in U(24).
\]

By v13.226,

\[
q\mid(24k+r)
\iff
k\equiv-r24^{-1}\pmod q.
\]

Thus every carrier slot occurs exactly once during a complete `q`-block cycle.

For an `H_8` character `psi`, define the Walsh coefficient of the crossing mask by

\[
\boxed{
\widehat C_q(k;\psi)
=\sum_{r\in U(24)}C_q(k;r)\psi(r).
}
\]

Use the character order from v13.229:

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12},
\chi_{-24},\chi_{24},\chi_8,\chi_{-8}).
\]

## 2. Exact q=5 crossing cycle

Since `24=-1 mod 5`, the hit condition is

\[
k\equiv r\pmod5.
\]

The five block classes give:

\[
\boxed{
\begin{array}{c|c|c}
k\bmod5 & \text{hit slots} & \widehat C_5(k)\\
\hline
0&\{5\}&(1,1,-1,-1,1,1,-1,-1)\\
1&\{1,11\}&(2,0,0,2,2,0,0,2)\\
2&\{7,17\}&(2,0,0,-2,0,-2,2,0)\\
3&\{13,23\}&(2,0,0,2,-2,0,0,-2)\\
4&\{19\}&(1,-1,1,-1,-1,1,-1,1)
\end{array}}
\]

The discriminant-12 channel across the five-cycle is therefore

\[
\boxed{
\widehat C_5(k;\chi_{12})=(-1,2,-2,2,-1),
}
\]

while its sheet-odd partner is

\[
\boxed{
\widehat C_5(k;\chi_{-8})=(-1,2,0,-2,1).
}
\]

Neither channel is isolated: other quadratic-character channels are nonzero in the same cycle.

## 3. Exact q=7 crossing cycle

Since `24^{-1}=5 mod 7`, the hit condition is

\[
k\equiv-5r\equiv2r\pmod7.
\]

The seven block classes give:

\[
\boxed{
\begin{array}{c|c|c}
k\bmod7 & \text{hit slots} & \widehat C_7(k)\\
\hline
0&\{7\}&(1,-1,1,-1,1,-1,1,-1)\\
1&\{11\}&(1,-1,-1,1,1,-1,-1,1)\\
2&\{1\}&(1,1,1,1,1,1,1,1)\\
3&\{5,19\}&(2,0,0,-2,0,2,-2,0)\\
4&\{23\}&(1,-1,-1,1,-1,1,1,-1)\\
5&\{13\}&(1,1,1,1,-1,-1,-1,-1)\\
6&\{17\}&(1,1,-1,-1,-1,-1,1,1)
\end{array}}
\]

Hence

\[
\boxed{
\widehat C_7(k;\chi_{12})=(-1,1,1,-2,1,1,-1),
}
\]

and

\[
\boxed{
\widehat C_7(k;\chi_{-8})=(-1,1,1,0,-1,-1,1).
}
\]

Again, the first crossing prime does not excite only the `chi12/chi_{-8}` pair. Single-slot hits generically have nonzero amplitude in all eight Walsh channels.

## 4. Exact answer to the question posed in v13.229

The first post-`2,3` parabolic crossings `q=5,7` do **not** define a closed two-channel subsystem on

\[
(\chi_{12},\chi_{-8}).
\]

The reason is structural. A single residue-space delta `e_r` has Walsh transform equal to the full character column

\[
\boxed{
H_8e_r=(\psi(r))_\psi,
}
\]

so every one-slot crossing has support in all eight character channels.

Two-slot crossings can cancel selected channels, as seen above, but the surviving subset depends on the actual block class. There is no block-independent projection onto only the discriminant-12 pair.

Therefore the exact conclusion is

\[
\boxed{
\text{local parabolic crossings require the full }H_8\text{ cube.}
}
\]

The `chi12/chi_{-8}` pair remains distinguished arithmetically by the quadratic-field interpretation of v13.229, but it is not dynamically closed under the raw `q=5,7` crossing masks.

## 5. Full-cycle cancellation of every nonprincipal channel

Although local crossing masks populate many Walsh channels, the complete `q`-block cycle is perfectly balanced.

Each carrier slot is struck exactly once, so

\[
\sum_{k=0}^{q-1}C_q(k;r)=1
\qquad(r\in U(24)).
\]

Thus

\[
\sum_{k=0}^{q-1}C_q(k)=\mathbf 1,
\]

and applying `H_8` gives

\[
\boxed{
\sum_{k=0}^{q-1}\widehat C_q(k)
=(8,0,0,0,0,0,0,0).
}
\]

For every nonprincipal character `psi`, including `chi12` and `chi_{-8}`,

\[
\boxed{
\sum_{k=0}^{q-1}\widehat C_q(k;\psi)=0.
}
\]

This is an important guardrail: the ordinary periodic sieve itself has no net long-cycle preference for the discriminant-12 mode. The nonprincipal amplitudes are oscillatory local structure whose mean vanishes over a complete crossing cycle.

For `q=5`, indeed

\[
-1+2-2+2-1=0,
\]

and for `q=7`,

\[
-1+1+1-2+1+1-1=0.
\]

## 6. Combined 5-and-7 supercycle

Now form the union mask

\[
C_{5\cup7}(k;r)
=1
\iff
5\mid(24k+r)\ \text{or}\ 7\mid(24k+r).
\]

The natural joint period is `35` blocks.

Across the 35 block classes, the number of distinct removed carrier slots per block is exactly distributed as

\[
\boxed{
\begin{array}{c|c}
\text{removed slots in block} & \text{number of block classes}\\
\hline
2&20\\
3&12\\
4&3
\end{array}}
\]

so every block loses at least two carrier positions, recovering the sharp `<=6` prime ceiling of v13.226.

The total number of removed carrier positions over the full supercycle is

\[
20\cdot2+12\cdot3+3\cdot4=88.
\]

This also follows from inclusion-exclusion:

\[
56+40-8=88,
\]

because the `q=5` sieve contributes `8\cdot7=56` hits, the `q=7` sieve contributes `8\cdot5=40` hits, and exactly `8` carrier positions are simultaneous multiples of `35`, one per carrier slot by CRT.

Hence the survivors are

\[
280-88=192,
\]

which is exactly

\[
280\cdot\frac45\frac67=192.
\]

This independently reproduces the exact wheel-sieve density from v13.226.

## 7. Character balance of the 35-block union sieve

For each fixed carrier slot `r`, among 35 consecutive blocks the union condition occurs

\[
7+5-1=11
\]

times. Therefore

\[
\sum_{k=0}^{34}C_{5\cup7}(k)=11\mathbf1.
\]

Applying `H_8`,

\[
\boxed{
\sum_{k=0}^{34}\widehat C_{5\cup7}(k)
=(88,0,0,0,0,0,0,0).
}
\]

So the complete `5x7` CRT supercycle again contains only the principal component after averaging; every quadratic-character channel cancels exactly.

This sharpens the distinction between two effects:

1. **prime selector increments** from v13.229, where a prime residue has a definite quadratic-character signature;
2. **composite sieve crossings**, where the local masks fluctuate through the full Walsh cube and all nonprincipal components cancel over the complete period.

These are related by the same transform but are not the same operator.

## 8. Geometric interpretation

For each hit `r` in a block `k`, the integer

\[
N=24k+r
\]

has a row-parabola crossing at `y=q` because

\[
q\mid N.
\]

Thus the Walsh spectrum above is the exact character decomposition of the set of Paper-A row-parabola crossings on the eight-state mod-24 carrier.

The result is therefore a genuine arithmetic/geometry/transform bridge:

\[
\boxed{
\text{row-}q\text{ parabolic crossings}
\longleftrightarrow
\text{residue-space crossing mask}
\xleftrightarrow{H_8}
\text{quadratic-character spectrum}.
}
\]

However, `H_8` is a change of basis, not a physical time-evolution operator. The block index `k` supplies a discrete periodic schedule, but no Hamiltonian or wave equation has been introduced.

## 9. New structural conclusion

The branch now separates three exact levels:

\[
\boxed{
\text{position basis: carrier slots }r\in U(24),
}
\]

\[
\boxed{
\text{character basis: eight quadratic Walsh modes},
}
\]

and

\[
\boxed{
\text{block-time schedule: }k\bmod q\text{ for each sieve prime }q.
}
\]

The crossing operator is sparse in the position basis, broad and oscillatory in the character basis, and periodic in the block index. This is the first exact three-way decomposition of the parabolic sieve in the Cone project.

The discriminant-12 mode remains special because of its independent Legendre/splitting/Fourier/Cone meaning, not because raw `5,7` crossings project exclusively onto it.

## 10. Next task

The natural next transform is now on the **block index** itself. For each `q`, take the cyclic `q`-point DFT of

\[
k\mapsto\widehat C_q(k;\psi).
\]

Because every carrier slot follows a single arithmetic progression in `k mod q`, this second transform should diagonalize the periodic crossing schedule. The resulting object is a two-stage transform:

\[
\boxed{
\text{carrier }U(24)
\xrightarrow{H_8}
\text{quadratic characters}
\quad\text{and}\quad
\text{block index }\mathbf Z/q\mathbf Z
\xrightarrow{\mathrm{DFT}_q}
\text{crossing frequencies}.
}
\]

That is the correct place to test whether the user's string/harmonic picture acquires a precise spectral meaning for the divisor-crossing dynamics.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.
