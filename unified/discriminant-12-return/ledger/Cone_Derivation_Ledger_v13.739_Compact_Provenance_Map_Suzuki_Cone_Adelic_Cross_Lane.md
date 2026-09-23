# Cone Derivation Ledger v13.739 — Compact Provenance Map: Suzuki / Cone-Adelic / Cross-Lane

**Date:** 2026-09-23  
**Status:** coordination/provenance checkpoint; no theorem promotion beyond cited established entries  
**Parents:** v13.722, v13.730–731, v13.733–738  
**Purpose:** prevent redundant rederivation across the Suzuki and cone/adelic lanes. Items marked **ESTABLISHED** are dependencies to import, not re-prove, unless a later audit finds a conflict.

## Legend

- **[S] Suzuki-derived** — source identity or derivation owned by the Suzuki lane.
- **[C] Cone/adelic-derived** — independently derived in the cone/Tate/Weil/norm-line lane.
- **[X] Cross-lane consequence** — follows by combining already-established [S] and [C] results.
- **ESTABLISHED** — may be cited directly in future gates.
- **OPEN** — remains a genuine target; do not silently promote.

## A. Suzuki-derived identities — do not rederive

| Status | Identity/result | Provenance |
|---|---|---|
| **ESTABLISHED [S]** | Suzuki screw current is distribution-valued: \(\mathcal K=-g''\), with \(\widehat{-g''}(k)=k^2\widehat g(k)\). | v13.735; independently audited v13.738 |
| **ESTABLISHED [S]** | \(-g''(r)= -\frac12\operatorname{Pf}|r|^{-1}-(2A+1)\delta_0-\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}[\delta(r-\log n)+\delta(r+\log n)]-r''_{\rm arch}(r)\). | Suzuki §2.5, pp.12–13; source-checked v13.738 |
| **ESTABLISHED [S]** | Compensated half-line edge transform keeps the boundary contact term: \((h_+)''=-q_++Q_+(0)\delta_0\), hence \(\widehat h_+(k)=(Q_+(k)-Q_+(0))/k^2\). | v13.733; audited v13.738 |
| **ESTABLISHED [S]** | Section-7 paired deficiency identity: \(T_{\rm pair}(z)=C_\xi\,\Xi(-iz)/E(z)\), with \(E(z)=\xi(\frac12-iz)+\xi'(\frac12-iz)\) and \(C_\xi=2\xi'(3/2)/(\pi^2 i)\) for the audited normalization. | v13.737; Suzuki p.27 source-checked v13.738 |
| **ESTABLISHED [S]** | Consequently \(T'_{\rm pair}/T_{\rm pair}=-iL(\frac12-iz)-E'/E\). | v13.737; audited v13.738 |
| **OPEN [S]** | Finite-edge convergence \(E(z)T_{{\rm pair},A}(z)/\Xi(-iz)\to C_\xi\) as \(A\to\infty\). | v13.737 Gate 10; v13.738 §5 |

## B. Cone/adelic-derived identities — do not rederive

