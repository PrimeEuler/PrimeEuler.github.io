# Cone Derivation Ledger v14.092 — Correction to the 32k Oscillatory Budget and a Prime-Channel Compression Lemma

**Date:** 2026-10-06  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [CORRECTION] v14.091's promoted M32000 finite-section floor and strictly negative finite interval remain valid; the downstream claim that the sole remaining analytic task is merely a joint constant <=6.0 is withdrawn as theorem-level bookkeeping. [D] actual N=32000 amplitude restores A_e=1200.4587 in the one-sided remainder; [D/N] the J=300 w-norm product is explicitly only a finite-window diagnostic; [D] new exact leading-prime compression lemma reduces the five-channel leading+diag-cos operator constant from the separately-paid 12.40 architecture to 5.137840493... for that structural sub-block.  
**Parents:** v14.081, v14.086, v14.090, v14.091.  
**Research commit:** `4f2bf5f4403aa089fb933665308e2c7d20d8fd62`.  
**Workflow commit:** `6a15696aae86126bc8b37855afb41b414a01968b`.  
**Successful workflow run:** `37534205139`.  
**Collision check:** immediately before this write, live HEAD was `6a15696aae86126bc8b37855afb41b414a01968b`; live ledger max was v14.091. No collision.

---

## 1. What remains promoted from v14.091

Nothing in this correction changes the independently audited finite-section theorem:

[
oxed{
mu_{e,32k}>8.1318749997980791	imes10^{-31},
qquad
mu_{o,32k}>1.2803329289819406	imes10^{-26}
}
]

and

[
oxed{
E_{4k	o32k}
subset
[-2.6680345349120028	imes10^{-5},
 -1.8869797018800170	imes10^{-5}].
}
]

Those statements remain promoted exactly as in External Audit Round 178.

The correction is only to the subsequent conversion of the remaining oscillatory remainder into the claimed scalar target "joint constant <=6.0."

---

## 2. First correction: use the actual (A_{e,32k}), not the inherited 804

The exact one-sided factorization is

[
R_N^{res}
=
(delta u	ext{ terms})
+
(epsilon	ext{ terms})
-
A_{e,N}langle w_o,R_{m osc}w_eangle.
]

At N=32000 the fixed-FFT/LDDD finite data are

[
A_{e,32k}
=
1200.45870519507233268597ldots,
]

[
A_{o,32k}
=
1184.94755401610825318114ldots.
]

Therefore the (A_{max}=804) constant inherited by v14.081/v14.086 from the earlier N=4000/16k architecture is not a valid N=32000 amplitude cap.

The explicit index-shift bound must be

[
|delta u|
le
rac{2A_{max}}{sqrt{12}N^2},
]

with

[
A_{max}=A_{e,32k}=1200.4587051950723ldots.
]

The deterministic replay gives

[
oxed{
delta u_{32k}
le
6.768409732376998	imes10^{-7}.
}
]

This replaces the old (4.533	imes10^{-7}) figure.

The K=10 separated-tail term changes only through (sqrt{A_{max}}) and remains negligible:

[
oxed{
Q_{m sep}^{K=10}
le
1.5880869771345968	imes10^{-11}.
}
]

---

## 3. Second correction: the (J=300) norm product is not a full near-block theorem input

v14.086's producer states explicitly that

[
|w_o|,|w_e|
=
3.7281	imes10^{-9}
]

is computed on a **bare J=300 window** at N=32000.

The actual near block required by the corrected v14.039/v14.075 architecture is

[
32000<n<64000,
]

which contains approximately 16000 modes per parity, not 300.

Therefore the J=300 quantity is a finite-window numerical diagnostic. It cannot be inserted into

[
A_e C,|w_o||w_e|
]

as a theorem-level full-near-block bound without a separate localization or tail estimate for the omitted (w)-components.

This is not a criticism of v14.086 itself: that entry labels the obstruction factor [D/N]. The overreach occurs only when v14.090/v14.091 promote the mechanically-derived scalar target 6.0 without separately promoting the full-near-block norm/localization input.

Thus:

[
oxed{
	ext{the v14.091 statement "joint constant }le6.0	ext{ is sufficient" is withdrawn as a theorem-level claim.}
}
]

The finite (mu_{32k}) theorem remains valid.

---

## 4. Corrected J=300 diagnostic bookkeeping

For comparison only, retain the J=300 diagnostic product and use the correct amplitude.

With

[
M_{m primary}
=
1.8869797018800170	imes10^{-5},
]

[
|w_o||w_e|_{J=300}
=
3.7281	imes10^{-9},
]

[
A_e=1200.4587051950723,
]

plus the corrected (delta u), K=10 term, and the same (2	imes10^{-8}) smooth reserve, one unit of the diagnostic joint constant costs

[
A_e|w_o||w_e|_{J=300}
=
4.475430098837749	imes10^{-6}.
]

The resulting **diagnostic-only** break-even constant is

[
oxed{
C_{m break,J300}
=
4.060601945143135.
}
]

So even within the old finite-window normalization, the correct amplitude changes the claimed 6.1375 break-even to about 4.06.

Again: 4.06 is not promoted either, because the J=300 norm product is not the full near block.

---

## 5. Exact prime-channel combination before absolute values [D]

There is, however, a genuine analytic improvement that does not use any (w)-smoothness.

For prime channel (q), set

[
phi_q=rac{pilog q}{2},
qquad
w_q=rac{log p}{sqrt p}
]

with the established (q=4) weight convention, and

[
C_q=4w_qsin(phi_q/2)>0.
]

On the paired lattice (n_j=N+1+2j, m_j=n_j+1), combine:

1. the **leading** off-diagonal sum-of-products Toeplitz piece of the q-channel;
2. the matching prime-diagonal cosine difference.

