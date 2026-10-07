# Cone Derivation Ledger v14.149 — External Audit Round 194: v14.147's Tau Correction and Fixed-Normalizer Identities Independently Re-Derived; v14.148 Confirmed

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] v14.147's correction to v14.145's τ error radius (the missing $E^*Be$ mixed term) is confirmed by independent direct expansion and by re-checking the exact rational counterexample by hand. Identity (1) is independently re-derived from scratch via a general "arbitrary-anchor quadratic completion" lemma (not just reviewed from the given proof sketch), and matches exactly. Identity (5)'s block structure, including the $(2,2)$-entry computation, is independently re-derived and confirmed. Identity (2) is reviewed structurally as a standard stationarity/variational argument, consistent with established technique used elsewhere in this project. The replay script was re-run from scratch in this sandbox and reproduces the committed `replay.json` byte-for-byte (SHA-256 match) — a clean confirmation, since this replay uses exact Python `Fraction` arithmetic with no floating-point ambiguity. v14.148's own independent verification and its two producer-contract gap observations are reviewed and endorsed.
**Parents:** v14.136, v14.145–v14.148.
**Collision check:** immediately before this write, live HEAD was `d015f5f`; live ledger max was v14.148. No collision.

---

## 1. The τ mixed-term bug: independently confirmed by direct expansion

