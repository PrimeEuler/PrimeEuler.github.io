# Cone Derivation Ledger v15.1404 — Null-affine three-sheet 3:1 ratio and a precise ln2 boost bridge at the historical Dirac depth

**Date:** 2026-11-24 Eastern. **Lane:** Gravity/Cone. **Status:** [EXACT POSITIVE, representation geometry] for any fixed positive null factor U and transverse coordinate Y, the intersections of one affine ambient null line with Q_null=0, Q_q2=1/16, Q_EM=1/4 have exact consecutive null-affine separation ratio **3:1**; this ratio is preserved by every linear ambient Lorentz transformation acting on the entire line/triple, independent of finite rapidity/volume regulator; [EXACT POSITIVE] for Y=0, matching the q2 and EM hyperboloids at identical U requires boost rapidity difference **ln2**, not equal rapidity; [NEGATIVE] the particular null congruence, its affine normalization and physical current/transition law remain unselected, so the 3:1 is not an action-derived coupling; the Dirac rapidity 45.310004305 still uses observed G as input. Parent v15.1401 (3:1 fixed-T area and 7:1 proper-radius volume), v15.1402 (2:1 Hilbert count), v15.1403 (historical Dirac rapidity retrieval). **Pre-ledger verified live HEAD:** 329c6075cccde394774b1bf0b9c23c8d73969513. Strictly additive.

## Gate 1332 — three hyperboloids on the *same null affine line*

In 2+1 ambient representation-space Minkowski metric diag(1,−1,−1), define null factors `U=T+X,V=T−X` and `Q=UV−Y²`. Use one affine line `U=U0>0,Y=Y0`, varying V. It is actually **null** as an ambient curve: writing `P(V)=((U0+V)/2,(U0−V)/2,Y0)`, the tangent `dP/dV=(1/2,−1/2,0)` has vanishing Minkowski norm.

The intersection with a prescribed level Q=μ occurs at `V_μ=(Y0²+μ)/U0`. For the correct nested levels `μ_null=0, μ_q2=1/16, μ_EM=1/4`, the differences are

`ΔV_(q2-null)=1/(16 U0)`,
`ΔV_(EM-q2)=3/(16 U0)`,
`ΔV_(EM-null)=1/(4 U0)`.

Thus **ΔV_EM-q2 / ΔV_q2-null=3** for every U0>0, every Y0, with NO rapidity or volume cutoff. The three corresponding spacetime-displacement vectors satisfy `P_EM−P_q2=3(P_q2−P_null)` and each is null. Under ANY **linear ambient Lorentz transformation** Λ∈SO+(2,1), this vector equality remains `Λ(P_EM−P_q2)=3Λ(P_q2−P_null)`, so the affine-separation *ratio* survives. This is a Lorentz-covariant relation of three **already paired collinear points**, not a unique Lorentz-invariant scalar distance between two separate arbitrary sheets, and its construction chooses a null line U0,Y0. A Lorentz transform of the complete triple will generally NOT leave the coordinates U=U0,Y=Y0 unchanged; the invariant object is the ordered triple and its affine ratio. Absolute null separation has no timelike invariant length and is subject to affine rescaling.

At Y0≠0 the null surface intersection has V_null=Y0²/U0 rather than V=0; this does not change the differences. For Y0=0 the three V values are 0,b²/U0,a²/U0, with b²=1/16 and a²=1/4.

## Gate 1333 — match the historical 45.310 rapidity across sheets at common U

The historical observed Dirac force ratio D=2.26866143917643529×10^39 (v14.621) defines `ψ_D=½lnD=45.31000430498158484287108433`. At Y=0, a positive-radius timelike hyperboloid has `U=r e^η,V=r e^(−η)`. Fix the q2 radius `r_q2=1/4` and q2 rapidity η_q2=ψ_D. Then `U0=(1/4)e^ψ_D≈1.19076168878800936×10^19`. On the **same null line** the EM radius r_EM=1/2 must have

`η_EM=ln(U0/r_EM)=ψ_D−ln2≈44.61685712442163953`.

This exact `ln2` shift is a consequence of the 2:1 radius ratio, not a special property of the enormous Dirac hierarchy; it holds for arbitrary η_q2. With this chosen U0, the three V factors are

`V_null=0`,
`V_q2≈5.248741254315484×10^(−21)`,
`V_EM≈2.099496501726194×10^(−20)`,

so the EM-to-q2 affine spacing is ≈1.574622376294645×10^(−20), exactly three times the q2-to-null spacing. These values are dimensionless and depend on the observed input ψ_D and the chosen q2 reference rest point. In double-precision arithmetic T≈X with a difference ≈10^(−20), so calculations should retain factor coordinates and high precision to avoid catastrophic cancellation. At *equal rapidity* the two timelike sheets have different U factors and are not on this same affine null line; matching the forward factor U explicitly is essential.

**New exact reproduced script:** `research-notes/k4_null_affine_em_quarter_boost_v15_1404.py`, SHA **c4b9a9fec431683be89b0bea0a391920213dd1e4**, re-derives all points Q=μ, affine-null tangent, exact 3:1 vector relation, and invariance after a composition of nonparallel X and Y ambient Lorentz boosts; evaluates Dirac rapidity and ln2 shift to 65-digit mpmath precision. Locally executed equivalent file `/mnt/data/cone_gate/k4_null_affine_em_quarter_boost_v15_1404.py` PASS. Exact GitHub-byte independent replay pending.

## Gate 1334 — physical selector and measure limitations

This null-affine ratio is **more robust than the flat-area 3:1 volume in v15.1401** in one carefully defined sense: it requires no finite volume cutoff and is covariant for a given ordered null-collinear triple. It is still not an action-derived quantum or optical flux: we have chosen an auxiliary representation-space null line, pairing of three surface intersections and affine congruence. The measure on the line, relative sector occupations, photon transition amplitude and physical coupling are unselected. A constant density integrated along V would trivially give 3:1 weights, but **that density would be stipulated**, not derived from the frozen EH+Maxwell+K4 or sigma model. This does not contradict v15.1401's 7:1 regulated volume or v15.1402's 2:1 state count, because they use different geometric/quantum measures.

Even though `ln2` is an exact matched-forward-factor boost shift, the project cannot claim a physical EM→G process with that rapidity or a physical acceleration without a bona fide representation-to-spacetime energy/momentum map. Each finite quarter shell does not possess a nontrivial unitary continuous SO+(2,1) boost action (v15.1393), and the continuous H² sigma-EFT coupling is still free under the quarter radius reparameterization (v15.1387/v15.1398). The 45.31 number was computed from an empirical ratio **already containing G** and so is NOT a G-free prediction.

**AUDIT PRIORITY:** replay v15.1403/1404 exact committed scripts, check 65-digit Dirac input precision and Q levels, 3:1 ratio at fixed U,Y, full Lorentz-covariance-of-triple argument, null-affine distance versus scalar Lorentz length, and difference between same-U and same-rapidity sheets. Check whether any canonical symplectic flux or conserved current actually *forces* a uniform density along this null line; do not convert a geometrically paired ratio into a measured electromagnetic or gravitational coupling.

**NEXT:** derive a physical canonical measure from the existing EM/q2 Hilbert carriers or the EH/Maxwell/H² field action that **selects a null congruence and density**; use it to weight the three Q levels, then check a true amplitude/transition operator against v15.1397's low-rank selection and the matched same-action EFT null. If nothing selects the current, preserve the elegant 3:1 affine and ln2 geometrical correspondence as an exact—but not predictive—result.
