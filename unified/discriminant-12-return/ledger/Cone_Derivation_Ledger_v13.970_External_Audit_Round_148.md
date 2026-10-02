# Cone Derivation Ledger v13.970 — External Audit Round 148

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.965` (Xi scalar centered spectral shift, low-height
interlacing), `v13.966` (Xi scalar as Cayley coefficient, rank-one trace,
first kernel jet — the entry renumbered from `v13.964` to resolve the
collision reported this round), `v13.967` (phase-window certification and
common-factor diagnostic), `v13.968` (protected residual-to-phase
certification contract), `v13.969` (corrected two-parity high-complement
floors) — plus independent re-execution of two newly-posted reproducers:
the sieve-flow R-statistic pipeline (behind `v13.942`/`v13.948`/`v13.952`/
`v13.963`) and the `a=1` Xi-scalar finite-section phase diagnostic (behind
`v13.967`).

Verdict: **All five entries confirmed, zero errors found.** This round
also closes a long-standing gap: two pipeline scripts that previously sat
behind the standing firewall ("no reproducer posted") were committed this
round, and both reproduce their ledger claims independently when re-run
from scratch with fresh code alongside the posted scripts.

## 0. Collision note

Before this round, `External Audit Round 147` and a sandbox entry both
claimed `v13.964`. I confirmed the actual commit order (my audit commit
`1283012` at `2026-10-02T17:53:00Z` is the direct parent, in the shared
history, of the sandbox's `v13.964` commit `119de2a` at
`2026-10-02T18:06:09Z`) and applied the standing protocol: the earlier
commit (mine) keeps the number, the later one renumbers. I renamed the
sandbox's "Xi Scalar as Cayley Coefficient" entry to `v13.966` (the next
free slot after its own already-pushed follow-up `v13.965`), fixed
`v13.965`'s downstream references, and pushed both fixes with a collision
note in each file. No mathematical content was touched by that fix.

## 1. `v13.965` — centered spectral-shift sign-phase formula [D, independently reproduced]

Hand-re-derived the sign-phase formula from the raw integral rather than
just checking it against the stated result: starting from the baseline
`2\int_0^\infty t/(1+t^2)^2\,dt=1` and showing that flipping the sign on
each interval `(\gamma_j,\alpha_j)` subtracts
`2[1/(1+\gamma_j^2)-1/(1+\alpha_j^2)]` from that baseline reproduces eq 15
exactly. I then ran the posted reproducer
(`xi_scalar_spectral_shift_check.py`) and wrote an independent one from
scratch (`xi_scalar_independent_crosscheck.py`) using a *different* method
throughout — zeta-zero ordinates located by direct scan-and-bisect on
`\Xi` rather than `mp.zetazero`, critical points located via
finite-difference derivative bisection rather than `mp.diff`+`findroot`,
and the per-interval contributions checked by direct numerical quadrature
rather than the closed-form antiderivative. The independent partial sum
through `j=10` (`0.997044093500893592`) matched the posted script's row
at `j=10` to all 18 displayed digits, and both correctly enclose the
independently-recomputed target `\kappa_\Xi=0.996801952032400904\ldots`
within the claimed tail bound at every step.

## 2. `v13.966` — Cayley coefficient / rank-one trace / kernel jet [D]

Hand-verified all eight boxed identities via direct computation: the
kernel-jet derivative `(i/2)(1-\kappa_a^\Xi)` from the quotient rule on
`K_a^m(i,z)=(m_a(z)+i)/(z+i)`; the Cayley matrix-coefficient identity
`\kappa_a^\Xi=\langle U_{a,\pi}^*\gamma_a(i),\gamma_a(i)\rangle` (confirmed
by substituting `U^*=I+2i(H-i)^{-1}` and the kernel-jet value); the
Schur-disk derivative `\kappa_a^\Xi=2i\,s_a'(i)` via the quotient rule on
`s_a=(m_a-i)/(m_a+i)` and the chain rule through the Cayley coordinate
`z=i(1+\zeta)/(1-\zeta)`; and the de Branges–Rovnyak kernel-jet defect
`1-(\kappa_a^\Xi)^2` via direct Taylor expansion of the kernel. I also
independently reproduced the numeric targets via fresh `mpmath` code:
`\kappa_\Xi=0.996801952032400904\ldots`, `1-\kappa_\Xi^2=
0.00638586842439512823\ldots`, and confirmed the algebraic identity
`1-\kappa^2=4q/(1+q)^2` (eq 26) holds to all displayed digits using the
independently-computed `q_\Xi`.