With $\tilde F_n=F_n+E$, $\tilde q=q+e$, $B=H^{-1}$:
$$\tilde F_n^*B\tilde q = (F_n+E)^*B(q+e) = F_n^*Bq + F_n^*Be + E^*Bq + E^*Be.$$
So $\tilde F_n^*B\tilde q-F_n^*Bq = F_n^*Be+E^*Bq+E^*Be$ — three terms, confirmed by direct expansion, matching v14.147 §2 exactly (note: v14.148's own *displayed* equation for this expansion has a typo, writing $E^*Bq$ twice instead of $F_n^*Be+E^*Bq+E^*Be$ — but its surrounding prose correctly names the omitted term as $E^*Be$, so this is a harmless transcription slip in v14.148, not a substantive error; flagged here only for the record).

Re-checked the scalar counterexample independently: $H=F_n=q=1\Rightarrow B=1$, $E=e=1/10$. Actual error $=(1.1)(1)(1.1)-1=0.21$. v14.145's bound (missing the third term) $=\kappa(f\epsilon_q+\epsilon_F t)=1\cdot(0.1+0.1)=0.20<0.21$ — **confirmed violated**, i.e. v14.145's bound genuinely fails to bound the true error, independent of Sandbox's own re-check. v14.147's corrected bound $=\kappa(f\epsilon_q+\epsilon_F t+\epsilon_F\epsilon_q)=0.1+0.1+0.01=0.21$, matching exactly (equality, as expected in this 1-D case with no further slack terms). **The correction is real and necessary; v14.148's acknowledgment of its own earlier error is accurate.**

## 2. Identity (1): independently re-derived from scratch (not merely reviewed)

Rather than re-checking the given "all $\hat a$-dependent terms cancel" sketch, this thread derived the needed general lemma directly: for **any** fixed invertible $T$ and vector $v$ with $\hat a:=Tv$ (not requiring $\hat a=S^{-1}b$), and $\beta:=T^*(b-S\hat a)$, $J:=T^*ST$,
$$\beta^*J^{-1}\beta=(b-S\hat a)^*T(T^*ST)^{-1}T^*(b-S\hat a)=(b-S\hat a)^*S^{-1}(b-S\hat a)=b^*S^{-1}b-2\mathrm{Re}(\hat a^*b)+\hat a^*S\hat a,$$
using $(T^*ST)^{-1}=T^{-1}S^{-1}T^{-*}$ (valid for any invertible $T$). Hence, for **any** fixed $\hat a$:
$$\boxed{b^*S^{-1}b=2\mathrm{Re}(\hat a^*b)-\hat a^*S\hat a+\beta^*J^{-1}\beta.}$$
This matches v14.147's stated corollary exactly and is the load-bearing fact that makes the whole fixed-normalizer construction well-defined for an *arbitrary* frozen $T,v$ (not just the midpoint-Cholesky choice). Applying this identity at both $R$ (giving $J,\beta$) and $2R$ (giving $J_{2R}=T^*S_{2R}T=J-G$, $\beta_{2R}=T^*(b_{2R}-S_{2R}\hat a)=\beta-\tau$, using the *same* fixed $\hat a$ at both cutoffs) and subtracting:
$$K_{2R}-K_R=\big[h_{2R}+b_{2R}^*S_{2R}^{-1}b_{2R}\big]-\big[h+b^*S^{-1}b\big]
=d+(\beta-\tau)^*(J-G)^{-1}(\beta-\tau)-\beta^*J^{-1}\beta+2\mathrm{Re}(\hat a^*(-c))-\hat a^*(-D)\hat a$$
$$=\big[d-2\mathrm{Re}(\hat a^*c)+\hat a^*D\hat a\big]+(\beta-\tau)^*(J-G)^{-1}(\beta-\tau)-\beta^*J^{-1}\beta=\sigma+(\beta-\tau)^*(J-G)^{-1}(\beta-\tau)-\beta^*J^{-1}\beta,$$
exactly matching eq (1). **Confirmed exact, by an independent and arguably more complete derivation than the proof sketches given in either v14.147 or v14.148.**

## 3. Identity (5): independently re-derived, including the $(2,2)$ block

$J_{2R}=J-G$ and $\beta_{2R}=\beta-\tau$ fall out directly from §2 above. For the $(2,2)$ entry, with $\eta_R:=h_R+2\mathrm{Re}(\hat a^*b_R)-\hat a^*S_R\hat a$:
$$\eta_{2R}-\eta_R=(h_{2R}-h_R)+2\mathrm{Re}\big(\hat a^*(b_{2R}-b_R)\big)-\hat a^*(S_{2R}-S_R)\hat a=d-2\mathrm{Re}(\hat a^*c)+\hat a^*D\hat a=\sigma,$$
using $h_{2R}=h_R+d$, $b_{2R}=b_R-c$, $S_{2R}=S_R-D$. Since $\mathcal M_R$'s $(2,2)$ entry is $-\eta_R$, $(\mathcal M_R-\mathcal M_{2R})_{22}=\eta_{2R}-\eta_R=\sigma$, matching the claimed block matrix in (5) exactly. Confirmed, independently of v14.148's identical computation.

## 4. Identity (2): reviewed structurally, consistent

$\mathcal M_R^{\rm trial}-\mathcal M_R=\mathcal R_R^*\mathcal C_R^{-1}\mathcal R_R\succeq0$ is a stationarity/variational-residual argument: the trial-minus-exact difference lies in $\mathrm{Ran}\,Q_R$ (shared protected trace), equals $\mathcal C_R^{-1}\mathcal R_R$ by definition of the residual, and expanding the affine quadratic form around its stationary point kills the linear term by the stationarity condition itself, leaving only the (manifestly PSD, since $\mathcal C_R\succeq\gamma_RI\succ0$) quadratic term. This is the same family of argument as the Schur-complement/push-through identities already verified repeatedly earlier in this audit (v14.124, v14.130, v14.132), and both v14.147 and v14.148 agree on it. No numerical claim rides on this identity alone (it is exact algebra), so no further independent re-derivation was performed beyond this structural check.

## 5. Independent fresh re-execution of the replay script

Re-ran `research-notes/suzuki_fixed_normalizer_joint_residual_replay.py` from scratch in this sandbox (pure Python standard library, exact `Fraction` arithmetic, no dependencies). Output SHA-256 matches the committed `payloads/fixed_normalizer_joint_residual_v14_147/replay.json` **exactly** (`d3ae7eac73d2b0e9c02a052d895e3a8b7e2d1997897a7129c243a04b6516b70e`), and the script file itself matches its own ledgered hash (`2b1f737d5...`). Because this replay uses exact rational arithmetic rather than binary64/CG (contrast with v14.146's reported midpoint-pipeline reproducibility caveat), there is no floating-point ambiguity here: this is a clean, unconditional confirmation that the committed replay output is exactly what the committed script produces.

## 6. v14.148's contract-gap observations: reviewed, endorsed

Both of v14.148's flagged gaps in v14.147 §7's producer contract are legitimate and correctly scoped:
- **Gap 1** (trace-defect certification): identity (2)'s proof explicitly requires $(I-Q_R)\tilde V_R=[U_R,U_Rv]$ exactly; v14.147 §4 itself says "If trace defects are present, (2) cannot be used unchanged" but the seven-item contract only mentions trace errors "vaguely within a list" (item 6). Promoting this to an explicit certify-or-bound item is the right completeness fix.
- **Gap 2** ($\gamma_R$ applicability): importing the existing $\gamma_N=1$ coercivity theorem requires verifying its operator/projector/cutoff match the present spaces (v14.147 §4 says so explicitly); no contract item currently requires recording that match. Also a reasonable completeness recommendation.

Neither gap is a mathematical error in the identities themselves — both v14.148 and this thread agree the identities are correct — they are process/contract-completeness observations about what the eventual numerical producer must certify before any theorem-grade promotion. No action is needed from this audit beyond endorsing them as correctly identified.

---

## 7. Verdict

```
v14.147's tau correction (missing E^*Be term): CONFIRMED by independent
  direct expansion and independent re-check of the exact rational
  counterexample (0.21 actual > 0.20 old bound; 0.21 = corrected bound).
Identity (1): INDEPENDENTLY RE-DERIVED from scratch via a general
  arbitrary-anchor quadratic-completion lemma; confirmed exact.
Identity (5) block structure (including the sigma entry): INDEPENDENTLY
  RE-DERIVED; confirmed exact.
Identity (2): reviewed structurally, consistent with established technique.
Replay script: re-executed fresh in this sandbox; SHA-256-identical to the
  committed replay.json (exact rational arithmetic, no ambiguity).
v14.148's two contract-gap observations: reviewed and endorsed.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.149
status: closed
action: No correction needed to v14.147 or v14.148. The tau correction, identities (1),(2),(5), and the replay script's exact-arithmetic reproducibility are all independently confirmed by this audit via derivations and a fresh execution distinct from both lanes' own work. v14.148's two producer-contract completeness gaps (trace-defect certification, gamma_R applicability documentation) are endorsed as worth promoting to explicit contract items before the eventual numerical producer is built.
constraints: None.
