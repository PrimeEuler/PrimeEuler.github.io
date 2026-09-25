# Cone Derivation Ledger v13.783 — External Audit Round 100

Date: 2026-09-25

Auditor: External audit thread (Claude, independent instance).

Scope: v13.781 ("Lane A Primitive-Affine Nonclosure and Correct Pre-Integrated Compatibility Gate") and v13.782 ("Lane A Source Resolution: Exact Pre-Integrated Deficiency Solve and Global Scalar Closure of the Affine Ratios").

Verdict: **PASS** on both. v13.782's central move — solving for the true deficiency vector directly via \(T_a\)-invertibility rather than any \(S_a\)-based shortcut — is source-faithful and, on close inspection, is *not* a relabeled resurrection of the Round-88/v13.741 error. Details below, including a clarification of *why* that is true that goes beyond what either entry states explicitly.

## 1. v13.781 — primitive-affine nonclosure

Re-checked the three closure attempts against prior audited results:

- **(i) basepoint moments**: matches the tautology already established in v13.773 and confirmed again in v13.779 §2 — evaluating (E)/(O) at the basepoint returns a definitional identity, not new information. Consistent.
- **(ii) formal Schur/inverse feedback**: cites v13.773's \(M_{00}=M_{1x}=-1\), \(M_{0e}=M_{1e}=0\) — independently re-derived by this auditor via sympy in Round 97 (v13.775) and reconfirmed here by direct substitution; the resulting ratios are \(0/0\) exactly as claimed.
- **(iii) Section-6 Green transverse traces** (the new content of this entry): given the von Neumann boundary-triple coordinates \(\Gamma_0,\Gamma_1\) inherited from v13.661 (\(\Gamma_0v_e=\sqrt{h_A}\), \(\Gamma_1v_e=0\); \(\Gamma_0v_o=0\), \(\Gamma_1v_o=i\sqrt{h_A}\)), the argument that these vanish identically on the corresponding parity deficiency directions is straightforward linear algebra once the coordinates are accepted, and the resulting nonclosure (all three closure routes fail structurally, not by accident) is a clean, well-supported conclusion.

**Caveat, not a finding of error**: the \((\Gamma_0,\Gamma_1)\) boundary-triple formulas are imported from v13.661, a parent entry from well before this session's audit window; this round did not re-derive them from the Suzuki PDF's own (differently-notated) boundary form \(W(u,v)=\langle D_a^*u,v\rangle_{T_a}-\langle u,D_a^*v\rangle_{T_a}\) (Section 6.4-6.5 of the source). The internal logic of v13.781 is sound conditional on v13.661; that parent identity itself is outside this round's re-verification scope.

## 2. v13.782 — source-level resolvent solve

### 2a. Citation check against the PDF, Sections 6.2 and 8.3

Read `research-notes/2606.09096v2.pdf` directly (pages 21, 29-30). Every quoted identity is verbatim accurate:

