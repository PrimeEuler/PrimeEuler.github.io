# Cone Derivation Ledger v14.771 — Gravity anchored-wall count and radial translation covariance

Date: 2026-10-23. Lane: gravity only. Parents v13.770, v14.766–770. Prewrite master HEAD: 84606bdd13a773f5a859d7018d390d8340b99558. Research note: research-notes/Gravity_Anchored_Radial_Cutoff_Covariance.md, commit 84606bdd. All Suzuki/far-tail work reserved and untouched.

## Exact anchored-boundary theorem [D]

Let \(x=ha\), \(y=hb\) for positive integers \(a,b\). Let \(r=\log(xy)\), with one common wall \(r\le L\), and \(D(M)=\sum_{n\le M}d(n)\). Then
\[
N_h(L)=D(\lfloor h^{-2}e^L\rfloor).
\]
For \(h_{\rm EM}=1\), \(h_{\rm G}=1/2\),
\[
\boxed{N_{\rm G}(L)-N_{\rm EM}(L)
=D(\lfloor4e^L\rfloor)-D(\lfloor e^L\rfloor)}.
\]
Using \(D(\lfloor t\rfloor)=t\log t+(2\gamma-1)t+O(\sqrt t)\) at \(t=e^L\to\infty\),
\[
N_{\rm G}(L)-N_{\rm EM}(L)
=t\big[3\log t+4\log4+3(2\gamma-1)\big]+O(\sqrt t),
\quad\boxed{\lim_{L\to\infty}N_{\rm G}(L)/N_{\rm EM}(L)=4}.
\]
The asymptotic is a factor-pair density ratio, not a force or coupling ratio.

## Passive coordinate invariance versus independent walls [D]

A simultaneous change \(r'=r+s,\ L'=L+s\) leaves the comparison unchanged. But allowing the half-grid its own shifted reference wall yields
\[
\boxed{N_{1/2}(L-\log4)=N_1(L)}.
\]
Thus a common numerical coordinate L alone is insufficient: the two sectors must share an operationally anchored physical wall to distinguish their populations.

## Radial Mellin transform [D]

For \(\Re s>1\), the Laplace/Mellin transform of the ordered factor-pair radial measure is
\[
Z_h(s)=\sum_{n\ge1}d(n)e^{-s r_h(n)}=h^{-2s}\zeta(s)^2.
\]
Therefore \(\boxed{Z_{\rm G}(s)=4^sZ_{\rm EM}(s)}\). Centered cumulants (second and higher derivatives of \(\log Z_h\)) are identical; the first cumulant differs by the constant \(-\log4\). This is a coordinate-translation identity, not a dynamical thermal partition function or a Suzuki trace formula.

## Selector status [O]

The mathematical fixed-wall contrast is genuine under the stated common wall, but identifying such a detector, EM/G shell carriers, and a regulator-independent action remains open. v13.770 bars replacing Suzuki/Weil spectral current by divisor counts. The radial shift cannot be promoted into G or a coupling hierarchy without these inputs.

Next gate: test a concrete local boundary-response model and distinguish noncircular boundary calibration from an arbitrary wall parameter. Audit requested: reproduce the asymptotic and wall-shift cancellation; guard against a false physical ratio.

Flags: anchored-wall count EXACT; factor-four asymptotic EXACT; independent-wall cancellation EXACT; physical selector OPEN; Suzuki payload touched FALSE; far-tail touched FALSE.

HANDOFF
target: external-audit
type: scoped-gravity-verification
parent: v14.771
status: open
action: Independently verify the asymptotic difference, the exact independent-wall cancellation, and the Mellin translation; inspect no-coupling and arithmetic-carrier guardrails.
deliverable: audit verdict without modifications to Suzuki or far-tail payloads.
