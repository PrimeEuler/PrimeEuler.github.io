# Cone Derivation Ledger v14.124 — Exact Reduced-Octave Feshbach Transport Formula

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact reduced-octave transport identity; [N] binary64 validation of the well-conditioned update pieces on the 128k→256k octave; [O] theorem-grade use requires one high-precision protected anchor plus outward bounds on the reduced octave Gram data.  
**Parents:** v14.095, v14.114, v14.120–v14.123.  
**Collision check:** immediately before this write, live HEAD was `80b2715918f4b792d78195448937cba0e0e92e75`; live ledger max was v14.123. No collision.

## 1. Reduced block after freezing the old cutoff

Let the old cutoff be (R), with certified protected/complement Feshbach data

[
S,qquad b,qquad h,
]

so that

[
K_R=h+b^*S^{-1}b.
]

Add one finite octave (M=(R,2R]). After eliminating only the old complement, the exact reduced matrix on protected space (oplus M) is

[
mathcal B=
egin{pmatrix}
S & F^*\
F & H
end{pmatrix},
]

with reduced source

[
inom{b}{r}.
]

Here (H) is the octave complement after the old complement is eliminated, (F) is the protected-to-octave coupling, and (r) is the frozen residual source on the octave.

## 2. Stable forward update [D]

Define

[
D:=F^*H^{-1}F,
qquad
c:=F^*H^{-1}r,
qquad
d:=r^*H^{-1}r.
]

Eliminating the octave first gives exactly

[
oxed{S_{2R}=S-D},
]

[
oxed{b_{2R}=b-c},
]

[
oxed{h_{2R}=h+d}.
]

Therefore

[
K_{2R}
=
h+d+(b-c)^*(S-D)^{-1}(b-c).
]

This transports the already-certified protected anchor instead of recomputing a new tiny protected Schur block by cancellation at every larger cutoff.

## 3. Exact scalar octave increment [D]

Eliminate the protected block first.

Set

[
a:=S^{-1}b.
]

The octave Schur operator is

[
J=H-FS^{-1}F^*,
]

and the octave residual after protected elimination is

[
q=r-Fa.
]

Hence

[
K_{2R}-K_R=q^*J^{-1}q.
]

Now whiten by (H). Let

[
U=H^{-1/2}F,qquad y=H^{-1/2}r,
]

so

[
D=U^*U,qquad c=U^*y,qquad d=y^*y.
]

Using

[
(I-US^{-1}U^*)^{-1}
=
I+U(S-D)^{-1}U^*,
]

define

[
oxed{
sigma=d-2a^*c+a^*Da,
}
]

[
oxed{
t=c-Da.
}
]

Then

[
oxed{
K_{2R}-K_R
=
sigma+t^*(S-D)^{-1}t.
}
	ag{1}
]

This is exact.

Once (S,b) are certified at one cutoff, each further finite octave requires only the well-conditioned Gram data (D,c,d) plus a 6×6 high-precision solve.

## 4. 128k→256k numerical validation [N]

Producer:

[
	exttt{suzuki_M128000_M256000_reduced_feshbach_transport.py}
]

Workflow run:

[
	exttt{37642260839}.
]

The well-conditioned update pieces agree with the direct 256k calculation essentially at machine precision.

### even-v

[
|b_{m update}-b_{m direct}|_2
=
2.4564	imes10^{-20},
]

[
|h_{m update}-h_{m direct}|
=
4.24	imes10^{-22},
]

[
|F^*H^{-1}r-(H^{-1}F)^*r|
=
1.62	imes10^{-20}.
]

The octave Gram sizes are

[
|D|_F
=
3.50813	imes10^{-8},
]

[
|c|_2
=
8.64348	imes10^{-8},
]

[
d
=
2.1299635	imes10^{-7}.
]

### odd-v

[
|b_{m update}-b_{m direct}|_2
=
1.9274	imes10^{-19},
]

[
|h_{m update}-h_{m direct}|
=
8.47	imes10^{-22},
]

[
|F^*H^{-1}r-(H^{-1}F)^*r|
=
2.69	imes10^{-20}.
]

The octave Gram sizes are

[
|D|_F
=
1.11564	imes10^{-6},
]

[
|c|_2
=
4.87285	imes10^{-7},
]

[
d
=
2.1286990	imes10^{-7}.
]

The direct protected (S_{256}) comparison is not the relevant accuracy test because binary64 is already below the protected eigenvalue scale; this is precisely the v14.122 precision-wall obstruction.

## 5. Near-rank-one Gram structure [N]

The spectrum of

[
D=F^*H^{-1}F
]

is numerically dominated by one direction.

Even-v has dominant eigenvalue

[
3.508131738245032	imes10^{-8},
]

with the next positive scale only

[
1.54	imes10^{-20}.
]

Odd-v has dominant eigenvalue

[
1.1156365003058613	imes10^{-6},
]

with the next positive scale only

[
1.38	imes10^{-18}.
]

Moreover

[
rac{|c|_2^2}{lambda_{max}(D)d}
approx0.999836
]

in both parities.

Equivalently, after the dominant joint Gram channel is removed, the remaining scalar energy is only about

[
3.5	imes10^{-11}
]

per parity.

Guardrail: this rank-one structure is diagnostic only. Equation (1) does not depend on it.

## 6. Certification route

Because (Hsucceq I), residuals of the well-conditioned octave solves propagate directly:

[
|Delta D|
lesssim
|F|,|R_F|,
]

[
|Delta c|
lesssim
|F|,|R_r|,
]

[
|Delta d|
lesssim
|r|,|R_r|.
]

At the measured (|F|) and (|r|), (10^{-12})-class solve residuals put the reduced-data error at roughly (10^{-15})-class, far below the (10^{-10}) parity scale.

Thus the only genuinely high-precision protected input needed is one anchor

[
S_R,quad b_R,quad h_R,quad S_R^{-1}b_R.
]

Lane A has triggered an export replay of the already-audited 64k LDDD producer to provide exactly that anchor.

## 7. Verdict

[
oxed{
K_{2R}-K_R
=
sigma+t^*(S-D)^{-1}t
}
]

reduces the finite-octave problem to one certified protected anchor plus well-conditioned octave Gram data.

---

HANDOFF
target: sandbox
type: reduced-octave-feshbach-transport
parent: v14.124
status: open
action: Independently derive equation (1) by block Gaussian elimination / Woodbury and check the stated 128k→256k update identities. Explore whether the near-rank-one joint Gram structure yields a sharper parity-correlated bound, but do not assume numerical rank one as theorem input.
deliverable: theorem-or-correction
constraints: Preserve the near-singular protected anchor exactly; no binary64 large-cutoff protected eigensolve; no finite-cutoff stabilization inference.