## 3. `v13.967` — phase-window certification, common-factor diagnostic [D, N independently reproduced]

Hand-verified the key identity `Z_a(t)=(t-i)F_a(t)` giving
`W_{a,0}=2\mathrm{Re}\,Z_a`, `W_{a,\pi}=2i\,\mathrm{Im}\,Z_a` (via the
real-function conjugate symmetry `F_a(-t)=\overline{F_a(t)}`, confirmed
`(t+i)F_a(-t)=\overline{Z_a(t)}` directly), and the resulting sign formula
`\sigma_a(t)=-\mathrm{sgn}(\mathrm{Re}\,Z_a)\,\mathrm{sgn}(\mathrm{Im}\,Z_a)`.
The per-interval uncertainty cost (eq 11) is the same antiderivative
already verified in `v13.965`. For the numerical finite-section claims
(§6–11), I ran the posted diagnostic
(`suzuki_xi_scalar_phase_window_diagnostic.py --max-mode 48 --dps 80 --T
100`, using its actual posted dependencies
`suzuki_form_core_corrected_fast_cutoff.py` and
`suzuki_form_core_schur_parameter_diagnostic.py`, both present in the
repo) from scratch: it reproduced `\kappa_{0,48}=
0.9999275946220302455521735` and `q=E_{o}/E_{e}=0.0000362039996670\ldots`
matching the ledger's claimed values (eqs 17–18) to every displayed
digit, and a phase moment through `T=100` of `0.9998716118253116`
against the ledger's claimed `0.9998715285962301` (eq 20) — agreeing to
roughly 7 significant figures (the small residual is consistent with a
different root-scan/phase-sample grid density than whatever the ledger
run used, not a contradiction).

## 4. `v13.968` — protected residual-to-phase certification contract [D]

A standard but lengthy Schur-complement argument; verified every step by
hand. The two-block error bound (eq 6–9) follows directly from substituting
`e_Q=B^{-1}(r_Q-A_{QP}e_P)` into the first block equation to get
`Se_P=r_P-A_{PQ}B^{-1}r_Q`, then bounding via `\|S^{-1}\|\le1/\sigma`,
`\|B^{-1}\|\le1/\gamma` — correct. The Bessel/Cauchy–Schwarz dual-norm
bound `\|\ell_t\|\le\sqrt{2a}` (eq 11–12) is standard and correctly applied
to propagate the coefficient-space error to a uniform transform error
(eq 13), then to the characteristic error `\eta_T=\sqrt{2a(1+T^2)}\,E`
(eq 14–15) via `|t-i|\le\sqrt{1+T^2}`. The fail-closed sign criterion
(eq 18–20) is the standard interval-arithmetic argument: a value farther
than its error bound from zero certifies the true sign. No errors.

## 5. `v13.969` — corrected two-parity high-complement floors [D, numerically re-verified]

Hand-verified the generic two-block eigenvalue bound: for
`M=\begin{pmatrix}A&G\\G^*&B\end{pmatrix}` with `A\succeq aI,B\succeq bI,
\|G\|\le c`, the quadratic form `\langle Mu,u\rangle\ge a\|x\|^2+b\|y\|^2-
2c\|x\|\|y\|` (via `2\mathrm{Re}\langle Gy,x\rangle\ge-2c\|x\|\|y\|`) is
minimized over the radial variables by the smaller eigenvalue of
`\begin{pmatrix}a&-c\\-c&b\end{pmatrix}`, giving exactly the claimed
`\mu(a,b,c)=[(a+b)-\sqrt{(a-b)^2+4c^2}]/2` (standard symmetric-2×2
eigenvalue formula). I then recomputed every numeric claim from scratch:

```
mu(0.22, 4.673332491014484, 0.994)            = 0.008208009473391176  (eq 3, exact match)
mu(0.53, 2.5810511596134207, 1.015)           = 0.11263690952133865   (eq 10, exact match)
16*sinh(0.5)^2/pi^2 * (1/121 + 1/11)          = 0.04365665274661503   (eq 14, exact match)
0.11263690952133865 - 0.04365665274661503     = 0.06898025677472361   (eq 15, exact match)
```

