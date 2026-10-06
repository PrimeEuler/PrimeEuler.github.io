# Cone Derivation Ledger v14.076 — Sandbox Handoff: 16k→32k Coarse Operator-Radius Audit and Sign-Flip Gate

**Date:** 2026-10-06  
**Track:** Lane A coordination / sandbox audit handoff  
**Status:** [N] fixed-FFT 16k/32k midpoint complete; [N] deliberately coarse operator-radius budget passes with large negative sign margin; [O] theorem status depends only on whether the promoted global relative operator/source representation radius transports through the 32k nested finite section.  
**Parents:** v14.052–v14.060, v14.071–v14.075.  
**Research commits:** `eecc1170de60762b4295fcdd0f6b856fccdc8c60`, `c8abd47a1619e126d4f1f18d1ac203620d7d26c5`.  
**Collision check:** immediately before this write, live HEAD was `cf4cba8c0a81016a0ab29dc3d279430516c30150`; live ledger max was v14.075. No collision.

---

## 1. Why this is worth auditing separately

The already-promoted cumulative finite interval through 16k is

[
E_{4k\to16k}\in
[3.45557892442104\times10^{-7},
 1.97545933653356\times10^{-6}],
]

strictly positive but with a small worst-case lower margin.

The calibrated fixed full-lattice FFT solver gives at 32k:

[
C_{e,32k}\approx7.485609640013522\times10^{-30},
qquad
C_{o,32k}\approx2.158138843073839\times10^{-25}.
]

Using the promoted 16k capacities, the exact midpoint shell ratios are

[
eta_{e,16k\to32k}
=0.001909244425063178ldots,
]

[
eta_{o,16k\to32k}
=0.001885308845264730ldots,
]

hence

[
oxed{
E^{mid}_{16k\to32k}
=-2.393557979844793\times10^{-5}.
}
]

This midpoint is sufficiently far from zero that common-mode source-gradient cancellation may not be necessary merely to certify the shell sign.

---

## 2. Deliberately coarse budget

The executable target

`research-notes/suzuki_M16000_M32000_coarse_shell_budget.py`

pays the certified global relative operator radius independently at both cutoffs instead of subtracting common-mode gradients.

Conditional premise for parity (p):

[
(1-	heta_p)A^{rep}_{p,N}
\preceq A^{exact}_{p,N}
\preceq
(1+	heta_p)A^{rep}_{p,N}
]

at both (N=16000) and (N=32000), with the same promoted values used in v14.052/v14.058:

[
	heta_e=3.899270146651301\times10^{-6},
qquad
	heta_o=9.69258681013552\times10^{-11}.
]

Then for (C=(f^TA^{-1}f)^{-1}),

[
|\log(C^{exact}/C^{rep})|
\le -\log(1-	heta_p).
]

Paying both cutoffs independently gives

[
L_{src,p}=2[-\log(1-	heta_p)].
]

The already-audited public finite-solve cap (R_{cap}=10^{-7}) contributes

[
L_{solve}=2[-\log(1-R_{cap})].
]

No common-mode cancellation is used in this target.

CI reproduces:

### even
[
L_e=7.998555507649803\times10^{-6},
]
[
R_{eta,e}=8.01389080419907\times10^{-6}.
]

### odd
[
L_o=2.001938617362128\times10^{-7},
]
[
R_{eta,o}=2.00571329147653\times10^{-7}.
]

Therefore

[
W_{16k\to32k}
=8.21446213334672\times10^{-6},
]

and the conditional outward shell interval is

[
oxed{
E_{16k\to32k}
\in
[-3.21500419317947\times10^{-5},
 -1.57211176651012\times10^{-5}].
}
]

It is strictly negative with substantial margin despite throwing away common-mode source cancellation.

---

## 3. Consequence if the premise audits

Adding the already-promoted theorem interval through 16k gives

[
oxed{
E_{4k\to32k}
\in
[-3.18044840393526\times10^{-5},
 -1.37456583285676\times10^{-5}]
}
]

under the same premise.

Thus the cumulative finite sign would flip from the small positive 16k interval to a **large strictly-negative theorem interval through 32k**.

This changes the final-tail acceptance geometry materially: once promoted, the infinite remainder need only be shown unable to cross a negative margin of at least (1.37\times10^{-5}), rather than preserving the obsolete (+3.46\times10^{-7}) lower margin at 16k.

Guardrail: none of this is promoted yet. Finite-cutoff stabilization is not used as an infinite-tail proof.

---

## 4. Exact audit question

The old (	heta_p) values were produced by

`research-notes/suzuki_arch200_capacity_source_perturbation_budget.py`

from:
- interval-certified scalar representation radii;
- an exact global shifted-front floor from the protected/complement graph factorization;
- a two-longdouble source-vector split bound.

The scalar representation part has now been replayed through 32k:
- odd sector passes the prior caps directly;
- even sector's 16k→32k max (z)-error is (5.877332881956699\times10^{-39}), which exceeds a tighter internal old maximum but remains below the promoted public theorem cap (5.88\times10^{-39}).

The open question is therefore **not** scalar arithmetic. It is whether the global relative operator/source bracket giving (	heta_p) transports to the 32k nested finite operator with the same or a still-small-enough constant.

---

## 5. Sandbox task

Independently prove one of:

**Outcome A — transport.** Derive from the existing exact nested/Feshbach structure (especially v14.044/v14.046 and v14.071) a global floor/bracket through (N=32000) that implies the old (	heta_p), or explicit replacement values (	heta^{32k}_p). Recompute the coarse shell interval with those outward values. If the upper endpoint remains (<0), return theorem-grade shell bounds for independent audit.

**Outcome B — obstruction.** If the old global floor does not transport automatically, identify the exact missing finite primitive (for example a protected Schur floor, graph-shear norm, complement floor, or source-vector norm), and compute the maximum admissible (	heta_e^{32k}) for which the shell still remains strictly negative.

Do not fall back to the expensive common-mode gradient replay unless necessary. The shell has enough sign margin that a coarse bound is preferred if it can be justified.

---

## 6. Acceptance / collision rules

- Preserve the distinction between the promoted public scalar cap (5.88\times10^{-39}) and the tighter historical internal maximum.
- Include source-vector representation error if it is not already absorbed in the chosen (	heta_p).
- Do not use finite-cutoff stabilization to bound (E_{>32k}).
- No theorem promotion without independent audit.
- Re-read live HEAD/ledger before writing and use the next free version if another entry lands.

---

HANDOFF  
target: sandbox  
type: coarse-shell-operator-radius-audit  
parent: v14.076  
status: open  
action: Audit whether the promoted global exact-source/operator radius used in v14.052/v14.058 transports through the nested N=32000 fixed-FFT finite section. If yes, certify the coarse 16k→32k interval [-3.21500419317947e-5,-1.57211176651012e-5] and cumulative 4k→32k interval [-3.18044840393526e-5,-1.37456583285676e-5]. If not, return the exact missing primitive and the largest admissible theta_e that preserves negativity.  
deliverable: theorem-grade interval target or quantified obstruction  
constraints: no common-mode gradient replay unless needed; include source representation; no infinite-tail inference; independent audit required.
