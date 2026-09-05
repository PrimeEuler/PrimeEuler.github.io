# Cone Derivation Ledger v13.232 — q=7 Legendre-Resonance Rigidity

Date: 2026-09-04
Status: EXACT NEW RESULT — continuation of v13.231; research branch remains open

## 0. Pre-write synchronization

Immediately before this write, the authoritative README and current `master` tip were re-fetched. The tip remained

`712a097136855da1cc205e829d7f4cb5ac9bc9fc`

with v13.231 as the highest ledger checkpoint. No newer external-audit checkpoint had landed. This entry extends that reconciled branch without revising the audited principal paper.

## 1. Question

Ledger v13.231 found the exact identity

\[
\widehat C_7(k;\chi_{-8})=-\left(\frac{k-3}{7}\right)
\]

and hence the flat nonzero Gauss spectrum

\[
|\mathcal C_7(m;\chi_{-8})|=\sqrt7,
\qquad m\ne0.
\]

The next question was whether this belongs to a larger family of crossing primes `q`: can another quadratic `H_8` character produce, up to shift and sign, a Legendre sequence in the block variable?

The answer for the fixed eight-state `U(24)` carrier is much more rigid than expected.

## 2. General crossing signal

Let

\[
R=U(24)=\{1,5,7,11,13,17,19,23\},
\]

and let `psi` be one of the seven nonprincipal quadratic characters of `U(24)`. For prime `q>=5`, define

\[
f_{q,\psi}(k):=\widehat C_q(k;\psi)
=\sum_{r\in R\atop k\equiv-r24^{-1}\,(q)}\psi(r).
\]

When the eight carrier residues are distinct modulo `q`, `f_{q,psi}` has exactly eight nonzero entries, each equal to `+1` or `-1`.

For every nonprincipal `psi`,

\[
\sum_{k\bmod q}f_{q,\psi}(k)=\sum_{r\in R}\psi(r)=0.
\]

## 3. Support obstruction to a Legendre-sequence family

A shifted signed Legendre sequence

\[
g_{q,a,\epsilon}(k)
=\epsilon\left(\frac{k-a}{q}\right),
\qquad \epsilon\in\{\pm1\},
\]

has exactly one zero and therefore exactly `q-1` nonzero entries.

For every prime `q>23`, the eight carrier residues are distinct modulo `q`, so `f_{q,psi}` has exactly eight nonzero entries. Hence equality

\[
f_{q,\psi}=g_{q,a,\epsilon}
\]

would force

\[
q-1=8,
\]

which is impossible for prime `q`.

Therefore

\[
\boxed{
q>23\Longrightarrow
f_{q,\psi}\text{ is never a shifted signed Legendre sequence.}
}
\]

This is an exact obstruction, not a numerical observation.

Thus the v13.231 phenomenon cannot extend to arbitrarily large crossing primes on the fixed eight-state carrier.

## 4. Finite small-prime audit

The only remaining primes are

\[
q\in\{5,7,11,13,17,19,23\}.
\]

An exhaustive exact audit was performed over:

- all seven nonprincipal `H_8` characters
  \[
  \chi_{-4},\chi_{-3},\chi_{12},\chi_{-24},\chi_{24},\chi_8,\chi_{-8};
  \]
- every shift `a mod q`;
- both overall signs `epsilon=+/-1`.

The unique match is

\[
\boxed{
(q,\psi,a,\epsilon)=(7,\chi_{-8},3,-1).
}
\]

Equivalently,

\[
\boxed{
\widehat C_7(k;\chi_{-8})
=-\left(\frac{k-3}{7}\right)
}
\]

is the unique shifted signed Legendre sequence among all prime crossing schedules on the fixed `U(24)` carrier.

The finite audit is only needed for `q<=23`; the support argument proves all larger primes impossible.

## 5. Flat-spectrum rigidity theorem for large q

The Legendre identity is stronger than flat Fourier magnitude, so we separately ask whether another crossing signal can have a flat nonzero-frequency spectrum without literally being a Legendre sequence.

Assume `q>23`, so the eight crossing times are distinct. Let

\[
f(k)=f_{q,\psi}(k).
\]

Then

\[
\sum_k|f(k)|^2=8,
\qquad
\widehat f(0)=0.
\]

Suppose all nonzero DFT frequencies have a common squared magnitude `A`:

\[
|\widehat f(m)|^2=A,
\qquad m\ne0.
\]

Parseval gives

\[
(q-1)A=8q,
\]

so

\[
A=\frac{8q}{q-1}.
\]

Now let the cyclic autocorrelation be

\[
R(t)=\sum_{k\bmod q}f(k)f(k+t).
\]

By inverse Fourier transform of the power spectrum, for every nonzero `t`,

