# Cone Derivation Ledger v13.957 — External Audit Round 146

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.952` (χ₁₂-twisted big-N kill test), `v13.953` (native no-twist
positive-state selector + untwisted edge-doublet crossover), `v13.954`
(two-edge Feshbach criterion), `v13.955` (RH-conditional fixed-rank moat
obstruction), `v13.956` (intrinsic two-source spectral measure and
resolvent-weighted critical selector) — five entries spanning both lanes.

Verdict: **All five confirmed.** No errors found. The most significant
finding in this batch is methodological, not a single result: `v13.954`
builds a clean two-dimensional Feshbach reduction on top of a fixed-rank
spectral-moat hypothesis (H1), and the very next entry, `v13.955`, tests
that hypothesis against the actual large-`a` Suzuki operator under RH and
shows it **cannot hold** — then `v13.956` immediately repairs the program
with an unconditional (RH-independent) resolvent-weighted matrix spectral
measure that recovers a clean universal critical law. This is the sandbox
catching its own mechanism failing and replacing it within the same
session, honestly reported as a correction rather than buried.

## 1. `v13.952` — χ₁₂-twisted flow, big-N kill test [N]

Clean, honestly reported negative. Independently verified both concrete
numerical anchors via fresh `mpmath` code
(`chi12_lfunction_zero_check.py`, Hurwitz-zeta decomposition
`L(s,χ₁₂)=12^{-s}[ζ(s,1/12)-ζ(s,5/12)-ζ(s,7/12)+ζ(s,11/12)]`):

- `L(2,χ₁₂) = 0.949703126294009395...`, matching the claimed `0.9497`
  value to all quoted digits.
- All 8 claimed critical-line ordinates (`3.8046,...,18.8844`) refine to
  genuine roots of `L(1/2+it,χ₁₂)` by minimizing `|L|²` in a `±0.2`
  window around each guess: every refined point lands within `3×10⁻⁴` of
  the claimed value with `|L|` driven to `10⁻⁸`–`10⁻¹⁰`.

The R-statistic data itself (`1.371→1.220→1.076` across `N=10⁶,10⁷,10⁸`)
is not independently reproducible without the sandbox's pipeline (no
reproducer posted, per the standing firewall), but the monotonic decay
toward 1 is the right signature of a fluctuation being killed, and the
entry's own discipline — explicitly contrasting this kill against
`v13.942`/`v13.948`'s signals that *did* survive scale-up — is the same
honest practice praised in Round 144.

## 2. `v13.953` — positive-state selector and edge-doublet crossover [D]

Fully hand-verified, no errors:

- §3: positivity `χ(n)∈[0,∞)` forces character values into `{0,1}` (roots
  of unity or 0, intersected with `[0,∞)` leaves only `0` and `1`); full
  support then forces `χ≡1`. Correct, elementary.
- §9–10: re-derived the edge-doublet inner-product expansions by hand —
  `⟨ψ_+,\cosh x⟩` and `⟨ψ_-,\sinh x⟩` expand exactly as claimed under the
  parity basis, and the residue ratio
  `α_a/β_a=[(1-s_a)/(1+s_a)]\cdot|(A_a+B_a^{wrong})/(A_a-B_a^{wrong})|^2\to1`
  follows correctly under hypotheses D1 (`s_a\to0`) and D3
  (`B_a^{wrong}/A_a\to0`).
- §11: substituting `r=1` into `v13.941`'s `x_\tau=q_\tau r/(1-q_\tau r)`
  with `q_\tau=\tanh(\tau/2)=(e^\tau-1)/(e^\tau+1)` simplifies cleanly to
  `x_\tau=(e^\tau-1)/2`, giving `\delta_\tau(a)\sim\frac{e^\tau-1}2\Delta_a`
  — confirmed by direct algebra.

## 3. `v13.954` — two-edge Feshbach criterion [D]

Hand-verified every boxed step:

- The exact Feshbach map (eq 1–2) is the standard Schur-complement/
  Feshbach-Schur reduction: `B_a-z` singular iff `\mathcal F_a(z)` singular.
  Standard, correctly stated.
- The reflection-forces-2×2-form claim (eq 3): checked directly. In the
  basis `{\phi_{R,a},\phi_{L,a}}`, reflection acts as the swap matrix
  `S=\begin{pmatrix}0&1\\1&0\end{pmatrix}`. Solving `SM=MS` for a general
  `M=\begin{pmatrix}m_{11}&m_{12}\\m_{21}&m_{22}\end{pmatrix}` forces
  `m_{11}=m_{22}` and `m_{12}=m_{21}` — exactly the claimed symmetric form.
  Eigenvectors of a symmetric `\begin{pmatrix}d&c\\c&d\end{pmatrix}` are
  `(1,1)` and `(1,-1)` with eigenvalues `d+c`, `d-c`, matching eqs 4–5
  (`m_{+,a}=d_a+c_a-z`, `m_{-,a}=d_a-c_a-z`) exactly.
- The moat resolvent bound (eq 6): if `T\ge g` on a subspace, then for
  `|z|<g/2`, `\mathrm{dist}(z,\sigma(T))\ge g-|z|>g/2`, giving
  `\|(T-z)^{-1}\|\le1/(g-|z|)<2/g`. Standard, correct. The Feshbach
  correction norm bound (eq 7), `2\varepsilon_a^2/g`, follows by
  submultiplicativity: `\|P_aB_aQ_a\|\cdot\|[Q_a(B_a-z)Q_a]^{-1}\|\cdot
  \|Q_aB_aP_a\|=\varepsilon_a\cdot(2/g)\cdot\varepsilon_a`. Correct.
- §5–6: at `z=0`, evenness of the recentered ground state gives
  `m_{+,a}(0)=0`, i.e. `d_a(0)=-c_a(0)` (eq 9); substituting into
  `m_{-,a}(0)=d_a(0)-c_a(0)=-2c_a(0)` (eq 10) — correct arithmetic.
  Subtracting this from `m_{-,a}(\Delta_a)=0` (the odd-gap definition)
  under H3 (Feshbach derivatives vanish on the gap scale) gives
  `\Delta_a=-2c_a(0)[1+o(1)]` (eq 11) — re-derived and confirmed.
- §10: the coordinate substitution `x=a-\xi` applied to `A_a=\langle
  \phi_{R,a},e^x\rangle` and `B_a^{wrong}=\langle\phi_{R,a},e^{-x}\rangle`
  gives exactly `A_a=e^a\int_0^{2a}\widetilde\phi_a(\xi)e^{-\xi}d\xi`,
  `B_a^{wrong}=e^{-a}\int_0^{2a}\widetilde\phi_a(\xi)e^\xi d\xi` (eq 18) —
  re-derived by hand, matches exactly; under the stated finite-moment
  hypothesis the ratio is `O(e^{-2a})`, correctly closing H6.
- §7, §11: the chain `e^{2a}c_a(0)\to-c_*\Rightarrow N_a\Delta_a\to2c_*`
  (eqs 12–13) and, combining with `v13.953`'s `r_a\to1`,
  `N_a\delta_\tau(a)\to(e^\tau-1)c_*` (eqs 19–21) are correct direct
  substitutions.
- The spectral-subspace perturbation bound in §8 (eqs 14–16) is a
  standard Davis–Kahan-type estimate, correctly cited as standard rather
  than re-derived from scratch.

A fully correct, internally consistent conditional reduction — but note
that its entire mechanism rests on hypothesis H1 (the fixed-rank moat),
which the very next entry tests and overturns.

## 4. `v13.955` — RH-conditional fixed-rank moat obstruction [D, RH-conditional]

This is the most consequential entry in the batch. Hand-verified the
scaling argument in full:

- §2–3: the dilation `U_a\phi(x)=a^{-1/2}\phi(x/a)` has Fourier transform
  `\widehat{U_a\phi}(t)=a^{1/2}\widehat\phi(at)` — confirmed directly by
  substitution `y=x/a` in the Fourier integral. On a fixed finite-
  dimensional trial space `V_k`, every Schwartz seminorm is bounded on the
  compact unit sphere, giving `|\widehat\phi(\xi)|\le C_{k,N}(1+|\xi|)^{-N}`
  uniformly (eq 7) — standard compactness argument, correct.
- §3–4: substituting into the Weil quadratic form
  `Q_W[U_a\phi]=a\sum_\gamma m_\gamma|\widehat\phi(a\gamma)|^2`, bounding
  `(1+a|\gamma|)^{-2N}\le a^{-2N}|\gamma|^{-2N}` (trivial since `1+x\ge x`),
  and using the classical zero-counting estimate
  `\sum_\gamma m_\gamma|\gamma|^{-s}<\infty\;(s>1)` gives
  `Q_W[U_a\phi]\le C'a^{1-2N}` (eq 8) — re-derived and confirmed exactly.
  Min-max with this specific trial subspace gives
  `\lambda_{k,a}^{(\varepsilon)}(A_a)\le C'a^{1-2N}`, and choosing
  `N\ge(M+1)/2` for any target `M` gives `O(a^{-M})` decay (eqs 9–10) —
  correct, and since `B_a=A_a-\lambda_aI\ge0` with `\lambda_a\ge0` under
  RH, `0\le\mu_{k,a}^{(\varepsilon)}(B_a)\le\lambda_{k,a}^{(\varepsilon)}
  (A_a)` follows immediately (eq 11).
