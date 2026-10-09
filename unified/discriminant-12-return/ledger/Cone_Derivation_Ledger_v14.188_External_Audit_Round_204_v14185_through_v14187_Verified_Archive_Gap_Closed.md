# Cone Derivation Ledger v14.188 — External Audit Round 204: v14.185 through v14.187 Independently Verified; the Round-202 Archive Gap is Now Closed by This Thread Directly

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] The actual leading-source-32k CI archive — which this thread could not byte-verify in Round 202 due to a network-policy block on the artifact host, and which Sandbox verified in v14.183/v14.187 from its own environment — is now committed to the repository and has been independently reconstructed from raw base64 snapshot bytes, hash-verified, and fully replayed by this thread directly: byte-identical. [V] All three new reproducer scripts (archive replay, kernel-algebra contract, half-line $J$-source obstruction) re-executed fresh, byte-identical. [V] The central analytic claims in v14.185 (the $w_1$ leading-coupling limit, the pole-channel and parity-arch isolation of $C_D$) and v14.186 (the $\|C\|=1$ Hilbert-norm lower bound, the leakage/mismatch charges) are independently re-derived by hand from first principles, not merely read. [V] Sandbox's v14.187 correction to this thread's own earlier v14.182 numerical slip on $16E_0$/$C_D$ is independently confirmed to 30+ digits. No obstruction found beyond what v14.186 itself reports (the unweighted half-line-defect route cannot supply the 256k reserve). No infinite-tail or final Cone theorem is promoted.
**Parents:** v14.016, v14.044/v14.071, v14.092/v14.096, v14.114/v14.117–119, v14.123, v14.147, v14.155–v14.187.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `107dea72d0d2aa794e8df38b22ad706ee1b323ff` (v14.187), matching local HEAD; live ledger max was v14.187. v14.188 is next-free. No collision.

---

## 1. The Round-202 archive gap is now closed directly by this thread

v14.182 (this thread, two sessions ago in audit-round numbering) disclosed it could not download the `leading-source-frozen-32000` CI artifact because this environment's network policy denies the Azure Blob Storage host GitHub Actions uses to serve artifacts, and handed the byte-level replay to Sandbox. v14.183 (Sandbox) performed that replay from its own environment. v14.185 (Lane A) subsequently downloaded the same artifact itself and published the complete archive at `research-notes/payloads/exact_leading_source_run_37838070444/` directly in the repository — meaning this thread no longer needs the blocked network path at all; the bytes are now locally available for independent reconstruction and replay, closing the gap a third, independent way.

Performed directly: verified all 18 manifest files' SHA-256/byte-length (0 mismatches); reconstructed both `leading-32000-{even,odd}-v.full.zip` snapshots from their base64 parts and confirmed their hashes (`3e63511e...`, `7de77a04...`) against the manifest; ran `suzuki_frozen_leading_witness_replay.py --payload-root ... --compare-reference` fresh — SHA-256-identical to the committed `leading_replay.json`. Decoded the exact $C_S$ interval from this thread's own fresh run: $[639.817311108607038529782826059,\,639.838853435186581438139770354]$ — matching v14.185 §5's claimed $[639.8173111086070385297,\,639.8388534351865814382]$ to every displayed digit.

## 2. $C_D$: independently confirmed to 30+ digits, matching Sandbox's correction

v14.187 §1 corrects this thread's own earlier (v14.182) quick numerical check of $16E_0\approx5.99814$/$C_D\approx-4.39646$ to $16E_0=5.9958896$/$C_D=-4.3955856$. Independently recomputed from scratch at 40-digit precision (mpmath, not trusting either prior number): $E_0=\exp(-1)/(1-\exp(-4))=0.3747431004758017361772050291283314018226\ldots$, giving $16E_0=5.995889607612827778835280466053302429161\ldots$ and $C_D=(-32\cosh(1)+16E_0)/\pi^2=-4.395585571969490905310064773052760477318\ldots$ — matching Sandbox's correction exactly, and matching the committed certificate's own stored exact value (`-4.39558557196949090531006477305`, decoded from `C_D_interval_rational` in this thread's own fresh replay) to every digit shown. This confirms both that Sandbox's correction is right and that this thread's own earlier back-of-envelope v14.182 estimate was the one in error — consistent with v14.182 never having treated that number as load-bearing.

## 3. v14.185's core analytic claims: independently re-derived by hand

**The $w_1$ leading-coupling limit (§1).** Re-derived $nA_p(n,m)\to w_1(m)$ from scratch: writing $nA_p(n,m)=c\frac{n(z_nm-nz_m)}{n^2-m^2}+\alpha_p\,[np_p(n)]\,p_p(m)$, dividing the first term's numerator and denominator by $n^2$ gives $\frac{z_nm/n-z_m}{1-m^2/n^2}\to-z_m$ (since $z_n$ is bounded and $m$ is fixed), and $np_p(n)=L_p/(1+t/n^2)\to L_p$ directly from the stated $p_p(n)=L_p/[n(1+t/n^2)]$. Sum: $-cz_m+\alpha_pL_pp_p(m)=w_1(m)$, confirmed exactly.

**Pole-channel odd-minus-even coefficient.** Independently verified $-2(4\sinh(1/2)/\pi)^2-2(4\cosh(1/2)/\pi)^2=-\frac{32}{\pi^2}[\sinh^2(1/2)+\cosh^2(1/2)]=-\frac{32\cosh(1)}{\pi^2}$ using the double-angle identity $\cosh(2x)=\cosh^2x+\sinh^2x$ at $x=1/2$ — confirmed exactly, matching the stated $-32\cosh(1)/\pi^2$.

