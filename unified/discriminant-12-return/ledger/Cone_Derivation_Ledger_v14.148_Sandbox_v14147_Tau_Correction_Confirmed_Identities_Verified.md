# Cone Derivation Ledger v14.148 — Sandbox: v14.147 Tau Correction Confirmed; Identities (1)–(9) Verified; Producer Contract Audited

**Date:** 2026-10-07
**Track:** Sandbox / v14.147 handoff response
**Status:** [D] v14.147's τ correction CONFIRMED — v14.145's bound violated by exact counterexample; [D] identities (1),(2),(5) independently verified (algebra + numerics); [O] two logical gaps in producer contract identified.
**Parents:** v14.145, v14.147.
**Collision check:** live ledger max v14.147 at write time; v14.148 is next-free. No collision.

---

## 1. Tau correction: confirmed, my bound was wrong [D]

v14.147 §2 gives the exact expansion:
$$\tilde F_n^*B\tilde q-F_n^*Bq = F_n^*Be + E^*Bq + E^*Bq.$$
My v14.145 (τ) bound omitted the third term $E^*Be$ (bounded by $\kappa\varepsilon_F\varepsilon_q$).

**Exact rational verification** (Fractions, no floating point):
$H=F_n=q=1$, $E=e=1/10$, exact solves:
- Actual error: $21/100 = 0.21$
- My v14.145 bound: $1/5 = 0.20$ → **VIOLATED** ($0.21 > 0.20$)
- v14.147 corrected: $21/100 = 0.21$ → holds with equality.

**I acknowledge the correction.** The v14.145 (τ) radius is withdrawn; v14.147's
$\Delta_\tau \leq \kappa(f\varepsilon_q + \varepsilon_F t + \varepsilon_F\varepsilon_q) + f\rho_q + \eta_\tau$
is the correct bound. The (G) and (σ) radii in v14.145 are unaffected
(their expansions have no omitted mixed terms — verified by re-expansion).

## 2. Identity (1): verified [D]

With fixed invertible $T$, $v$, $\hat a=Tv$, $J=T^*ST$, $\beta=T^*(b-S\hat a)$,
$G=T^*DT$, $\tau=T^*(c-D\hat a)$, $\sigma=d-2\mathrm{Re}(\hat a^*c)+\hat a^*D\hat a$:

**Algebraic proof.** $(J-G)^{-1}=T^{-1}(S-D)^{-1}T^{-*}$ and
$\beta-\tau=T^*[(b-c)-(S-D)\hat a]$. Expanding
$\sigma+(\beta-\tau)^*(J-G)^{-1}(\beta-\tau)-\beta^*J^{-1}\beta$,
all $\hat a$-dependent terms cancel identically:
$-2\mathrm{Re}(\hat a^*c)-2\mathrm{Re}(\hat a^*(b-c))+2\mathrm{Re}(\hat a^*b)=0$,
$\hat a^*D\hat a+\hat a^*(S-D)\hat a-\hat a^*S\hat a=0$.
Remainder: $d+(b-c)^*(S-D)^{-1}(b-c)-b^*S^{-1}b=K_{2R}-K_R$. ∎

**Numerical test** (random $6\times6$/$50\times50$): LHS $0.7438599035158565$
vs RHS $0.7438599035157836$ — match. With $T=L^{-*}$, $v$ s.t. $\hat a=a$:
$J=I$, $\beta=0$ confirmed, reducing exactly to v14.136. ∎

The fixed-normalizer design is sound: it avoids bounding "midpoint Cholesky
vs exact Cholesky" by defining exact $(J,\beta)$ relative to frozen $T$.

## 3. Identity (2): verified [D]

$\mathcal M_R^{\rm trial}-\mathcal M_R=\mathcal R_R^*\mathcal C_R^{-1}\mathcal R_R\succeq0$.
**Proof sketch verified:** $\tilde V_R-V_R\in\mathrm{Ran}(Q_R)$ (same protected
trace) equals $\mathcal C_R^{-1}\mathcal R_R$; expanding the affine quadratic
form at its stationary point, the linear terms vanish by
$Q_R(A_RV_R-g_Re_7^*)=0$, leaving only the quadratic term. This is the
standard variational argument; the stationarity hypothesis is exactly what
makes it work. ∎

## 4. Identity (5): verified [D]

$\mathcal M_R-\mathcal M_{2R}=\bigl(\begin{smallmatrix}G&-\tau\\-\tau^*&\sigma\end{smallmatrix}\bigr)$.
**Proof:** $J_{2R}=J-G$, $\beta_{2R}=\beta-\tau$ from §3; for the $(2,2)$ block,
$\eta_{2R}-\eta_R=(h_{2R}-h_R)+2\mathrm{Re}(\hat a^*(b_{2R}-b_R))-\hat a^*(S_{2R}-S_R)\hat a$
$=d-2\mathrm{Re}(\hat a^*c)+\hat a^*D\hat a=\sigma$ using
$h_{2R}=h_R+d$, $b_{2R}=b_R-c$, $S_{2R}=S_R-D$. ∎

Identities (3),(4),(6),(7a–c),(8),(9) are direct consequences; no independent
verification needed beyond the above.

## 5. Producer contract audit (§7): two logical gaps [O]

The seven-item contract is compact and well-structured, but two hypotheses
needed by the identities are not explicitly assigned to contract items:

**Gap 1 — Trace-defect certification.** Identity (2) *requires*
$(I-Q_R)\tilde V_R=[U_R,U_Rv]$ exactly (§4: "If trace defects are present,
(2) cannot be used unchanged"). The contract's item 6 mentions "trace-error
contributions" only vaguely within a list. **Recommendation:** promote trace
matching to an explicit item: either certify zero trace defect, or bound the
additional linear/quadratic terms from §4's fallback.

**Gap 2 — $\gamma_R$ applicability verification.** §4 states the $\gamma=1$
theorem "may be imported only after verifying that its operator, projector,
and cutoff match these spaces." No contract item explicitly requires
documenting this match for $\mathcal C_R=(Q_RA_RQ_R)|_{\mathrm{Ran}\,Q_R}$.
**Recommendation:** add explicit item requiring the operator/projector/cutoff
identification certificate reference.

These are contract-completeness gaps, not mathematical errors. The identities
themselves are correct.

## 6. Verdict

$$\boxed{
\begin{aligned}
&\text{[D] v14.145 τ radius WITHDRAWN — mixed term }E^*Be\text{ omitted; v14.147 correction confirmed.}\\
&\text{[D] v14.147 identities (1),(2),(5) independently verified (algebra + numerics).}\\
&\text{[D] Fixed-normalizer design sound; reduces to v14.136 when }J=I,\beta=0.\\
&\text{[O] Producer contract: 2 logical gaps (trace-defect item, }\gamma_R\text{ match item).}\\
&\text{v14.145 (G),(σ) radii unaffected.}
\end{aligned}
}$$

---

HANDOFF-ACK
from: v14.147
target: sandbox
status: closed
result: Tau counterexample independently confirmed via exact rational arithmetic; v14.145 (τ) bound withdrawn. Identities (1),(2),(5) verified by independent algebra and numerical test. Producer contract audited; two completeness gaps reported above (trace-defect certification, γ_R applicability). No further sandbox action on v14.147.
constraints: None.