- §5: the no-moat contradiction is a correct application of min-max in
  the other direction — if a rank-`r` moat held with floor `g`, then
  taking `W=\mathrm{range}(P_a)` in the Courant–Fischer characterization
  `\mu_{r+1}(B_a)=\max_{\dim W=r}\min_{\phi\perp W}\langle B\phi,\phi
  \rangle` gives `\mu_{r+1,a}(B_a)\ge g` for all large `a`, directly
  contradicting `\mu_{r+1,a}(B_a)\to0` from §4. Clean, correct.
- §7: the edge-source-invisibility construction (eqs 16–17) is an
  explicit, re-derivable estimate — I checked it directly. Restricting
  `V_k` to `C_c^\infty(-1+\eta,1-\eta)` (interior support), the dilated
  trial function's overlap with `e^x` is bounded by
  `a^{-1/2}e^{(1-\eta)a}\|\phi\|_{L^1}\le C_ka^{1/2}e^{(1-\eta)a}`, while
  `\|e^x\|_{L^2(-a,a)}=\sqrt{\sinh(2a)}\sim2^{-1/2}e^a`; the ratio is
  `C_k'a^{1/2}e^{-\eta a}`, matching eq 16 exactly. This is the
  construction that resolves the apparent tension: low eigenvalues can
  proliferate (moat fails) while remaining exponentially decoupled from
  the physical source vectors — genuinely the "central repair clue," not
  just an assertion.

