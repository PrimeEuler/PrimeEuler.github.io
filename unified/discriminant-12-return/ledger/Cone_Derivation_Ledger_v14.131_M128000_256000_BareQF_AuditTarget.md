# Cone Derivation Ledger v14.131 — Full 128k→256k Bare Outward QF Certificate Target

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [AUDIT TARGET] Full exact-source bare oscillatory quadratic-form certificate on the complete (128k<nle256k) octave. No infinite-tail theorem inferred.  
**Parents:** v14.120, v14.123, v14.128–v14.130.  
**Producer:** `research-notes/suzuki_M128000_bare_fullnear_outward_certificate.py`.  
**Successful workflow run:** `37641669108`.  
**Collision check:** immediately before this write, live HEAD was `6f72abe59e837d0ffdb509b8d9feb70d71656d02`; live ledger max was v14.130. No collision.

---

## 1. Exact-source solve certification

The complete octave has

[
N=128000,qquad J=64000.
]

The producer uses the same architecture independently promoted on the two previous octaves:

1. validated FFT candidate;
2. independent chunked-dense nominal action;
3. exact-vs-LDDD scalar inflation;
4. 1000x adversarial stress on the complete residual budget;
5. residual-to-solution control through the promoted coercive interface;
6. exact Abel telescope;
7. conservative (|C_D|le4.4).

The scalar-cap consumer is the through-256k public envelope from v14.123.

---

## 2. Residual budgets

### even-v

FFT recomputed residual:

[
1.876121486122663	imes10^{-15}.
]

Unstressed exact-source residual upper bound:

[
6.442216251465198	imes10^{-13}.
]

After the full

[
1000	imes
]

stress:

[
oxed{
6.442216251465198	imes10^{-10}<10^{-9}.
}
]

### odd-v

FFT recomputed residual:

[
1.887922295073241	imes10^{-15}.
]

Unstressed exact-source residual upper bound:

[
6.852595576824617	imes10^{-13}.
]

After stress:

[
oxed{
6.852595576824618	imes10^{-10}<10^{-9}.
}
]

Both fail-closed residual checks pass.

---

## 3. Partial-sum / Abel certificate

Using the same candidate vectors whose exact-source residuals are certified,

[
S_{max}^{m cand}
=
3.6076085604877852	imes10^{-6}.
]

After public solution-error inflation,

[
oxed{
S_{max}^{m out}
=
4.113572986114726	imes10^{-6}.
}
]

The Abel coefficient telescopes exactly to

[
rac1{128001}.
]

Therefore the linear term is bounded by

[
3.2137037883412836	imes10^{-11}.
]

The conservative rank-one term contributes

[
1.6785061348904866	imes10^{-11}.
]

Hence

[
oxed{
|Q_{m bare}^{128k	o256k}|
le
4.89220992323177	imes10^{-11}.
}
]

Against the public target

[
10^{-8},
]

the headroom is

[
oxed{
204.40660063487317	imes.
}
]

All fail-closed checks pass.

---

## 4. Dyadic comparison

The promoted previous-octave bounds are

[
|Q_{m bare}^{32k	o64k}|
le
7.66163003022406	imes10^{-10},
]

[
|Q_{m bare}^{64k	o128k}|
le
1.932592637896439	imes10^{-10}.
]

The new candidate bound is

[
|Q_{m bare}^{128k	o256k}|
le
4.89220992323177	imes10^{-11}.
]

Thus the outward certificate itself decreases by approximately a factor of four per dyadic octave:

[
rac{1.9325926	imes10^{-10}}
     {7.6616300	imes10^{-10}}
approx0.252,
]

[
rac{4.8922099	imes10^{-11}}
     {1.9325926	imes10^{-10}}
approx0.253.
]

**Guardrail:** this is an observed pattern in already-outward finite-octave bounds, not yet an infinite geometric-series theorem.

---

## 5. Relevance to the protected reduction

The bare oscillatory parity-difference contribution is now rigorously tiny on three consecutive complete octaves.

The unresolved large common-mode behavior identified in v14.119–v14.130 is therefore confined to the exact protected/Feshbach feedback, not to the bare oscillatory source operator.

This sharpens the final target to the at-most-six-dimensional normalized protected term

[
DeltaLambda_parallel
]

from v14.130.

---

## 6. Verdict

[
oxed{
|Q_{m bare}^{128k	o256k}|
le4.89221	imes10^{-11}
}
]

with (204.4	imes) headroom.

No infinite-tail conclusion is drawn from finite-cutoff decay alone.

---

HANDOFF
target: external-audit
type: 128k-256k-bare-qf-audit
parent: v14.131
status: open
action: Independently rerun the M128000 bare full-near outward certificate using the through-256k scalar envelopes. Verify both stressed residual caps, the exact Abel telescope, and the final 4.89220992323177e-11 bound. If all pass, promote this finite-octave bound only.
deliverable: theorem-or-obstruction
constraints: No geometric-series extrapolation to infinity from the three finite-octave bounds.
