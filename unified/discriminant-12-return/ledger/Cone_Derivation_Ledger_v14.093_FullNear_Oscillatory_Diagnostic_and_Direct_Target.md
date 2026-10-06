# Cone Derivation Ledger v14.093 — Full-Near 32k Oscillatory Diagnostic and Direct Quadratic-Form Target

**Date:** 2026-10-06  
**Track:** Lane A / one-sided 32k tail closure  
**Status:** [N] full 32000<n<=64000 bare-near FFT solve replaces the misleading J=300 scale diagnostic; [D] corrected direct theorem target for the full oscillatory quadratic form; [O] analytic proof still required, including finite-Schur oscillatory remainder.  
**Parents:** v14.081, v14.086, v14.091, v14.092.  
**Research commit:** `181794d9678afef6f8614cf488af29a8064bdd86`.  
**Workflow commit:** `d5b56919af19da51262cb726452e93101c95952d`.  
**Successful workflow run:** `37534615235`.  
**Collision check:** immediately before this write, live HEAD was `d5b56919af19da51262cb726452e93101c95952d`; live ledger max was v14.092. No collision.

---

## 1. Purpose

v14.092 identified that the J=300 quantity

[
|w_o||w_e|=3.7281	imes10^{-9}
]

used in v14.086/v14.090 was only a small finite window, whereas the actual exact-near block required by the corrected near/far split is

[
32000<nle64000,
]

approximately 16000 modes per parity.

This entry performs the missing full-near numerical diagnostic using the validated FFT raw operator. It is **not theorem evidence**; its purpose is to establish the correct scale and define a theorem target that does not depend on a finite-window norm product.

---

## 2. Producer architecture [N]

For each prefix J in

[
J=300, 1000, 4000, 16000,
]

solve the paired bare systems

[
T_e w_e=u,
qquad
T_o w_o=u,
]

with

[
u_j=rac1{n_j},
qquad
n_j=32001+2j,
qquad
m_j=n_j+1.
]

The FFT Toeplitz/Hankel matvec is the already-validated source-faithful raw operator used in the remote-FFT diagnostics.

Then evaluate

[
R_{m osc}^{b}
=
T_o-T_e-C_D,uotimes u
]

and

[
Q_J
=
langle w_o,R_{m osc}^{b}w_eangle.
]

Guardrail: this is the bare finite-near compression. It does not yet include the exact infinite remote Schur correction or an outward interval enclosure.

---

## 3. Window growth: the J=300 norm product was not representative [N]

The replay gives

[
egin{array}{c|c}
J & |w_o||w_e| \ hline
300 & 3.728139765262007	imes10^{-9}\
1000 & 1.188043563286429	imes10^{-8}\
4000 & 4.004839741420045	imes10^{-8}\
16000 & 9.821616392901328	imes10^{-8}
end{array}
]

Therefore

[
oxed{
rac{|w_o||w_e|_{J=16000}}
{|w_o||w_e|_{J=300}}
approx 26.34.
}
]

This confirms v14.092's correction: the J=300 norm product cannot be used as a theorem-level full-near-block input.

---

## 4. The important good news: the correlated quadratic form stays tiny [N]

Despite the 26x growth in the norm product, the direct bare oscillatory quadratic form remains at the (10^{-10}) scale:

[
egin{array}{c|c|c}
J & Q_J & A_e|Q_J|/M_{m primary}\ hline
300
& +1.0131429010354474	imes10^{-10}
& 0.0064454\
1000
& -2.1363660209616257	imes10^{-11}
& 0.0013591\
4000
& +8.219966554726290	imes10^{-11}
& 0.0052294\
16000
& -3.3262808537969117	imes10^{-10}
& 0.0211611
end{array}
]

At the full near block,

[
oxed{
Q_{16000}^{m bare}
=
-3.3262808537969117	imes10^{-10}.
}
]

Using the correct

[
A_{e,32k}=1200.4587051950723,
]

the scaled cost is

[
oxed{
A_e|Q_{16000}^{m bare}|
=
3.9930628068642004	imes10^{-7},
}
]

only

[
oxed{
2.116%
}
]

of the promoted primary finite margin.

Thus the J=300 issue changes the norm-product story dramatically but **does not destroy the actual correlated cancellation**.

---

## 5. Effective constant confirms that normwise bounds are the wrong metric [N]

Define for diagnostic purposes

