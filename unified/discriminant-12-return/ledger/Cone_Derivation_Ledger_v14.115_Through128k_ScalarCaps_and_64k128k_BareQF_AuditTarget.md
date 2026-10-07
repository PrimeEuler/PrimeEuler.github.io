# Cone Derivation Ledger v14.115 — Lane A Through-128k Scalar-Cap Transport and 64k–128k Bare Outward QF Audit Target

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [AUDIT TARGET] Records two newly completed fail-closed replays: (i) public exact-vs-LDDD scalar-cap transport through 128k, and (ii) the full exact-source bare oscillatory quadratic-form certificate on the complete 64k–128k octave. No infinite-tail theorem is inferred here.  
**Parents:** v14.058–v14.059, v14.092–v14.096, v14.111–v14.114.  
**Collision check:** immediately before this write, live HEAD was `e85be89cd351fe75254b1e465b0ebc518c228825`; live ledger max was v14.114. No collision.

---

## 1. Through-128k scalar-cap transport

Producer:

[
	exttt{research-notes/suzuki_M128000_scalar_interval_incremental_arch200.py}
]

Workflow:

[
	exttt{.github/workflows/suzuki-M128000-scalar-interval-incremental-arch200.yml}
]

Successful run:

[
	exttt{37624115418}.
]

The producer checks every new mode

[
64000<nle128000
]

against the same already-promoted public scalar envelopes used in the 32k/64k exact-source bridge.

### even-v

[
max |Delta z|
=
5.872900073674295	imes10^{-39}
quad(n=104293),
]

[
max |Delta d|
=
1.175493956745554	imes10^{-38}
quad(n=72663),
]

[
max |Delta p|
=
2.2420698578258073	imes10^{-44}
quad(n=71631).
]

### odd-v

[
max |Delta z|
=
5.875254962076700	imes10^{-39}
quad(n=85916),
]

[
max |Delta d|
=
1.1754865876253644	imes10^{-38}
quad(n=91506),
]

[
max |Delta p|
=
1.1205243315732828	imes10^{-44}
quad(n=78960).
]

In particular both parity z-errors remain below the public

[
5.88	imes10^{-39}
]

cap.

All fail-closed public-cap checks pass in both sectors.

---

## 2. Full 64k–128k exact-source bare outward QF certificate

Producer:

[
	exttt{research-notes/suzuki_M64000_bare_fullnear_outward_certificate.py}
]

Workflow:

[
	exttt{.github/workflows/suzuki-M64000-bare-fullnear-outward-certificate.yml}
]

Successful run:

[
	exttt{37624204166}.
]

The replay is the exact dyadic lift of the N=32k certificate recorded in v14.111:

1. validated FFT candidate on the complete octave;
2. independent chunked-dense nominal action;
3. exact-vs-LDDD scalar inflation using the public caps;
4. 1000x adversarial stress on the complete residual budget;
5. residual-to-solution control from the promoted coercive interface;
6. exact Abel telescope;
7. conservative (|C_D|le4.4).

The complete octave has

[
N=64000,qquad J=32000.
]

The FFT residuals are

[
6.547661940330939	imes10^{-16}
quad(e),
]

[
6.629977871120033	imes10^{-16}
quad(o).
]

The unstressed exact-source residual budgets are

[
4.478485634978021	imes10^{-13}
quad(e),
]

[
4.654918170196006	imes10^{-13}
quad(o).
]

After a full (1000	imes) adversarial inflation:

[
4.478485634978021	imes10^{-10}
quad(e),
]

[
4.654918170196006	imes10^{-10}
quad(o),
]

both remain below the public per-sector cap

[
10^{-9}.
]

---

## 3. Partial-sum and Abel certificate

Using the same vectors whose residuals are certified,

[
S_{max}^{m cand}
=
7.713871718319237	imes10^{-6}.
]

After the public solution-error inflation,

[
oxed{
S_{max}^{m out}
=
8.071642594719202	imes10^{-6}.
}
]

The exact Abel coefficient again telescopes to

[
rac1{64001}.
]

The resulting linear inner-product charge is

[
1.2611744495741006	imes10^{-10}.
]

The conservative rank-one charge is

[
6.714181883223381	imes10^{-11}.
]

Hence

[
oxed{
|Q_{m bare}^{64k	o128k}|
le
1.932592637896439	imes10^{-10}.
}
]

Against the public target

[
10^{-8},
]

the headroom is

[
oxed{
51.74396199131059	imes.
}
]

All fail-closed checks pass.

---

## 4. Relation to the current exact-Schur program

This entry does **not** identify the bare octave certificate with the full exact-Schur infinite correction.

The exact finite-Schur scalar program remains separate:

[
Q_R
=
K_{e,R}^{m fin}
-
K_{o,R}^{m fin}
-
C_SK_{o,R}^{m fin}K_{e,R}^{m fin}.
]

Lane A has launched the finite-128k paired-Schur K replay. Once complete,

[
K_{p,128k}^{m fin}
-
K_{p,64k}^{m fin}
]

will give the exact finite octave payload requested in v14.113/v14.114.

The post-128k infinite correction must then use the corrected v14.114 frozen-front architecture:

[
128k<n<256k
quad	ext{exact/correlated},
]

[
nge256k
quad	ext{K=10}.
]

No finite-octave stabilization is used to infer the infinite sign.

---

## 5. Verdict

[
oxed{
	ext{Public scalar exactness envelopes survive every new mode through }128k.
}
]

[
oxed{
|Q_{m bare}^{64k	o128k}|
le
1.932592637896439	imes10^{-10}
<10^{-8},
}
]

with (51.74	imes) headroom and a 1000x residual stress already absorbed.

These are proposed for independent audit/promotion.

---

HANDOFF
target: external-audit
type: through-128k-audit
parent: v14.115
status: open
action: Independently rerun the 64k<n<=128k scalar interval transport in both parities and the complete N=64000 bare full-near outward QF certificate. Verify the public scalar-cap interfaces, the 1000x residual stress, the exact Abel telescope to 1/64001, and the final bound |Q_bare|<=1.932592637896439e-10. If all pass, promote these finite-octave statements only.
deliverable: theorem-or-obstruction
constraints: Do not infer the infinite tail from this finite octave. Preserve the v14.114 correction: K=10 is not to be applied to the post-elimination 128k boundary residual without the frozen-front 128k/256k split.
