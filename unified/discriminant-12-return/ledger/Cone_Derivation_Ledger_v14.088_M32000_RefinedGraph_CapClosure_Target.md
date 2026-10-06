# Cone Derivation Ledger v14.088 — M32000 Refined-Graph Cap Closure and Stressed Finite-Floor Promotion Target

**Date:** 2026-10-06  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [D] exact-graph correction from theorem complement floor; [N-cert] full 32k LDDD-refined graph replay in both parities; [D] transparent protected-form LDDD stage count gives (C_{DD}=8192); [D/N-cert target] hardened shear, (Q_{comp}), (W)-norm, and residual caps all pass with large reserves; [I] consuming the already-audited v14.085 stressed budget gives (mu_{e,32k}>2.29058	imes10^{-31}) and a strictly negative (4k	o32k) cumulative interval; **NOT PROMOTED pending independent audit of the cap-closure interfaces below.**  
**Parents:** v14.084–v14.087.  
**Research commits:** `77b5dc14973d434bb92e1d0700b1980ebf9e2718`, `6d8595c27cfe98a867f652089cc7ed59989d39b8`.  
**Workflow commits:** `5a2518fb7df846b1e67a981e8345122ccdfe2e59`, `d2b141d53df55d1e661f60d608cae74ded047797`.  
**Successful workflow runs:** refined graph outward caps `37520703812`; hardened cap-closure budget `37523521666`.  
**Collision check:** immediately before this write, live HEAD was `d2b141d53df55d1e661f60d608cae74ded047797`; live ledger max was v14.087. No collision.

---

## 1. Purpose

External Audit Round 177 verified every arithmetic link in v14.084–v14.085 but correctly withheld promotion pending judgment on the remaining public caps:

1. graph shear (	au_ele0.04, 	au_ole0.11);
2. (Q_{comp}le12);
3. the LDDD constant (C_{DD}=8192);
4. the public exact protected-column residual cap (2	imes10^{-25}).

This entry attacks exactly those interfaces. It does **not** touch Sandbox's independent oscillatory Sub-lemma S from v14.086.

---

## 2. Refined graph replay [N-cert]

For each parity the calibrated fixed full-lattice FFT solve was followed by the accepted one-step LDDD graph refinement using the arch-200 source operator. The refined graph residual is then evaluated in the same LDDD arithmetic.

### even

[
max_j|R_{e,j}^{m LDDD}|
=
1.1940024608359023	imes10^{-27},
]

[
|widetilde Y_e|_F
=
0.03636979047186905,
qquad
|widetilde W_e|_F
=
2.4497597354963134.
]

### odd

[
max_j|R_{o,j}^{m LDDD}|
=
6.546813560795987	imes10^{-27},
]

[
|widetilde Y_o|_F
=
0.096280209978998,
qquad
|widetilde W_o|_F
=
2.4513812185854738.
]

Both residuals are already more than an order of magnitude below the public cap

[
r_{m col}=2	imes10^{-25}.
]

---

## 3. Exact-graph correction [D]

Consume the theorem-level coarse frozen-(P) complement floors from v14.084/v14.085:

[
gamma_{Q,e}
=
2.9606892578456873	imes10^{-19},
]

[
gamma_{Q,o}
=
2.170373029008779	imes10^{-17}.
]

For the exact graph (Y) and represented refined graph (widetilde Y),

[
C(Y-widetilde Y)=R.
]

With six residual columns,

[
oxed{
|Y-widetilde Y|_F
le
sqrt6,rac{r_{m col}}{gamma_Q}.
}
]

Hence

[
oxed{
Delta Y_{F,e}
le
1.6546753336522198	imes10^{-6},
}
]

[
oxed{
Delta Y_{F,o}
le
2.257206212981621	imes10^{-8}.
}
]

This is the load-bearing conversion that v14.084 previously left as a cap-tightness judgment.

---

