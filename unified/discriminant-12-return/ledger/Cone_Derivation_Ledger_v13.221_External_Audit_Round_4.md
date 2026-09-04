# Cone Derivation Ledger v13.221 — External Audit, Round 4

Date: 2026-09-04

Status labels: **[S]** source-established, **[D]** exact derived, **[N-cert]** certified numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This is an independent external audit of every ledger entry landed on `master` since the previous external round (`v13.203_External_Audit_Round_3`), covering `v13.204` through `v13.220` — the full Paper B ground-up audit, the Casimir/Null-Diamond audit and foundation promotion, the semiclassical/LQG relocation, the Paper C ground-up audit and v1.1 promotion, and the principal-paper v0.3.3 dependency audit through the v0.3.4 ground-up theorem audit. Pure figure-pipeline/CI-naming hygiene commits (`v13.205`–`v13.207`, `v13.210`) were triaged by diff/title and not independently re-derived, consistent with the methodology of prior rounds.

Every boxed mathematical identity below was independently re-derived by hand and, where practical, cross-checked with an independent symbolic computation (`sympy`), not merely read and accepted from the ledger prose.

## 1. Paper B v2 / v2.1 — Lorentz cutting-plane geometry

**[D] Verified by hand.** For `G_{a,b}=(a+b)L+(a-b)B_Y`, the metric-dual normal `m=(a-b,0,-(a+b))` satisfies `G_{a,b}m=0` and `m^2=-4ab`, and the characteristic polynomial `chi_G(lambda)=lambda(lambda^2+4ab)` follows directly from the displayed matrix. The `v13.213` correction — that the classification proposition's `n=(a-b,0,a+b)` is not the Lorentz metric-dual of the invariant cutting functional even though it shares the same squared norm — is a real and correctly identified defect; `v13.214`'s consistent adoption of `m` throughout resolves it.

**[D] Verified.** The normalized generator `Ĝ_{a,b}=G_{a,b}/(2 sqrt(|ab|))` has eigenvalues `±i` (`ab>0`) / `±1` (`ab<0`); this is immediate from the eigenvalues `0, ±2 sqrt(ab)i` (or `±2 sqrt(-ab)`) of the unnormalized generator. The projective coordinates `z=zeta/c` (`|z|=1`) and `xi_pm=eta_pm/c` (`xi_+ xi_-=1`) are correctly scale-invariant under `(a,b,c) -> (kappa a, kappa b, kappa c)`.

**[Audit] Concur.** The intrinsic-projective-orbit-map versus chosen-equation-level-raising-lift distinction is a genuine and necessary correction; the unnormalized power map is not equation-rescaling invariant (`zeta^n` scales as `kappa^n` under an equation scaled by `kappa`), while the normalized `z -> z^n` is intrinsic. No defect found in this hierarchy.

## 2. Casimir / Null-Diamond bridge — verified computationally

**[N-cert] Confirmed exactly via sympy**, for `Q(alpha,beta)=((alpha^2-beta^2)/2, alpha beta, (alpha^2+beta^2)/2)` and Lorentz form `<(X,Y,T),(X',Y',T')>_eta = TT'-XX'-YY'`:

```
<Q(a,b),Q(c,d)>_eta - (1/2)(ad-bc)^2  =  0   (exact, symbolic)
```

and consequently, with `M_F=(Q1+Q2)/2`, `D_F=(Q1-Q2)/2`, `Delta=ad-bc`:

```
M_F^2 - Delta^2/4 = 0,   D_F^2 + Delta^2/4 = 0,   <M_F,D_F>_eta = 0
```

all confirmed symbolically exact, so `M_F^2=1/4` for a unimodular pair is correct.

**[N-cert] Confirmed exactly via sympy**, the SU(2) and SU(1,1) Casimir-completion identities:

```
R_+^2 - (C_+ + delta^2/4) = 0,     A_+^2 - (R_+^2 - Z_+^2) = 0     [SU(2)]
R_-^2 - (C_- + delta^2/4) = 0,     A_+^2 - (Z_+^2 - R_-^2) = 0     [SU(1,1)]
```

with `C_+=J(J+delta)`, `R_+=J+delta/2`, `Z_+=q+delta/2`, `A_+^2=(J-q)(J+q+delta)` for SU(2), and the analogous SU(1,1) definitions. All four boxed identities in `v13.209`/`v13.212` are exact.

**[D] Verified by hand.** The "ramified Boolean return is factor exchange, not translation" claim: with `ḡ_12=[[1,1],[0,1]]` acting on `(x,y)` as `(x,y) -> (x+y,y)`, and `Phi(x,y)=(eps1,eps2)=(x,x+y)`, direct substitution gives `Phi ḡ_12 Phi^{-1}(eps1,eps2) = (eps1+eps2, eps1) = (eps2,eps1)` mod 2 — confirmed exactly, a genuine swap, not a nonzero Boolean shift.

