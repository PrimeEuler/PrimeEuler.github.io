# Cone Derivation Ledger v13.456 — Even Terminal Prime-Channel Cancellation Diagnostic

Date: 2026-09-14

Status labels: **[N]** numerical diagnostic, **[I]** interpretation, **[Audit]** guardrail.

## 0. Synchronization [Audit]

A live-head check immediately before this write found v13.455 as the newest numbered ledger entry; the new prime-channel research helper was unnumbered. Therefore v13.456 was free.

The theorem-level full parity bound remains

\[
\operatorname{ind}_{\le0}(A_{a=1})\le6.
\]

This checkpoint does not improve that theorem. It refines the structural interpretation of the unresolved even four-plane from v13.455.

## 1. Reproducible helper

The new diagnostic is

`research-notes/suzuki_terminal_even_prime_channel_diagnostic.py`.

It uses the frozen exact-dyadic six-dimensional positive basis on the even-v low core

\[
\{1,3,5,7,9,11,13,15,17,19\}
\]

and forms the numerical four-dimensional orthogonal complement. The complement is compared with the four unit residue classes \(1,5,7,11\pmod{12}\).

The same principal cosines as v13.455 are recovered:

\[
0.93574,\quad0.71268,\quad0.70240,\quad0.23512.
\]

Thus three unresolved directions are substantially residue/V4 aligned, while one is not.

## 2. Exceptional direction remains n=3 dominated [N]

The least-V4-aligned unresolved direction has absolute \(n=3\) coordinate above

\[
\boxed{0.94}.
\]

This confirms the v13.455 localization diagnostic.

## 3. Additive raw prime-source blocks [D formula / N evaluation]

For one source index \(q\in\{2,3,4,5,7\}\), define the additive prime sequence

\[
P_n^{(q)}
=
\frac{\Lambda(q)}{\sqrt q}
\sin\!\left(\frac{n\pi\log q}{2}\right),
\qquad
Z_n^{(q)}=2P_n^{(q)}.
\]

The same-parity off-diagonal prime block is

\[
(A_q)_{mn}
=-\frac{2}{\pi}
\frac{nZ_m^{(q)}-mZ_n^{(q)}}{n^2-m^2},
\qquad m\ne n,
\]

with the source-faithful diagonal contribution

\[
(A_q)_{nn}
=-\frac{\Lambda(q)}{\sqrt q}
\left[(2-\log q)\cos(k_n\log q)
+\frac{\sin(k_n\log q)}{k_n}\right],
\qquad k_n=\frac{n\pi}{2}.
\]

These blocks add linearly inside the raw low-core quadratic form.

## 4. Exceptional raw prime balance [N]

For the least-V4-aligned unresolved unit vector \(w_*\), the raw prime-block Rayleigh contributions are

\[
\boxed{
\begin{array}{c|r}
q&w_*^TA_qw_*\\
\hline
2&+0.5833984\\
3&-0.2956044\\
4&-0.1150869\\
5&-0.0166985\\
7&-1.13\times10^{-7}
\end{array}}
\]

Therefore the exceptional direction is **not** a pure q=3 channel.

Its prime contribution is instead governed by a strong cancellation pattern

\[
\boxed{
q=2\text{ positive}
\quad\text{versus}\quad
q=3,4\text{ negative},
}
\]

with q=5 secondary and q=7 essentially absent on this particular direction.

## 5. Interpretation [I]

v13.455 suggested that the fourth unresolved even direction might be a prime-3 ramified defect because it is concentrated on the first \(n=3\) core mode.

The prime-channel decomposition now sharpens that statement:

- the geometric/core localization at \(n=3\) is real numerically;
- however the source balance is not controlled by q=3 alone;
- the dominant mechanism is a cancellation between the q=2 channel and the q=3/q=4 channels.

This is compatible with the discriminant-12 local picture, where primes 2 and 3 are the two ramified primes selected intrinsically by the field. It suggests that the exceptional terminal direction may be a **ramified-prime interaction mode**, rather than a single-prime mode.

This interpretation remains provisional because the full finite Schur complement is nonlinear in the high-block inverse.

## 6. Why this is not yet a Schur decomposition [Audit]

The finite Schur complement is

\[
S_F=A_{CC}-A_{CF}A_{FF}^{-1}A_{FC}.
\]

Although the source operator itself is additive in cusp, archimedean, prime, and pole pieces, the inverse \(A_{FF}^{-1}\) mixes those channels. Therefore

\[
S_F\ne\sum_q S_F^{(q)}
\]

in any naive additive sense.

The numbers in Section 4 are exact-formula raw-core diagnostics only. They must not be interpreted as a theorem-level decomposition of the unresolved Schur eigenvalue.

## 7. Next target [O]

The next high-value test is a **leave-one-channel-out Schur sensitivity**:

1. reconstruct the canonical source-faithful finite matrix on \(C\cup F\);
2. compute the baseline finite Schur matrix;
3. remove one prime channel q at a time from the whole finite matrix before inversion;
4. compare the movement of the four terminal Schur eigenvalues/eigenspaces;
5. separately test cusp, archimedean, and PSD pole removal.

That nonlinear sensitivity experiment can answer whether the n=3-dominated terminal direction is genuinely controlled by the prime-2/prime-3 interaction after finite elimination, or whether the raw-core cancellation is washed out by the high modes.

## 8. Guardrails [Audit]

- No exact kernel or zero mode is claimed.
- The unresolved complement is numerical, not a frozen theorem input.
- Raw prime Rayleigh contributions are additive low-core quantities only.
- No source channel is identified as an exact symmetry carrier of the unresolved direction.
- The connection to the ramified primes 2 and 3 is interpretive until a source-faithful operator identity or robust Schur sensitivity pattern is established.
- No RH or GRH conclusion follows.

---

**Checkpoint conclusion.** The exceptional even terminal direction is sharply localized at n=3 but is not a pure q=3 source mode. Its raw prime energy is a cancellation between a strong positive q=2 contribution and negative q=3/q=4 contributions. This shifts the working hypothesis from a single prime-3 defect to a discriminant-12 ramified-prime interaction mode and motivates a nonlinear leave-one-channel-out Schur sensitivity audit next.
