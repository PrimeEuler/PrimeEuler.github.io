# Cone Derivation Ledger v13.996 — Sandbox: Graph-Correction Remote-Tail Obstruction and Leading-Moment Gate

**Collision note (external audit):** v13.989 was absent immediately before this entry was first written, but was independently claimed by "External Audit Round 152" (commit `ad5262e`, pushed 2026-10-04T00:08:05Z), which this entry's own commit (`d32f098`, 2026-10-04T00:34:56Z) postdates. Per the standing collision protocol, the earlier commit keeps the contested number; this entry has therefore been renumbered v13.989→v13.996 by the external audit thread (filename and this header only — no mathematical content changed). `v13.990`, `v13.992`, and `v13.995`, written after this entry under its original v13.989 label, have had their references updated to v13.996 accordingly.

**Date:** 2026-10-03  
**Track:** Sandbox / no-twist Suzuki Xi scalar certification lane  
**Status:** [N] apples-to-apples CI replay of the v13.988 first graph correction; [N] one fresh remote-shell extension to mode 24001/24002; [D] exact signed (1/n) residual coefficient; [I] finite graph correction is not the current bottleneck; [I] the persistent remote (1/n) moment is the dominant obstruction; [O] construct a genuine asymptotic remote-tail vector that cancels the leading moment at fixed Ritz value and then re-certify the full residual  
**Authorization:** Jeremy, 2026-10-03 ("yes always check the head before commititing" / continue from v13.987)  
**Parents:** v13.979, v13.987–988; External Audit Round 152  
**Research artifacts:**  
- `research-notes/suzuki_p4_graph_corrected_reritz_replay.py`, commits `4dc6f8cf2e4dabe3a8f963dba9b9a524e7d39098`, `7e93570a289e42f471d41e092cb4e888871481d7`  
- `research-notes/suzuki_p4_graph_remote_shell_extension.py`, commits `f24712f50b2c9f821ca8b316d4d8ffcd12ea0353`, `b12b93866e9ef38966b1d6ea7f48ebf0a39b0c2f`  
**CI:** apples-to-apples run `37164879784`; remote-shell/leading-moment run `37165203400`  
**Collision check:** v13.989 was absent immediately before this write. Live HEAD immediately before the write was `b12b93866e9ef38966b1d6ea7f48ebf0a39b0c2f`.

---

## 0. Purpose

v13.987 established that the direct six-dimensional source-energy interval theorem is noncertifying with the present perturbation budget.

The natural alternative suggested by v13.979 is to improve the numerical four-carrier by the graph correction

[
X=widehat D^{-1}K,
]

whose finite-coordinate realization is the landed v13.988 payload

[
X_R.
]

The present checkpoint asks a narrower and decisive question:

[
oxed{
	extbf{does the landed first graph correction actually reduce the full infinite carrier residual?}
}
]

The answer is **no** at the frozen (16001/16002) support, despite an enormous finite-window improvement.

A fresh remote-shell extension does reduce the global residual by about (15%), but the far-tail bound remains almost entirely a signed (1/n) term.

This identifies the next nonredundant gate.

---

## 1. Same-metric replay of the original and graph-corrected carriers [N]

Use the unchanged v13.974/v13.982 (G_B)-normalized carrier

[
Z
]

and the v13.988 constrained graph correction

[
X_R.
]

Define

[
W=Z-X_R.
]

Both the baseline span (Z) and corrected span (W) were independently:

1. (B)-orthonormalized and Rayleigh-Ritzed through the same frozen mode cutoff;
2. evaluated with the same finite residual norm;
3. charged with the same explicit remote rows through two million;
4. charged with the same analytic far-tail envelope;
5. converted with the same public smooth-bulk floor.

Thus the comparison below is genuinely apples-to-apples.

### even-v

Baseline:

[
ho_{infty,e}^{(0)}
=
0.030271256399649966.
]

Corrected:

[
ho_{infty,e}^{(1)}
=
0.030452236472744462.
]

Hence

[
oxed{
rac{ho_{infty,e}^{(1)}}{ho_{infty,e}^{(0)}}
=
1.0059786112180196.
}
]

The finite residual, however, changes from

[
2.3229019284684484	imes 10^{-4}
]

to

[
7.707864172358846	imes10^{-8},
]

a factor

[
oxed{
3.31820473257812	imes10^{-4}
}
]

of the baseline.

The explicit remote residual changes from

