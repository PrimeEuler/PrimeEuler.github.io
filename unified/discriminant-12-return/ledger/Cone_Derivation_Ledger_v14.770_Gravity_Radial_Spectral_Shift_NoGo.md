# Cone Derivation Ledger v14.770 — Gravity radial spectral-shift no-go

Date: 2026-10-23. Lane: gravity. Parents: v13.301, v13.770, v14.760–762, v14.768–769. Live prewrite HEAD: 83e8e4089d78780634a2ff4a958fdb359e305a03. Research: research-notes/Gravity_Radial_Shift_Observable_NoGo.md at commit 83e8e408. External audit v14.769 verified the preceding derivations and identified missing LaTeX backslashes in v14.768. Its ledger and research-note formatting was corrected in commits 0af3195c and 4c7dcb7b.

## Shift theorem [D, conditional]

For common shell index \(n\), the Cone coordinate matching is
\[
r_{\rm EM}(n)=\log n,\qquad r_{\rm G}(n)=\log(n/4)=r_{\rm EM}(n)-\log4.
\]
On a shared finite Hilbert space define diagonal logarithmic matrices \(L_{\rm EM}\) and \(L_{\rm G}\) with those entries. Then \(L_{\rm G}=L_{\rm EM}-(\log4)I\).

Under the deliberately conditional hypothesis of one common self-adjoint interaction \(K\),
\[
H_{\rm EM}=L_{\rm EM}+K,\quad H_{\rm G}=L_{\rm G}+K
\quad\Longrightarrow\quad
H_{\rm G}=H_{\rm EM}-(\log4)I.
\]
Every spectral gap is unchanged. Transition matrix elements for a fixed observable in the shared eigenbasis are unchanged. Such shift-invariant quantities cannot produce a coupling hierarchy merely from the radial origin.

## Absolute reference and its limitation [D]

For finite dimension \(N\), \(\operatorname{tr}H_{\rm G}=\operatorname{tr}H_{\rm EM}-N\log4\). For finite \(t\),
\[
\operatorname{tr}e^{-tH_{\rm G}}=4^t\operatorname{tr}e^{-tH_{\rm EM}}.
\]
Normalized Gibbs probabilities are identical; the prefactor cancels. A physical absolute-energy reference or independently imposed boundary is needed to interpret the unnormalized factor. The physical equality of K, domains and index bases has NOT been demonstrated.

The older action-selector obstruction remains controlling: a shift does not determine the independent variational coefficients in v14.760–761 or Newton's constant. The v13.770 divisor-versus-Suzuki carrier distinction remains enforced.

## Next gate [O]

Test a common radial boundary and prove exactly when an EM/G difference is invariant under a change of coordinate origin. Distinguish passive relabeling from an independently anchored physical detector. Derive no physical coupling by inserting one as a coefficient.

Flags: conditional spectral-gap no-go exact; physical radial-boundary selector open; gravity coupling not derived; Suzuki production and far-tail files untouched.

HANDOFF: target external-audit; parent v14.770; status open; action independently verify the conditional shift and its physical limitations, and confirm corrected v14.768 math displays; constraint no Suzuki far-tail or certified code changes.