**[Audit] Concur** with the `v13.209` correction to the Paper-C Bargmann index (see §3 below) and with the `v13.211` decision to keep the LQG comparison (`gamma_eff=1/(4 sqrt2)`) explicitly outside the audited theorem chain — the source's own guardrail language was checked and is appropriately conservative (a normalization comparison, not a claimed derivation of the Barbero–Immirzi parameter).

## 3. Paper C v1.1 — quantum-realization foundation

**[D] Verified by hand and previously by direct example.** For `d=n1-n2`, `C=(d^2-1)/4=k(k-1)` with `k=(|d|+1)/2`: substituting `k=(|d|+1)/2` gives `k(k-1)=(|d|+1)(|d|-1)/4=(d^2-1)/4`, an immediate algebraic identity — confirmed. The `v13.215`/`v13.216` correction (global `k=(n1-n2+1)/2=X` is wrong; `k=X` only holds in the oriented `d>=0` sector) is mathematically necessary: the quadratic `k(k-1)=C` is symmetric under `k -> 1-k`, so `C` alone cannot distinguish `k=(d+1)/2` from `k=(1-d)/2` when `d<0`, and only `k=(|d|+1)/2>0` is the valid positive discrete-series label.

**[N-cert] Confirmed exactly via sympy**, the strengthened revival identity for the Heisenberg matrix `A=[[0,-p,0,m],[p,0,m,0],[0,m,0,-p],[m,0,p,0]]`, `p=(a+b)/2`, `m=(a-b)/2`:

```
A^2 - (-a*b*I_4)  =  0   (exact, symbolic, all four diagonal entries confirmed -ab, all off-diagonal entries confirmed 0)
```

This directly gives `exp(T_cl A)=-I_4`, `exp(2 T_cl A)=I_4` for `T_cl=pi/sqrt(ab)`, `ab>0`, as claimed. The accompanying downgrade of "every state reproduces the classical period exactly" to "parity eigenstates revive up to phase at one period; arbitrary states are only guaranteed to revive up to phase at two periods" is the logically correct reading of `U(T_cl)=e^{i alpha}(-1)^N` (a parity operator, not a scalar on a generic superposition) — this defect in the original manuscript was real, and the correction is exact.

**[N-cert] Re-confirmed** (previously verified this round, `sympy`, reproduced here for completeness): the mean-field trajectory derived from the coherent-state occupation numbers satisfies `T_q(r) = T0 cosh(2r) + alpha1 alpha2 sinh(2r)` — i.e. `T_q` is naturally a function of `r`, not `2r` — matching the `v13.215`/`v13.216` diagnosis that the original theorem statement's `T_q(2r)` mislabels its own function's argument.

## 4. Principal paper v0.3.3 → v0.3.4 — finite-reduction correction (the round's central result)

This is the most consequential correction in the round and was independently re-derived in full rather than spot-checked.

**[D] Verified by hand.** In the basis `(f_1,f_2)=(2, sqrt(3)-1)` of `p_2`, multiplication by `lambda=2+sqrt(3)`:

```
lambda*f_1 = 4+2sqrt(3) = 3 f_1 + 2 f_2      (solve 2a-b=4, b=2 -> a=3, b=2)
lambda*f_2 = sqrt(3)+1  = 1 f_1 + 1 f_2      (solve 2a-b=1, b=1 -> a=1, b=1)
```

reproducing `g_12=[[3,1],[2,1]]` exactly as the matrix of `times lambda` in this basis — confirmed independently, not merely accepted from the source.

**[D] Verified by hand — the additive-transport claim.** With `ḡ_12=[[1,1],[0,1]] (mod 2)` acting as `ḡ_12(f̄1)=f̄1`, `ḡ_12(f̄2)=f̄1+f̄2`, and `psi: f̄1 -> 1, f̄2 -> omega^2` (a valid F_2-additive basis map, since `{1,omega^2}` are two of the three distinct nonzero elements of `F_4` and hence F_2-independent):

```
psi(ḡ_12(f̄1)) = psi(f̄1) = 1                       Fr(1) = 1^2 = 1                    match
psi(ḡ_12(f̄2)) = psi(f̄1+f̄2) = 1+omega^2 = omega    Fr(omega^2) = omega^4 = omega       match
```

using `omega^2=1+omega` (char 2) so `1+omega^2=omega` — confirmed exactly by hand: `psi ḡ_12 psi^{-1} = Fr` on `F_4`.