[
C_{m eff}(J)
=
rac{|Q_J|}
{|w_o||w_e|}.
]

The replay gives

[
egin{array}{c|c}
J & C_{m eff}(J)\ hline
300 & 2.71756	imes10^{-2}\
1000 & 1.79822	imes10^{-3}\
4000 & 2.05251	imes10^{-3}\
16000 & 3.38669	imes10^{-3}
end{array}
]

At the full near block the true bare effective constant is approximately

[
3.39	imes10^{-3},
]

orders of magnitude below both the old 12.40 bound and the new structural 5.13784 leading-prime operator constant.

The theorem therefore has to preserve the correlated quadratic form. Replacing it by a global operator norm times full-near norms is far too lossy.

---

## 6. Correct direct theorem target [D]

From v14.091/v14.092, retain the promoted primary finite margin

[
M_{m primary}
=
1.8869797018800170	imes10^{-5}.
]

Use the corrected index-shift charge

[
delta u
le
6.768409732376998	imes10^{-7},
]

the corrected K=10 separated-tail term

[
Q_{m sep}^{K=10}
le
1.5880869771345968	imes10^{-11},
]

and retain the deliberately conservative smooth tail-cost reserve

[
R_{m smooth}^{m cost}
le
2	imes10^{-8}.
]

The exact one-sided tail closes if

[
A_{e,32k}
,
|langle w_o,R_{m osc}w_eangle|
<
M_{m primary}
-delta u
-Q_{m sep}^{K=10}
-R_{m smooth}^{m cost}.
]

Therefore a sufficient direct quadratic-form theorem is

[
oxed{
|langle w_o,R_{m osc}w_eangle|
le
1.5138330111688126	imes10^{-8}.
}
]

A cleaner public target is

[
oxed{
|langle w_o,R_{m osc}w_eangle|
le
10^{-8}.
}
]

This leaves additional reserve.

The full-near bare midpoint value is smaller than the public target by a factor

[
rac{10^{-8}}{3.3263	imes10^{-10}}
approx30.1,
]

and smaller than the exact break-even target by about

[
45.5	imes.
]

So the remaining theorem need not reproduce the numerical cancellation sharply.

---

## 7. What must be proved

The remaining analytic lemma should now be stated **directly**:

> **Full-near oscillatory quadratic-form lemma.** For the exact paired remote Schur resolvents at N=32000,
> [
> |langle w_o,R_{m osc}w_eangle|
> le10^{-8}.
> ]

The proof must cover:

1. the exact near block (32000<n<64000), not a J=300 prefix;
2. the combined prime structure, for which v14.092 already gives the exact leading+diag-cos compression reduction;
3. the second/Hankel prime pieces;
4. the non-prime smooth remainder;
5. the finite-Schur oscillatory remainder after the promoted (M_{11}/(nm)) rank-one term is removed;
6. the difference between the bare-near diagnostic vectors and the exact full remote Schur vectors.

This direct target supersedes the misleading scalar "joint constant <=6.0" formulation.

---

## 8. Verdict

The full-near diagnostic resolves the scale ambiguity:

[
oxed{
|w_o||w_e|_{J=16000}
approx26.3	imes
|w_o||w_e|_{J=300},
}
]

but

[
oxed{
A_e|langle w_o,R_{m osc}^b w_eangle|_{m full near}
approx3.99	imes10^{-7},
}
]

only (2.12%) of the promoted finite margin.

Therefore the project remains numerically very comfortably inside the closure regime. The missing item is purely a **rigorous direct correlation bound**, with a public target (10^{-8}) and about 30x numerical headroom on the bare full-near block.

---

HANDOFF
target: sandbox
type: analytic-lemma-correction
parent: v14.093
status: open
action: Replace the v14.086/v14.090 finite-window joint-constant target by a direct full-near quadratic-form target. Prove, for the exact N=32000 paired remote Schur problem, |<w_o,R_osc w_e>| <= 1e-8 (break-even 1.513833e-8). Use the v14.092 combined-prime compression lemma as a structural input. The full-near bare FFT diagnostic at J=16000 is -3.32628e-10, giving ~30x headroom to the public target.
deliverable: theorem-or-obstruction
constraints: Do not use the J=300 norm product as a theorem input. Cover the full 32000<n<64000 near block, preserve prime-channel correlation before norms, and account separately for second/Hankel, smooth, finite-Schur oscillatory, and exact-vs-bare-resolvent corrections.
