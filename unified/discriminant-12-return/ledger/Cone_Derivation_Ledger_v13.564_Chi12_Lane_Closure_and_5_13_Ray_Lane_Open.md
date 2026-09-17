# Cone Derivation Ledger v13.564 — χ12/Suzuki Lane Closure and 5/13 Ray-Alignment Lane Open

**Renumbering note:** originally filed as v13.555, which collided with the already-pushed `Cone_Derivation_Ledger_v13.555_M16001_Remaining_Outward_Certification_DAG.md`. Renumbered to v13.564 during External Audit Round 50. Mathematical content is unchanged.

**Status:** χ12/Suzuki phase lane closed after the predeclared χ12-blind Level-1 failure. The unexpected q=5,13 directional alignment is retained as a separate exploratory lane. Finite binary64 observations only; no theorem promotion.

## 1. Lane decision

The χ12/Suzuki phase-bridge lane ends here in its present form.

v13.553 identified the sign-degeneracy of the original Level-0 test. v13.554 then performed the first genuinely χ12-blind Suzuki response test on q={5,7,11,13}. The predeclared partition {5,7} versus {11,13} failed stably across M=499,999,1999. Therefore the Level-0 algebraic PASS is not promoted into evidence for an operator-level χ12 phase law, and the failed Level-1 metric is not to be retuned to recover the desired partition.

This closure is a negative empirical result, not a theorem that no Suzuki observable can ever correlate with χ12.

## 2. Frozen Level-1 residual observation

The failed clustering test exposed a different feature in the already-frozen M=1999 Level-1 fingerprints F_q: q=5 and q=13 are the closest pair under the normalized directional distance

`D_F(q,q')=||F_q-F_q'||_2/sqrt(12)`.

The recorded value is

`D_F(5,13)=0.07687756223288036`,

well below the other five pair distances.

This observation is not assigned a χ12 interpretation. It becomes the starting datum for a new exploratory lane.

## 3. Frozen-fingerprint decomposition

No new Suzuki matrices or arithmetic labels were introduced. Only the existing Level-1 outputs R_q and F_q were analyzed.

For x=F_q and y=F_q', define

`theta=acos((x·y)/(||x|| ||y||))`,

`Delta_rad=| ||x||-||y|| |`,

and

`Delta_ang=2 sqrt(||x|| ||y||) sin(theta/2)`.

Then

`||x-y||^2 = Delta_rad^2 + Delta_ang^2`.

At M=1999 the q=5,13 pair has

- angle `theta(5,13)=8.488102 degrees`, the smallest of all six pairs;
- cosine similarity `0.9890465359802769`, the largest of all six pairs;
- radial separation `0.1253262990769628`, only the second-smallest radial separation;
- angular chord `0.2349792196304080`, the smallest angular chord.

The closest pair in scale is instead q=5,11, with radial separation `0.06341256081653035`.

**[OBS]** The q=5,13 proximity is therefore directional rather than uniquely scale-based.

## 4. Common-ray projection

For each pair x,y, define the common unit direction by the normalized angular bisector

`u=(x/||x|| + y/||y||)/||x/||x|| + y/||y||||`.

For d=x-y decompose

`d_parallel=(d·u)u`,

`d_perp=d-d_parallel`.

For q=5,13:

`||d_parallel|| = 0.12498263861997272`,

`||d_perp|| = 0.23516218858913948`.

The q=5,13 orthogonal residual is the smallest of all six pairs. The next-smallest is q=5,11:

`||d_perp(5,11)|| = 0.5328671893957349`.

Thus the q=5,13 orthogonal residual is only about 44.1% of the runner-up value.

The parallel residual does not select q=5,13: q=5,11 has the smaller parallel residual `0.06239666638675356`.

**[OBS]** The anomaly is a shared-ray phenomenon: F_5 and F_13 lie unusually close to one common direction, while their positions along that direction are not uniquely close.

## 5. Unit-core center check

The q=5,13 directional alignment is not confined to a single center stratum. Using the four existing three-coordinate blocks of F_q, the within-center cosine similarities are

| center r | cosine(F_5^(r),F_13^(r)) |
|---:|---:|
| 1 | 0.9884471278221679 |
| 5 | 0.9778023842009165 |
| 7 | 0.9969859194164030 |
| 11 | 0.9939743104036549 |

All four exceed 0.9778. The residual squared F-distance is distributed approximately 52.89%, 23.74%, 15.24%, and 8.14% over centers r=1,5,7,11 respectively.

**[OBS]** The shared direction is global across the four tested unit-core centers rather than being produced by one isolated block.

## 6. Evidence status and guardrails

**Legend:** `[EXACT]` exact recomputation/algebra; `[B64]` finite binary64 checkpoint output; `[OBS]` empirical pattern from frozen outputs; `[UNSUPPORTED]` conclusion not established by present evidence.

- **[B64]** All numerical values above are finite binary64 outputs derived from the frozen M=1999 Level-1 fingerprints.
- **[OBS]** q=5,13 are the closest directional pair among q={5,7,11,13}.
- **[OBS]** Their exceptional proximity is concentrated in shared response-ray orientation rather than unique response scale.
- **[OBS]** The alignment appears across all four existing unit-core center blocks.
- **[UNSUPPORTED]** The source-side cause of the q=5,13 alignment is unknown.
- **[UNSUPPORTED]** No arithmetic character, congruence class, log-frequency relation, Pell datum, or other invariant has yet been shown to predict the ray direction.
- **[UNSUPPORTED]** Four q-values are insufficient to establish a family, law, or asymptotic pattern.
- **[UNSUPPORTED]** Nothing here changes the certified Suzuki positivity/index status or any RH/GRH statement.

## 7. New exploratory lane

The new lane is deliberately neutral:

> What, if anything, organizes Suzuki response-ray direction?

The q=5,13 observation is a seed, not a proposed bridge.

The next test must expand the q sample under the same source-faithful construction and fixed baseline whitening, freeze normalized ray directions `U_q=F_q/||F_q||`, and construct the complete pairwise angular-distance matrix before consulting candidate explanatory labels.

Only after that geometry is frozen may independently specified source-side variables be compared with it. This ordering is required to prevent post-hoc fitting.

## 8. Closure/opening summary

`χ12/Suzuki phase lane: CLOSED as a failed Level-1 hypothesis in its present form.`

`5/13 Suzuki ray-alignment lane: OPEN as an exploratory, label-blind structural question.`

The canonical starting observation for the new lane is

`F_5 and F_13 have an unusually coherent common response direction, but the origin and generality of that direction remain unsupported.`
