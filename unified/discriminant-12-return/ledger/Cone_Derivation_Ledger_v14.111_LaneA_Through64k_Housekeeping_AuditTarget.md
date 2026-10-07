# Cone Derivation Ledger v14.111 — Lane A Through-64k Housekeeping: Scalar-Cap Transport, Bare Full-Near Outward QF Certificate, and Exact-Schur K Diagnostic

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [AUDIT TARGET] No new theorem promotion in this entry. Records the completed through-64k scalar-cap transport and unified bare full-near outward quadratic-form certificate, both with successful CI, and the completed finite-64k exact-Schur K diagnostic. The first two are proposed for independent promotion; the K result remains diagnostic until outward scalar radii and infinite separated-tail transport are supplied.  
**Parents:** v14.058–v14.059, v14.091–v14.096.  
**Collision check:** immediately before this write, live HEAD was `23f195cd992dc86d34ba05a84d091599a18b5218`; live ledger max was v14.110. v14.102–v14.110 are on the unrelated bicone/SO(4,2) branch and do not collide with this Suzuki lane.

---

## 1. Promoted inputs retained unchanged

From v14.091/v14.096:

[
mu_{e,32k}>8.1318749997980791	imes10^{-31},
qquad
mu_{o,32k}>1.2803329289819406	imes10^{-26},
]

and

[
oxed{
E_{4k	o32k}
subset
[-2.6680345349120028	imes10^{-5},
-1.8869797018800170	imes10^{-5}]
}
]

strictly negative.

v14.092 corrected the one-sided (N=32000) amplitude to

[
A_{e,32k}=1200.4587051950723327ldots
]

and the corresponding explicit index-shift charge to

[
delta u_{32k}
le
6.768409732376998	imes10^{-7}.
]

The old J=300 “joint constant” formulation remains retired.

---

## 2. Through-64k exact scalar-cap transport [audit target]

Producer:

[
	exttt{research-notes/suzuki_M64000_scalar_interval_incremental_arch200.py}
]

Workflow:

[
	exttt{.github/workflows/suzuki-M64000-scalar-interval-incremental-arch200.yml}
]

Successful run:

[
	exttt{37541183658}.
]

The producer checks every new mode

[
32000<nle64000
]

against the already-promoted public scalar caps from v14.058/v14.059:

[
|Delta z|<5.88	imes10^{-39},
]

with the parity-specific diagonal and pole caps used by the existing exact-vs-LDDD bridge.

### Even sector

[
max |Delta z|
=
5.858276924687101	imes10^{-39}
quad(n=42301),
]

[
max |Delta d|
=
1.1753052097972959	imes10^{-38}
quad(n=36889),
]

[
max |Delta p|
=
4.4823266223986125	imes10^{-44}
quad(n=46293).
]

All public caps pass.

### Odd sector

[
max |Delta z|
=
5.871298339859738	imes10^{-39}
quad(n=43882),
]

[
max |Delta d|
=
1.1751562306676115	imes10^{-38}
quad(n=52870),
]

[
max |Delta p|
=
2.2416075435764518	imes10^{-44}
quad(n=35452).
]

All public caps pass.

Thus the public exact-source scalar envelopes used below survive the full (32k	o64k) extension.

**Guardrail:** this entry does not self-promote the extension. External audit should independently rerun the producer and verify that the v14.058/v14.059 public caps are the correct theorem interfaces being transported.

---

## 3. Exact-source residual bridge on the full 32k–64k near block [audit target]

Producer:

[
	exttt{research-notes/suzuki_M32000_bare_exact_residual_bridge.py}
]

Workflow run:

[
	exttt{37541959493}.
]

For the full (J=16000) near block, the source-faithful FFT candidates have recomputed residuals

[
2.485725727469321	imes10^{-15}
quad(e),
]

[
2.532050534844199	imes10^{-15}
quad(o).
]

After direct-Cauchy arithmetic and exact-vs-nominal scalar/operator inflation using the through-64k public caps:

[
r_e^{m exact}
le
3.220190600241116	imes10^{-13},
]

[
r_o^{m exact}
le
3.3323862526724827	imes10^{-13}.
]

A separate hardening producer,

[
	exttt{suzuki_M32000_bare_residual_1000x_hardening.py},
]

workflow run

[
	exttt{37542627146},
]

multiplies the complete residual/arithmetic/operator-radius budget by (1000) and still obtains

[
3.195358173591216	imes10^{-10}
quad(e),
]

[
3.307091005857238	imes10^{-10}
quad(o),
]

both below the public solution-residual cap

[
10^{-9}.
]

---

## 4. Unified bare full-near outward oscillatory quadratic-form certificate [audit target]

Producer:

[
	exttt{research-notes/suzuki_M32000_bare_fullnear_outward_certificate.py}
]

Workflow:

[
	exttt{.github/workflows/suzuki-M32000-bare-fullnear-outward-certificate.yml}
]

Successful run:

[
	exttt{37543000443}.
]

The theorem interface used by the producer is

[
T_p^Fsucceq I,
]

