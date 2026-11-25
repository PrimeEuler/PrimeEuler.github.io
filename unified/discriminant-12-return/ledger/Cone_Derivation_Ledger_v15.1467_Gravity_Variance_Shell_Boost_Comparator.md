# Cone Derivation Ledger v15.1467 — Sandbox variance-shell synthesis versus genuine Lorentz-invariant mass-shell geometry

**Date:** 2026-11-25 Eastern. **Track:** Gravity/Cone (constructive comparator to Sandbox). **Parent:** Sandbox v15.1465 variance shells, commit **9f5430fa6cb95a360395f9e5313d2471572407a7**, including seven independently staged exact arithmetic checks; earlier gravity v15.1403–1407 nested observability hyperboloids and conditional ln2 H² holonomy. **Status:** [EXACT POSITIVE] two-point AM/GM gap is the pair population variance, and EM (2,1) and q2 (1,1/2) selected lattice pairs give respectively 1/4 and 1/16; [EXACT NEGATIVE] this statistical variance is **not invariant under Lorentz boosts** and is therefore not by itself the invariant quadratic form defining a physical massive shell or a universal Lorentz-independent Q=1/16 observability hyperboloid; [OPEN] physically distinguished pair/frame and proper mapping from the dimensionless sector variance onto invariant representation Q, graviton's actual null helicity-2 sector, and action-selected gravitational coupling. Pure representation-level variance-shell reading remains useful if it explicitly carries its choice of pair and frame. No prior Sandbox interpretation deleted or altered.

## Gate 1392 — exact AM–GM variance and the two shell candidates

Define `T=(n+k)/2`, `X=(n−k)/2` for positive real pair `(n,k)`. Its elementary *population variance* (equal weight) is

`V_pair=((n−k)/2)²=X²=T²−nk=AM²−GM²`.

Thus the chosen pair (2,1) yields `V_pair=1/4` and the chosen pair (1,1/2) yields `V_pair=1/16`, just as Sandbox independently established. These are exact arithmetic **labels** and especially natural for the frame's quarter offsets. But the **1+1 Minkowski mass-shell invariant** associated with the same (T,X) coordinates is

`Q=T²−X²=nk`,

not `X²`. In the archived 2+1 representation-space cone embedding, the point `(T,X,Y=sqrt(nk))` is null since `T²−X²−Y²=0` and the fixed-Y section `T²−X²=Y²=nk` is the hyperbola. The section's invariant radius is √(nk). Saying “the shell is the cone's constant pair-variance section” is **not literally frame-independent** under this coordinate dictionary. Its Q label can be held constant while the pair variance changes.

## Gate 1393 — exact Lorentz boost covariance test

Under a standard 1+1 boost of rapidity η, the null pair coordinates transform `n→n e^η, k→k e^{−η}`, giving

`T'=T coshη+X sinhη`, `X'=X coshη+T sinhη`.

Then `Q'=T'²−X'²=nk=Q` EXACTLY, while `V'_pair=(X')²=(X coshη+T sinhη)²`, generally different from `V_pair=X²`. The especially transparent counterexample is balanced `n=k=1`: initially `V_pair=0`, but after boost `V'_pair=sinh²η` while `Q=1` unchanged. A pair variance of 1/16 at a particular boost therefore is not a boost-invariant mass² or a physical graviton mass. Similarly, a previously defined constant-Q representation hyperboloid such as q2 Q=1/16 is Lorentz invariant in its ambient representation metric, but **cannot be identified with the sample-pair variance just because the numbers coincide**. Explicit additional mapping/selection is required to compare them.

**Numerical exact-symbolic test:** local actual executed `/mnt/data/cone_gate/variance_shell_covariance_v15_1467.py` (SymPy): all boost and variance identities pass. For the balanced (1,1) pair the variance at η=(0,.5,1) is (0,0.2715403174076219,1.3810978455418155), while nk stays exactly 1. **Additive independently authored GitHub source** `research-notes/k4_variance_shell_boost_covariance_v15_1467.py`, commit **6430c8e69fb751731d570404c26ecbb99903c8fa**, exact committed-byte Audit pending.

## Interpretation, opportunity, and clean boundary

The variance language still has attractive use for a **preferred arithmetic pairing frame** (e.g. normalized balanced n=k seat or a specified minimum-rung pair) or a statistically defined dispersion across sectors. It naturally distinguishes intrinsic chosen-rung offsets (1/4 and 1/16) and supplies a compact AM–GM interpretation. But without a map carrying the pair and its frame covariantly, “mass shell = constant variance” is ambiguous and often false. A graviton's **physical helicity-2 wave** can still be null, even if an elementary *gravity-sector rung label* lives at q2 variance 1/16. No physical rest mass or modification of the Einstein graviton dispersion follows. The historical observed Dirac rapidity 45.310 contains G in its definition; neither the variance dictionary nor the nested shells select that boost/scale.

**AUDIT/SANDBOX HANDOFF:** verify the boost explicitly and distinguish the *constant product* hyperboloid from *constant pair-variance* surfaces. Reconcile Sandbox v15.1465's phrasing “constant-variance sections of photon cone” with its own exact embedding `(T,X,sqrt(nk))` without discarding the exact V1–V7 identities. If a distinguished arithmetic rest frame is intended, name it and show whether the physical mapping to an invariant observable exists. Preserve graviton masslessness and report no new physical G or mass prediction.

**PRIORITY:** This variance interpretation is not a blocker to the current Einstein–H² numerical relativity milestone. Continue nonlinear generalized-harmonic Einstein–H² gauge evolution from v15.1453 using v15.1466's hyperbolic linear-wave benchmark; keep sector-variance vs invariant-mass-shell interpretation as an independent handoff.
