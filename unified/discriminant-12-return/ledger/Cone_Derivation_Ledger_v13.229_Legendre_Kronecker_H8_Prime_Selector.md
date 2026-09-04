# Cone Derivation Ledger v13.229 — Legendre/Kronecker H8 Prime Selector

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.225/v13.228; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README and current `master` tip were re-fetched. The tip remained

`8bdf8295335e00c0cf645dee0dfe33c114092027`

with v13.228 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry therefore extends the reconciled branch without overwriting newer work.

## 1. The discriminant-12 sign mode is the Legendre symbol (3/p)

For primes `p>3`, the primitive quadratic character of discriminant 12 satisfies

\[
\boxed{\chi_{12}(p)=\left(\frac{12}{p}\right)=\left(\frac{3}{p}\right).}
\]

Hence quadratic reciprocity gives

\[
\boxed{
\chi_{12}(p)=
\begin{cases}
+1,&p\equiv1,11\pmod{12},\\
-1,&p\equiv5,7\pmod{12}.
\end{cases}}
\]

Thus the previously derived string/Cone pattern

\[
\{1,11\}\mapsto +1,
\qquad
\{5,7\}\mapsto -1
\]

is exactly the quadratic-residue/nonresidue pattern for `3 mod p`.

For all integers, the precise extension is the Kronecker/Dirichlet character

\[
\chi_{12}(n)=\left(\frac{12}{n}\right),
\]

with value zero off the units. The `0` at the midpoint `6` is therefore a Dirichlet-character zero, not a Legendre symbol with denominator 6.

## 2. Splitting interpretation

For primes `p\nmid12`,

\[
\boxed{
\chi_{12}(p)=+1
\iff
p\text{ splits in }\mathbf Q(\sqrt3),
}
\]

and

\[
\boxed{
\chi_{12}(p)=-1
\iff
p\text{ is inert in }\mathbf Q(\sqrt3).
}
\]

The ramified primes `2,3` correspond to the zero value of the primitive discriminant-12 character.

Consequently the finite string sign mode already has the exact arithmetic meaning

\[
\boxed{+1=\text{split},\quad -1=\text{inert},\quad 0=\text{ramified/nonunit carrier}.}
\]

The last phrase is a carrier interpretation; only primes `2,3` are literally ramified primes.

## 3. The mod-24 sheet character is itself quadratic

Use the direct-product decomposition from v13.228,

\[
U(24)=A\times\langle13\rangle,
\qquad
A=\{1,5,7,11\}.
\]

Define the sheet character

\[
\eta(a13^\varepsilon)=(-1)^\varepsilon.
\]

Its values on the ordered carrier

\[
(1,5,7,11,13,17,19,23)
\]

are

\[
(1,1,1,1,-1,-1,-1,-1).
\]

Direct comparison with Kronecker characters gives the exact identity on `U(24)`

\[
\boxed{\eta=\chi_{-24}=\left(\frac{-24}{\cdot}\right).}
\]

Thus the extra Boolean sheet bit introduced by the mod-24 lift is not merely an abstract `C_2` coordinate: it is the quadratic character of the field

\[
\boxed{\mathbf Q(\sqrt{-6})}
\]

of fundamental discriminant `-24`.

## 4. The sheet-odd partner of chi12 is chi_{-8}

The sheet-even discriminant-12 mode is

\[
\widetilde\chi_{12}=\chi_{12}\otimes1.
\]

Multiplying by the sheet character gives its sheet-odd partner:

\[
(\chi_{12}\otimes1)\eta.
\]

On `U(24)`, Kronecker multiplication yields

\[
\boxed{\chi_{12}\chi_{-24}=\chi_{-8}.}
\]

Therefore

\[
\boxed{
\text{sheet-even }D=12\text{ mode}
\longleftrightarrow \chi_{12},
\qquad
\text{sheet-odd partner}
\longleftrightarrow \chi_{-8}.
}
\]

The sheet-odd companion is the primitive quadratic character of

\[
\boxed{\mathbf Q(\sqrt{-2})}.
\]

This is an exact character identity on the mod-24 unit carrier.

## 5. All eight H8 characters acquire quadratic labels

Start from the four `U(12)` characters

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12})
\]

and tensor them with sheet parity `1` or `eta=chi_{-24}`. In the product-character order

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12})\otimes(1,\eta),
\]

the sheet-odd products are

\[
\boxed{
\begin{aligned}
\chi_0\eta&=\chi_{-24},\\
\chi_{-4}\eta&=\chi_{24},\\
\chi_{-3}\eta&=\chi_{8},\\
\chi_{12}\eta&=\chi_{-8}.
\end{aligned}}
\]

Hence the eight Walsh characters on `U(24)` can be labeled by

\[
\boxed{
\chi_0,\chi_{-4},\chi_{-3},\chi_{12},
\chi_{-24},\chi_{24},\chi_8,\chi_{-8}.
}
\]