\[
R(t)
=\frac1q\sum_{m\bmod q}|\widehat f(m)|^2e^{-2\pi i mt/q}
=-\frac{A}{q}
=-\frac8{q-1}.
\]

But `f(k)` is integer-valued, so every `R(t)` is an integer. Hence

\[
\boxed{q-1\mid8.}
\]

No prime `q>23` satisfies this. Therefore

\[
\boxed{
q>23\Longrightarrow
\text{no nonprincipal }H_8\text{ crossing channel has flat nonzero DFT magnitude.}
}
\]

This is a stronger theorem than the support obstruction: even a non-Legendre flat spectrum is impossible at large crossing primes on the fixed eight-state carrier.

## 6. Small-prime flat-spectrum audit

The same exact finite audit for

\[
q\in\{5,7,11,13,17,19,23\}
\]

shows that the only nonprincipal crossing channel with constant magnitude over every nonzero block frequency is again

\[
\boxed{q=7,\qquad\psi=\chi_{-8}.}
\]

Its common magnitude is

\[
\sqrt7,
\]

as proved by the Gauss-sum formula in v13.231.

Combining the finite audit with the large-prime autocorrelation obstruction gives the global rigidity statement:

\[
\boxed{
\text{Among all prime }q\ge5\text{ and all nonprincipal }H_8\text{ channels,}
\quad
(q,\psi)=(7,\chi_{-8})
\text{ is the unique flat nonzero-frequency crossing spectrum.}
}
\]

This statement is for the fixed `U(24)` eight-state carrier and the crossing operator defined in v13.230. It should not be generalized to other carriers without a new proof.

## 7. Why q=7 can occur

The rigidity theorem clarifies the combinatorial reason `q=7` is exceptional.

A Legendre sequence modulo `q` has `q-1` nonzero positions. The eight carrier states must collapse modulo `q` so that their signed crossing contributions produce exactly that support and the required quadratic signs.

At `q=7`, the eight carrier states reduce with one collision pattern sufficient to produce the seven-point signal

\[
(-1,1,1,0,-1,-1,1),
\]

which is exactly a translated negative quadratic character.

For `q>23`, there are no carrier collisions at all, and the support is frozen at eight positions while a Legendre sequence grows to `q-1` positions. The resonance is therefore intrinsically a small-prime/carrier-size compatibility.

This is more precise than calling `7` a generic harmonic crossing prime.

## 8. Relation to the discriminant-12 channel

The exceptional character is

\[
\chi_{-8}=\chi_{12}\chi_{-24}.
\]

Thus the flat Legendre/Gauss mode is not the sheet-even discriminant-12 character itself. It is its sheet-odd partner in the mod-24 Boolean lift.

The exact hierarchy is now

\[
\boxed{
U(12)\text{ discriminant-12 mode }\chi_{12}
\xrightarrow{\text{mod-24 lift}}
(\chi_{12},\chi_{-8})
}
\]

and only the sheet-odd member satisfies

\[
\boxed{
\chi_{-8}
\xrightarrow{q=7\text{ crossings}}
-\left(\frac{k-3}{7}\right)
\xrightarrow{\mathrm{DFT}_7}
\text{flat quadratic Gauss spectrum}.
}
\]

This makes the sheet bit mathematically essential to the resonance.

## 9. Guardrails

1. `q=7` is uniquely resonant for this fixed eight-state crossing construction; this is not a claim that 7 is universally privileged in prime theory.
2. Flat DFT magnitude is a finite spectral property, not a physical energy spectrum unless a dynamical operator is separately introduced.
3. The Legendre character modulo 7 and the mod-24 character `chi_{-8}` live on different finite groups. Their equality occurs only after the crossing map converts the carrier character into a block-index signal.
4. The result does not revise the principal Discriminant-12 v0.3.5 theorem package.

## 10. Structural conclusion

The attempted search for a broad reciprocity family instead produced a rigidity theorem:

\[
\boxed{
\text{the }q=7,\chi_{-8}\text{ Gauss resonance is isolated on }U(24).
}
\]

The mechanism is now exact at three levels:

\[
\boxed{
\text{Boolean carrier character}
\longrightarrow
\text{parabolic-crossing time signal}
\longrightarrow
\text{cyclic Fourier spectrum}.
}
\]

At the unique resonant pair, the middle object becomes a quadratic character of the crossing prime itself.

## 11. Next task

The next useful question is no longer to search blindly over larger `q` on the same carrier. The rigidity theorem rules that out.

Instead, test **carrier scaling**. For a larger wheel `U(M)`, ask when a quadratic character on the carrier can descend through a crossing map to a shifted Legendre character modulo a crossing prime `q`. The support count suggests a necessary compatibility between `phi(M)`, collision multiplicities modulo `q`, and `q-1`.

That is the correct setting for a genuine family theorem, if one exists.

Do not revise the audited principal v0.3.5 source from this checkpoint alone.
