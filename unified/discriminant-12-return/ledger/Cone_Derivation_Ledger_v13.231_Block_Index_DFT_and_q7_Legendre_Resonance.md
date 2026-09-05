# Cone Derivation Ledger v13.231 — Block-Index DFT and q=7 Legendre Resonance

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.230; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative project README, current `master` tip, and v13.230 were re-fetched. The tip remained

`5e66b038d4e86735fa6ef198f31c21b4165f6ecf`

with v13.230 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry therefore extends the reconciled branch without overwriting newer work.

## 1. Second transform: Fourier analysis in block index

Retain the v13.230 crossing mask

\[
C_q(k;r)=1
\iff q\mid(24k+r),
\qquad r\in U(24),\quad k\in\mathbf Z/q\mathbf Z.
\]

For an `H_8` character `psi`, the Walsh coefficient is

\[
\widehat C_q(k;\psi)
=\sum_{r\in U(24)}C_q(k;r)\psi(r).
\]

Now take the unnormalized cyclic `q`-point DFT in the block variable:

\[
\boxed{
\mathcal C_q(m;\psi)
:=\sum_{k\bmod q}
\widehat C_q(k;\psi)
\exp\left(\frac{2\pi i mk}{q}\right),
}
\]

where `m in Z/qZ` is the block-frequency index.

By the exact crossing schedule

\[
k\equiv-r24^{-1}\pmod q,
\]

only one block class contributes for each fixed carrier slot. Therefore

\[
\boxed{
\mathcal C_q(m;\psi)
=
\sum_{r\in U(24)}
\psi(r)
\exp\left(
-\frac{2\pi i m r\,24^{-1}}{q}
\right).
}
\]

This is the exact mixed Walsh/cyclic transform of the parabolic crossing relation.

Thus the periodic crossing schedule is completely diagonalized in block-frequency space: each residue slot `r` contributes one pure phase

\[
\exp\left(-2\pi i m r24^{-1}/q\right).
\]

## 2. Exact two-stage transform

The full crossing data now lives on

\[
U(24)\times\mathbf Z/q\mathbf Z.
\]

Applying `H_8` in the carrier coordinate and `DFT_q` in the block coordinate gives

\[
\boxed{
C_q(k;r)
\xrightarrow{\ H_8\otimes\mathrm{DFT}_q\ }
\mathcal C_q(m;\psi).
}
\]

Equivalently,

\[
\boxed{
\text{carrier position}
\leftrightarrow
\text{quadratic-character mode}
}
\]

and independently

\[
\boxed{
\text{crossing time }k
\leftrightarrow
\text{block frequency }m.
}
\]

This is an exact finite spectral decomposition. It does not require a physical Hamiltonian.

## 3. Zero frequency recovers the full-cycle cancellation theorem

At `m=0`,

\[
\mathcal C_q(0;\psi)
=\sum_{r\in U(24)}\psi(r).
\]

Therefore

\[
\boxed{
\mathcal C_q(0;\chi_0)=8,
}
\]

while for every nonprincipal `H_8` character,

\[
\boxed{
\mathcal C_q(0;\psi)=0.
}
\]

Thus the v13.230 complete-cycle cancellation is exactly the statement that all nonprincipal crossing channels have zero DC component.

The local oscillations found in v13.230 are therefore entirely carried by nonzero block frequencies.

## 4. Parseval guardrail

For any fixed character `psi`, Parseval gives

\[
\boxed{
\sum_{m\bmod q}|\mathcal C_q(m;\psi)|^2
=q\sum_{k\bmod q}|\widehat C_q(k;\psi)|^2.
}
\]

For primes `q>23`, the eight elements of `U(24)` remain distinct modulo `q`, so every block class contains at most one hit from the eight-state carrier. Hence for every quadratic `H_8` character, whose carrier values are all `+/-1`,

\[
\sum_k|\widehat C_q(k;\psi)|^2=8.
\]

Consequently

\[
\boxed{
q>23
\Longrightarrow
\sum_m|\mathcal C_q(m;\psi)|^2=8q.
}
\]

For nonprincipal `psi`, the zero mode vanishes, so all `8q` units of spectral energy lie in the nonzero block frequencies.

For `q=5,7`, collisions of carrier residues modulo `q` modify the energy distribution, exactly as seen in v13.230.

## 5. The q=7 sheet-odd D=12 partner becomes a Legendre sequence

The most striking exact specialization occurs for

\[
q=7,
\qquad
\psi=\chi_{-8}.
\]

From v13.230,

\[
\widehat C_7(k;\chi_{-8})
=(-1,1,1,0,-1,-1,1),
\qquad k=0,\ldots,6.
\]

Let

\[
\lambda_7(t)=\left(\frac{t}{7}\right)
\]

be the quadratic Legendre character modulo `7`, extended by `lambda_7(0)=0`.

Direct comparison gives the exact identity

\[
\boxed{
\widehat C_7(k;\chi_{-8})
=-\left(\frac{k-3}{7}\right).
}
\]

Thus the block-time crossing signal in the `chi_{-8}` channel is itself a shifted quadratic character modulo the crossing prime `7`.

This is not an analogy: it is an exact equality of the seven values.

## 6. Gauss-sum diagonalization of the q=7 resonance

For `m neq 0 mod 7`, use the shifted Legendre identity:

