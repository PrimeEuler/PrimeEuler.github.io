# Cone Derivation Ledger v13.681 — Suzuki Source-Status Consolidation and Project-Model Boundary

Date: 2026-09-22

Status: authoritative project bookkeeping after External Audit Round 76 and direct repository archival of Suzuki's v2 PDF.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.680. No collision. v13.680 is directly relevant and is adopted here.

Authoritative source artifact now present:
\[
\texttt{research-notes/2606.09096v2.pdf}.
\]

## 1. Settled source facts

The uploaded PDF settles the previously unstable source questions.

### Corollary 1.6
Suzuki's equation (1.12) is
\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
\frac{\xi(1/2-iz)}
{\xi(1/2-iz)+\xi'(1/2-iz)}.
}
\]
Thus v13.280/v13.666 are correct on the target; v13.279/v13.660 are superseded on that point.

### Section 6.5
The finite characteristic convention is exactly
\[
\boxed{
W(a,\theta;z)
=
\overline{\mathcal W(v_{\bar z},w_\theta)}.
}
\]
Thus v13.675 §3 is source-confirmed.

### Section 7.8
Suzuki's raw de Branges boundary form and
\[
E(z)=\xi(1/2-iz)+\xi'(1/2-iz)
\]
are source-confirmed. His theta=pi calculation is explicitly presented as a HEURISTIC for (1.12).

## 2. Critical provenance boundary

The following are PROJECT-ORIGINAL constructions, not literal Suzuki theorems:
- the explicit infinite characteristic notation W_theta^infty;
- the identification of an infinite Weyl function m_infty by transporting the finite boundary-triple convention into Section 7.8;
- the finite Hermite-Biehler combination
\[
E_a^{proj}=W_\pi-c_\infty W_0;
\]
- the finite de Branges-space identification
\[
\mathcal H_{a,\rm simple}\cong\mathcal B(E_a^{proj});
\]
- the proposal to study a->infinity through m_a, Schur functions, and de Branges kernels.

These are mathematically motivated by and compatible with Suzuki's formulas, but their finite-to-infinite convergence is not proved by Suzuki's paper.

## 3. Results that remain exact independently of the heuristic

The following finite-a results survive without any infinite-source interpretation:
1. v13.661 exact boundary triple and normalized Krein determinant;
2. v13.667 exact unitary transport to the continuous-kernel model;
3. v13.676 finite HB theorem under canonical real/reflection normalization;
4. v13.677 exact kernel identity
\[
K_{E_a}(w,z)
=
\frac{c}{\pi}W_\pi(z)\overline{W_\pi(w)}
\frac{m_a(z)-\overline{m_a(w)}}{z-\bar w}.
\]

These are project theorems derived from the finite Suzuki setup.

## 4. Correct statement of the active research question

Do NOT say Suzuki proves
\[
E_a^{proj}\to E
\quad\text{or}\quad
m_a\to m_\infty.
\]

The source-faithful statement is:

Suzuki conjectures/heuristically motivates the Corollary-1.6 asymptotic. The project has constructed a finite-a boundary-triple/de-Branges model whose normalization-free ratio is designed to reproduce the same target IF an appropriate finite-to-infinite convergence theorem can be proved.

Thus the active theorem target is now a PROJECT theorem:
\[
\boxed{
\text{find sufficient conditions under which }
R_a^{proj}(z)
:=
\frac{W_\pi(a,z)}
{W_\pi(a,z)-c_\infty W_0(a,z)}
\longrightarrow
\frac{\Xi(z)}{\Xi(z)+\xi'(1/2-iz)}
}
\]
locally uniformly on the appropriate domain.

## 5. Standing citation rule

For Suzuki source claims, cite/read the archived PDF directly. Plain-text extraction is not sufficient for conjugation/sharp formulas; render the relevant PDF page when overbars/hats matter.

Historical contradictory ledger entries are retained for audit history but are not authoritative on source attribution where superseded by v13.680/v13.681.