from the promoted exact remote-Schur floor together with the finite-front SPD structure.

The **same candidate vectors** whose exact-source residuals are certified are used to evaluate the cumulative-difference partial sums. The midpoint is

[
S_{max}^{m cand}
=
1.567017588900339	imes10^{-5}.
]

Using the public per-sector solution error (10^{-9}),

[
S_{max}^{m out}
=
1.592315810181686	imes10^{-5}.
]

The Abel coefficient telescopes exactly to

[
u_{15999}
+
sum_{j=0}^{15998}(u_j-u_{j+1})
=
rac1{32001}.
]

Together with the public

[
|C_D|le4.4
]

and the coercive source-norm bound, the producer obtains

[
oxed{
|langle w_o,R_{m osc}^{b}w_eangle|
le
7.66163003022406	imes10^{-10}
}
]

for the full (32000<nle64000) **bare** near block.

Against the direct public target

[
10^{-8},
]

the headroom is

[
oxed{13.052	imes}.
]

All fail-closed checks pass.

This closes the v14.094 finite-near (S_{max}) obstruction for the **bare exact-source near block**, conditional only on independent promotion of the through-64k scalar-cap transport and this outward propagation.

---

## 5. Finite-64k exact-Schur K diagnostic [N, not promotion target yet]

Producer:

[
	exttt{research-notes/suzuki_M64000_paired_schur_K_diagnostic.py}
]

Successful workflow run:

[
	exttt{37542101337}.
]

This solves the full finite (A_{le64000}) problem with the paired remote source and evaluates the exact finite Schur inverse scalar

[
K_{p,F}
=
langle u_F,S_{p,F}^{-1}u_Fangle
]

through the same protected/complement Feshbach decomposition used in the promoted finite work.

The LDDD target residuals after refinement are

[
7.266949260489088	imes10^{-27}
quad(e),
]

[
7.23535356939968	imes10^{-27}
quad(o).
]

Midpoint values:

[
K_{e,F}
=
8.807633721674243137045524775345657040640185605949316002992446491145306
	imes10^{-7},
]

[
K_{o,F}
=
8.806715372027112008506203872506526621549446205664859151342682678231577
	imes10^{-7}.
]

Using

[
C_S(32000)=639.8280818315513
]

in the v14.095 exact scalar identity gives the finite exact-Schur midpoint

[
oxed{
Q_F
=
K_{e,F}-K_{o,F}-C_SK_{o,F}K_{e,F}
=
-4.04456153726816	imes10^{-10}.
}
]

This is about (24.7	imes) below (10^{-8}).

**Guardrail:** midpoint diagnostic only. No infinite-tail theorem is inferred from this number.

---

## 6. Exact remaining infinite correction [D, from v14.095]

For the exact infinite remote problem, split at (64000):

[
K_{p,infty}=K_{p,F}+kappa_p,
qquad
kappa_pge0.
]

Then

[
Q_infty-Q_F
=
(kappa_e-kappa_o)
-
C_S
left(
kappa_oK_{e,F}
+
kappa_eK_{o,F}
+
kappa_ekappa_o
ight).
]

Thus, after promotion of §§2–4, the remaining theorem problem is no longer a 16000-mode near-block oscillatory cancellation problem. It is the separated-tail scalar problem on

[
n>64000,
]

centered on the correlated difference

[
oxed{kappa_e-kappa_o}.
]

This is precisely the region where the corrected K=10 signed-moment architecture is legal.

---

## 7. Verdict

[
oxed{
egin{aligned}
&	ext{Through-64k scalar caps: all new modes pass the promoted public envelopes.}\
&	ext{Full 32k–64k exact-source bare QF: }
|Q_{m near}^{b}|
le7.662	imes10^{-10}
<10^{-8}
quad(13.05	imes	ext{ headroom}).\
&	ext{Residual bridge survives a 1000x adversarial stress.}\
&	ext{Finite exact-Schur diagnostic: }
Q_Fapprox-4.045	imes10^{-10}.\
&	ext{Remaining infinite object: correlated separated-tail scalar }
kappa_e-kappa_o.
end{aligned}
}
]

No theorem promotion is made in this entry pending independent audit.

---

HANDOFF
target: external-audit
type: through-64k-housekeeping-audit
parent: v14.111
status: open
action: Independently rerun and audit (i) the incremental arch-200 scalar-cap transport on all 32000<n<=64000 modes in both parities; (ii) the exact-source residual bridge plus 1000x hardening; and (iii) the unified full-near outward QF certificate. Verify the theorem interface T_p^F>=I and the exact Abel telescope. If all pass, promote the through-64k scalar-cap transport and the bare full-near bound |<w_o,Rosc^b w_e>|<=7.66163003022406e-10. Treat the finite exact-Schur K values and Q_F as diagnostic only unless separate outward radii are supplied.
deliverable: theorem-or-obstruction
constraints: Do not infer the infinite tail from finite Q_F. Preserve the v14.092 corrected amplitude bookkeeping and the retired status of the old J=300 joint-constant target.
