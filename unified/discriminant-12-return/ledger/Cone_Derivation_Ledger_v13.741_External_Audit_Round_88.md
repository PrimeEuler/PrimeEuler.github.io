# Cone Derivation Ledger v13.741 — External Audit Round 88

Date: 2026-09-23

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: verify v13.739 (compact provenance map) and v13.740 (finite-edge paired transfer and convergence criterion), the two entries pushed since Round 87 (v13.738, commit `ffc3e01`).

## 0. Coordination note

No version-number collision this round. v13.739 and v13.740 landed sequentially with no overlap — the improved cross-thread coordination is working as intended. `git fetch` immediately before this write confirms `origin/master` is unchanged at `865ea9a` since these two entries landed; this entry is pushed as v13.741, the next free number.

## 1. v13.739 (Compact Provenance Map) — independently verified, no errors

The Section A/B rows cite results already independently verified in Round 87 (v13.738); this audit did not re-verify citations already checked, per the provenance registry's own stated purpose.

The Section C cross-lane algebra was re-derived by hand from the stated inputs \(E(z)=\xi(s)+\xi'(s)\), \(L(s)=\xi'(s)/\xi(s)\), \(s=\tfrac12-iz\), \(ds/dz=-i\):

- \(E(z)=\xi(s)[1+L(s)]\) — confirmed by direct factoring.
- \(E'/E=-i(L'+L+L^2)/(1+L)=-iL-iL'/(1+L)\) — confirmed by the chain rule: \(E'(z)=-i[\xi'(s)(1+L(s))+\xi(s)L'(s)]\), divide by \(E(z)=\xi(s)(1+L(s))\), simplify. Matches exactly.
- \(T_{\rm pair}(z)=C_\xi/(1+L(s))\) — confirmed by substituting \(\Xi(-iz)=\xi(s)\) into the established \(T_{\rm pair}=C_\xi\Xi(-iz)/E(z)\).
- \(T_{\rm pair}'/T_{\rm pair}=iL'/(1+L)\) — confirmed by differentiating \(T_{\rm pair}=C_\xi(1+L(s))^{-1}\) via the chain rule.
- Additive split \(-iL=T_{\rm pair}'/T_{\rm pair}+E'/E\) — confirmed: the two \(L'/(1+L)\) terms cancel with opposite sign, leaving exactly \(-iL\).
- Multiplicative closure \(ET_{\rm pair}=C_\xi\Xi(-iz)=C_\xi\widehat\Phi(z)\) — confirmed by direct substitution.
- Divisor allocation at a zero \(\rho\) of \(\xi\) of multiplicity \(m\): re-derived via local Laurent expansion (\(\xi(s)\sim c(s-\rho)^m\), \(\xi'(s)\sim cm(s-\rho)^{m-1}\), so \(E\sim cm(s-\rho)^{m-1}\) has order \(m-1\), and \(T_{\rm pair}=C_\xi\xi/E\sim(C_\xi/m)(s-\rho)\) has order exactly \(1\) regardless of \(m\)). Confirmed, including the boundary case \(m=1\Rightarrow E(\rho)\ne0\).
- The moment identity \(L=M_1/M_0\), \(L'=(M_2M_0-M_1^2)/M_0^2\) (cited from v13.730): re-derived from \(\Xi(w)=M_0(w)=\int\Phi(r)e^{wr}dr\), \(\Xi'(w)=M_1(w)\), \(M_0'(w)=M_1(w)\), \(M_1'(w)=M_2(w)\), giving the quotient rule directly. Confirmed.

No errors found in v13.739.

## 2. v13.740 (Finite-Edge Paired Transfer) — internal algebra correct, but foundational identity is source-contradicted

### 2a. Internal algebra: confirmed correct

Given the stated definitions \(A_A=(z-i)F_{A,+}\), \(B_A=(z+i)F_{A,-}\), \(P_A=A_A-B_A\), \(m_A=-i(A_A+B_A)/P_A\):

- \(A_A+B_A=im_AP_A\), hence \(A_A=(1+im_A)P_A/2\), \(B_A=(im_A-1)P_A/2\) — re-derived by hand from the \(m_A\) definition; confirmed.
- The ratio invariant \(\mathscr R_A(z;z_*)=[P_A(z)/P_A(z_*)]\cdot[\Xi(-iz_*)E(z)/(\Xi(-iz)E(z_*))]\) — confirmed by substituting the v13.739 closed form for \(T_{\rm pair}(z_*)/T_{\rm pair}(z)\).
- \(\Delta_A=P_A'/P_A-iL'/(1+L)\) and \(\log\mathscr R_A(z;z_*)=\int_{z_*}^z\Delta_A\,d\zeta\) — confirmed as the logarithmic derivative / path-integral identity.
- The theta-kernel rewrite \(\mathscr R_A=[EP_A(z)/EP_A(z_*)]\cdot[\widehat\Phi(z_*)/\widehat\Phi(z)]\) and the target \(d/dz\log[EP_A]\to d/dz\log\widehat\Phi=-iL(1/2-iz)\) — confirmed by substitution and by re-deriving \(d/dz\log\widehat\Phi(z)=-iL(1/2-iz)\) independently (chain rule on \(\Xi(-iz)\)).
- The divisor test in §8 is a correct restatement of the v13.739 divisor allocation. Confirmed.
- The §10 observation that \(m_A\) alone cannot fix \(P_A\) (since scaling \(A_A,B_A\) by a common factor leaves \(m_A\) invariant but rescales \(P_A\)) is correct — elementary but worth having stated explicitly.

All of this algebra is sound **conditional on** the definitions of \(F_{A,\pm}\), \(A_A\), \(B_A\) in §2 being the right objects.

### 2b. Foundational identity: contradicted by the source

Section 2 defines the finite deficiency pairing via
\[
S_Au_z=\bar De_z,\qquad S_Au_\pm=\bar De_{\pm i}
\]
"up to the fixed deficiency normalizations," citing this as "the established continuous-kernel defect pair."

The first relation, \(S_au_z=\bar De_z\), **is** verbatim in Suzuki (p. 30): *"For \(e_z(x):=\exp(-izx)\), the equation \(T_av_z=e_z\) becomes \(S_au_z=\bar De_z\)."* Confirmed accurate.

The second relation, applied at the deficiency points \(z=\pm i\), is **not**. Immediately after introducing \(v_\pm\) via the *different* equation \(T_av_\pm=C_\pm e_{\pm i}\) (note the extra unknown constant \(C_\pm\), and note this is stated as a separate definition from the generic \(v_z\) family, not a special case of it) and the resulting integral equation (8.5) — which carries extra boundary terms
\[
C_\pm e^{\pm x}+A_\pm x+B_\pm,
\qquad
A_\pm=\int_{-a}^a k_x(0,y)(-v_\pm(y))\,dy\mp C_\pm,
\quad
B_\pm=\int_{-a}^a k(0,y)(-v_\pm(y))\,dy-C_\pm
\]
— Suzuki writes explicitly: *"It should also be noted that the equation (8.5) is different from \(S_au_\pm=C_\pm\bar De_{\pm i}\)."*

This is a direct statement, in the source, that the relation v13.740 adopts as foundational (even with the constants \(C_\pm\) restored, which is more than v13.740's "up to normalization" hedge covers) is **not** the correct one. The true relation at the deficiency indices requires the extra domain-dependent affine terms \(A_\pm x+B_\pm\), which Suzuki traces to real boundary/domain effects ("we avoid expressing these equations in terms of the operators \(T_a\) or \(S_a\), since the above argument ignores domain issues").

**Consequence:** \(F_{A,\pm}(z):=\overline{\langle\bar De_{\bar z},S_A^{-1}\bar De_{\pm i}\rangle}\) is built by applying \(S_A^{-1}\) to \(\bar De_{\pm i}\) and calling the result (a multiple of) \(u_\pm\). Per Suzuki's explicit caveat, \(S_A^{-1}\bar De_{\pm i}\) is not \(u_\pm\) (or any fixed multiple of it) — the actual \(u_\pm\) satisfies the more complicated relation carrying the extra affine boundary data. This foundational substitution error propagates through every subsequent object in the entry: \(A_A\), \(B_A\), \(P_A\), \(m_A\), and hence the boxed convergence criteria \(\mathscr R_A\to1\) and \(\Delta_A\to0\) in §5–8 are not yet established tests of convergence to Suzuki's actual Section-7 target — they are correct algebraic consequences of an incorrectly-defined \(F_{A,\pm}\).

This is the same category of error as this auditor's own Round 85 mistake (conflating a relation that holds for a generic/regular parameter with what happens exactly at the deficiency-index points, where \(\bar D\) and domain effects require separate care) — flagged here for the same reason that one was retracted: because the source text says so explicitly, not merely because it looks suspicious.

**What is not affected:** the v13.739 registry (Section 1 above), and the *closed-form target* \(T_{\rm pair}(z)=C_\xi/(1+L(s))\) itself, which v13.740 correctly imports rather than re-derives. Only the *finite-\(A\) construction meant to approximate it* (§2 onward) rests on the contradicted identity.

**Not fixed here.** Per the standing audit rule, this auditor does not silently patch another thread's construction to manufacture a passing result. The correct next step belongs to the source thread: either (a) reformulate \(F_{A,\pm}\) using the actual equation (8.5), tracking the affine boundary terms \(A_\pm,B_\pm\) and the constants \(C_\pm\) as genuine unknowns, or (b) find an alternative route to the finite deficiency vectors \(u_\pm\) that does not go through the identity Suzuki flags as false.

## 3. Result

\[
\boxed{\textbf{PASS: v13.739 cross-lane algebra, fully independently re-derived, no errors.}}
\]
\[
\boxed{\textbf{PASS: v13.740 internal algebra (\S3, \S5--\S8), correct conditional on its \S2 definitions.}}
\]
\[
\boxed{\textbf{FAIL: v13.740 \S2 foundational identity } S_Au_\pm=\bar De_{\pm i}\textbf{ (up to normalization) contradicts Suzuki p.30's explicit statement that this differs from the correct equation (8.5).}}
\]

No errors were found in this auditor's own work this round.

## 4. Next gate

The source thread should re-derive \(F_{A,\pm}(z)\) (equivalently \(A_A,B_A,P_A\)) from Suzuki's actual equation (8.5) rather than from \(S_Au_\pm=\bar De_{\pm i}\), before the v13.740 convergence criteria \(\mathscr R_A\to1\) / \(\Delta_A\to0\) can be treated as meaningful finite-edge tests. This auditor will re-check the corrected construction, if and when it lands, against p.30–31 of the source PDF directly.
