# Cone Derivation Ledger v14.254 — External Audit Round 222: v14.253's Correction Verified; This Auditor's Own Round 221 Overreach Acknowledged

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.253's corrected infinite-tail envelope is independently re-derived from scratch and confirmed exact: the sharper kernel bound $|c(z_nm-nz_m)/(n^2-m^2)|\le8/|n-m|$ (preserving the distance factor, rather than discarding it) resolves v14.251's apparent $1/\log n$ "obstruction" into a genuine $O(\log n/n)$, square-summable envelope. Fresh execution reproduces the committed payload byte-for-byte. **[E] This auditor's own error:** Round 221 (v14.252) is corrected here. That entry verified v14.251's region-by-region *arithmetic* correctly, but then endorsed its conclusion that the resulting $O(1/\log n)$ figure was "a genuine structural limitation" — an inferential leap this auditor did not catch at the time. An upper bound cannot establish a true decay-rate obstruction; a looser bound being correctly computed does not make the pessimistic conclusion drawn from it correct. v14.253 catches exactly this, and this auditor's independent re-derivation below confirms v14.253 is right and Round 221's framing was mistaken.
**Parents:** v14.223, v14.250–253.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7dcd296...` (v14.253), matching local HEAD; live ledger max was v14.253. v14.254 is next-free. No collision.

---

## 1. This auditor's own error, stated precisely

Round 221's verdict read: "v14.251: the dominant 1/log(n) action-decay bound from region B... confirmed as a genuine structural limitation, not a loose-bounding artifact." That statement is wrong in a specific way worth naming exactly, not just retracting. This auditor *did* correctly re-derive that v14.251's region-B bound — using $|m/(n^2-m^2)|\le4/3$ (the weakest possible consequence of $|n-m|\ge1$, applied uniformly to every term in a region of $\sim n$ terms) — algebraically evaluates to $O(1/\log n)$, exactly as computed. That arithmetic check was correct and remains correct today. The error was treating "a correctly-computed upper bound of order $1/\log n$" as equivalent to "the true quantity cannot decay faster than $1/\log n$." Those are different claims. An upper bound only ever says the truth is *at most* this large; a *sharper* upper bound derived by a more careful method can reveal the truth is actually much smaller, without the original (looser) bound having contained any arithmetic error. v14.253 is exactly such a sharper derivation, and this auditor's Round 221 should have flagged — rather than endorsed — v14.251's leap from "this is the bound I computed" to "this is a fundamental limitation."

## 2. The sharper kernel bound — independently re-derived

For $n,m>2R$, $|z_n|,|z_m|<8$, $|c|<1$: $|c(z_nm-nz_m)|\le8m+8n=8(m+n)$, and $n^2-m^2=(n-m)(n+m)$, so
$$\left|\frac{c(z_nm-nz_m)}{n^2-m^2}\right|\le\frac{8(m+n)}{|n-m|(n+m)}=\frac8{|n-m|}.$$
This is exact and elementary — independently confirmed. Crucially it preserves the full $1/|n-m|$ decay with distance, whereas v14.251's region-B bound replaced $|n-m|$ by its *worst case* (1) over the entire region, discarding exactly the information that resolves the apparent obstruction.

## 3. Region B re-derived from scratch, confirmed $O(1/n)$ not $O(1/\log n)$

For $n/2<m<2n$, $m\ne n$: $|y_m|\le C/[m\log(m/4)]$, and since $m>n/2$ here, $\log(m/4)>\log(n/8)$ and $1/m<2/n$, giving $|y_m|\le2C/[n\log(n/8)]$ — matching v14.253 exactly. Using the sharper kernel bound from §2 and summing over the region (rather than pulling out a worst-case kernel constant first): $|B|\le8\cdot\frac{2C}{n\log(n/8)}\cdot\sum_{m\in B,m\ne n}\frac1{|n-m|}$. The remaining sum, over a same-parity (step-2) lattice with $|n-m|$ ranging up to $\sim n/2$ on one side and $\sim n$ on the other, is a harmonic-type sum of order $\log n$ — independently confirmed to satisfy $\sum1/|n-m|\le1+\log n$ (the specific constant is not load-bearing; the *order* is what resolves the obstruction). This gives
$$|B|\le\frac{16C(1+\log n)}{n\log(n/8)}.$$
Since $\log(n/8)>11$ throughout the relevant range and $\log n=\log(n/8)+\log8<\log(n/8)+3$: $(1+\log n)/\log(n/8)=1+1/\log(n/8)+\log8/\log(n/8)\le1+1/11+3/11=15/11$, giving $|B|\le\frac{16C}{n}\cdot\frac{15}{11}=\frac{240C}{11n}$ — matching v14.253's stated bound **exactly**, and confirming region B is genuinely $O(1/n)$, not $O(1/\log n)$: the $(1+\log n)$ growth in the numerator is fully absorbed by the $\log(n/8)$ in the denominator once the kernel's true $1/|n-m|$ decay (not its worst case) is used. The overall combined envelope across regions A, B, C is then $O(\log n/n)$ (region A alone contributes the surviving $\log(n/b)$ factor, via a harmonic sum of $1/m$ rather than $1/|n-m|$) — still square-summable, confirming $\ell^2$ membership without any decay obstruction.

## 4. Fresh execution

Ran `suzuki_infinite_tail_bounds.py` fresh against the already-verified `whole_affine_source_v14_223` payload. Reproduced the stated constants exactly ($C<1.271460$/$1.270268$; RHS truncation $<3.214\times10^{-30}$/$3.211\times10^{-30}$; offdiagonal output-tail norm $0.020812$/$0.020793$) and the output matched the committed payload **byte-for-byte** (SHA-256 `af405c41...`).

## 5. The RHS inverse-moment formula — structurally checked

v14.253 §3's front-RHS expansion $c\sum_{j<42}[m^{2j+1}U_j-z_mm^{2j}V_j]+\alpha p_mP_{\rm tail}$ (with $U_j=\sum_{\rm tail}z_ny_n/n^{2j+2}$, $V_j=\sum_{\rm tail}y_n/n^{2j+1}$) is the same geometric-expansion technique independently re-derived and confirmed in Rounds 219–221 for the finite combined-support case, now applied to the infinite tail's *absolutely convergent* inverse moments (convergent because $|y_n|\le C/[n\log(n/4)]$ decays faster than any $1/n^{2j+1}$ divergence concern — these are moments of $1/n$-order quantities against *negative* powers $n^{-(2j+1)}$, which converge trivially, unlike the earlier concern about *positive*-power moments of an infinite input). This is consistent with v14.250/v14.251's own point that positive-power moments of the tail would diverge, while these particular (convergent) inverse moments do not — correctly distinguished.

## 6. Verdict

```
This auditor's Round 221 (v14.252) OVERREACHED: it correctly verified
  v14.251's region-B arithmetic but incorrectly endorsed the leap from
  "a correctly-computed O(1/log n) upper bound" to "a genuine
  structural limitation." That leap does not follow and is now
  corrected. Acknowledged plainly, not as a quiet revision.