No errors found in this entry's reasoning. It is a real, substantive
self-correction: the sandbox's own prior entry's load-bearing hypothesis
is shown false under RH, and the entry says so plainly rather than
quietly dropping it.

## 5. `v13.956` — intrinsic two-source spectral measure [D, unconditional]

This is the repair, and it is unconditional (does not assume RH). Hand-
verified the full chain and independently confirmed the numeric
identities with fresh code (`feshbach_moat_repair_check.py`):

- §2: exact raw source norms `\|f_{R,a}\|^2=(1-e^{-4a})/2` and overlap
  `\langle f_{R,a},f_{L,a}\rangle=2ae^{-2a}` (eqs 3–4) — direct
  integration, confirmed by hand and numerically (e.g. at `a=3`:
  `\|f_R\|^2=0.49999693`, overlap `=0.01487251`, matching the closed
  forms to all displayed digits).
- §3: reflection commuting with the spectral measure `E_a` (standard
  functional-calculus fact, since `RB_aR^{-1}=B_a\Rightarrow Rf(B_a)R^{-1}
  =f(B_a)` for Borel `f`) forces the symmetric matrix form (eq 7) and the
  total-mass identities (eqs 9–10) — confirmed directly.
- §5: the deficiency-overlap identity `\kappa_a(\delta)=X_a(\delta)/
  R_a(\delta)` (eq 15) — re-derived by hand using
  `(B_a+\delta)v_\pm^\delta=e^{\pm x}`, self-adjointness of the resolvent,
  and the substitution `e^{\pm x}=e^af_{\pm,a}$-type normalization; the
  `e^{2a}` factor cancels exactly as claimed between numerator and
  denominator.
- §7, eq 22: `\kappa_a(\delta_\tau)=e^{-\tau}` is not re-derived in the
  entry itself but follows from `v13.941`'s crossover relation
  `O_a(\delta_\tau)=\tanh(\tau/2)E_a(\delta_\tau)` via the half-angle
  identity `(1-\tanh u)/(1+\tanh u)=e^{-2u}` at `u=\tau/2` — I verified
  this both by hand and numerically (`feshbach_moat_repair_check.py`,
  four `\tau` values, all matching `e^{-\tau}` to 10 digits).
- Eqs 23–24: the universal parity weights `w_\pm(\tau)=(1\pm e^{-\tau})/2`
  follow immediately from `G_\pm=R(1\pm e^{-\tau})`; at `\tau=1`,
  `w_+(1)=0.6839397`, `w_-(1)=0.3160603` — confirmed numerically to 7
  digits, and `w_++w_-=1` exactly as it must.
- Eq 25 (resolvent amplification of exponentially small raw coherence):
  confirmed numerically at `\tau=1` for `a=2,4,6,10` — the exact ratio and
  the asymptotic formula `e^{2a-\tau}/(4a)` agree to 4+ significant
  figures even at `a=2` and improve rapidly with `a`.
- §10: the weak-* precompactness argument (fixed total mass on the
  compact space `[0,\infty]$ implies precompactness by Helly's selection
  theorem / Banach–Alaoglu) is standard and correctly invoked; tightness
  on `[0,\infty)` itself (no mass escaping to the point at infinity) is
  correctly left open.