- "\(T_a(D_a^*v)=i(T_av)'\)" — page 21, exact match.
- "Since \(\lambda<\lambda_a\), \(T_a=A_a-\lambda I\) is invertible... \(T_av_+=C_+e^x\), \(T_av_-=C_-e^{-x}\) have unique solutions" — page 21, exact match, and this is the content of the source's own rigorously proved Lemma 6.2.
- Equations (8.4)/(8.5) and the affine coefficients \(A_\pm=\int k_x(0,y)(-v_\pm(y))dy\mp C_\pm\), \(B_\pm=\int k(0,y)(-v_\pm(y))dy-C_\pm\) — page 30, exact match, including signs. Substituting these into eq. (9) of v13.782 (\(A_+/C_+=-(1+r_{1,a})\), \(B_+/C_+=-(1+r_{0,a})\)) checks out by direct algebra using \(I_{0,a}=(K_av_e)(0)\), \(I_{1,a}=(K_av_o)'(0)\) as in v13.779's convention.
- The warning "(8.5) is different from \(S_au_\pm=C_\pm\bar De_{\pm i}\)" — page 30, exact match.

### 2b. Does this resurrect the Round-88 error? Independent resolution.

This is the substantive question, and it required going beyond what v13.782 itself argues. Round 88 (v13.741, this auditor's own entry) retracted v13.740 for treating \(S_Au_\pm=\bar De_{\pm i}\) as the defining relation for the true deficiency vectors, citing the same page-30 sentence quoted above.

On rereading the source in full this round (not just the flagged sentence), the following mechanism resolves *why* that retraction was correct and *why* v13.782's current construction does not repeat it — a distinction neither v13.741 nor v13.782 states explicitly in operator-theoretic terms:

- \(S_a\) (Section 8.3) is defined as \(S_a:=G_a-\lambda(-\Delta_N)^{-1}\), where \(G_a=P_aGP_a\) carries the **projection \(P_a\) onto \(L^2_0(-a,a)\)** (the mean-zero subspace). Its rigorous identity \(S_a=\bar DT_a\bar D^{-1}\) (established via the isometry \(\|u\|_{S_a}^2=\|v\|_{T_a}^2\) for \(u=Dv\)) is exact, and it genuinely implies \(S_au_z=\bar De_z\) for the resolvent family \(v_z\) (\(T_av_z=e_z\)), including at \(z=\pm i\) — this part of Round 88's audit was correct to confirm as verbatim-in-source, and by linearity (\(v_\pm=C_\pm v_{\pm i}\)) it also gives \(S_Au_\pm=C_\pm\bar De_{\pm i}\) rigorously.
- The kernel \(k(x,y)=g(x-y)-\lambda N(x,y)\) appearing in (8.4)/(8.5), however, is applied as a **raw, unprojected** integral operator (\(\int_{-a}^a k(x,y)v(y)\,dy\)), not composed with \(P_a\). This raw kernel operator is *not* the same operator as \(G_a=P_aGP_a\) (equivalently \(S_a\) is not literally "\(-\)the (8.5) kernel operator"), because \(P_a\) is a nontrivial mean-subtraction projection. This is almost certainly the concrete referent of Suzuki's "the above argument ignores domain issues" — the naive double-integration from (8.4) to (8.5) does not track the \(P_a\)-projection that the rigorous \(S_a\)/\(G_a\) machinery carries, which is exactly why (8.5) needed the extra explicit affine terms \(A_\pm,B_\pm\) that a clean \(S_a\)-inverse would not.
- v13.740/v13.776 (retracted) tried to use "\(S_A^{-1}\bar De_{\pm i}\)" as a shortcut standing in for the (8.5)-side finite deficiency construction — i.e. conflating the projected/\(S_a\) picture with the raw-kernel/(8.5) picture. That conflation is the actual error, and it is what Round 88 correctly (if not fully explicitly) flagged.
- **v13.782 does not make this conflation.** Its construction \(v_{a,\pm}=C_{a,\pm}T_a^{-1}e^{\pm x}\) works entirely on the \(T_a\) side (Section 6.2's rigorously invertible operator, proved via Lemma 6.2, no projection subtlety), and \(u_{a,\pm}:=\bar Dv_{a,\pm}\) is defined by applying \(\bar D\) directly — never through \(S_a^{-1}\), and never through the raw (8.5) kernel operator either. It is a third, valid route that happens to agree with (via the exact isometry) what \(S_au_\pm\) would rigorously equal, without ever needing to invoke \(S_a\) or resolve the projection subtlety at all.

This confirms v13.782's own claim in §6 ("No specialization of the generic \(S_a^{-1}\bar De_z\) formula is used") is correct, and supplies the operator-theoretic reason it is correct, which the entry itself does not spell out. This is offered as a positive clarification, not a correction — no error is found in v13.782.

### 2c. Parity/reflection step

\(T_a=A_a-\lambda I\) commutes with the reflection operator \(J\) because \(A_a\) does (Suzuki, Section 4.5, page 18: "\(G_aJ=JG_a\)... both \(B_a=D^*G_aD\) and its Friedrichs extension \(A_a\) commute with \(J\)", and \(\lambda I\) trivially commutes with \(J\)). Hence \(T_a^{-1}\) also commutes with \(J\) (standard: if \(T_aJ=JT_a\) then \(T_a^{-1}J=JT_a^{-1}\)), which licenses splitting \(w_a=T_a^{-1}e^x=T_a^{-1}(\cosh x+\sinh x)\) into \((T_a^{(+)})^{-1}\cosh x\) (even) and \((T_a^{(-)})^{-1}\sinh x\) (odd) — eqs. (5E)/(5O). Confirmed correct and source-grounded.

### 2d. Affine coefficient formulas, eq. (9)

Direct substitution: \(B_+/C_+=(\int k(0,y)(-v_+(y))dy-C_+)/C_+=-(K_av_+)(0)/C_+-1=-(I_{0,a}/C_+)-1=-(1+r_{0,a})\), using \((K_av_+)(0)=(K_av_A)(0)=I_{0,a}\) (parity reduction, matching v13.779 eq. 2). Matches exactly. Same check for \(A_+/C_+=-(1+r_{1,a})\).

## 3. Self-audit note

No error of my own is disclosed this round. The deep dive into the \(S_a\) vs. raw-(8.5)-kernel distinction was necessary to be confident that v13.782 is not quietly repeating the error this auditor itself flagged in Round 88 — it is not, and the mechanism is now on record.

## Result

\[
\boxed{\textbf{PASS: v13.781 (primitive-affine nonclosure) and v13.782 (source-level global resolvent closure).}}
\]

The affine-closure question is resolved: \(r_{0,a},r_{1,a}\) are global resolvent traces of \(T_a^{-1}\), not locally-determinable extension data, and no shortcut through \(S_a\) or the raw (8.5) kernel is used or needed. The next gates (bounding the resolvent traces as \(a\to\infty\), per v13.782 §8) are appropriately scoped as open, not claimed.
