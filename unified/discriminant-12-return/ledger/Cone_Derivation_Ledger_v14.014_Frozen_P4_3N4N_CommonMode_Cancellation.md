# Cone Derivation Ledger v14.014 — Frozen-P4 3N/4N Common-Mode Cancellation

**Date:** 2026-10-04
**Track:** Lane A / no-twist Suzuki Xi scalar certification
**Status:** [N] frozen N=4000 six-plane extended unchanged through M=12000 and M=16000; [N] complement floors remain stiff; [N] one LDDD refinement remains at 1e-26/1e-27 scale; [N] shell-by-shell parity remainder continues to oscillate; [N] cumulative 4000→16000 parity mismatch collapses to 1.095e-6 against a 1.032e-2 common correction; [D] consistent with v14.012 structural common-mode theorem; [G] finite-section complement floors/all-mode arithmetic remain midpoint diagnostics; [O] convert the observed common-mode cancellation into an outward relative-tail enclosure.
**Parents:** v14.011–013.
**Research commits:** f0e222b631371ec072c05ab1b8689aa5498cfc54, e5942a8397cb181f172259af10891c6e7bc00f9c.
**Artifact-label cleanup:** fe408711f74caccce64baf068601b4f7ecdd98ff and 68305804e06b0040cd91759ab3d8caa4c0d36e8c make the parameterized result fields target-generic; the M12000/M16000 runs themselves predate that cosmetic rename, but their target cutoff and numerical values are unambiguous in the workflow/job metadata.
**Collision check:** immediately before this write, live HEAD was 68305804e06b0040cd91759ab3d8caa4c0d36e8c and no v14.014 ledger entry was present.

---

## 1. Frozen-carrier extension

The protected six-plane is exactly the v14.013 N=4000 plane, zero-extended into every larger finite section. No re-Ritz, graph update, carrier rotation, or source-dependent basis change is performed.

The target sections are

\[
M=12000\quad(6000\ \text{modes per parity}),
\]

and

\[
M=16000\quad(8000\ \text{modes per parity}).
\]

Therefore all cutoff dependence reported below is operator/source finite-section dependence, not basis drift.

---

## 2. Embedded complement stability [N]

At M=12000 the lowest midpoint complement eigenvalues begin at

\[
\boxed{\gamma_e^{12000}=0.15533249604320207},
\qquad
\boxed{\gamma_o^{12000}=0.532281668062889}.
\]

At M=16000 they begin at

\[
\boxed{\gamma_e^{16000}=0.155261854486282},
\qquad
\boxed{\gamma_o^{16000}=0.5321909766281885}.
\]

For comparison, v14.013 at M=8000 gave

\[
0.15547279716163812,
\qquad
0.5324618186102422.
\]

Thus the embedded complement floor drifts only mildly downward and no new soft direction appears numerically through 4N.

---

## 3. LDDD refinement stability [N]

After one LDDD residual correction:

### M=12000

\[
\max_j\|R_{e,j}\|_2
=
1.9047803048865015\times10^{-26},
\]

\[
\max_j\|R_{o,j}\|_2
=
4.4802512538542065\times10^{-27}.
\]

### M=16000

\[
\max_j\|R_{e,j}\|_2
=
2.5643740168663672\times10^{-26},
\]

\[
\max_j\|R_{o,j}\|_2
=
6.0626306040390436\times10^{-27}.
\]

The v14.008 arithmetic mechanism therefore remains stable at 8000-dimensional parity sections.

---

## 4. M12000 finite capacities [N]

At M=12000,

\[
\boxed{
C_e(12000)
=
7.50918248380484040140723917779\times10^{-30}
}
\]

and

\[
\boxed{
C_o(12000)
=
2.16485952666524360537473506072\times10^{-25}.
}
\]

Hence

\[
q_{12000}
=
3.46866962558628855525491690400\times10^{-5},
\]

\[
\kappa_{12000}
=
0.999930629013738603647587431773\ldots.
\]

Relative to M=8000, the shell corrections are

\[
\eta_e^{8\to12}
=
0.00239997165988999143\ldots,
\]

\[
\eta_o^{8\to12}
=
0.00238807881876927022\ldots,
\]

so

\[
\boxed{
\Delta\eta^{8\to12}
=
-1.1892841120721211\times10^{-5}.
}
\]

This reverses the positive sign of the M=4000→8000 remainder.

---

## 5. M16000 finite capacities [N]

At M=16000,

\[
\boxed{
C_e(16000)
=
7.49990166134719143253836606117\times10^{-30}
}
\]

and

\[
\boxed{
C_o(16000)
=
2.16220760132471493716793165961\times10^{-25}.
}
\]

Thus