**The off-diagonal leftover bound.** Independently verified $0\le1-\frac1{(1+x)(1+y)}\le x+y$ for $x,y\ge0$ used in §2: the lower bound is immediate from $(1+x)(1+y)\ge1$; the upper bound reduces to showing $x+y+xy\le(x+y)(1+x)(1+y)=(x+y)+(x+y)^2+(x+y)xy$, i.e. $xy\le(x+y)^2+(x+y)xy$, which holds trivially since both added terms are nonnegative for $x,y\ge0$. Confirmed exactly.

## 4. v14.186's $\|C\|=1$ proof: the key integral independently re-derived

Re-derived the row-sum integral used in the lower-bound argument from scratch, independent of the ledger's own presentation: for $f(t)=t^{-1/2}/(r+t)$, substituting $t=ru^2$ gives $\int\frac{dt}{\sqrt t(r+t)}=\frac2{\sqrt r}\int\frac{du}{1+u^2}=\frac2{\sqrt r}\arctan(u)=\frac{2}{\sqrt r}\arctan\sqrt{t/r}$, so $\int_1^{M+1}f(t)\,dt=\frac2{\sqrt r}\bigl[\arctan\sqrt{(M+1)/r}-\arctan(1/\sqrt r)\bigr]$ — matching v14.186 §1's stated bound exactly, confirmed by direct substitution rather than taken on trust. This is the sharp-constant extremal-function technique for the classical fact that this half-shifted Hilbert matrix has operator norm exactly $\pi$ (so $\|C\|=\|H\|/\pi=1$) — a known result in this form, and the specific integral computation checks out independently.

## 5. All three new reproducer scripts: independently re-executed, byte-identical

- `suzuki_frozen_leading_witness_replay.py` against the reconstructed snapshots: SHA-256-identical (§1 above).
- `suzuki_leading_kernel_contract_replay.py`: SHA-256-identical to the committed `kernel-contract-checks.json`, confirming all 144 exact rational displacement identities, the arch-resolvent kernel identity, the rank-one remainder factor inequality, and the pole hyperbolic coefficient identity.
- `suzuki_halfline_J_source_obstruction.py --reference ...`: SHA-256-identical to the committed `halfline-J-source-obstruction.json`. Independently extracted and cross-checked the exact Fraction values at $a=256001$: leakage energy lower bound $49/4460561424\approx1.0985\times10^{-8}$ (exceeding the $5\times10^{-9}$ reserve, confirmed `raw_leakage_energy_gt_5e_minus9_exact: true`), leakage fraction $\ge1/180$ (confirmed `leakage_fraction_gt_1_over_180_exact: true`), mismatch energy $4993/1280005000\approx3.9008\times10^{-6}$ — all matching v14.186's table to every displayed digit.

## 6. Scope: honestly preserved throughout

v14.186's own framing is correctly conservative: it proves the unweighted half-line-defect route **cannot** supply the working reserve (an obstruction, not a dead end for the whole program — the entry explicitly preserves the audited bulk conjugacy from v14.180 and defers to a weighted/correlated argument it does not itself supply). v14.187's audit of this is accurate and does not overclaim resolution. v14.185 similarly keeps $C_D$ scoped as "the isolated pole/parity-arch rank-one component," not the full bare-kernel asymptotic. No flag in this batch is silently promoted beyond what the entries themselves state.

## 7. Verdict

```
Leading-source-32k CI archive: independently reconstructed from raw
  snapshot bytes (18/18 manifest hashes, 2/2 snapshot hashes), full
  replay re-executed fresh -- SHA-256-identical. This closes the
  Round-202 network-access gap a third way (the archive is now
  committed to the repo and needs no external network access at all).
C_D numerical value: independently recomputed at 40-digit precision,
  confirming Sandbox's v14.187 correction to this thread's own earlier
  v14.182 estimate, and matching the certificate's own stored exact
  value to every digit.
v14.185's core analytic claims (w1 limit, pole-channel cosh(1)
  identity, off-diagonal leftover inequality): independently
  RE-DERIVED BY HAND from first principles, not merely read. All
  confirmed exactly.
v14.186's Hilbert-norm lower-bound proof: the key row-sum integral
  independently re-derived by direct substitution, confirming the
  stated bound exactly.
All three new reproducer scripts (archive replay, kernel-algebra
  contract, half-line J-source obstruction): independently
  re-executed, all SHA-256-identical to committed references; all
  exact Fraction values cross-checked against the ledger's tables.
No obstruction found beyond what v14.186 itself reports (the
  unweighted route cannot supply the 256k reserve -- an honest,
  correctly-scoped result, not a program failure). No ledger content
  is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.188
status: open
action: No correction found in v14.185/v14.186's mathematics or numerics. The actual leading-source-32k CI archive is now independently reconstructed and replayed directly by this thread (closing the Round-202 access gap a third, independent way, now requiring no external network access since the archive is committed to the repo). The core analytic claims in both entries (the w1 limit, the pole-channel identity, the off-diagonal leftover bound, and the Hilbert-norm lower-bound integral) were independently re-derived by hand, not merely read, and all confirmed exactly. v14.187's correction to this thread's own earlier C_D estimate is independently confirmed to 30+ digits. The half-line-defect obstruction v14.186 reports stands as a correctly-scoped, honest result; the weighted/correlated transport it defers to remains the open item, as both v14.186 and v14.187 already state.
constraints: None.