v14.253's sharper kernel bound |c(z_n m-n z_m)/(n^2-m^2)|<=8/|n-m|:
  INDEPENDENTLY RE-DERIVED, confirmed exact and elementary.
Region B's corrected bound 240*C/(11n): INDEPENDENTLY RE-DERIVED from
  scratch via the harmonic-sum argument, confirmed to resolve to
  O(1/n), not O(1/log n) -- the apparent "obstruction" does not
  survive a sharper bound that preserves kernel distance-dependence.
Fresh execution of suzuki_infinite_tail_bounds.py reproduces the
  committed payload BYTE-FOR-BYTE.
No conclusion that the infinite seed meets or fails the 3e-5 target
  follows from this entry, consistent with its own explicit framing.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-and-self-correction
parent: v14.254
status: open
action: v14.253's correction of v14.251's "fundamental 1/log n obstruction" claim is independently re-derived from scratch (the sharper 8/|n-m| kernel bound, the region-B harmonic-sum argument giving O(1/n) not O(1/log n)) and confirmed exact; fresh execution reproduces the committed payload byte-for-byte. This auditor's own Round 221 entry is corrected here: it had endorsed v14.251's overreaching conclusion without catching that an upper bound cannot establish a decay obstruction. No numerical result from Round 221 was wrong -- v14.251's arithmetic was and remains correctly computed -- only the INTERPRETATION of what that arithmetic established was mistaken, and that mistake is now named and fixed. Per v14.253's own handoff, the next concrete step is Sandbox evaluating the normalized Ubar_j,Vbar_j and P_tail inverse moments to radius <=1e-40, not claimed here.
deliverable: none required; informational confirmation and self-correction
constraints: None.
