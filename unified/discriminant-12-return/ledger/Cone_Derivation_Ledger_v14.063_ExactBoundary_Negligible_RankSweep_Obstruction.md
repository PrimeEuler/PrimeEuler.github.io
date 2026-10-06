# Cone Derivation Ledger v14.063 — Exact Odd M16000 Boundary Replay: Boundary Term Negligible

**Date:** 2026-10-06  
**Track:** Lane A / correction and obstruction isolation  
**Status:** [D] exact-boundary replay complete; [D] n=16000 K=10 boundary contribution is negligible at the theorem endpoint; [N] higher-rank sweep fails to converge to theorem endpoint; [O] exact-near matrix-free endpoint replay in flight.  
**Parents:** v14.061–v14.062; research-note `suzuki_M8000_remote_schur_16000_exact_boundary.py`.  
**Collision check:** immediately before this write, live HEAD was `dbbf875248d41c1118657eeaaf9358cd14ba9fb6`; live ledger max was v14.062. No collision.

---

## 1. Correction to the diagnostic interpretation in v14.062

v14.062 correctly identified a code-path distinction: in odd parity at (M=16000), the row (n=16000) is not in the exact-near lattice and is therefore handled by the K=10 separated representation in the original remote-Schur diagnostic.

However, the inference that this row plausibly dominates the observed (sim2.2	imes10^{-6}) odd endpoint plateau is now **refuted by direct replay**.

A dedicated cross-check represented (n=16000) exactly as its own front-coupling channel and moved the K=10 representation to (n>16000), leaving the rank-24 near compression otherwise unchanged.

Original rank-24 odd endpoint:

[
eta_{o,mathrm{orig}}=0.0036152617805427956.
]

Exact-(n=16000) boundary replay:

[
eta_{o,mathrm{bd-exact}}=0.003615261648251742.
]

Difference:

[
oxed{
eta_{o,mathrm{bd-exact}}-eta_{o,mathrm{orig}}
=-1.322910536	imes10^{-10} 	ext{(approximately)}.
}
]

This is more than four orders of magnitude smaller than the theorem-endpoint mismatch

[
eta_{o,mathrm{orig}}-eta_{o,mathrm{theorem}}
approx -2.2357	imes10^{-6}.
]

Therefore the single K=10 boundary row is **not** the source of the odd plateau.

The boundary replay retained excellent numerical residuals:

[
|r_{m CG}|_2approx1.235	imes10^{-13},
qquad
	ext{front target residual}approx6.074	imes10^{-26}.
]

---

## 2. Rank sweep obstruction sharpened

The completed deterministic rank sweep gives the following signed endpoint errors relative to the promoted v14.059 midpoints.

Even parity:

[
egin{array}{c|c}
r & eta^{m remote}_e-eta^{m theorem}_e\ hline
32 & +1.1545874670410277	imes10^{-5}\
48 & +8.718673673588709	imes10^{-6}\
64 & +5.68992533192406	imes10^{-6}\
96 & +9.012666192367413	imes10^{-6}
end{array}
]

Odd parity:

[
egin{array}{c|c}
r & eta^{m remote}_o-eta^{m theorem}_o\ hline
32 & -2.221385221408325	imes10^{-6}\
48 & -2.203522498015007	imes10^{-6}\
64 & -2.3263742186460656	imes10^{-6}\
96 & -2.2875698129994244	imes10^{-6}
end{array}
]

There is no monotone or convincing convergence toward the theorem endpoint through (r=96). The earlier working hypothesis that the rank-24 endpoint discrepancy was overwhelmingly discarded-SVD compression is therefore **not supported** by the sweep.

At minimum, another rank-insensitive structural/arithmetic mismatch is present; in odd parity it dominates the observed error. Even parity also shows a persistent several-(10^{-6}) discrepancy with rank-dependent fluctuations.

---

## 3. Current Lane A gate

Lane A has launched an exact-near matrix-free Schur replay:

`research-notes/suzuki_M8000_remote_schur_exact_near_endpoint.py`

with the near Schur action evaluated as

[
xmapsto B_{m near}F_{m eff}^{-1}B_{m near}^{T}x
]

using the refined LDDD/Feshbach front response dynamically, rather than through any global SVD compression. The odd (n=16000) boundary is exact and the remote archimedean diagonal is set to arch-200 for endpoint alignment.

That replay is now the decisive endpoint gate. If it reproduces v14.059, the global SVD path can be discarded. If it does not, the remaining mismatch must be sought in the remote raw operator/source normalization/front-response transport rather than blamed on compression rank.

---

## 4. Sandbox handoff amendment

The v14.061 sandbox compression-certificate task remains useful for quantifying discarded-SVD error, but **do not assume endpoint mismatch = SVD error** in either parity.

Please:

1. derive the SVD perturbation bound intrinsically from (|Delta B|) and operator/resolvent data;
2. do not calibrate that bound by forcing it to explain the observed theorem mismatch;
3. treat the exact-boundary result above as evidence that the odd plateau is not a K=10 boundary artifact;
4. watch the next ledger entry for the exact-near endpoint replay before assigning the remaining structural discrepancy.

---

HANDOFF-AMENDMENT  
target: sandbox  
type: correction / obstruction update  
parent: v14.061–v14.062  
status: open  
action: Continue intrinsic discarded-SVD perturbation work, but do not identify the raw endpoint mismatch with SVD error. Exactizing odd n=16000 changes eta by only ~1.32e-10, so the ~2.2e-6 odd plateau comes from elsewhere. Await/consume the exact-near endpoint replay when it lands.  
deliverable: intrinsic SVD-error bound plus any newly isolated structural term  
constraints: no finite-cutoff monotonicity inference; no theorem promotion without independent audit; re-check live HEAD before writing.
