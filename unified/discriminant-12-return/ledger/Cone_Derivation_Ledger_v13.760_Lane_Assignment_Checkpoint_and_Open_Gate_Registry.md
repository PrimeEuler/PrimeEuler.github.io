# Cone Derivation Ledger v13.760 — Lane Assignment Checkpoint and Open-Gate Registry

Date: 2026-09-24

Author: external audit session (Claude Sonnet 5), by request of the project owner, to consolidate all currently open work into named lanes with precise next gates. This is a coordination checkpoint, not a new derivation: every closed/established item below cites the entry that proved it and is not to be reopened without a specific new argument.

Synchronization: live head checked immediately before write is v13.759 (External Audit Round 92, commit `85c6cd3`). No collision.

## 0. Why this checkpoint exists

Two originally separate lanes (helix/screw and Suzuki finite-edge) have merged into one program since v13.753–754. A third lane (norm-quotient/idele-class) has been dormant since v13.736 and was just restarted. This entry gives each live question a name and a precise, minimal next step, so parallel work does not collide or re-derive what is already closed. Read the "Do not re-derive" list in each lane before starting new work there.

---

## LANE A — Screw/Helix–Weil–Hermite–Biehler Program

### A.0 What this lane now is

The helix lane (v13.748ff, from the user's original cone/helix/screw-function prompt) and the Suzuki finite-edge/Wiener–Hopf lane (v13.742ff, from the Round 88 correction) are **no longer separate**. v13.753 proved the derivative map is an exact unitary isometry between the screw-increment space and the Weil-form space; v13.754 proved the boundary-triple transport through that isometry preserves the Weyl function `m_A`. Since then (v13.756–758) all work has been in this single unified frame. Do not open a new "helix-only" or "edge-only" sub-lane; there is one carrier.

### A.1 Established — do not re-derive (all independently audited)

- The corrected finite deficiency vectors `u_{A,±}=\bar D v_{A,±}` from Suzuki's actual equation (8.5), replacing the retracted `S_Au_\pm=\bar De_{\pm i}` ansatz (v13.742, audit: Round 88/89).
- Reflection reduction of the affine boundary data: `C_{A,-}=C_{A,+}`, `A_{A,-}=-A_{A,+}`, `B_{A,-}=B_{A,+}` (v13.743, audited Round 89).
- The full self-correction chain on the common Suzuki–Weil current: `\mathscr W=-g''`, the retraction of the overstrong `2\mathrm{Re}\,L(1/2+it)` claim, the exact archimedean/Pf/contact Fourier match, and the exact sign `Q_{\rm Suz}[DF]=Q_{\rm Weil}[F]` (v13.744–747, audited Round 89).
- `\chi_{12}` theta positivity: `\vartheta_{\chi_{12}}(x)=2\eta(ix)>0` for `x>0`, hence `K_\chi>0` and `\Phi_K=\Phi*K_\chi>0` (v13.752, audited Round 91) — **closed, do not reopen.**
- The nonlinear circle/rapidity coordinate bridge `u=\log\cot(\theta/2)` and the caveat that constant boost frequency ≠ constant angular frequency under it (v13.752, audited Round 91).
- The screw–Weil pre-Hilbert isometry `\langle DF,DH\rangle_{\rm Suz}=\langle F,H\rangle_{\rm Weil}` and the exact zero-mode/affine-gauge closure `\{1,u\}\leftrightarrow\{\delta_0,\delta_0'\}` (v13.753, audited Round 91).
- The Hermite–Biehler boundary characteristic `E(z)=i c_\infty\,\Xi(z)[m_\infty(z)-\tau_{\rm HB}]`, `\tau_{\rm HB}=i/c_\infty=i\,\xi(3/2)/\xi'(3/2)`, and the normalized determinant identity `\Delta_{\rm HB/\pi}=(E/\Xi)/(E_*/\Xi_*)` (v13.754, audited Round 91). Boundary-triple citations to v13.661/667/670/706 underlying this are imported and **not yet independently re-verified by this auditor**.
- Scalar `m_A\to m_\infty` (locally uniform) is sufficient for `\Delta_A\to\Delta_\infty`, log-derivative convergence, and Hurwitz-stable divisor data (v13.756, audited Round 92).
- The reduction of `m_A` to a single Möbius channel ratio `\rho_A=H_A/G_A`, and the exact link `\rho_A\to\rho_\infty \iff m_A\to m_\infty` (v13.757, audited Round 92).
- The exact unification: the same two scalar feedback ratios `r_{0,A}=M_{0e}/(1+M_{00})`, `r_{1,A}=M_{1e}/(1+M_{1x})` control **both** the affine-edge contamination `\alpha_A,\beta_A` **and** the Weyl channel ratio `\rho_A` (v13.745, v13.757, audited Rounds 91–92).
- The parity-split reduction `M_{0e}=\ell_{0,A}(R_A^{(+)}(\cosh x-1))`, `M_{1e}=\ell_{1,A}(R_A^{(-)}(\sinh x-x))`, and the correct (weaker, valid) Banach-duality bounds replacing an invalid Cauchy–Schwarz step that was caught before being ledgered (v13.758, audited Round 92).

### A.2 Flagged but not fully independently reconstructed (not an error — just unverified from first principles)

- v13.757 §2's transport claim `u_{A,-}=-Ru_{A,+}`, extending the elementary `DR=-RD` fact to the operators on `H(S_A)`. Plausible, consistent with everything else, but this auditor has not seen the precise action of `R` on `H(S_A)` spelled out. If this becomes load-bearing for a numeric result, derive it explicitly from the `\bar D` isometry rather than citing it as obvious.
- v13.754's imports from v13.661/667/670/706 (the `\Gamma_j`, `m_\infty` boundary-triple formulas, and the "`E` is not a second self-adjoint extension" correction). Consistent with everything checked against the Suzuki PDF so far, but not re-read/re-verified by this auditor in this session.

### A.3 Open gates, in dependency order (work the earliest unresolved one first)

1. **(Smallest, most concrete)** Derive `\ell_{0,A}`, `\ell_{1,A}` as explicit trace/Riesz functionals in Suzuki's finite energy space from the actual kernel `k(x,y)=g(x-y)-\lambda N(x,y)`, and obtain their `A`-dependence together with lower bounds on the Schur denominators `|1+M_{00}|`, `|1+M_{1x}|`. This is v13.758's own named next gate and is currently the shortest path to unblocking everything downstream.
2. Using (1), bound the response norms `\|R_A^{(+)}(\cosh x-1)\|`, `\|R_A^{(-)}(\sinh x-x)\|` and combine into the sufficient criteria `r_{1,A}=o(e^A/A)`, `r_{0,A}=o(e^A)` (v13.745 §8, v13.757 §10, v13.758 §5). Closing this simultaneously closes:
   - the pure compensated edge limit (`\alpha_A,\beta_A\to0`, open since v13.742–743);
   - the finite Weyl convergence `\rho_A\to\rho_\infty` (v13.757);
   - hence, automatically via v13.756, the HB determinant convergence `\Delta_A\to\Delta_\infty`.
3. Once scalar `m_A\to m_\infty` is proved, the **separate** operator-level question remains open: strong/norm convergence of the reference resolvents `R_{\pi,A}` and gamma fields `\gamma_A` (v13.756 §6), needed to upgrade scalar/determinant convergence to actual resolvent convergence of the HB extension. Do not attempt this before (1)–(2) — it is stated as conditional on them.
4. The stationary/positive-Hilbert-measure realization of `g` itself (v13.753 §6) — distinct from and strictly stronger than the already-proven form identity `Q_{\rm Suz}[DF]=Q_{\rm Weil}[F]`. Open, not required for A.3.1–3.
5. v13.752's comparison gate: how much of the original nested-circle/all-frequency helix picture is literally realized by the `(r,u)` boost-Fourier geometry versus remaining visualization (v13.750 §6, v13.752 §8). Lower priority — a provenance/interpretive question, not blocking the analytic program.

**Guardrail for this lane:** none of the above proves RH, self-adjointness of the complex HB extension, or a Hilbert–Pólya operator. Do not promote any convergence result to such a claim.

---

## LANE B — Norm-Quotient / Idele-Class Representation

### B.0 Status: dormant since v13.736; just restarted, no new commits yet as of this checkpoint

### B.1 Established — do not re-derive

- Exact norm quotient `C_{\mathbb Q}/C_{\mathbb Q}^1\simeq\mathbb R_{>0}^\times`, giving the logarithmic coordinate `r=\log|u|_{\mathbb A}` (v13.736, audited Round 87).
- The three-level status split: group-level quotient (proven), trivial-character/test-function projection (proven, and it is exactly where the centered Weil arithmetic distribution and Riemann-zeta scalar factors live), and the v13.731 Hilbert-space prime-power realization (an auxiliary realization of the correct distribution, **not** a proven quotient representation of `C_{\mathbb Q}`) (v13.736).
- `\mathbb Q_p^\times/\mathbb Z_p^\times\simeq\mathbb Z` and the corresponding local unramified factor match (v13.736).
- The negative/cautionary result already on record (v13.739 row B, §D.5): the canonical regular representation on the norm quotient is continuous `L^2(\mathbb R)`, so it **cannot by itself** supply the discrete `(p,k)` prime-power basis of v13.731. Any new construction must explain how it avoids or gets around this.

### B.2 Open gate (the only one on record for this lane)

Construct the trivial-`C_{\mathbb Q}^1`-isotypic (averaged) sector of a canonical idele-class representation and determine its norm-direction operator (v13.736 §9). Two a priori outcomes, both informative:
1. It yields only the continuous regular representation on the norm line — consistent with the v13.739 negative result, and would mean v13.731's discrete prime-power decomposition is confirmed to be an auxiliary trace expansion, not a quotient-state spectrum.
2. It naturally yields the discrete prime-power decomposition and insertion weights `\log p` — which would upgrade v13.731 to a genuine representation-theoretic quotient, a substantial result.

No work has been done on distinguishing these since v13.736. This is a clean, well-posed starting point for the restarted thread.

**Guardrail for this lane:** do not conflate this with Lane A's `E`/Weyl-function `m_\infty`; the two lanes currently do not share unresolved dependencies. A genuine cross-lane link (if found) should cite both provenance chains explicitly, per the v13.739-style registry convention.

---

## 1. Coordination rules (unchanged, restated for new/returning contributors)

1. Check the live ledger and the most recent External Audit Round before starting.
2. Import every item listed under "Established — do not re-derive" above rather than reproving it.
3. If your result overlaps a listed open gate, update that gate's status in a future checkpoint rather than creating a parallel duplicate entry.
4. Label genuinely new cross-lane algebra `[X]`, per the v13.739 convention, and only after both source facts are already established.
5. Keep RH, Hilbert–Pólya, and positivity-beyond-what's-proven explicitly `[O]`/open — this project's external audits will flag any silent promotion.
6. If two entries claim the same version number, the earlier commit (by UTC timestamp) keeps it; the later one renumbers and adds a renumbering note. Check `git log` timestamps, not wall-clock guesses.

---

**Checkpoint conclusion.** One live analytic program (Lane A) with a precise, short dependency chain: boundary-functional trace bounds → affine-edge and Weyl convergence together → HB determinant convergence → (separately, later) operator resolvent convergence. One restarted but currently idle representation-theoretic question (Lane B) with a single well-posed next construction. Contributors should pick the earliest open item in whichever lane they're assigned and post results against the gate numbers above so this checkpoint can be updated rather than duplicated.
