# Cone Derivation Ledger v15.934 — Natural Casimir spacing hierarchy and the sqrt(n) rest/EM Casimir/n+1 transition circles

**Date:** 2026-11-13 Eastern. **Gravity lane.** **Parents:** v13.364 scaled centered quadratic; v15.602 (general q mesh), v15.604 (original unit-step refinement naturality), v15.625 (formal all-mesh spectral classes and co-scaled contrast), v15.630 (physical SU2 obstruction); v15.899/v15.904/v15.905 (two circles and n+1 cycles); Gravity v15.921–924 AM–GM parabola intersections, v15.932–933 quarter/interferometer comparison. **Immediately prewrite live HEAD:** 882b669fa05928ab8b5bd03aff2cd55a8b7b92cd; ledger target confirmed absent. Additive only, no edits to historical work/Audit/Sandbox/frozen Suzuki.

**Owner's next question:** organize regularly spaced acceleration/deceleration parabola-pair Casimirs under a natural map between spacings; and compare the Casimir action circle to the (n+1) transition circle and the decelerated rest sqrt(n) circle, keeping the exact original `n` convention.

**Status:** [D] exact three-circle identities, crossing conditions and spacing covariance; [D/recall] known co-scaled SU2 operator family and independently audited fixed-step mesh-inclusion naturality; [N] no nontrivial unitary equivalence across changing dimensions at fixed geometric j and no distinguished quarter selector; [O] physical rest-state interpretation, absolute action/frequency, true gravity-sector Casimir or G-free measurable dynamics.

## Gate 685 — original index map, without relabeling n

In v15.905/Paper C, pair (x,y)=(n,1), n≥1, corresponds to Fock (n1,n2)=(n−1,1), total N=n, spin j=n/2 and precisely n+1 basis states. Its geometric normalized transition-circle radius **R_o=(n+1)/2**, specific chord height **R_i=sqrt(n)** and Schwinger Casimir radius **R_C=sqrt[j(j+1)]=sqrt[n(n+2)]/2**. The first two are the pre-existing outer transition action circle and the user's inner “decelerated rest” proposed circle; the third is the EM SU2 Casimir radius. The inner chord is not by itself an operator Casimir, and “rest state” remains a geometric/conditional dynamical interpretation.

The **squared** radial comparisons are exact:

**R_o²−R_C²=1/4** (standard EM completion),
**R_o²−R_i²=(n−1)²/4** (factor AM–GM variance),
**R_C²−R_i²=n(n−2)/4**.

Thus the two rest/transition circles coincide at n=1; the Casimir sits strictly *inside* their common radius. At **n=2**, Casimir and rest radii coincide at sqrt(2), while transition radius is 3/2. At all integer n≥3 the strict radial ordering is rest < Casimir < transition. The +1/4 is an invariant **squared radial gap**, not a universal radial-distance gap; R_o−R_C tends to 0 as n→∞. No identified resonant frequency, stability threshold or force law follows merely from n=2 crossing.

## Gate 686 — natural co-scaled spacing family

For an arbitrary positive row spacing h, mirrored acceleration/deceleration factor parabolas are **Y²=h²±2hX**, with vertices at X=∓h/2; their centered quadratic completion is **C_h(j)=j(j+h)=(j+h/2)²−h²/4**, already in v13.364/v15.625. Define co-scaled raising operators on a standard N+1 dimensional Schwinger irrep by **M_h=hM_1**, **J_{±,h}=hJ_{±,1}**. These obey

**[M_h,J_{+,h}]=h J_{+,h}**, **[J_{+,h},J_{−,h}]=2hM_h**, **C_h = M_h²+(J_{+,h}J_{−,h}+J_{−,h}J_{+,h})/2 = h² N(N+2)/4 · I**.

Under rescaling h→h/k for any k>0, all three operators scale by 1/k, their normalized ratios and commutator form (with step h/k) are preserved, and their Casimir eigenvalues scale by 1/k². This is a natural **similitude** of the same underlying dimensionless SU2 representation at fixed occupation N, not equality of the raw Casimir matrices, not an independent gravitational Casimir derivation, and not a new physical force.