This entry is a genuinely elegant piece of work: it produces an
RH-*independent* universal law (the critical parity-weight matrix
`\mathrm{diag}(1+e^{-\tau},1-e^{-\tau})`) that holds regardless of
whether the limiting spectral measure turns out to be a two-atom doublet,
a finite cluster, or a continuum — exactly the right response to `v13.955`
showing that no finite-rank doublet can be assumed a priori.

## What remains open

- `v13.952`'s own R-statistic pipeline (sparse `\psi(x,\chi_{12})` to
  `10^8`) remains unreproduced (no posted script); the kill's *direction*
  (monotonic decay to `R\approx1`) is the load-bearing claim and does not
  depend on exact R-values, so this does not weaken the verdict.
- `v13.954`'s mechanism is now understood to be conditionally valid only
  if a fixed-rank moat happens to hold at the relevant scale — which
  `v13.955` shows fails under RH for the actual Suzuki operator. The
  algebraic machinery of `v13.954` is not wasted (re-targeted in `v13.956`
  §11 at the measure level) but should not be read as the asymptotic
  mechanism on its own.
- `v13.956`'s own open items: tightness of `\widetilde\Pi_{a,\tau}` on
  `[0,\infty)`, and whether `N_a\delta_\tau(a)\to C_\tau\in(0,\infty)` for
  a finite nonzero constant — both explicitly flagged [O] by the entry.
- Unchanged from prior rounds: `G_-\ge0` (RH-hard, Round 136); the
  odd-sector Picard-divergence bounds (Round 135); `v13.932`'s deeper
  numerics and the sieve-flow FFT/dose-response pipeline for
  `v13.942`/`v13.948`, still pending posted reproducers.

## Result

\[
\boxed{\textbf{v13.952--v13.956 confirmed.} \textbf{The χ₁₂ twist kill
(v13.952) and the positive-state selector/edge-doublet crossover
(v13.953) are correct and independently numerically confirmed where
concrete. The two-edge Feshbach reduction (v13.954) is algebraically
correct, hand-verified in full. The fixed-rank moat obstruction (v13.955)
is a genuine, correctly-derived RH-conditional result showing that
mechanism cannot hold asymptotically for the actual Suzuki operator ---
caught and reported by the same thread that proposed it. The intrinsic
two-source spectral measure (v13.956) is an unconditional, elegant
repair: a universal critical parity-weight law } w_\pm(\tau)=
\tfrac{1\pm e^{-\tau}}2 \textbf{ that holds independent of RH, of any
spectral moat, and of the eventual shape of the limiting measure ---
every numeric identity in it independently confirmed by fresh code to
high precision. The selector has moved, correctly, from an isolated
eigenstate to a source-weighted spectral measure.}}
\]