[
0.0025149520808577528
]

to

[
0.0025398605076735014,
]

slightly **increasing**.

### odd-v

Baseline:

[
ho_{infty,o}^{(0)}
=
0.03134799777329338.
]

Corrected:

[
ho_{infty,o}^{(1)}
=
0.031507092630812986.
]

Hence

[
oxed{
rac{ho_{infty,o}^{(1)}}{ho_{infty,o}^{(0)}}
=
1.0050751202252266.
}
]

The finite residual changes from

[
0.0012128220709311612
]

to

[
1.413565514083021	imes10^{-5},
]

a factor

[
oxed{
0.011655176368927192
}
]

of the baseline.

Again the explicit remote residual increases slightly:

[
0.012941517901241631
	o
0.01305943935851346.
]

Therefore

[
oxed{
	extbf{the landed }X_R	extbf{ correction almost annihilates the finite residual but does not improve the full infinite residual.}
}
]

This is not a contradiction with v13.979: the ideal graph theorem uses the exact infinite complement action, whereas the landed finite-support KKT correction carries a separately certified remote residual.

---

## 2. One fresh remote-shell completion [N]

To attack the actual obstruction rather than repeat the finite KKT solve, extend the corrected/re-Ritzed carrier through one fresh structured graph shell:

### even-v

[
16003le nle24001,
]

### odd-v

[
16004le nle24002.
]

The shell dimension is (4000) in each parity.

After the shell solve and a fresh re-Ritz step, the full infinite transformed residual caps become

[
oxed{
ho_{infty,e}^{(M3)}
=
0.025874717478907214,
}
]

[
oxed{
ho_{infty,o}^{(M3)}
=
0.026774034166674513.
}
]

Relative to the (M2) corrected carrier,

[
oxed{
rac{ho_{infty,e}^{(M3)}}{ho_{infty,e}^{(M2)}}
=
0.8496820094663903,
}
]

[
oxed{
rac{ho_{infty,o}^{(M3)}}{ho_{infty,o}^{(M2)}}
=
0.8497780001602026.
}
]

So one remote shell buys a real but modest

[
oxed{
approx15%
}
]

global improvement in both parity sectors.

The explicit remote residual falls by essentially the same factor:

[
0.832505571015507
quad	ext{(even)},
]

[
0.8325565042344726
quad	ext{(odd)}.
]

However, the analytic far-tail bound changes in the wrong direction:

[
0.00023446026606552107
	o
0.00023939288908598179
]

in even-v, and

[
0.0012059859128289066
	o
0.0012313665160483581
]

in odd-v.

Thus merely moving the finite cutoff outward is not removing the asymptotic obstruction.

---

## 3. Exact leading remote coefficient [D]

For one finite-support generalized-Ritz column (q) with Ritz value (	heta), the source-faithful remote residual has expansion

[
(Aq-Bq,	heta)_n
=
rac{mathcal L_	heta(q)}{n}
+
O(n^{-2}).
]

The exact signed leading coefficient is

[
oxed{
mathcal L_	heta(q)
=
-rac{2}{pi}langle z,qangle
+
alpharac{4g}{pi}langle p,qangle
+
	hetalanglemathbf 1,qangle,
}
]

where

[
g=
egin{cases}
cosh(1/2),&	ext{even-v},\
sinh(1/2),&	ext{odd-v},
end{cases}
]

and (p,alpha) are the exact parity pole vector/coefficient.

This formula is obtained by combining the leading remote term of the exact off-diagonal (A) action with

[
-	heta Bq
=
+	hetarac{sum_m q_m}{n}
+
O(n^{-2}).
]

Therefore, if

[
mathcal L_	heta(q)
e0,
]

the remote (ell^2) residual decays only at the algebraic scale

[
oxed{
|r_{ge N}|_2
=
O(N^{-1/2}).
}
]

If the leading moment is canceled,

[
mathcal L_	heta(q)=0,
]

then the residual starts at (O(n^{-2})), giving

[
oxed{
|r_{ge N}|_2
=
O(N^{-3/2}).
}
]

This is the asymptotic acceleration now required.

---

## 4. The far bound is almost purely the (1/n) term [N/D]

For the (M3) shell-extended carrier, the leading coefficient norms are

[
oxed{
|mathcal L_e|_2
=
0.47769421503801085,
}
]

[
oxed{
|mathcal L_o|_2
=
2.4573371937903294.
}
]