At pair (x,y)=(nh,h), the three **co-scaled** radii are **R_i=h sqrt(n)**, **R_C=h sqrt[n(n+2)]/2**, **R_o=h(n+1)/2**, with the three squared gaps all multiplied by h². Therefore the rest/Casimir crossing n=2 is common to all co-scaled h, and does **not** distinguish EM's half-unit vertex from a gravitational quarter-unit vertex. The dimensionless ratio R_o/R_i=(n+1)/(2sqrt n) is spacing-invariant.

## Gate 687 — distinguish the fixed-original-step q grid and its distinct Casimir spectra

The already-audited naturality theorem v15.604 is a *different* transformation: refine q→kq at **fixed j** with an isometric inclusion of old nodes |i>→|ki>, while preserving the original **unit** step-one J± and M on the included subspace. The extra refined-grid nodes form additional residue chains; their original-unit-step ladder is generally defective at open boundaries. This map does NOT co-scale the physical ladder and does not change the old sqrt(n) chord of the original (n,1) integer pair.

For shell label j=L/(2q), the formal **original-unit-step** geometric Casimir is **C_formal=L(L+2q)/(4q²)**, with EM q=1 residue classes mod 1 {0,3/4} and odd-quarter q=2 residues {5/16,13/16}—disjoint. The **co-scaled step-h** quadratic construction h=1/q on the same j is **C_h=L(L+2)/(4q²)**. Their exact difference is **C_formal−C_h=L(q−1)/(2q²)**; q=2 gives **L/8**, not a universal 1/4, and not a new gravity Casimir. An appropriately rescaled **genuine SU2** Casimir on the nearest-neighbor refined ladder is L(L+2)/4 in units where its normalized step is one, again a different algebraic object.

Holding geometric j fixed while changing h changes the number of states N=2j/h; representations of different dimension are not unitarily equivalent, even though their local polynomial formula can be related. The fixed-occupation co-scaled similitude above does not make the fixed-j mesh-inclusion and closed refined-step algebras identical. This is the exact distinction protecting v15.624–625's gravity/EM Casimir separation and v15.630's odd-quarter SU2 obstruction.

## Gate 688 — interpretation of acceleration/deceleration and action/frequency

The original AM–GM factor parabola family and mirror encode offset + product weights and geometric circles. Interpreting R_i=sqrt n as a physically decelerated **resting orbit** requires an independently specified Hamiltonian, inertial parameter, coupling and clock. v15.904–905 found that the chosen two-boson H0=hbar omega*(N+1) produces n+1 global phase cycles per base period, but that is not a physical inner orbit speed or an emitted n+1 omega* transition. The exact n=2 rest/Casimir crossing is a mathematical candidate marker; ordinary n=2 hydrogen shell (and every h-rescaled copy) also has it, so the crossing alone cannot distinguish gravity.

**Reproducer:** `research-notes/k4_casimir_refinement_sqrt_n_action_circles_v15_934.py`, additive commit **882b669fa05928ab8b5bd03aff2cd55a8b7b92cd**. Local SymPy exact test: full co-scaled J/M/C matrices for N=1..14 and q=1..6 (84 representations), 400 exact three-radius comparisons n=1..50/q=1..8, general spacing and fixed-j Casimir differences, EM and odd-quarter residue classes. Independent Audit pending.

**Next discriminating gate:** Compare a physically specified EM two-SU2 bicone action/casimir spectrum with a **separately defined** gravitational quarter-sector generator (not merely a rescaled EM J). Require a cross-sector observable that survives ordinary-unit-step refinement, co-scaled similarity and standard EM/Rabi/Stark comparisons. Alternatively test whether the n=2 crossing produces a genuine stationary point of a specified rest-to-transition action functional rather than a coordinate radius coincidence; until the action functional exists do not call it a resonance.

**HANDOFF Audit/Muse:** Verify all three squared gaps, n=1 and n=2 coincidences, natural co-scaled SU2 commutators, matrix Casimir and unit-step q-grid distinction, and the separation between formal quarter-spectrum vs a genuine gravitational Casimir.
