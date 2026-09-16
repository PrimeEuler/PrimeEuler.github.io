# Cone Derivation Ledger v13.485 — chi12 Prime-Phase Bridge Level-0 Gate

Date: 2026-09-16

Status labels: **[D]** exact derived, **[N]** numerical diagnostic, **[Audit]** guardrail.

## 0. Synchronization

Live ledger checked before work and immediately before this write. Parallel work had advanced through v13.484; v13.485 was free.

## 1. Purpose

Start the preregistered source-faithful numerical test of whether the discriminant-12 local phase law

\[
\Theta_{p,m}(t)=m(\pi\epsilon_p-t\log p),\qquad
\chi_{12}(p)=(-1)^{\epsilon_p},
\]

can propagate from Euler prime-power source channels into the Suzuki spectral reduction.

This first checkpoint is deliberately only **Level 0**: verify provenance and the algebraic clock identity on the prime-power support actually used by the canonical source-faithful M=3999 replay. No downstream bridge statistic is inspected yet.

## 2. Frozen source provenance [Audit]

The canonical M=3999 unresolved-four-plane replay uses

\[
q\in\{2,3,4,5,7\},
\]

with von-Mangoldt source bases

\[
\{2,3,2,5,7\}
\]

and weights

\[
\frac{\Lambda(q)}{\sqrt q}.
\]

Its scalar prime source is

\[
P_n=\sum_q\frac{\Lambda(q)}{\sqrt q}
\sin\!\left(\frac{n\pi}{2}\log q\right),
\]

and its prime diagonal source is decomposed from the same q channels before entering the finite Schur pipeline.

The new diagnostic preserves exactly this support rather than inserting a larger Euler product by hand.

## 3. Local clock identity [D]

For an unramified prime p, write

\[
\chi_{12}(p)=(-1)^{\epsilon_p},\qquad \epsilon_p\in\{0,1\}.
\]

For q=p^m,

\[
\chi_{12}(q)=\chi_{12}(p)^m=e^{im\pi\epsilon_p}.
\]

Therefore

\[
-\Im e^{i\Theta_{p,m}(t)}
=\chi_{12}(p)^m\sin(t\log p^m).
\]

This is an exact identity. It is a unit/provenance check, not evidence for a spectral bridge.

The ramified p=2,3 channels are retained as controls and are not assigned epsilon_p.

## 4. First executable artifact [N]

Added

`research-notes/suzuki_chi12_prime_phase_bridge_level0.py`.

It:

1. resolves every canonical q into p^m;
2. records p,m,q, log p, log q, Lambda(q)/sqrt(q), residue mod 12, chi12(p), chi12(q), epsilon_p, and ramification status;
3. evaluates the source channels on every odd mode 1<=n<=3999;
4. independently evaluates the Theta clock channel;
5. asserts agreement for all unramified canonical channels;
6. keeps the diagonal-source decomposition explicit for the next Schur-derivative stage.

A local independent binary64 replay of the unramified q=5,7 identity over all odd n<=3999 gives maximum discrepancy approximately

\[
\boxed{2.43\times10^{-13}},
\]

comfortably inside the deliberately conservative 2e-12 Level-0 assertion. This discrepancy is ordinary finite-precision trigonometric argument reduction; the mathematical identity is exact.

## 5. Important limitation discovered before Level 1 [Audit]

The current canonical Suzuki source support contains only q=2,3,4,5,7. Consequently its **unramified chi12 channels are only p=5 and p=7**, both with chi12=-1 and m=1.

Therefore the present source cannot by itself test:

- positive chi12 prime classes p=1,11 mod 12;
- unramified m>=2 exponent alternation;
- a statistically meaningful many-prime phase law.

Those channels must not be fabricated and inserted into the canonical operator. A genuine larger-prime test requires deriving the corresponding source-faithful Suzuki formula/support first.

This changes the immediate Level-1 design: first test whether the existing p=5 and p=7 channel perturbations propagate coherently through the exact M3999 Schur map; treat p=2,3,4 as ramified controls. Any broader Euler-prime test remains a separate derivation target.

## 6. Next executable target

Implement the analytic Frechet derivative of the M=3999 Schur complement

\[
S=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC}
\]

under a source-channel perturbation:

\[
\begin{aligned}
dS={}&dA_{CC}-dA_{CF}A_{FF}^{-1}A_{FC}
-A_{CF}A_{FF}^{-1}dA_{FC}\\
&+A_{CF}A_{FF}^{-1}dA_{FF}A_{FF}^{-1}A_{FC}.
\end{aligned}
\]

Then project

\[
B_q=N^T(dS_q)N
\]

onto the already-frozen unresolved four-plane. No terminal-direction fitting is permitted before this propagation stage is frozen.

## 7. Guardrail

Level-0 PASS means only that the local chi12 phase identity has been implemented correctly on the canonical source channels. It is not evidence for Pell/Euler/Suzuki intertwining and implies no exact-zero, kernel, critical-line, RH, or GRH statement.

Artifact commit:
`9b9b67170a0dbdf4434f49ec6350a6678d4568fd`