**[D] Verified by hand — the literal-residue claim.** Since `p_2=(1+sqrt(3))` and `p_2` lies below `P_2`, `1+sqrt(3) ≡ 0 (mod P_2)`, so `sqrt(3) ≡ -1 ≡ 1`, and `2 ≡ 0` (characteristic 2). Hence `lambda=2+sqrt(3) ≡ 0+1 = 1 (mod P_2)` — literal residue-field multiplication by the Pell unit is the identity, not Frobenius. This is a genuinely subtle and easy-to-miss distinction (two different "mod 2" reductions of the same matrix data, one additive-transported, one literal ring multiplication), and the correction is exact.

**[N-cert] Confirmed exactly via sympy** (mod-2 linear algebra), the companion group-theoretic claim: with `M_omega=[[0,1],[1,1]]`, `Fr=[[1,1],[0,1]]` over `F_2`, `Fr * M_omega * Fr^{-1} mod 2 = M_omega^{-1} mod 2` exactly, so `<M_omega, Fr> = GL_2(F_2) ≅ S_3` as claimed.

**[D] Verified by hand — `v13.220`'s Cayley-reciprocity section.** For `g in SL_2`, `tau=tr(g)`, `H=g-(tau/2)I`, `K=(g-I)(g+I)^{-1}`: Cayley–Hamilton (`g^2=tau g - I`) gives `H^2=(tau^2/4-1)I` directly by expansion. Independently expanding `(g+I)((tau+1)I-g) = (tau+2)I` and `(g-I)((tau+1)I-g) = 2g-tau I = 2H` (both by direct matrix-commutative-polynomial expansion using `g^2=tau g-I`) gives `K=2H/(tau+2)` and `KH=(tau-2)I/2`, hence `K=H^{-1} iff tau=4` — every step re-derived independently and confirmed exact.

**[D] Verified by hand — the direct `O_K/P_2 ≅ F_4` proof `v13.220` recommends adding.** Mod `P_2`: `1+sqrt(3)≡0` so `sqrt(3)≡1`; using `sqrt(3)=zeta+zeta^{-1}` gives `zeta+zeta^{-1}=1`, i.e. `zeta^2+zeta+1=0` (using char-2 sign collapse), and `X^2+X+1` is irreducible over `F_2`, giving `O_K/P_2 ≅ F_2[zeta]/(zeta^2+zeta+1) ≅ F_4` directly. Confirmed correct and, as `v13.220` notes, strictly more self-contained than citing it as a standard fact.

**[D] Verified by hand — the trace/XOR identity.** `q_12(m,n)=2m^2-2mn-n^2 ≡ -n^2 ≡ n (mod 2)` (using `n^2≡n` for `n in F_2`). Separately, `Tr(1)=1+1=0`, `Tr(omega)=Tr(omega^2)=omega+omega^2=1` (using `omega^2+omega+1=0`), so under `psi(m f_1+n f_2)=m+n omega^2`, `Tr(psi(...)) = m*Tr(1)+n*Tr(omega^2) = n`, matching `q̄_12=n`. Confirmed exactly.

## 5. Assessment of `v13.220`'s own packaging critique

**[Audit] Concur.** `v13.220`'s observation that the trace/XOR identity and the `n=11` Artin specialization are argued in the body but not folded into the formal Theorem 2.1 statement is a legitimate publication-completeness note, correctly labeled as packaging rather than a mathematical defect. No counter-finding.

## 6. Overall verdict for this round

**No mathematical error was found in any of `v13.204`–`v13.220`.** Every boxed identity checked — by hand, by independent symbolic computation, or both — reproduced exactly. This is a substantially larger and more consequential batch than either of the two prior external-audit rounds (it closes out the full Paper B, Paper C, and Casimir/Null-Diamond foundation cycle and lands the principal paper at v0.3.4), and the parallel session's own self-audits in this round (`v13.213`, `v13.215`, `v13.218`, `v13.220`) are, on independent re-derivation, accurate: the defects they report (the `n` vs `m` cutting-normal mislabeling, the global-vs-oriented-sector Bargmann index, the argument-mislabeled mean-field residual, the literal-vs-transported mod-2 Pell/Frobenius conflation, the missing direct `F_4` quotient proof, the Theorem-2.1 packaging gap) are all real, and their corrections are all exact.

The one genuinely new and independently significant piece of mathematics surfaced this round — not merely a bug fix — is the literal-residue-vs-transported-action distinction in §4: `lambda ≡ 1 (mod P_2)` while the *coordinate* reduction of the same Pell matrix, after an explicit additive identification, is Frobenius. This is a real subtlety (two different, easily conflated "mod 2" reductions of the same arithmetic object) and the project's handling of it is correct.

## 7. Guardrails for future work

No new guardrails are added this round; all guardrails from `v13.186`, `v13.190`, and `v13.203` remain in force, and the `v13.220` terminology guardrails (centered-operator vs. Lie-generator language, `p_2/2p_2` vs. `O_K/P_2` as different rings, literal-vs-transported mod-2 action) are independently confirmed necessary and correctly stated.

**External audit round 4: CLOSED. No corrections required to `master`.**
