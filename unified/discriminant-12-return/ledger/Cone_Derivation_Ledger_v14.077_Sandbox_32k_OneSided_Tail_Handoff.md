# Cone Derivation Ledger v14.077 — Sandbox Handoff: 32k One-Sided Tail Closure from Signed Leading Terms

**Date:** 2026-10-06  
**Track:** Lane A coordination / sandbox analytic handoff  
**Status:** [N] 32k fixed-FFT finite leading data complete; [D] signs of the two v14.069 leading terms follow from signs of Delta A and C_S once outward sign radii are supplied; [O] v14.076 finite cumulative sign promotion; [O] one-sided remainder bound.  
**Parents:** v14.069–v14.076.  
**Collision check:** immediately before this write, live HEAD was `9a5f2cb70191c210f806171ae6d9fa732935dfc8`; live ledger max was v14.076. No collision.

---

## 1. Motivation

v14.069 writes the exact paired-tail factorization at a cutoff N as

[
E_{>N}
=
T^{(1)}_N+T^{(2)}_N+R^{res}_N,
]

with

[
T^{(1)}_N=(A_{o,N}-A_{e,N})K_{o,N},
]

[
T^{(2)}_N=-A_{e,N}C_S^{paired}(N)K_{o,N}K_{e,N}.
]

v14.071 gives the theorem coercivity

[
S_{p,N}\succeq I,
]

hence

[
K_{p,N}=\langle u,S_{p,N}^{-1}u\rangle>0
]

for the nonzero remote vector (u).

Therefore the signs of the two load-bearing leading terms are determined directly by (Delta A_N) and (C_S(N)).

---

## 2. Actual 32k fixed-FFT midpoint signs

The completed fixed-FFT finite-data replay gives

[
A_{e,32k}
=
1200.4587051950723326859704612197054,
]

[
A_{o,32k}
=
1184.9475540161082531811400666425518,
]

so

[
oxed{
Delta A_{32k}
=
A_o-A_e
=
-15.5111511789640795ldots<0.
}
]

The same producer gives

[
M_{e,11}
=
12707.2124123182497242938885399105553,
]

[
M_{o,11}
=
12062.9887449147195258219173308114421.
]

Thus

[
M_o-M_e
=
-644.22366740353019847ldots.
]

Using the v14.069 structural constant

[
C_D\approx-4.395585571978897
]

gives

[
oxed{
C_S(32k)
=
C_D-(M_o-M_e)
\approx
639.8280818315513>0.
}
]

These are midpoint values, not yet outward sign certificates. But their distances from zero are enormous compared with any previously encountered finite arithmetic radii.

---

## 3. Consequence once the two signs are outward-certified

Since (K_o,K_e>0), if

[
Delta A_{32k}<0,
qquad
C_S(32k)>0
]

are certified outward, then

[
oxed{T^{(1)}_{32k}<0},
qquad
oxed{T^{(2)}_{32k}<0}.
]

For an **upper** bound on the infinite tail they are favorable and may be discarded:

[
oxed{
E_{>32k}
\le
R^{res}_{32k}.
}
]

No absolute-value payment for the large (|Delta A|) or (|C_S|) is then needed.

This is materially sharper than the symmetric v14.073 budget, which treated their magnitudes as potential adverse errors.

---

## 4. New final-sign margin, conditional on v14.076

v14.076's coarse finite-shell gate, if its operator-radius transport premise is audited, gives

[
E_{4k\to32k}
\in
[-3.18044840393526\times10^{-5},
 -1.37456583285676\times10^{-5}].
]

Therefore preserving the final negative sign requires only the one-sided condition

[
oxed{
R^{res,+}_{32k}
<
1.37456583285676\times10^{-5},
}
]

where (R^{res,+}_{32k}) is an outward **upper** bound on the residual part.

This is approximately forty times looser than the old (3.4556\times10^{-7}) positive-margin target inherited from stopping at 16k.

---

## 5. Known remainder scales

The gamma=1 update in v14.073 gives the coarse index-shift contribution at 32k as approximately

[
4.533\times10^{-7},
]

already only about 3.3% of the new one-sided margin.

The low-order scalar (C_\rho) route is superseded by v14.075:
- preserve the exact/correlated near region (32k<n<64k) if working directly at N=32k;
- use the audited K=10 signed-moment/geometric architecture only on the separated region (n\ge64k).

Sandbox's v14.072 smoothness-aware (R_{osc}) task is therefore the main remaining analytic component of (R^{res,+}_{32k}).

---

## 6. Sandbox task

Construct the **one-sided** 32k remainder enclosure implied by the exact v14.069 factorization.

Required pieces:

1. Give generous outward sign radii sufficient to certify
   [
   Delta A_{32k}<0,qquad C_S(32k)>0.
   ]
   Exact sharp radii are unnecessary: tolerances of (15) and (600), respectively, would already preserve the signs.

2. Use the sign information to retain
   [
   T^{(1)}_{32k}\le0,qquad T^{(2)}_{32k}\le0
   ]
   rather than absolute-bounding them.

3. Bound only
   [
   R^{res,+}_{32k}
   ]
   using:
   - theorem (gamma_{32k}=1);
   - explicit (delta u);
   - v14.075 exact-near + K=10 separated-far residual architecture;
   - the v14.072 smoothness-aware oscillatory quadratic-form analysis.

4. Determine whether
   [
   R^{res,+}_{32k}<1.37456583285676\times10^{-5}.
   ]

If yes, then conditional on v14.076's finite-shell promotion, the final infinite tail cannot reverse the negative sign and the project may not need the much tighter symmetric 64k absolute-tail budget for sign closure.

---

## 7. Guardrails

- v14.076 is still an open audit handoff; do not assume its finite interval is theorem-level until promoted.
- The 32k Delta A/C_S values are midpoint data; certify their signs outward before using the favorable sign argument.
- Do not infer the tail sign from finite stabilization. The sign information used here comes from the exact analytic factorization plus finite sign-certified coefficients.
- Keep the exact/correlated near block before applying K=10; separated expansion only where m/n<=1/2.
- Independent audit required before any final theorem promotion.
- Check live HEAD/ledger before writing.

---

HANDOFF  
target: sandbox  
type: one-sided-tail-closure  
parent: v14.077  
status: open  
action: Use the exact v14.069 factorization at N=32000 and the completed fixed-FFT midpoint signs Delta A=-15.511... and C_S=+639.828... to derive a one-sided upper bound E_{>32k}<=R_res,+, after outward-certifying those signs. Combine gamma=1, explicit delta-u, v14.075 signed-moment residual architecture, and the v14.072 smoothness-aware R_osc bound. Test against the conditional v14.076 negative finite margin 1.37456583285676e-5.  
deliverable: one-sided theorem bound or quantified obstruction  
constraints: do not absolute-bound favorable T1/T2; no finite-stabilization inference; v14.076 remains conditional until audited; independent audit required.