\[
\boxed{
q_{16000}
=
3.46863162295435614511653984636\times10^{-5},
}

and

\[
\boxed{
\kappa_{16000}
=
0.999930629773738517897853287342\ldots.
}
\]

Relative to M=12000,

\[
\eta_e^{12\to16}
=
0.00123745921969620524\ldots,
\]

\[
\eta_o^{12\to16}
=
0.00122648969456213131\ldots,
\]

so

\[
\boxed{
\Delta\eta^{12\to16}
=
-1.0969525134073936\times10^{-5}.
}
\]

The shell common mode continues to decrease while the parity remainder remains an order of magnitude smaller and oscillatory.

---

## 6. Shell-by-shell profile [N/I]

Using the exact finite-capacity identity

\[
\eta_{p;A\to B}=\frac{C_p(A)}{C_p(B)}-1,
\]

the recent shells are:

\[
\begin{array}{c|c|c|c}
\text{shell}&\eta_e&\eta_o&\eta_o-\eta_e\\ \hline
3072\to4000&3.6788620\times10^{-3}&3.6440342\times10^{-3}&-3.48278\times10^{-5}\\
4000\to8000&6.6553856\times10^{-3}&6.6794496\times10^{-3}&+2.40640\times10^{-5}\\
8000\to12000&2.3999717\times10^{-3}&2.3880788\times10^{-3}&-1.18928\times10^{-5}\\
12000\to16000&1.2374592\times10^{-3}&1.2264897\times10^{-3}&-1.09695\times10^{-5}
\end{array}
\]

The common correction decreases on the outer shells. The parity remainder has no stable sign and must not be enclosed by a one-sided asymptotic ansatz.

---

## 7. Four-N cumulative cancellation [N/D/I]

Across the entire extension from the original theorem-scale cutoff M=4000 to M=16000,

\[
\boxed{
\eta_e^{4\to16}
=
0.01032001465045383846\ldots,
}
\]

\[
\boxed{
\eta_o^{4\to16}
=
0.01032111000408773715\ldots.
}
\]

The common cumulative correction is therefore about

\[
\bar\eta^{4\to16}\approx1.0320562\times10^{-2}.
\]

Yet the parity mismatch is only

\[
\boxed{
\Delta\eta^{4\to16}
=
+1.0953536338986866\times10^{-6}.
}
\]

Thus

\[
\boxed{
\frac{|\Delta\eta^{4\to16}|}{\bar\eta^{4\to16}}
\approx
1.0613\times10^{-4}.
}
\]

In words: roughly 99.989% of the normalized 4000→16000 correction is common-mode at this finite cutoff.

This is a strong quantitative consistency check for the v14.012 structural theorem.

---

## 8. Projective stability [N]

Relative to M=4000,

\[
\frac{q_{16000}}{q_{4000}}-1
=
1.08416503485547\times10^{-6}.
\]

The absolute quotient shift is

\[
q_{16000}-q_{4000}
\approx
3.76056505\times10^{-11}.
\]

Most strikingly,

\[
\boxed{
\kappa_{16000}-\kappa_{4000}
\approx
-7.52060836\times10^{-11}.
}
\]

Thus a roughly one-percent common change in each separate source capacity induces only a 1e-10-scale change in the projective Xi scalar over this 4N extension.

This does not replace an outward infinite-tail certificate, but it demonstrates why the relative consumer is vastly better conditioned than either absolute capacity.

---

## 9. Certification consequence [I/O]

The numerical evidence now separates the remote problem into two scales:

1. a positive, slowly decaying, parity-common bulk correction that may be bounded relatively coarsely;
2. a much smaller arithmetic/sampling remainder whose sign oscillates and must be preserved before absolute values.

The correct theorem target remains

\[
\eta_o-\eta_e,
\]

not separate absolute tails.

v14.011 identifies the sign-carrying arithmetic cross/feedback terms; v14.012 proves the common-mode structure; the present gate shows that their cancellation remains extremely effective through 4N without moving the carrier.

---

## 10. Guardrail

All M12000/M16000 values here remain finite-section midpoint diagnostics.

The LDDD residual mechanism is extremely tight, but the embedded Euclidean complement floor and all-mode scalar arithmetic at these larger cutoffs have not yet been converted into outward intervals.

No infinite-cutoff value is extrapolated from the finite sequence.

---

HANDOFF
target: sandbox
type: payload
parent: v14.014
status: open
action: Use the M12000/M16000 frozen-carrier profile as a quantitative check for the active relative-kernel enclosure. In particular, the cumulative 4000→16000 parity mismatch is +1.09535e-6 against a 1.03206e-2 common correction, while individual shell remainders remain sign-changing.
deliverable: consistency-check-or-obstruction
constraints: Do not fit a one-sided power law to the parity remainder; preserve prime/sampling oscillations and the v14.011 arithmetic cross term. Treat the tiny cumulative mismatch as a check target, not as a certified infinite-tail bound.