\[
\mathcal C_7(m;\chi_{-8})
=-\sum_{k\bmod7}
\left(\frac{k-3}{7}\right)
 e^{2\pi i mk/7}.
\]

Set `t=k-3`. Then

\[
\mathcal C_7(m;\chi_{-8})
=-e^{6\pi i m/7}
\sum_{t\bmod7}
\left(\frac{t}{7}\right)e^{2\pi i mt/7}.
\]

The quadratic Gauss sum satisfies

\[
\tau_7
:=\sum_{t\bmod7}
\left(\frac{t}{7}\right)e^{2\pi i t/7}
=i\sqrt7,
\]

and for `m neq 0`,

\[
\sum_t
\left(\frac{t}{7}\right)e^{2\pi i mt/7}
=\left(\frac{m}{7}\right)\tau_7.
\]

Hence

\[
\boxed{
\mathcal C_7(m;\chi_{-8})
=-i\sqrt7
\left(\frac{m}{7}\right)
 e^{6\pi i m/7},
\qquad m=1,\ldots,6.
}
\]

Therefore every nonzero block frequency has the same magnitude:

\[
\boxed{
|\mathcal C_7(m;\chi_{-8})|=\sqrt7,
\qquad m\ne0.
}
\]

Equivalently,

\[
\boxed{
|\mathcal C_7(m;\chi_{-8})|^2=7
\quad\text{for all }m=1,\ldots,6.
}
\]

This is a perfectly flat nonzero-frequency spectrum.

## 7. Uniqueness inside the nonprincipal H8 channels at q=7

An explicit audit of all eight `H_8` channels at `q=7` shows:

- the principal channel has the expected nonzero DC term and equal unit magnitude in its six nonzero frequencies;
- among the seven nonprincipal quadratic-character channels, only `chi_{-8}` has a flat nonzero-frequency power spectrum.

Thus within the nonprincipal `H_8` sector,

\[
\boxed{
\chi_{-8}
\text{ is uniquely selected at }q=7
\text{ by flat block-frequency magnitude.}
}
\]

This is much stronger than the raw crossing-space observation of v13.230, where the `chi_{-8}` channel did not appear dynamically closed.

The second transform reveals a hidden quadratic regularity that is invisible in the local Walsh amplitudes alone.

## 8. Relation back to the discriminant-12 mode

From v13.229,

\[
\chi_{-8}=\chi_{12}\chi_{-24},
\]

so `chi_{-8}` is exactly the sheet-odd partner of the original discriminant-12 character.

Therefore the first generator-side crossing prime `7` produces the chain

\[
\boxed{
\chi_{12}
\xrightarrow{\text{mod-24 sheet odd}}
\chi_{-8}
\xrightarrow{\ q=7\text{ crossings}}
-\left(\frac{k-3}{7}\right)
\xrightarrow{\mathrm{DFT}_7}
\text{flat Gauss spectrum of radius }\sqrt7.
}
\]

This is the first place in the branch where the string/harmonic intuition becomes an exact arithmetic spectral theorem rather than only a geometric metaphor.

The word `harmonic` is justified here in the finite Fourier sense: the crossing sequence has an exact cyclic Fourier spectrum governed by a quadratic Gauss sum. No physical wave equation is being claimed.

## 9. Comparison with q=5

For `q=5`, the discriminant-12 pair from v13.230 is

\[
\widehat C_5(k;\chi_{12})=(-1,2,-2,2,-1),
\]

\[
\widehat C_5(k;\chi_{-8})=(-1,2,0,-2,1).
\]

Neither is a shifted Legendre character modulo `5`, and neither has a flat nonzero-frequency power spectrum.

Therefore the `q=7`, `chi_{-8}` resonance is not a generic artifact of applying a second DFT to every crossing prime.

At the first two post-`2,3` sieve primes,

\[
\boxed{
q=5:\ \text{no corresponding pure quadratic block signal found},
}
\]

whereas

\[
\boxed{
q=7:\ \chi_{-8}\text{ becomes exactly a shifted Legendre sequence}.
}
\]

This distinction should be retained as an exact observed theorem at `q=7`, not extrapolated to all primes without proof.

## 10. Mixed transform kernel as the next general object

The natural general object is now

\[
\boxed{
K_q(m,\psi)
:=
\sum_{r\in U(24)}
\psi(r)
\exp\left(-\frac{2\pi i m r24^{-1}}q\right).
}
\]

For fixed `q`, this is an `8 x q` mixed character/exponential kernel.

It intertwines three structures already established independently:

1. the Boolean unit group `U(24) ~= C_2^3`;
2. its eight quadratic Kronecker characters;
3. the cyclic crossing clock `Z/qZ` generated by the row-`q` parabola.

The `q=7`, `chi_{-8}` row of this kernel is an exact shifted quadratic Gauss-sum row.

A high-value next audit is to classify for which primes `q` and which `H_8` characters `psi` the sequence `k -> C_hat_q(k;psi)` becomes, up to shift/sign/scale, a multiplicative character modulo `q`, or equivalently when the mixed kernel row has Gauss-sum flatness.

That classification could determine whether the `q=7` resonance is isolated, belongs to a congruence family, or reflects a deeper reciprocity relation between the mod-24 quadratic field labels and the crossing prime.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.
