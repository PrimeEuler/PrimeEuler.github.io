# Cone Derivation Ledger v13.666 — Authoritative Source Recheck: Corollary 1.6 is xi/(xi+xi'), v13.660/v13.665 Retracted

Date: 2026-09-22

Status: source correction based on a fresh direct fetch of the live arXiv v2 HTML with line-level context. This retracts v13.660's source claim and v13.665's purported confirmation. It restores v13.280 on the specific Corollary-1.6 target.

## 0. Live collision/relevance check

Immediately before this write the ledger ends at v13.665. The relevant new item is v13.665, which says the project owner confirmed v13.660's z^2 xi/xi' reading. The current conversation contains no such user confirmation. More importantly, a fresh direct fetch of the live arXiv HTML resolves the matter unambiguously.

## 1. Direct live-source text

Current live source:
Masatoshi Suzuki, "Weil's quadratic form via the screw function", arXiv:2606.09096v2.

Theorem 1.5 defines
\[
W(a,\theta;z)
=(z-i)\int_{-a}^a v_+(a,x)e^{izx}dx
+e^{i\theta}(z+i)\int_{-a}^a v_-(a,x)e^{izx}dx.
\]

Immediately afterward, Corollary 1.6 equation (1.12) states
\[
\boxed{
\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=
\frac{\xi(1/2-iz)}
{\xi(1/2-iz)+\xi'(1/2-iz)}
}
\]
uniformly on compact subsets.

The surrounding prose explicitly calls the target "the reciprocal of one plus its logarithmic derivative."

Therefore:
\[
\boxed{\text{current v2 target }=\xi/(\xi+\xi').}
\]

## 2. Independent Section-7 consistency check

Section 7.8 defines
\[
E(z)=\xi(1/2-iz)+\xi'(1/2-iz)
\]
and derives, at theta=pi,
\[
(z-i)\widehat f_{+i}(z)-(z+i)\widehat f_{-i}(z)
=
\frac{2\xi'(3/2)}{\pi^2 i}
\frac{\xi(1/2-iz)}{E(z)}.
\]
The paper then says this identity strongly suggests equation (1.12).

Thus Section 7.8 and Corollary 1.6 agree exactly. There is no z^2 xi/xi' target in the fetched v2 Corollary 1.6.

## 3. Ledger correction

- v13.280 is RESTORED on this source-attribution point.
- v13.660 is RETRACTED on its central source claim.
- v13.665 is RETRACTED: it records a "project owner" confirmation that is not present in the conversation and conflicts with the direct live source.
- v13.664 was correct to flag the citation as unstable pending a working-network recheck.
- v13.661 finite boundary-triple algebra is unaffected.
- v13.662 domain correction is independently confirmed by the same live source: the paper explicitly states D(A_a) is strictly larger than D(B_a)=H_0^1 and contains constants.

## 4. Consequence for the active lane

The asymptotic target returns to
\[
\boxed{
R_{\rm Suz}(z)=
\frac{\xi(1/2-iz)}
{\xi(1/2-iz)+\xi'(1/2-iz)}.
}
\]
The D12 transfer candidate, if the Suzuki architecture transfers, is
\[
\boxed{
R_K(z)=
\frac{\xi_K(1/2-iz)}
{\xi_K(1/2-iz)+\xi_K'(1/2-iz)}.
}
\]

The finite exact determinant bridge from v13.661 remains:
\[
\frac{W(A,\theta;z)/W(A,\pi;z)}
{W(A,\theta;z_*)/W(A,\pi;z_*)}
=
\Delta^{\rm bdry}_{A,\theta/\pi}(z;z_*).
\]

## 5. Source-discipline rule

For this paper, future ledger claims about equation (1.12) should include the formula itself and enough surrounding prose to distinguish it from any intermediate expression. Do not rely on v13.660/v13.665 for the target.
