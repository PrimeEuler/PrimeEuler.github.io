# Cone Derivation Ledger v13.572 — 12-Prime Hadamard Projection-Retention Audit

**Status:** preregistered label-blind projection gate completed at `M=3999`. Finite binary64 diagnostic only; no theorem, asymptotic, arithmetic-causation, Pell/Suzuki, RH, or GRH promotion.

## 1. Frozen input

Sample:

`Q={5,7,11,13,17,19,23,29,31,37,41,43}`.

Canonical background/whitening remains `B0={arch,2,3,4,5,7}` exactly as in `suzuki_ray_alignment_expanded_blind.py`. The full 12-source geometry had already passed the four-cutoff stability gate through `M=3999`; arithmetic explanatory labels remained blinded for the present decision statistics.

Reproducible script:

`research-notes/suzuki_12prime_hadamard_projection_audit.py`

commit `2e8ad08f1be2cba3bc49dfb34cf42d64334ccf18`.

## 2. Faithful Hadamard projection definition

A precision to the preregistration wording is necessary. The source response has four unit-core stars, and each star has three outer-edge singular contributions. Therefore there is not one canonical three-vector per source before choosing/aggregating a star.

For each source `q` and star center `r`, embed its three normalized leading-singular edge contributions into a four-residue vector with zero at the center, apply `H4/2`, and retain the three nonprincipal coordinates. Concatenate those four three-vectors to obtain a 12-dimensional projected source vector, then normalize it. This preserves the already-frozen star structure without selecting a favored center after inspection.

`Delta57` is correspondingly recorded **per star**, giving four values per source, rather than collapsed post hoc to one scalar.

## 3. Preregistered geometry-retention statistics

At `M=3999`, comparing all 66 full-ray angular distances with all 66 projected angular distances:

- Pearson correlation: `0.9934590071333118`
- Spearman rank correlation: `0.9913161465400272`
- mean top-3-neighbor Jaccard overlap: `0.9583333333333334`

The preregistered retention gate required

`Spearman >= 0.80` and `mean top-3 Jaccard >= 0.60`.

Therefore

**PASS — HADAMARD GEOMETRY RETAINED.**

The result is well above both frozen thresholds.

Eleven of twelve sources preserve their complete top-3 neighbor set. The only partial change is source `q=11`:

- full-ray top 3: `{5,17,29}`
- projected top 3: `{5,13,17}`
- Jaccard: `0.5`.

All other source-wise top-3 Jaccards are exactly `1.0`.

## 4. Five closest full-ray pairs

The preregistered close-pair audit gives:

| pair | full angle (deg) | projected angle (deg) | ||Delta57(q)-Delta57(r)|| over four stars |
|---|---:|---:|---:|
| 13,31 | 1.1678905531462331 | 1.4621571062330776 | 0.09456534131816027 |
| 5,37 | 3.0270223014577704 | 4.007275965819458 | 0.20436142210353891 |
| 5,13 | 8.491989771702148 | 9.876502129854407 | 0.08946280057059719 |
| 5,31 | 8.767014094877185 | 10.20745208138955 | 0.08913070876776934 |
| 31,37 | 9.392374720913647 | 11.097563166764061 | 0.18033916809349468 |

Thus the Hadamard projection does not create the nearest-neighbor geometry; it closely tracks geometry already present in the full Suzuki response rays.

## 5. Delta57 four-star vectors

In star order `(1,5,7,11)`:

- q=5: `(-0.9398274496659105, -0.05682365774873338, -0.8437908482707006, -0.8624458365209435)`
- q=7: `(-0.42615924650775205, -0.7073221725468092, +0.18416268218007747, -0.33883390907429795)`
- q=11: `(-0.8899155086970778, +0.6215237099921214, -0.8365479985538645, +0.07802933478416661)`
- q=13: `(-0.8981011524063062, -0.00795350143327083, -0.879225442693459, -0.8112735183915637)`
- q=17: `(-0.8863492767617435, +0.763628484206851, -0.8724705150365989, -0.5844517475547621)`
- q=19: `(+0.024193619971970268, +0.5135126082576194, -0.1634934601908495, -0.055023256418853694)`
- q=23: `(+0.020198236335099953, +0.7069350232835662, -0.8666619391891822, +0.009676649152612163)`
- q=29: `(-0.8057842410999442, +0.17714522759842688, -0.8717546946158022, +0.0842844564334198)`
- q=31: `(-0.8951687060842571, -0.10246612655251412, -0.8801444076431525, -0.8119972128568378)`
- q=37: `(-0.9373213474210212, -0.26066967755477466, -0.8404122538641804, -0.8763273207639999)`
- q=41: `(-0.5330421739212616, -0.5630380028254838, -0.7502431835909109, -0.4516711959047246)`
- q=43: `(-0.2275927904541268, -0.652835554020236, -0.5511155688761675, -0.010281837858201606)`.

These values are recorded as diagnostics, not used to retroactively define a success criterion.

## 6. Interpretation

The main positive result is narrow but strong: the nonprincipal Hadamard star coordinates retain essentially all of the rank ordering of the complete 12-prime source-ray geometry (`rho_S=0.9913`) and nearly all local top-3 neighborhoods (`J=0.9583`). This makes the Hadamard/unit-core coordinate system a faithful descriptive chart for the stable finite Suzuki source manifold.

It does **not** restore the failed chi12 sign-clustering hypothesis, does not make 5/13 special, and does not establish an exact V4 symmetry. The previous blind failures remain binding.

## 7. Next gate

The label-blind projection audit is now frozen. Arithmetic/group-theoretic unblinding is permitted next, but must compare pre-existing labels/invariants against the already-frozen geometry rather than choose a new pair or coordinate after inspection.

The clean next comparison is against the independently derived surviving `J`-compatible relabelings / orientation structures (`sigma_A`, `sigma_B`) and other pre-existing arithmetic labels, using the full 66-pair geometry and/or frozen projected coordinates. Any explanatory claim must beat simple controls and cannot be rescued by selecting only the visually strongest pair.