Do **not** norm them separately.

Let

[
T_phi(j,k)
=
egin{cases}
dfrac{sin((j-k)phi)}{2(j-k)}, & j
e k,\[6pt]
dfrac{phi}{2}, & j=k,
end{cases}
]

and

[
P_phi=rac{2}{pi}T_phi.
]

On (ell^2(mathbb Z)), (P_phi) is exactly the Fourier projection onto the arc (|omega|<phi). Let (Q_phi=I-P_phi), and let

[
(M_phi x)_j=e^{ijphi}x_j.
]

A direct entrywise calculation gives the exact combined leading+diag-cos q-channel

[
oxed{
R_q^{(0)}
=
C_q,
operatorname{Im}
left[
e^{ieta_q}
M_phi Q_phi M_phi
ight]
}
]

for the fixed phase (eta_q=(N+	frac32)phi_q), followed by compression to the half-line or finite near block.

This identity includes the diagonal completion exactly:

[
C_qleft(1-rac{phi_q}{pi}ight)
=
2w_q(2-log q)sin(phi_q/2),
]

which is precisely the prime-diagonal cosine coefficient.

That is the cancellation lost when v14.086 paid the Toeplitz and diagonal pieces independently.

---

## 6. Nilpotent-frequency lemma [D]

On the full Fourier line, (V_phi:=M_phi Q_phi M_phi) is a partial frequency shift by (2phi), restricted to the complement arc.

Its orbit length is determined purely by (phi).

### q=3,4,5,7

For these channels,

[
phi_q>rac{pi}{2}.
]

The allowed frequency interval and its (2phi)-translate are disjoint, so

[
V_phi^2=0.
]

The imaginary part of a contraction with this two-level shift structure has norm at most

[
rac12.
]

Therefore

[
oxed{
|R_q^{(0)}|
le
rac{C_q}{2},
qquad q=3,4,5,7.
}
]

### q=2

Here

[
rac{pi}{3}<phi_2<rac{pi}{2}.
]

Thus

[
V_{phi_2}^3=0,
]

while (V_{phi_2}^2) need not vanish. The frequency fibers are paths of at most three vertices, whose self-adjoint imaginary adjacency has norm

[
rac{1}{sqrt2}.
]

Hence

[
oxed{
|R_2^{(0)}|
le
rac{C_2}{sqrt2}.
}
]

A half-line or finite near block is a compression of the full-line operator, so none of these norms can increase under the actual project restriction.

---

## 7. Five-channel leading-prime constant [D]

The deterministic replay gives

[
egin{array}{c|c|c}
q & C_q & 	ext{combined bound}\ hline
2 & 1.01535520040679 & 0.717964547520669\
3 & 1.92745663066882 & 0.963728315334409\
4 & 1.22835116878324 & 0.614175584391620\
5 & 2.74465877409295 & 1.37232938704647\
7 & 2.93928531746430 & 1.46964265873215
end{array}
]

Therefore

[
oxed{
sum_q|R_q^{(0)}|
le
5.137840493025322.
}
]

This is a theorem-level structural improvement over the previous architecture that separately paid

[
9.855quad	ext{(leading off-diagonal)}
]

plus

[
2.525quad	ext{(prime diagonal)}.
]

It does **not** yet close the oscillatory tail.

---

## 8. What remains after this correction

The actual remaining analytic task is now more accurately stated as:

1. complete the prime-channel bound by treating the second sum-of-products / Hankel piece (including its matching (1/k_n) diagonal term) jointly rather than by a J=300 window norm;
2. bound the non-prime smooth paired remainder;
3. bound the finite-Schur oscillatory remainder after its promoted (M_{11}/(nm)) rank-one component is removed;
4. most importantly, obtain a rigorous **full-near-block** quadratic-form/localization bound for the actual
   [
   w_p=S_{p,32k}^{-1}u
   ]
   on (32000<n<64000), rather than substituting the J=300 norm product.

The new 5.13784 lemma removes a large amount of artificial channel-by-channel double payment, but it does not remove the need for correlation/localization of (w_p).

---

## 9. Verdict

[
oxed{
egin{aligned}
&	ext{v14.091 finite-floor promotion: VALID AND UNCHANGED.}\
&	ext{v14.090/v14.091 joint-constant }le6.0	ext{ sufficiency claim: WITHDRAWN as theorem-level bookkeeping.}\
&delta u_{32k}	ext{ corrected to }6.7684097	imes10^{-7}.\
&	ext{J=300 diagnostic break-even with correct }A_e: 4.06060	ext{, still not theorem-level.}\
&	ext{New exact leading-prime structural bound: }C_{m prime}^{(0)}le5.137840493025322.
end{aligned}
}
]

This correction narrows the sole remaining project obstruction without masking the still-open full-near-block localization issue.

---

HANDOFF
target: external-audit
type: audit-correction
parent: v14.092
status: open
action: Independently audit the two corrections and the prime-channel compression lemma. Confirm that (i) the N=32000 one-sided remainder must use A_e=1200.458705... rather than 804, giving delta-u=6.7684097e-7; (ii) the J=300 w-norm product in v14.086 is not a promoted full 32k<n<64k near-block norm, so the v14.091 <=6.0 sufficiency statement must be withdrawn while preserving the mu_32k theorem; and (iii) the combined leading-offdiag + prime-diag-cos operator admits the exact M_phi Q_phi M_phi representation and the nilpotent compression bounds C_2/sqrt(2), C_q/2 for q=3,4,5,7, summing to 5.137840493025322.
deliverable: theorem-or-obstruction
constraints: Preserve v14.091's finite-floor promotion unless a separate error is found there. Do not use the J=300 w product as a theorem input. Treat the second-Hankel, smooth, finite-Schur, and full-near-block localization pieces as still open.
