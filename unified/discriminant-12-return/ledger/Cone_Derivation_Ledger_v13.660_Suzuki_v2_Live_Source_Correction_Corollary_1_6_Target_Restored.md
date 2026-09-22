# Cone Derivation Ledger v13.660 — Suzuki v2 Live-Source Correction: Corollary 1.6 Target Restored to z^2 xi/xi'

Date: 2026-09-22

Status: authoritative live-source correction. This supersedes the source-attribution portions of v13.274/v13.278/v13.280 that state the current v2 target is xi/(xi+xi'). The live arXiv v2 HTML, fetched 2026-09-22, states z^2 xi/xi'.

## 0. Live collision/relevance check

Immediately before this write the live ledger ends at v13.659. v13.659 is the cone-complexification audit and does not collide. The relevant discovery is external: the current arXiv v2 source itself contradicts the project's v13.280 source attribution.

## 1. Authoritative source state

Masatoshi Suzuki, arXiv:2606.09096v2, revised 17 Aug 2026, current HTML:
- Theorem 1.5 defines W(a,theta;z) by the two deficiency-vector Fourier transforms.
- Corollary 1.6 equation (1.12) states
\[
\boxed{\lim_{a\to\infty}e^{\phi(a,z)}W(a,\theta;z)
=z^2\frac{\xi(1/2-iz)}{\xi'(1/2-iz)}}
\]
uniformly on compact subsets, as a sufficient condition for RH.
- Section 8.3 says numerical experiments support (1.12) for theta=pi.

Therefore the current source target is NOT xi/(xi+xi').

## 2. Why the project became inconsistent

v13.279 had stated z^2 xi/xi' but was later superseded by v13.280, which claimed a line-by-line source audit showed xi/(xi+xi'). The live source now confirms the v13.279 target and contradicts that specific v13.280 attribution.

The de Branges Section 7 formulas involving
\[
E(z)=\xi(1/2-iz)+\xi'(1/2-iz)
\]
are genuinely present in v2. In particular Section 7.8 derives
\[
(z-i)\widehat f_{+i}(z)-(z+i)\widehat f_{-i}(z)
=
\frac{2\xi'(3/2)}{\pi^2 i}\frac{\xi(1/2-iz)}{E(z)}.
\]
But that heuristic intermediate ratio is NOT equation (1.12). The paper itself then says this identity strongly suggests (1.12). Thus the project incorrectly promoted the Section-7 intermediate ratio into the statement of Corollary 1.6.

## 3. Consequences

Restored Suzuki target:
\[
\boxed{R_{\rm Suz}(z)=z^2\xi(1/2-iz)/\xi'(1/2-iz).}
\]

For D12 the source-faithful transfer target is therefore
\[
\boxed{R_K(z)=z^2\xi_K(1/2-iz)/\xi_K'(1/2-iz),}
\]
as a PROJECT transfer, not a Suzuki theorem.

The target is odd in centered z because Xi_K(z)=xi_K(1/2-iz) is even and xi_K'(1/2-iz)=i Xi_K'(z) is odd up to the fixed i factor. This restores the relevance of the phase-covariant parity analysis in v13.279.

The Section-7 ratio Xi/E remains mathematically meaningful as an intermediate de Branges boundary expression but must not be called the current Corollary-1.6 target.

## 4. Effect on the current Krein lane

The finite Theorem-1.5 boundary characteristic and Section-6 deficiency algebra used in v13.647/v13.654 remain valid. The source correction changes the proposed infinite target, not the finite boundary form.

The next gate is therefore:
1. derive the finite boundary triple directly from Suzuki Section 6, fixing all phase signs from his actual convention;
2. identify W exactly with the scalar boundary characteristic up to an explicit nonzero factor;
3. only afterward revisit the A->infinity renormalization against the restored z^2 xi/xi' target.

## 5. Guardrail

No RH/GRH claim is made. This is a source-state correction. Any ledger entry relying specifically on xi/(xi+xi') as Suzuki's Corollary-1.6 target must be read as superseded on that point.
