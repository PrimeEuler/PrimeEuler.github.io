# Magnetic-driver correction to divisor j weights: transverse inertia and half-step transition

Date 2026-10-25. Parents v13.364, v13.595, v14.366–367, v14.858; research-notes/Jx_Jy_V4_Quarter_Shift_Findings.md. Gravity/arithmetic lane. Additive only.

The divisor-contact labeling v14.858 uses n1=a-1,n2=b-1, j=(a+b-2)/2,m=(a-b)/2. It is an explicitly chosen occupation convention, not evidence of physical independent modes.

The relevant established magnetic-drive Hamiltonian, from v13.595, is H_perp(t)=-(γB1/2)(e^{-iωt}J_+ +e^{iωt}J_-), with the quantization axis Z corresponding to Cone X. The magnetic dynamics is ONE connected 2j+1 multiplet; individual m->m+1 edge blocks are not independent driven systems when multiple edges are resonant. Define T_c=j+1/2, X_m=m+1/2. Then the EXACT half-step transition matrix element obeys
\[
|\langle j,m+1|J_+|j,m\rangle|²=(j-m)(j+m+1)=T_c²-X_m².
\]
The exact SU(2) Casimir completion is j(j+1)=T_c²-1/4. The expectation of the transverse quadratic moment in |j,m> is
\[
\langle J_x²+J_y²\rangle=j(j+1)-m²=(j+1/2)²-1/4-m².
\]
This is not equivalent to the ONE-EDGE weight T_c²-(m+1/2)²: the former averages the two up/down transition squares with appropriate normalization. In ħ-full units every J² term carries ħ². A perpendicular transverse component is not automatically a physical energy; Zeeman response uses H, spectral gaps, state preparation and occupation.

Define an arithmetic **candidate** transverse moment
\[
W_\perp(N)=\sum_{ab\le N}[j(a,b)(j(a,b)+1)-m(a,b)^2].
\]
Using the occupation convention, the summand simplifies EXACTLY:
\[
j(j+1)-m²=(a-1)(b-1)+(a+b-2)/2
=ab-(a+b)/2.
\]
Thus for N=12 the six ordered contacts weigh [11/2, 19/2, 21/2,21/2,19/2,11/2], total 51, contrasting with W2 shell weight 113. Check: (1,12) j=11/2,m=-11/2 gives j=11/2 transverse; (2,6) j=3,m=-2 gives 8; correction: exact pair values should be recalculated rather than using unverified illustrative list. The symbolic identity ab-(a+b)/2 is definitive, and at N=12 gives (1,12):11/2, (2,6):8, (3,4):17/2, (4,3):17/2,(6,2):8,(12,1):11/2, shell sum 44. This note records the corrected values explicitly; prior draft values are not authoritative. [CORRECTION: total 44].

The correct unit-circle / half-step mapping, contact occupancy, and magnetic-drive operator are distinct requirements. A pair contact may label an m state within a multiplet; D(N) counts ordered pairs, not independent j multiplets or separate frequencies. The quarter Casimir is a universal centering term, not proof the physical u=1/2 gravity interlay is selected: u=1/2 is a factor-coordinate rescaling whereas δ²/4 in v13.364 comes from a specific normalized cell spacing and operator centering.

OPEN: derive weighted contact sums and their asymptotics and determine actual driven spectral/ground-state response through full Jx Hamiltonian or Kubo susceptibility, with explicit physical state preparation and a seat-displacement coupling; do not equate transverse J² expectation with measured stiffness or Newton G. This corrects focus of v14.858 without deleting its exact mathematical W2.