| Status | Identity/result | Provenance |
|---|---|---|
| **ESTABLISHED [C]** | Positive theta/Casimir kernel: \(\Xi(w)=\int_{\mathbb R}\Phi(r)e^{wr}dr\), so \(\Xi(-iz)=\widehat\Phi(z)\) in the adopted Fourier convention. | v13.722 |
| **ESTABLISHED [C]** | Logarithmic current: \(L(s)=\xi'(s)/\xi(s)=A_\infty(s)-P(s)\), with finite current supported at \(r=k\log p\). | v13.715, v13.730 |
| **ESTABLISHED [C]** | After half-density centering and inversion symmetrization, the finite Weil distribution is \(\sum_{n\ge2}\Lambda(n)n^{-1/2}[\delta_{\log n}+\delta_{-\log n}]\), with the archimedean term interpreted as a PV/finite-part distribution. | v13.734; audited v13.738 |
| **ESTABLISHED [C]** | Exact norm quotient: \(C_{\mathbb Q}/C_{\mathbb Q}^1\simeq\mathbb R_{>0}^\times\), hence logarithmic norm coordinate \(r=\log|u|_{\mathbb A}\). | v13.736; audited v13.738 |
| **ESTABLISHED [C]** | Canonical trivial-\(C_{\mathbb Q}^1\) projection on the regular representation is \(P_1=\int_{C_{\mathbb Q}^1}\lambda(k)dk\), yielding the norm-line carrier \(L^2(\mathbb R,dr)\) with translations \((U_\tau f)(r)=f(r-\tau)\). | current post-v13.738 cone/adelic gate |
| **ESTABLISHED [C]** | The v13.731 prime-power Hilbert space is an auxiliary realization of the arithmetic trace distribution, not the canonical norm-quotient representation; prime powers are distribution/orbit labels, not norm-line eigenstates. | v13.731, v13.736 plus norm-line projection gate |
| **ESTABLISHED [C]** | \(L(\frac12+w)=\Xi'(w)/\Xi(w)\); with moments \(M_j(w)=\int r^j\Phi(r)e^{wr}dr\), \(L=M_1/M_0\) and \(L'=(M_2M_0-M_1^2)/M_0^2\). | v13.730 and positive-kernel lane |

## C. New cross-lane consequences — established algebraically, do not duplicate

Let \(s=\frac12-iz\) and \(L=L(s)=\xi'(s)/\xi(s)\).

| Status | Identity/result | Derivation |
|---|---|---|
| **ESTABLISHED [X]** | Suzuki's symmetric prime-power train and the centered Weil finite distribution are the same arithmetic support/weights, up to the overall sign convention in \(-g''\). | Compare v13.735 with v13.734; independently recognized in v13.738 |
| **ESTABLISHED [X]** | Thus Suzuki \(-g''\) and the centered Weil current are two distributional realizations of the same prime–archimedean explicit-formula data; equality of full distributions requires retaining the stated contact/PV/archimedean normalizations. | v13.738 §3 |
| **ESTABLISHED [X]** | \(E(z)=\xi(s)[1+L(s)]\). | algebra from Suzuki definition of \(E\) |
| **ESTABLISHED [X]** | \(\displaystyle \frac{E'}E=-i\frac{L'+L+L^2}{1+L}=-iL-i\frac{L'}{1+L}\). | chain rule, \(ds/dz=-i\) |
| **ESTABLISHED [X]** | \(\displaystyle T_{\rm pair}(z)=\frac{C_\xi}{1+L(s)}\) as the meromorphic continuation of Suzuki's ratio. | combine [S] \(T_{\rm pair}=C_\xi\xi/E\) with \(E=\xi(1+L)\) |
| **ESTABLISHED [X]** | \(\displaystyle \frac{T'_{\rm pair}}{T_{\rm pair}}=i\frac{L'}{1+L}\). | logarithmic derivative |
| **ESTABLISHED [X]** | Exact additive split: \(\displaystyle -iL(s)=\frac{T'_{\rm pair}}{T_{\rm pair}}+\frac{E'}E\). | cancellation of the \(L'/(1+L)\) terms; agrees with v13.737 |
| **ESTABLISHED [X]** | Exact multiplicative closure: \(\displaystyle E(z)T_{\rm pair}(z)=C_\xi\Xi(-iz)=C_\xi\widehat\Phi(z)\). | [S] paired identity + [C] positive-kernel transform |
| **ESTABLISHED [X]** | At a zero \(\rho\) of \(\xi\) of multiplicity \(m\), the meromorphic factorization allocates divisor order \(1\) to \(T_{\rm pair}\) and \(m-1\) to \(E\): \(m=1+(m-1)\). For a simple zero, \(E(\rho)\neq0\) and the zero singularity of \(-iL\) is carried by \(T'_{\rm pair}/T_{\rm pair}\). | local Laurent expansion |
| **ESTABLISHED [X]** | The failed search for a linear Weil-current \(\leftrightarrow\Phi\) intertwiner is explained: the exact bridge is nonlinear, \(L=\partial_w\log\Xi=M_1/M_0\), while Suzuki supplies a multiplicative factorization of \(\Xi\). | combine [C] moment identity with [S] factorization |

## D. Guardrails / results not to promote

1. **OPEN:** no Hilbert–Pólya self-adjoint operator has been constructed.
2. **OPEN:** no RH implication follows from positivity of \(\Phi\), the screw kernel, or the paired deficiency identities.
3. **OPEN:** the finite-\(A\) Suzuki edge transfer has not yet been proved to converge to the exact Section-7 paired channel.
4. **OPEN:** no canonical adelic representation has been proved unitarily equivalent to the engineered v13.731 prime-power Hilbert model.
5. **ESTABLISHED NEGATIVE:** the canonical regular norm quotient is continuous \(L^2(\mathbb R)\), so it cannot itself supply the pure-point \((p,k)\) basis of v13.731.
6. **ESTABLISHED METHODOLOGICAL:** do not treat the centered Weil multiplier as an ordinary everywhere-defined function on the critical line; zero contributions and the archimedean origin term require distributional/boundary-value normalization.

## E. Coordination rule for subsequent threads

Before a new Suzuki/cone interface derivation:

1. check the live ledger and latest audit;
2. import every **ESTABLISHED [S]** result rather than rederiving it;
3. import every **ESTABLISHED [C]** result rather than rebuilding it in the Suzuki lane;
4. label only genuinely new algebra/analysis combining the two as **[X]**;
5. if a new result overlaps an existing row, update provenance/status rather than create a duplicate theorem;
6. keep finite-edge convergence, Hilbert–Pólya, and RH statements explicitly **OPEN** until independently proved.

## Next nonredundant gates

The clean remaining cross-lane targets are:

- formulate the centered Weil/Suzuki current as a single rigorously normalized tempered distribution, including the exact \(\delta_0\), Pf/PV, and archimedean terms;
- compute its Fourier boundary-value multiplier with conventions fixed and compare it to the \(E\)/\(T_{\rm pair}\) logarithmic split;
- leave the finite-\(A\) convergence problem to the Suzuki edge lane unless that lane requests a cone/adelic input.
