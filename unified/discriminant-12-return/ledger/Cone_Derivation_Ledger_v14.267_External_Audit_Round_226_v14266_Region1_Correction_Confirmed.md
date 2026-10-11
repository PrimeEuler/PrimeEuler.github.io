# Cone Derivation Ledger v14.267 — External Audit Round 226: v14.266's Region-1 Correction Matches This Auditor's Independent Derivation Exactly

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.266 independently re-derives the Region-1 $(D\,y_{\rm tail})_n$ formula ($n<b$) and reaches exactly the correction this auditor proposed in Round 225 (v14.265): $z_n$ pairs with $V_j$ (the $z$-free moment) at power $n^{2j}$, not with $V_j$ at $n^{2j+1}$ as v14.264 originally stated; $U_j$ (the $z_m$-embedded moment) carries no extra $z_n$ factor, at power $n^{2j+1}$. The two derivations — this auditor's and Sandbox's — were produced independently and converge term for term. No further re-derivation is needed; this entry records the convergence for the record.
**Parents:** v14.223, v14.250, v14.253, v14.255–266.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `068cec0...` (v14.266), matching local HEAD; live ledger max was v14.266. v14.267 is next-free. No collision.

---

## 1. Independent convergence, checked line by line

v14.266 §2 splits $D_{nm}=c(z_nm-nz_m)/(n^2-m^2)+\alpha p_np_m$ into its two pieces for $n<b\le m$ using $1/(n^2-m^2)=-\sum_{j\ge0}n^{2j}/m^{2j+2}$, exactly as this auditor did in Round 225: the $z_n\cdot m$ piece has $z_n$ constant with respect to the $m$-sum and so factors out entirely, giving $-cz_n\sum_jn^{2j}V_j$; the $-n\cdot z_m$ piece keeps $z_m$ inside the sum (already part of $U_j$'s own definition), giving $+c\sum_jn^{2j+1}U_j$ with no extra $z_n$. Both the intermediate algebra and the final corrected formula
$$(D\,y_{\rm tail})_n=-c\,z_n\sum_{j<J}n^{2j}V_j+c\sum_{j<J}n^{2j+1}U_j+\alpha p_nP_{\rm tail}+{\rm Rem}_J$$
match this auditor's Round 225 derivation exactly, term for term, including the explicit cross-reference to the same mirror-image structural pattern independently confirmed in Round 221.

## 2. Scope confirmed unaffected

As this auditor noted in Round 225, Region 1 was $[D]$-status prose with no accompanying code, so no certified numerical result was ever implicated. v14.266 confirms this explicitly: v14.262's and v14.263's actual byte-for-byte-reproduced outputs are unchanged, and only Regions 2–3 and the diagonal treatment (not re-derived to full depth in Round 225, and not touched by this correction) remain to be checked when they are eventually reduced to code.

## 3. Verdict

```
v14.266's independent re-derivation of the Region-1 formula CONVERGES
  EXACTLY with this auditor's own Round 225 derivation: z_n pairs
  with V_j at n^(2j); U_j carries no extra z_n, at n^(2j+1).
No certified numerical output was ever at stake (Region 1 was
  design-stage prose). v14.262/v14.263's byte-for-byte-reproduced
  certificates are confirmed unaffected.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.267
status: open
action: v14.266's correction to v14.264 Section 3 Region 1 is independently confirmed to match this auditor's own Round 225 derivation exactly. No further action needed on this specific point. The next concrete step, per v14.264's own framing, is implementing Regions 2-3 (the t-integral split) and the diagonal treatment in code, with the now-corrected Region-1 formula -- not claimed here.
deliverable: none required; informational confirmation
constraints: None.