Guardrail: the first four are lifts to modulus 24 and need not all be primitive at conductor 24. The identities above are asserted on `U(24)`; global Dirichlet-series statements must retain the conductor/Euler-factor distinctions already emphasized in v13.225.

## 6. Exact H8 prime-selector theorem

For any character `psi` of `U(24)`, define

\[
a_\psi(m)=(1*\psi)(m)=\sum_{d\mid m}\psi(d).
\]

For a prime `p>3`,

\[
\boxed{a_\psi(p)=1+\psi(p).}
\]

Thus every H8 character channel receives either `2` or `0` at a prime.

Use character order

\[
(\chi_0,\chi_{-4},\chi_{-3},\chi_{12},
\chi_{-24},\chi_{24},\chi_8,\chi_{-8}).
\]

Then the exact increment table is

\[
\boxed{
\begin{array}{c|c}
p\bmod24 & \Delta\widehat S_{H_8}(p)\\
\hline
1  &(2,2,2,2,2,2,2,2)\\
5  &(2,2,0,0,2,2,0,0)\\
7  &(2,0,2,0,2,0,2,0)\\
11 &(2,0,0,2,2,0,0,2)\\
13 &(2,2,2,2,0,0,0,0)\\
17 &(2,2,0,0,0,0,2,2)\\
19 &(2,0,2,0,0,2,0,2)\\
23 &(2,0,0,2,0,2,2,0)
\end{array}}
\]

The first four entries reproduce the v13.225 mod-12 selector. The final four entries are its exact sheet-parity refinement.

## 7. Sheet-even versus sheet-odd selector formula

Write a prime carrier residue uniquely as

\[
p\equiv a13^\varepsilon\pmod{24},
\qquad a\in A,
\quad \varepsilon\in\{0,1\}.
\]

For a base `U(12)` character `chi`, the two H8 channels are

\[
\chi_{\rm even}=\chi,
\qquad
\chi_{\rm odd}=\chi\eta.
\]

Their prime increments are

\[
\boxed{
a_{\chi_{\rm even}}(p)=1+\chi(a),
}
\]

and

\[
\boxed{
a_{\chi_{\rm odd}}(p)=1+(-1)^\varepsilon\chi(a).}
\]

Therefore:

- on the lower sheet `epsilon=0`, even and odd partner channels receive the same selector;
- on the upper sheet `epsilon=1`, the odd partner is the Boolean complement of the even selector: `1-chi(a)` instead of `1+chi(a)`.

For the discriminant-12 pair specifically,

\[
\boxed{
a_{12}(p)=1+\left(\frac3p\right)}
\]

and

\[
\boxed{
a_{-8}(p)=1+\left(\frac{-2}{p}\right).}
\]

Thus the mod-24 sheet refinement splits the prime response into two genuine quadratic-residue tests.

## 8. Walsh inversion makes the selector geometrically sharp

Let `v_p(psi)=1+psi(p)` be the eight-component character-channel selector vector for a fixed `p\in U(24)`. Character orthogonality gives

\[
\sum_\psi (1+\psi(p))\psi(r)
=8\,\delta_{r,1}+8\,\delta_{r,p}.
\]

Equivalently, with the unnormalized `H_8` convention,

\[
\boxed{
H_8v_p=8(e_1+e_p).
}
\]

Hence the apparently distributed `0/2` prime response in character space is exactly a two-point object in residue space: the identity state plus the prime's own carrier state.

This is the cleanest finite intertwiner statement yet for the divisor selector:

\[
\boxed{
\text{prime residue }p
\xleftrightarrow{\ H_8\ }
\{\psi:\psi(p)=+1\}.
}
\]

The Walsh transform converts a residue location into the set of quadratic characters for which that residue is a `+1` state.

## 9. Relation to the string picture

The 12-node string mode

\[
\chi_{12}:\quad \{1,11\}\mapsto+1,
\quad \{5,7\}\mapsto-1
\]

is therefore simultaneously:

1. the Cone-symmetric sign pattern about `T=6`;
2. the primitive Legendre/Kronecker test `(3/p)`;
3. the split/inert character of `Q(sqrt3)`;
4. a 12-point DFT eigenmode;
5. the sheet-even `D=12` Walsh character inside `U(24)`.

Its mod-24 sheet-odd companion is not an arbitrary new bit: it is

\[
\chi_{-8}=\left(\frac{-8}{\cdot}\right),
\]

the quadratic character of `Q(sqrt{-2})`.

Thus the two-sheet lift exposes a second quadratic field while preserving the original discriminant-12 mode exactly.

## 10. Scope and next task

This checkpoint establishes exact finite-character and prime-selector identities. It does **not** yet identify the physical string analogy with a dynamical Hamiltonian, nor does it claim that sieve crossings act diagonally as time evolution.

The next high-value audit is to combine this H8 selector with the exact divisor-crossing schedules from v13.226. For each sieve prime `q`, derive the Walsh spectrum of the eight-slot crossing mask as block index `k` varies, and test whether the `chi12/chi_{-8}` pair is singled out by the first crossings `q=5,7`.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.