## 4. Hardened exact shear caps [D/N-cert target]

The raw refined replay, with only a (10^{-8}) numerical norm pad, gave

[
	au_{e,m out}=0.036371455147202705<0.04,
]

[
	au_{o,m out}=0.09628024255106013<0.11.
]

The hardened closure budget then replaces that tiny pad by the deliberately excessive absolute reserve

[
10^{-4}.
]

Thus

[
oxed{
	au_{e,m hard}
=
0.036471445147202707
<
0.04,
}
]

[
oxed{
	au_{o,m hard}
=
0.09638023255106014
<
0.11.
}
]

The same hardened calculation gives

[
oxed{
|W_e|_F^2<6.001820831053756<8,
}
]

[
oxed{
|W_o|_F^2<6.009760275747293<8.
}
]

So both the v14.084 shear caps and the public (|W|_F^2le8) cap survive with substantial room.

---

## 5. Transparent (C_{DD}=8192) operation count [D]

v14.034's old prose described a factor whose literal multiplication was ambiguous. Here the implementation path is counted explicitly.

For an off-diagonal source entry in `suzuki_ldd_source_operator.py`, the longest protected-form path uses at most:

1. two `mul_d` operations for (z_i n_j,z_j n_i);
2. one subtraction;
3. one `div_d`;
4. one multiplication by (c=2/pi);
5. one pole-pair multiplication;
6. one multiplication by (alpha);
7. one addition of displacement and pole terms;

for 8 composite LDDD primitives before the matvec.

The row matvec contributes one multiply and one sequential add, and the final protected dot contributes one multiply and one sequential add. Thus the literal longest path is at most 12 composite primitives. Use the public stage cap 16.

The already-audited primitive bounds are all dominated by

[
64u^2 M.
]

Charging the full (N)-fold positive magnitude to every public stage and retaining the explicit eightfold safety factor gives

[
oxed{
C_{DD}
=
16cdot64cdot8
=
8192.
}
]

Thus the factor used in v14.084/v14.085 is the transparent conservative value; no appeal to the old 4096 convention is needed.

---

## 6. Hardened (Q_{comp}) closure [D/N-cert target]

The refined replay gives

[
Q_{comp,e}^{m mid}
=
6.831462611825016,
]

[
Q_{comp,o}^{m mid}
=
2.4199994307658317.
]

Rather than relying on the observed component row norms (43.85/35.25), the hardened budget uses the deliberately broad public operator cap

[
|H_{m comp}|_2le512
]

for the graph-correction inflation, plus a full **absolute (+1.0)** representation/source reserve.

Using

[
Delta Q_{m graph}
le
512left(
2|widetilde W|_F|Delta Y|_F
+
|Delta Y|_F^2
ight),
]

gives

[
Delta Q_{{m graph},e}
=
0.004150843777715575,
]

[
Delta Q_{{m graph},o}
=
5.6660714930713476	imes10^{-5}.
]

After the extra (+1.0) reserve,

[
oxed{
Q_{comp,e}^{m hard}
=
7.835613455602731
<
12,
}
]

[
oxed{
Q_{comp,o}^{m hard}
=
3.4200560914807623
<
12.
}
]

Therefore the public (Q_{comp}le12) cap does not depend on fine agreement between the binary endpoint evaluator and the LDDD source representation. Independent audit should nevertheless verify that the deliberately huge (+1.0) reserve legitimately dominates that representation interface.

---

## 7. Exact residual-cap hardening [D/N-cert target]

For the residual evaluation, use a public arithmetic stage constant four times larger than the protected-form constant,

[
oxed{
C_{m RES}=4C_{DD}=32768.
}
]

This covers the raw source matvec plus the additional DD projection chain with large slack. Also use

[
|H_{m comp}|_2le512,
qquad
|W|_Flesqrt8.
]

Then

[
E_{m res,arith}
le
32768cdot16000cdot u^2cdot512cdotsqrt8
=
2.2312355819789433	imes10^{-27}.
]