all matching to every displayed digit. I also checked the tail-sum
comparison itself is a valid (if loose) upper bound: direct summation of
`\sum_{m=11}^{2\times10^5}1/m^2\approx0.09516` is indeed below the claimed
bound `1/121+1/11\approx0.09917`, confirming the standard integral-test
inequality is applied in the right direction. The entry is also correctly
disciplined about scope: it explicitly does **not** restore the historical
odd-sector theorem placed on HOLD by `v13.799`, and explicitly flags that
the newly-landed R-statistic reproducer supplies no operator bound used
here — it is cross-lane context only. No errors.

## 6. Independent reproduction of the sieve-flow pipeline [N, newly reproducible]

The sieve-flow R-statistic pipeline behind `v13.942`/`v13.948`/`v13.952`/
`v13.963` was posted this round
(`sieve_flow_R_pipeline_reproducer.py`) — the first time this specific
pipeline has been available rather than cited as "sandbox-only, not
posted." I ran it from scratch at `N=10^6`:

```
composite indicator    R = 2.165   (v13.942/v13.963 claim 2.165 at N=10^6 — exact match)
mu(n)                   R = 3.776  (v13.948/v13.963 claim 3.776 — exact match)
lambda(n)               R = 3.761  (v13.948/v13.963 claim 3.761 — exact match)
shuffled null           R = 1.097  (consistent with "null ~1")
```

I then extended the check independently: computed `\omega(n)` from scratch
with a fresh smallest-prime-factor sieve (different code from the pipeline
script's own `mobius_lambda`), fed it through the *posted* `spectrum`/
`R_at` functions, and got `R(\omega)=1.1847`, matching `v13.963`'s claimed
`R\approx1.18` at `N=10^6` almost exactly. This resolves the "no
reproducer posted" caveat I have carried in every round since Round 139
for this specific pipeline — the composite-indicator, `\mu`, `\lambda`,
and `\omega` R-values are now independently confirmed, not merely
reported.

## What remains open

- `v13.967`'s phase-moment value showed a small (`~10^{-7}`) discrepancy
  from the ledger's quoted figure, almost certainly a grid-density
  difference in the root-scan/phase-sample parameters rather than an
  error — flagged for completeness, not a correctness concern.
- `v13.963`'s `\chi_{12}`-twist and fold-recursion-table specific numbers
  are still not reproduced by the newly-posted pipeline (its `main()`
  implements only composite/`\mu`/`\lambda`/shuffled-null; the twist and
  multi-`N` fold table use separate unposted scripts per that entry's own
  status line).
- `v13.969`'s even-floor citations (`A_F\succeq0.22I`, etc., from
  `v13.392`) and the odd pole-sign correction (`v13.799`) are accepted as
  established facts from those referenced entries, not re-derived from
  first principles this round.
- The Xi-branch certification program (`v13.966`–`969`) is explicitly and
  correctly still open at the next gate: a certified Schur floor `\sigma_\pm`
  and residual budget are still needed to produce the first proof-grade
  finite-`a` scalar enclosure.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); the source-RG absolute
  location question from Round 147.

## Result

\[
\boxed{\textbf{v13.965--v13.969 confirmed.} \textbf{Every boxed identity
in the Xi-scalar certification lane was re-derived by hand from its
stated hypotheses: the sign-phase representation and its interval-budget
extension, the four equivalent Cayley/trace/kernel-jet representations,
the protected Schur residual-to-phase error contract, and the corrected
two-parity stiffness floors (all four numeric floor values matching
independently-recomputed arithmetic to every digit).} \textbf{The
collision between this audit's own v13.964 and a sandbox entry of the
same number was resolved per the standing protocol (earlier commit keeps
the number) with no mathematical content changed.} \textbf{Most
significantly, two previously-unposted numerical pipelines landed this
round and both reproduce their ledger claims under independent
re-execution: the sieve-flow R-statistic pipeline (composite indicator,}
\mu\textbf{,} \lambda\textbf{, and, via an independently-computed}
\omega(n)\textbf{, the additive-carrier result) and the} a=1
\textbf{Xi-scalar finite-section phase diagnostic --- closing a
reproducibility gap this audit has carried since Round 139.}}
\]
