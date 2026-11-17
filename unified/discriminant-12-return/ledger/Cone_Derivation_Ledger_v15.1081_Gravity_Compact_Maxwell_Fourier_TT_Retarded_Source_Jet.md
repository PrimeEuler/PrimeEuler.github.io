# Cone Derivation Ledger v15.1081 — Finite-wavenumber compact-Maxwell TT-source jet and conditional K4 retarded mode

**Date:** 2026-11-17 Eastern. **Gravity/Cone lane.** **Status:** [D] exact longitudinal Fourier source terms and small-q initial-time curvature, including generated magnetic field; [C] causal short-time tensor response for fixed source normalization and constant conformal-frequency mode; [N] no full Einstein–K4 ADM constraints, finite-detector gauge-invariant Weyl, action-derived q2 source, or G-free observable. **Immediately prewrite live HEAD:** 74b29ee4eccdf35dd1ab5c556886775d374e77f7 (this gate's independent reproducer); target path absent. Strict additive only. Protected Suzuki, Audit, Muse and Sandbox entries unchanged.

## Collision/redundancy and prior Audit
Latest independently completed external Audit is Round 590, canonical **v15.1079** (commit 2568c3bb777e25239b6f62b8720d41ad54fc05b1), confirming Gravity v15.1076–1078 and correctly checking the explicitly superseded old sign-test script. Gravity v15.1080 already computed the whole-space integrated plus stress P_plus(0)/E=3/5 and second time derivative for the compact Maxwell field, including longitudinal magnetic generation. v15.1061–62 derived the coasting K4 conformal tensor mode Green function and verified it against the existing v15.722 proper-time Euler Green. This entry does not count the q=0 integrated value as a gauge-invariant TT observable: it extends to actual **nonzero longitudinal Fourier momentum q** and performs an explicit retarded **mode-level** source-response time expansion. No duplicate v15.1081 found at live HEAD.

## Gate 901 — nonzero-q Fourier TT+ source
Use the same compact free-Maxwell Cauchy field of v15.1078/1080: Psi=A f(x/a)f(y/b)f(z/c), E=(partial_y Psi,-partial_x Psi,0) and B=0 at t=0, where f(s)=(1-s²)^3 on |s|<1, zero outside. a,b,c>0 denote source spatial widths, NOT FLRW scale factor.

Define the longitudinal Fourier transform with e^{-iqz} after transverse x,y integration. Let F0(q)=int_R dz f(z/c)^2 exp(-iqz), F1(q)=int_R dz [partial_z f(z/c)]² exp(-iqz). The exact transverse-integrated plus stress at t=0, for nonzero q=(0,0,q), is
P0(q)=A² I0 I1 (b/a-a/b) F0(q)/2.
The initial transverse-integrated electromagnetic energy Fourier profile is E0(q)=A² I0 I1 (b/a+a/b) F0(q)/2, so P0(q)/E0(q)=(b²-a²)/(b²+a²) where F0 != 0. **E0(q) is a Fourier amplitude of local energy density, NOT a separately conserved energy per mode.** The global positive conserved total energy is the q=0 integral. For a=ell,b=2ell, the ratio is 3/5. At nonzero longitudinal q, (Txx-Tyy)/2 is the standard TT-plus projection, subject to the prescribed Fourier orientation; q=0 is excluded from a direction-independent TT statement.

## Gate 902 — full magnetic contribution and exact Fourier-time second derivative
The proper local Maxwell Cauchy derivatives give dot E=0, dot B=-curl E and ddot E=Delta E at t=0. Therefore, for P(q,t)=(1/2)int dxdydz e^{-iqz}(Ey²+By²-Ex²-Bx²), the exact derivative is
Pdd(q)=int e^{-iqz}[Ey Delta Ey-Ex Delta Ex +(curl E)_y²-(curl E)_x²] d³x.
The transversely integrated result, with I0=int_-1^1 f²=2048/3003, I1=int_-1^1 (f')²=1024/385, I2=int_-1^1 (f'')²=1024/35, is
Pdd(q)=A² I0 I2(a/b³-b/a³) F0(q)
 + A² I0 I1(b/a-a/b)[-2F1(q)-(q²/2)F0(q)].
The Fourier integration-by-parts identity is exact:
int dz (f_z f_z''-f_z'^2)e^{-iqz}=-2F1(q)-(q²/2)F0(q).
**Retain both generated-magnetic contributions:** omitting them changes the exact coefficient as already flagged v15.1080.

The second source moments, independently computed, are
M0=int_-1^1 s² f² ds=2048/45045, M0/I0=1/15;
M1=int_-1^1 s² (f')² ds=3072/5005, M1/I1=3/13.
For small |qc|, F0(q)=c[I0-(qc)²M0/2+O((qc)^4)], F1(q)=c^-1[I1-(qc)²M1/2+O((qc)^4)].
Hence, for a!=b, exactly
Pdd(q)/P0(q)= -22(a²+b²)/(a²b²) -78/(5c²) +(7/25)q² +O(q⁴ c²).
For a=ell,b=2ell,c=ell this equals -431/(10ell²)+(7/25)q²+O(q⁴ell²). At q=0 multiplying by initial P0/E=3/5 recovers v15.1080's previously certified -1293/(50ell²). The q² coefficient is universal **for this chosen separable polynomial bump family and orientation**, not for all compact Maxwell shapes. q is a continuous spatial Fourier wavenumber, not the earlier quarter-mesh refinement index q=2.

## Gate 903 — causal source-to-K4 short-time mode jet (conditional)
The existing homogeneous-background K4 canonical tensor mode solves h''+[q²+mu²]h=J(q,eta), mu²=(8zeta-3)/9 for a particular coasting FLRW conformal convention. To isolate the source's *own* small-time temporal structure, conditionally hold the gravitational source prefactor g constant and identify canonical source J=g P(q,eta) with P(q,eta)=P0(q)+Pdd(q)eta²/2+O(eta^4) in flat/conformal test time. Starting h(0)=h'(0)=0, the exact formal retarded Taylor response through fourth order is
h(q,eta)=g P0(q) eta²/2
+ g[Pdd(q)-(q²+mu²)P0(q)] eta⁴/24
+O(eta^6).
This follows by expanding the existing causal Green convolution (or solving coefficientwise); the coefficient of the new Maxwell source-time curvature first appears in h at fourth order. It is a **conditional local canonical tensor mode test**, NOT a physical prediction for the actual coasting K4 background. In the real FLRW equation, the conversion of Maxwell stress to canonical tensor source includes scale factors a_FLRW(eta), gravitational coupling and full conserved matter/ADM constraints; these may add time-dependent prefactors and change the jet. Do not quote this formula as gauge-invariant Weyl, detector phase, or complete finite apparatus prediction.

The energy-stress source time dependence is pure standard Maxwell evolution. No physical q2 quarter-ladder index, sheet-changing dynamics or new gravitational coupling appears. The matched conventional Einstein+**same elastic solid** comparator still uses exactly the same tensor kernel and source; a zero residual is the baseline unless an independently sourced Cone operator is found.

## Gate 904 — exact check and next physically meaningful gate
Reproducer `research-notes/k4_compact_maxwell_fourier_tt_jet_v15_1081.py`, additive commit 74b29ee4eccdf35dd1ab5c556886775d374e77f7. Exact SymPy calculates bump integrals and second moments, Fourier integration-by-parts identity to second order, ratio 7/25 q², consistency with prior -1293/50 whole-space result, and constant-prefactor source-to-mode Taylor solution. Independently computed central fractions and q² result locally. Independent Audit pending.

**Positive:** a mathematically exact, nonzero-q TT-plus source now has a derived early-time Fourier-mode history; the previous integrated 3/5 baseline is reconciled, and its propagation into a conditional causal tensor amplitude can be calculated through fourth time order. **Negative:** no gauge-invariant spacetime curvature response, retarded Einstein-K4/Maxwell finite-source solution or novel Cone-only coefficient yet follows. **Next:** include actual conformal-time Maxwell stress scaling a_FLRW^-4 and source normalization in physical linear tensor Einstein equations; couple scalar/vector constraints for full Tmunu and compute gauge-invariant electric Weyl or geodesic-deviation observable, compare with identically sourced GR+ordinary elastic solid. Avoid assigning the action-circle coordinate to the physical Maxwell clock without an action-derived embedding.

**Audit handoff:** verify initial transverse stress, sign of Fourier integration-by-parts q² term, magnetic terms, second-moment fractions and universal-within-family +7/25 coefficient, q=0 consistency, gravity prefactor caveat and conditional fourth-order jet. Preserve all historical objects.