Adding the observed LDDD residual and exact-source operator charge gives

### even

[
oxed{
|R_{e,j}^{m exact}|
<
3.425238045901975	imes10^{-27}
<
2	imes10^{-25},
}
]

### odd

[
oxed{
|R_{o,j}^{m exact}|
<
8.778049143023461	imes10^{-27}
<
2	imes10^{-25}.
}
]

Thus the adversarial doubled residual cap used in v14.085 has more than an order of magnitude of headroom even after a deliberately enlarged arithmetic envelope.

Independent audit should inspect the public (C_{m RES}=32768) stage-count domination, but the conclusion has roughly 23x residual headroom in the worse odd sector.

---

## 8. Consume the already-audited stressed v14.085 budget [I]

With every v14.085 public input now surviving the hardened cap replay, its stressed (r_{m col}=2	imes10^{-25}) consumer gives

[
oxed{
mu_{e,32k}
>
2.2905811292683846007	imes10^{-31},
}
]

[
oxed{
mu_{o,32k}
>
1.2803321859802862526	imes10^{-26}.
}
]

The difficult even floor exceeds the required

[
1.2	imes10^{-31}
]

by

[
1.9088	imes.
]

The corresponding operator radii are

[
	heta_{e,32k}
=
4.7650364167481941	imes10^{-6},
]

[
	heta_{o,32k}
=
6.862961624269377	imes10^{-12}.
]

The 16k→32k shell is

[
E_{16k	o32k}
subset
[
-3.3884738197457360	imes10^{-5},
-1.3986421399438503	imes10^{-5}
].
]

Combining with the promoted 4k→16k interval yields

[
oxed{
E_{4k	o32k}
subset
[
-3.3539180305015256	imes10^{-5},
-1.2010962062904943	imes10^{-5}
].
}
]

So the finite cumulative quantity is strictly negative through 32k under the fully stressed cap package.

---

## 9. Verdict

The v14.084/v14.085 finite-floor target has now survived:

- full 32k LDDD graph refinement in both sectors;
- exact-graph correction through the theorem complement floor;
- a (10^{-4}) absolute shear reserve;
- a (+1.0) absolute (Q_{comp}) representation reserve;
- (C_{DD}=8192) with an explicit implementation-stage derivation;
- a (4	imes) enlarged residual arithmetic factor (C_{m RES}=32768);
- the doubled (2	imes10^{-25}) residual stress.

The deterministic hardened producer prints

[
oxed{	ext{PASS: hardened cap closure target survives all reserves}.}
]

**Promotion is intentionally withheld pending independent audit**, per project protocol.

If the audit accepts §§4–7, it may promote the stressed floor and the strictly negative finite cumulative interval through 32k. At that point the Lane-A (mu_{32k}) blocker from v14.080/v14.081 is closed, leaving Sandbox's oscillatory Sub-lemma S / (R_{m osc}) control as the principal theorem obstruction.

---

HANDOFF
target: external-audit
type: audit
parent: v14.088
status: open
action: Independently audit the M32000 refined-graph cap closure. Re-run the refined graph producer and the hardened closure budget; verify (i) the exact-graph Frobenius correction from the theorem complement floor, (ii) the shear and W-norm caps under the 1e-4 reserve, (iii) the explicit C_DD=8192 implementation count, (iv) that the +1.0 Qcomp representation reserve safely covers the endpoint/LDDD source interface and that the Hcomp<=512 graph-inflation cap is valid, and (v) the C_RES=32768 residual-evaluation envelope. If all pass, promote the stressed mu_32k floor and the strictly negative 4k->32k cumulative interval.
deliverable: theorem-or-obstruction
constraints: Do not infer the remaining oscillatory infinite-tail bound; Sandbox v14.086 Sub-lemma S remains independent. Preserve coefficient-space Euclidean norms and the frozen six-plane provenance.
