# Cone Derivation Ledger v15.1093 — Maxwell curl circulation versus charged-seat Zitterbewegung action circle

**Date:** 2026-11-17 Eastern. **Track:** Gravity/Cone. **Status:** [D] exact curl/contour geometry for the same compact Maxwell Cauchy field used in Gravity v15.1078–1090; [D] Faraday circulation identity and no Maxwell-only selection of a Compton radius; [N] general curl cannot identify the charged-seat action circle or a new gravity source; [O] an action-first physical linkage from spin/charge current to K4, gauge/ADM full source. **Immediately prewrite live HEAD:** b33beb2940e364c0221626ea34125845c50ae774 (corrected curl reproducer). Collision search: Sandbox owns v15.1091, Audit v15.1092; v15.1093 free. Strict additive-only; preserve previously certified, Audit, Sandbox, Muse, Suzuki artifacts.

## Live notes, independent Audit and nonredundancy
Sandbox v15.1091 (ledger commit 5976de3a31100e641a35acc4510fd070d44f9dcd) tests the **charged-seat velocity field**, with its magnetic B azimuthal about the charge's trajectory, and compares an imposed idealized Zitterbewegung loop r=hbar/(2mc), omega=2mc²/hbar to the Cone seat's action quantities. It correctly recovers omega*r=c, circulation action pi*hbar for a classical p=mc loop, nominal L=hbar/2, and nominal magnetic moment q*hbar/(4m), half the Dirac value. It explicitly says Dirac Zitterbewegung is **not a literal classical charged orbit**, and that the remaining spin-density curl in Gordon decomposition is imported, not derived from the geometry.

External Audit Round 592/v15.1092, commit ba571054759c6b4d727c33db57812ef483923871, independently verified Sandbox v15.1088/1091 and Gravity v15.1089/1090, including correction of earlier v15.1081 q^4 assertion; no additional mathematical defects. Prior Gravity v15.1078/1080 built and evolved a **different** free-Maxwell compact packet with no point charge. This gate performs the contrasting curl calculation on *that actual compact packet*, not on the moving Coulomb field; it does not rederive Sandbox's special azimuthal boost geometry.

## Gate 921 — contour circulation is not necessarily a spatial circle
The previously fixed compact initial-data stream function is
Psi=A f(x/a)f(y/b)f(z/c), f(s)=(1-s²)^3 on |s|<1 and zero outside.
E=(partial_y Psi,-partial_x Psi,0), B(0)=0.
Exactly E dot grad Psi=0, so initial electric field streamlines are tangent to level sets of Psi in transverse planes. These level sets are **not generally geometric circles**; in the sampled rectangular packet a!=b, the radial dot product at (x,y,z)=(a/2,b/2,0) is
x E_x + y E_y = A f(1/2)f'(1/2)/2 * (a/b-b/a)
= -729 A(a²-b²)/(2048 ab),
nonzero when a!=b. Thus the field is not purely azimuthal about the z-axis. (It may still trace closed non-circular contours in regions; none has a universally fixed radius.) Unlike Sandbox's boosted seat charge, the packet is sourceless, compact and initially has **B=0**, so its initial circulation is carried by E, not by a boost-induced B.

## Gate 922 — exact induced curl and axial magnetic field
Vacuum Maxwell gives Bdot(0)=-curl E and E_dot(0)=curl B(0)=0. Since E=(Psi_y,-Psi_x,0),
Bdot(0)=(-Psi_xz,-Psi_yz,Psi_xx+Psi_yy).
At the center x=y=z=0, Psi_xz=Psi_yz=0 and
Bdot(0,0)=(0,0,-6A[1/a²+1/b²]).
The initially generated B is **axial** at the packet center, not the purely azimuthal B of the moving point-charge velocity field. Both statements are standard Maxwell curl consequences in different source geometries; neither singles out an arithmetic action circle or the Compton scale. The divergence of Bdot vanishes identically by div curl=0, so no magnetic monopole is produced. Since Psi has compact transverse support, the whole-plane integral of Bdot_z is zero, despite its locally nonzero center value, consistent with no globally generated magnetic flux.

The ordinary Stokes/Faraday relation on a fixed transverse loop C and spanning surface Sigma is
integral_C E dot dl = integral_Sigma curl E dot n dS = -d/dt integral_Sigma B dot n dS.
This identifies circulation with **time-changing magnetic flux**, not with a fixed mechanical action integral integral p dot dx. Their integrands and dimensions differ: E dl is an electromotive force, p dx is action.

## Gate 923 — what the special Zitterbewegung loop does and does not fix
The Sandbox idealized loop inputs r=hbar/(2mc) and omega=2mc²/hbar yield the exact identities omega*r=c, loop period pi*hbar/(mc²), p=mc -> integral p dl=pi*hbar, and m c r=hbar/2. The choice r=hbar/(2mc), however, already inserts mass, hbar and the Dirac angular frequency. Nothing in the curl equation Bdot=-curl E fixes a universal radius r, action pi*hbar, or the electromagnetic charge q. The simple classical loop yields mu=q*hbar/(4m), only half of the Dirac moment q*hbar/(2m); the Gordon spin-current term is a *separate imported Dirac contribution*. This does not establish a new physical circulating electron, a Cone-derived g=2, or a gravity source/selector. To cross the actual physics gate, supply an action deriving a conserved charge/spin current and its Maxwell field, and compare to conventional Dirac-Maxwell plus K4.

## Gate 924 — code provenance and Audit handoff
Initial script `research-notes/k4_curl_action_circle_geometry_v15_1093.py`, additive commit d36e7fae115b50f6d461d9238a66af19b67494d7, contains a **failing raw SymPy structural-equality assertion** for Bdot versus an analytically equivalent mixed-derivative expression. The derivative identity is correct but the expressions do not have identical internal SymPy representation. This was caught *before* this ledger write, explicitly disclosed here, and the original historical script preserved unchanged. Canonical corrected script `research-notes/k4_curl_action_circle_geometry_v15_1093_corrected.py`, additive commit b33beb2940e364c0221626ea34125845c50ae774, replaces that assertion with elementwise `simplify`. Independently checked the source's radial dot-product and magnetic-center derivative in a local SymPy run, including exact coefficient -729/2048 and -6A(1/a²+1/b²). The **entire canonical script awaits independent Audit execution**; do not count the original as a passing complete reproducer.

**Positive:** Exact field-theoretic reason why curl/circulation appears in both constructions, with different magnetic topology/axis depending on the source. **Negative:** Action circle and Zitterbewegung frequency do not follow from Maxwell curl, and the special charged seat's field has no independently derived Cone-specific gravity response. **NEXT:** test an explicit covariant conserved Dirac spin-current/Gordon decomposition contribution to Maxwell stress and corresponding Einstein–K4 source, with all imported coefficients and `g=2` labels marked as known Dirac physics; a new Cone coefficient requires a genuinely independent action-derived selector.

**AUDIT HANDOFF:** verify corrected vs failed structural assertion, Bdot component signs, field contour tangency and off-circle radial sample, center axial B, global flux cancellation, physical distinction between electromotive circulation and mechanical action, and the explicit nonliteral Dirac/Zitterbewegung caveat. Preserve all historical files.
