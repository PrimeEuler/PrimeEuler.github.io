# Cone Derivation Ledger v14.071 — Nested Remote-Schur Coercivity Inheritance and 32k/64k Fixed-FFT Finite-Data Launch

**Date:** 2026-10-06  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] theorem-level Euclidean remote coercivity `gamma_N=1` inherited for every exact nested cutoff `N>=4000`; [D] fixed full-lattice FFT route already calibrated at 8k/16k; [N] new 32k/64k finite-data producer launched in both parities; [O] outward finite radii and final infinite-tail enclosure.  
**Parents:** v14.044, v14.046, v14.065–v14.070.  
**Research commit:** `7a07f49d5585182c3b683c224270e4745193e0dd`.  
**Workflow commit:** `eb6464583347da8157b2c067c2ec0e75f80cba2b`.  
**Collision check:** immediately before this write, live HEAD was `eb6464583347da8157b2c067c2ec0e75f80cba2b`; live ledger max was v14.070. No collision.

---

## 1. Context

Sandbox v14.069 and External Audit Round 173 (v14.070) reduce the compression-free infinite-tail enclosure to finite cutoff data, with the scaling indicating that `N≈64000` is the first plausible cutoff where the operator-driven second-order term can fit below the current worst-case positive cumulative margin

[
m_* = 3.45557892442104	imes 10^{-7}.
]

The requested finite inputs are:

[
Delta A_N=A_{o,N}-A_{e,N},
qquad
C_S^{paired}(N),
qquad
gamma_N,
qquad
C_ho
]

(or the higher-order signed-moment replacement for the last item).

The fixed full-lattice FFT route from v14.065 has already passed its acceptance gate: it reproduces the promoted 8k→16k capacity ratios to about `1.1e-12` in even parity and `2.7e-15` in odd parity, with post-refinement residuals at the `1e-26` scale. The old transported-front remote-Schur path is therefore no longer used for the new finite data.

---

## 2. Euclidean coercivity is already theorem-level for every later nested cutoff [D]

v14.044/v14.046 promote, in coefficient-space Euclidean norm,

[
S_{e,4000}succeq I,
qquad
S_{o,4000}succeq I.
]

Fix either parity and any exact later cutoff `N>=4000`. Split the remote space of `S_{p,4000}` as

[
mathcal H_{>4000}
=
mathcal H_{4000<nle N}
oplus
mathcal H_{>N},
]

and write

[
S_{p,4000}
=
egin{pmatrix}
A & B\
B^* & D
end{pmatrix}.
]

By associativity of exact Schur complementation, the remote operator after enlarging the finite section to `N` is

[
S_{p,N}=D-B^*A^{-1}B.
]

For any `zinmathcal H_{>N}`,

[
z^*S_{p,N}z
=
min_y
egin{pmatrix}y\zend{pmatrix}^*
S_{p,4000}
egin{pmatrix}y\zend{pmatrix}.
]

Since `S_{p,4000}succeq I`,

[
egin{aligned}
z^*S_{p,N}z
&ge
min_yleft(|y|^2+|z|^2ight)\
&=
|z|^2.
end{aligned}
]

Therefore

[
oxed{
S_{p,N}succeq I
quad	ext{for every }Nge4000,
}
]

hence the v14.069 conditional theorem may take

[
oxed{gamma_N=1}
]

at `N=16000,32000,64000` and every later nested cutoff, without a new eigensolve.

This is a direct theorem consequence of the already-promoted v14.044/v14.046 Euclidean result, not a midpoint diagnostic.

---

## 3. New finite-data producer [N]

Added:

`research-notes/suzuki_full_fft_extended_finite_data.py`

with workflow:

`.github/workflows/suzuki-full-fft-extended-finite-data.yml`.

The matrix runs

[
Nin{32000,64000},
qquad
pin{e,o}.
]

For each point, one shared fixed full-lattice FFT operator solves:

1. the six protected-coupling columns;
2. the finite source right-hand side;
3. the leading remote coupling right-hand side

[
w^{(1)}_p
=
-rac{2}{pi}z
+
alpha_prac{4g_p}{pi}p_p.
]

After the same arch-200 LDDD refinement used by the calibrated 8k/16k replay, it reports

[
C_{p,N},
qquad
L_{p,N},
qquad
sigma_{p,N}=operatorname{sign}(L_{p,N}),
]

[
A_{p,N}=C_{p,N}L_{p,N}^2,
]

and

[
M_{p,11}
=
(w^{(1)}_p)^T A_{p,N}^{-1}w^{(1)}_p.
]

The paired outputs give directly

[
Delta A_N=A_{o,N}-A_{e,N},
]

and, using the already-reconciled v14.021 normalization,

[
C_S(N)
=
C_D-left(M_{o,11}-M_{e,11}ight),
qquad
C_Dapprox-4.396.
]

No old rank-compressed or transported-front response enters this producer.

---

## 4. Acceptance gate

Before any 32k/64k midpoint is consumed as evidence, require:

1. all fixed-operator CG solves report success and independently recomputed residuals remain small;
2. arch-200 LDDD refinement returns residuals comparable in quality to the calibrated 8k/16k route;
3. the 32k/64k `A_N` and direct `M_{11}` values are stable enough that the v14.069 conditional theorem can be evaluated without fitting or extrapolation;
4. no inference of the infinite-tail sign is made from finite-cutoff stabilization;
5. outward finite-source/capacity radii are added before theorem promotion.

---

## 5. Sandbox coordination

The `gamma_N` request in v14.069 is now closed structurally:

[
oxed{gamma_N=1quad(Nge4000).}
]

Sandbox should use this exact theorem input in the conditional enclosure rather than the earlier exploratory `gammaapprox6.38` diagonal/window value.

The remaining load-bearing finite inputs are therefore

[
oxed{Delta A_N,quad C_S(N)}
]

from the running fixed-FFT jobs, together with the correlated residual/remainder quantity (preferably the established signed-moment/K=10 architecture rather than a low-order absolute `C_ho`).

---

HANDOFF  
target: sandbox  
type: theorem-input-update  
parent: v14.071  
status: open  
action: Replace the open gamma_N input in the v14.069 conditional theorem by the inherited theorem value gamma_N=1 for every N>=4000. Proof: v14.044/v14.046 give S_{p,4000}>=I; exact later S_{p,N} is a nested Schur complement, and the variational characterization preserves the unit Euclidean floor. The 32k/64k fixed-FFT producer for Delta A_N and C_S(N) is now running; consume those only after Lane A records the completed outputs.  
deliverable: update the conditional enclosure constants with gamma_N=1 and report the resulting admissible budgets for Delta A_N, C_S(N), and the residual remainder at N=32k and N=64k  
constraints: no finite-cutoff stabilization inference; do not consume uncompleted CI values; retain common-mode cancellation before absolute values; no theorem promotion without independent audit.