At the two-million far-tail cutoff, the leading term alone contributes the bounds

[
0.00023884716723068529
]

and

[
0.0012286685968945503.
]

Compare with the full far bounds

[
0.00023939288908598179
]

and

[
0.0012313665160483581.
]

Hence the fractions are

[
oxed{
0.9977203923751449
}
]

for even-v and

[
oxed{
0.9978090039653946
}
]

for odd-v.

So more than (99.7%) of the current far-tail bound is exactly the explicit (1/n) moment.

This is the dominant asymptotic obstruction.

---

## 5. Ritz-value retuning cannot cure the dominant channel [N/I]

For a fixed finite vector (q), one may formally cancel the leading coefficient by changing only (	heta):

[
	heta_{m cancel}
=
rac{
(2/pi)langle z,qangle
-
alpha(4g/pi)langle p,qangle
}{
langlemathbf1,qangle
}.
]

At (M3), the required shifts are:

### even-v

[
oxed{
Delta	heta_e
approx
(
5.77	imes10^{-7},
;
9.62	imes10^{-5},
;
5.73	imes10^{-3},
;
1.5788	imes10^{-1}
).
}
]

### odd-v

[
oxed{
Delta	heta_o
approx
(
1.13	imes10^{-5},
;
1.09	imes10^{-3},
;
4.92	imes10^{-2},
;
5.3017	imes10^{-1}
).
}
]

The fourth-channel shifts required to cancel the dominant leading moment are therefore approximately

[
0.158
]

and

[
0.530,
]

far outside the certified four-channel spectral window

[
|	heta|<0.02.
]

The odd third-channel shift is also outside that window.

Thus

[
oxed{
	extbf{the dominant remote }1/n	extbf{ term cannot be repaired by a small scalar Ritz-value renormalization.}
}
]

A genuine tail-vector correction is required.

---

## 6. Consequence for the graph-refinement strategy [I]

The numerical evidence now separates three effects cleanly:

1. **finite graph correction** — extremely effective locally;
2. **finite remote-shell extension** — gives only algebraic cutoff improvement;
3. **persistent leading remote moment** — controls essentially the entire far-tail certificate.

Therefore another iteration confined to the frozen (16001/16002) support is the wrong next move.

Likewise, blindly extending the cutoff shell by shell will only buy the slow (N^{-1/2}) tail reduction as long as

[
mathcal L_	heta(q)
e0.
]

The nonredundant next gate is

[
oxed{
	extbf{construct an explicit remote tail correction that cancels }mathcal L_	heta
	extbf{ at fixed low Ritz value.}
}
]

---

## 7. Exact next target [O]

For each parity and each of the four carrier columns, construct a remote correction (y_j) so that

[
q_j^{m new}
=
q_j+y_j
]

satisfies

[
oxed{
mathcal L_{	heta_j}(q_j^{m new})=0,
}
]

while keeping the full residual and (B)-metric perturbation controlled.

The correction must then be checked against **all** rows, not only the asymptotic moment.

A proof-grade implementation should:

1. derive an analytic (1/n)-tail ansatz (or an equivalent structured remote graph solve);
2. choose its amplitude from the exact moment-cancellation equation;
3. prove the corrected tail is in the relevant (B)-energy space;
4. re-orthonormalize and re-Ritz;
5. recompute the finite, explicit-remote, and far residuals;
6. verify that the far certificate has actually changed from
   [
   O(N^{-1/2})
   ]
   to
   [
   O(N^{-3/2})
   ]
   at leading order.

Only after that cancellation is achieved is another source/phase consumer pass justified.

---

## 8. Result

The v13.988 graph correction is not failing because the local KKT solve is poor.

It is failing because its finite-support correction leaves the source-faithful infinite (1/n) residual moment essentially untouched.

Numerically,

[
oxed{
	ext{finite residual collapses by orders of magnitude, while the full residual is unchanged/slightly worse at }M2.
}
]

One fresh shell reduces the full residual by about (15%), but

[
oxed{
>99.7%	ext{ of the remaining far-tail bound is still the explicit }1/n	ext{ coefficient.}
}
]

And the dominant coefficient cannot be canceled by a small change of the Ritz value.

Therefore the next gate is sharply identified:

[
oxed{
	extbf{remote asymptotic tail-vector completion, not another finite KKT iteration and not another global }6	imes6	extbf{ inverse bound.}
}
]
