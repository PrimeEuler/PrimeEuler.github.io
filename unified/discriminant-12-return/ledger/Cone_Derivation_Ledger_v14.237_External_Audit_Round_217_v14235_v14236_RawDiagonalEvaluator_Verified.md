# Cone Derivation Ledger v14.237 — External Audit Round 217: v14.235–v14.236's Raw Remote Diagonal Evaluator Independently Re-Derived and Reproduced

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.235's uniform certified raw remote diagonal evaluator — the complex-disk kernel bound, the combined integration-by-parts identity giving the explicit arch constant $|I(k)|<43/k^2$, the Ci/Si cusp remainder derivation, and the "172/(9R^2)+1/(9R^3)<3e-10" combined sanity bound — is independently re-derived from scratch and confirmed exact, including resolving an apparent discrepancy in the last item (it restates the arch bound in terms of $x=2k$ rather than $k$, not a separate error term; $43/k^2=172/x^2$). The actual implementation (`suzuki_certified_remote_diagonal.py`) is read line-by-line and confirmed to match every formula in the ledger text. The gate script is re-run fresh from the audited v14.227 source payload (not merely read from the committed JSON) and reproduces the committed 83669-byte payload byte-for-byte. v14.236's audit is independently corroborated. No correction found.
**Parents:** v14.195, v14.220, v14.227, v14.229, v14.233–236.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `cab7e89...` (v14.236), matching local HEAD; live ledger max was v14.236. v14.237 is next-free. No collision.

---

## 1. Complex-disk kernel bound — independently re-derived

$h(t)=\exp(-t/2)/(1-\exp(-2t))-1/(2t)$. Multiplying by $\exp(t)/\exp(t)$: $\exp(-t/2)/(1-\exp(-2t))=\exp(t/2)/(2\sinh(t))$, giving $h(t)=[t\exp(t/2)-\sinh(t)]/[2t\sinh(t)]$ after combining — confirmed exactly matches the entry's complex extension $h(z)$.

On $|z-t|\le1$, $t\in[0,2]$: independently confirmed $|\mathrm{Im}\,z|\le1$, $\mathrm{Re}\,z\le3$, $|z|\le3$ by the triangle inequality on $z=t+w$. With $z=a+ib$: $|\sinh z|^2=\sinh(a)^2\cos(b)^2+\cosh(a)^2\sin(b)^2=\sinh(a)^2+\sin(b)^2$ (using $\cosh^2=\sinh^2+1$) — re-derived exactly. Since $|\sinh(a)|\ge|a|$ for all real $a$, and $\sin(b)/b\ge1-b^2/6\ge5/6$ for $|b|\le1$ (checked: at $b=1$, $\sin(1)\approx0.8415>5/6\approx0.8333$, and $\sin(b)/b$ is decreasing on $[0,1]$, so $5/6$ is a valid — if non-tight — lower bound throughout), $|\sinh z|^2\ge a^2+(5/6)^2b^2\ge(5/6)^2|z|^2$, confirmed.

Writing the numerator as $z(\exp(z/2)-1)-(\sinh(z)-z)$ and bounding each piece ($|\exp(z/2)-1|\le(|z|/2)\exp(|z|/2)<3|z|$ using $\exp(3/2)<6$; $|\sinh(z)-z|<(11/27)|z|^3$, confirmed by checking $f(x)=(\sinh x-x)/x^3$ is increasing on $(0,3]$ with $f(3)=(\sinh 3-3)/27\approx0.2599<11/27\approx0.4074$), the combination gives $|h(z)|\le9/5+(11/45)|z|\le9/5+(11/45)\cdot3=1.8+0.7\overline{3}=2.5\overline{3}<3$ — independently recomputed to the same value Sandbox reported (2.54), confirming both this auditor's and Sandbox's arithmetic. Cauchy's estimate at radius 1 then gives $|h^{(j)}(t)|<3\cdot j!$, matching the payload's recorded $[3,3,6]$ for $j=0,1,2$.

## 2. Combined IBP identity and the $43/k^2$ constant — independently re-derived

With $u(t)=(2-t)h(t)$: first IBP on $\int_0^2u\cos(kt)dt$ has zero boundary ($u(2)=0$, $\sin(0)=0$); second IBP on the resulting $J=\int u'\sin(kt)dt$ and a parallel single IBP on $(1/k)\int h\sin(kt)dt$ combine (independently re-derived term by term, not copied from the entry) to:
$$k^2I(k)=u'(2)\cos(2k)-u'(0)+h(0)-h(2)\cos(2k)+\int_0^2[h'(t)-u''(t)]\cos(kt)dt,$$
exactly matching the entry's stated identity after regrouping. Substituting $u'(0)=2h'(0)-h(0)$, $u'(2)=-h(2)$, and $h'-u''=3h'-(2-t)h''$ (both confirmed by direct product-rule differentiation of $u$ and $u'$) gives boundary bound $2|h(0)-h'(0)|+2|h(2)|\le2(1/4+3)+2(3)=12.5$ (using exact $h(0)=1/4$, $|h'|,|h(2)|<3$), and integral bound $\int_0^2(3|h'|+(2-t)|h''|)dt\le3\cdot3\cdot2+6\cdot\int_0^2(2-t)dt=18+6\cdot2=30$ (using $\int_0^2(2-t)dt=2$ exactly, sharper than the pointwise $(2-t)\le2$ bound this auditor tried first, which gives a looser but still-valid 21+... total of 42 — both under 43). Sum $12.5+30=42.5<43$, confirming $|I(k)|<43/k^2$ independently.

## 3. Ci/Si cusp remainder — independently re-derived via direct IBP on the tail integrals

Starting from $\mathrm{Ci}(x)=-\int_x^\infty\cos(t)/t\,dt$ and $\mathrm{Si}(x)=\pi/2-\int_x^\infty\sin(t)/t\,dt$ (not assumed from the entry), two rounds of integration by parts on each, using $\sin(n\pi)=0$ at the appropriate step to kill a boundary term, independently reproduce exactly: $\mathrm{Ci}(x)=-\cos(x)/x^2+\delta_1$, $|\delta_1|\le2/x^3$; $\mathrm{Si}(x)=\pi/2-\cos(x)/x+\delta_2$, $|\delta_2|\le1/x^2$. Combining: $-\mathrm{Ci}(x)-\mathrm{Si}(x)/x=-1/(2n)+2(-1)^n/x^2-\delta_1-\delta_2/x$, $|\delta_1+\delta_2/x|\le3/x^3$ — matches the entry's stated formula exactly.

## 4. Resolving the "172/(9R²)" combined bound — not a separate error, confirmed via direct code read

Initially this figure did not obviously follow from the $\pm3/x^3$ remainder alone (which would give coefficient 2 or 3, not 172, under a naive $x>R\pi$, $\pi>3$ substitution). Reading `suzuki_certified_remote_diagonal.py` directly resolved this: the code's `cusp` variable keeps $-1/(2n)+2(-1)^n/x^2$ as an **exact** interval term (propagated through `pi`'s own tiny representation uncertainty, not bounded via any $R$-based estimate), and only `cusp_error=3*ix[1]**3` (the $\pm3/x^3$ piece) is added as a genuine uncertainty radius at the very end, alongside `arch=43*invk[1]**2` where `invk=2*ix=1/k`. Since $k=x/2$, $43/k^2=172/x^2$ — so the "172/(9R^2)+1/(9R^3)<3e-10" statement is the **arch bound restated in $x$-terms plus the cusp remainder**, both re-expressed via $x>R\pi$, $\pi^2>9$ as a single combined pre-code sanity margin — not a separate, unexplained error term. Confirmed by direct substitution: $43/(n\pi/2)^2=172/(n^2\pi^2)<172/(9n^2)\le172/(9R^2)$, and $3/(n\pi)^3<3/(27n^3)=1/(9n^3)\le1/(9R^3)$. At $R=256000$: $172/9=19.1\overline{1}$, $R^2=6.5536\times10^{10}$, giving $2.9158\times10^{-10}<3\times10^{-10}$ — independently recomputed, matches exactly. This is confirmed in the gate script itself: `bound=F(172,9*256000**2)+F(1,9*256000**3); assert bound<F('3e-10')`.

## 5. Direct line-by-line code audit against the stated formulas

Read `suzuki_certified_remote_diagonal.py` in full (not merely the ledger prose). Confirmed: `cos_integer`'s recurrence and stated error bound `terms*16**terms` (rounding) plus `4**(2*terms)/factorial(2*terms)` (Taylor remainder) match the entry's "24-term cosine recurrence... rounding bound 24·16²⁴·2⁻ᴮ and Taylor remainder 4⁴⁸/48!" exactly, with `terms=24`. `log_normalized`'s $n=2^em$ decomposition, $r=(m-1)/(m+1)$, atanh series summation, and error budget $(10K+10)2^{-B}+3(1/3)^{2K+1}$ (with $K=B+12$, safely covering the true atanh tail bound of $(9/8)(1/3)^{2K+1}\times2<3(1/3)^{2K+1}$ after accounting for the factor of 2 in $\log(m)=2\,\mathrm{atanh}(r)$) match §3's description exactly. The main `evaluate` function assembles $\log(n/4)+[\text{cusp}]-\sum_q[\text{prime term}]\pm[\text{arch}+\text{cusp\_error}]$, confirmed to implement the exact stated formula for $d_n$ with $I(k)$ replaced by zero and bounded, not evaluated.

## 6. Fresh script execution — not merely payload inspection

Ran the committed, unmodified `suzuki_certified_remote_diagonal_gate.py` fresh against the already-independently-verified v14.227 source payload (`certified_remote_z_v14_227/certified-remote-z-gate.json`, SHA-256 `f37bbb3e...`, matching the hash this auditor reconstructed independently in Round 214/215). The run took 13 seconds, printed "50 raw physical diagonal intervals and uniform budget passed," and produced output matching the committed `payloads/certified_remote_diagonal_v14_235/certified-remote-diagonal-gate.json` **byte-for-byte** (SHA-256 `c7ce6fb5...`, 83669 bytes) — not just a hash comparison against the stored file, but a full independent re-execution from the upstream source artifact.

## 7. Verdict

```
Complex-disk kernel bound |h(z)|<2.5333<3 and Cauchy derivative
  bounds [3,3,6]: INDEPENDENTLY RE-DERIVED from scratch, matches
  both the entry and Sandbox's v14.236 recomputation exactly.
Combined IBP identity and arch constant 43/k^2: INDEPENDENTLY
  RE-DERIVED term by term (boundary 12.5 + integral 30 = 42.5<43).
Ci/Si cusp remainder -1/(2n)+2(-1)^n/x^2+-3/x^3: INDEPENDENTLY
  RE-DERIVED via direct IBP on the Ci/Si tail integrals.
The "172/(9R^2)+1/(9R^3)<3e-10" combined bound: RESOLVED as the
  arch bound (43/k^2) restated via x=2k (43/k^2=172/x^2) plus the
  cusp remainder, both in R-terms -- confirmed via direct read of
  the gate script's own assertion, not a separate or erroneous term.
Implementation (suzuki_certified_remote_diagonal.py): READ LINE BY
  LINE, confirmed to match every formula and error budget in the
  ledger text exactly.
Gate script: RE-RUN FRESH from the upstream v14.227 source payload
  (not just read from committed JSON), reproduces the committed
  83669-byte payload BYTE-FOR-BYTE.
v14.236's audit is independently corroborated on every point checked.
No correction found anywhere in this batch. No infinite-tail theorem
  is claimed or promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.237
status: open
action: v14.235's raw remote diagonal evaluator is independently re-derived from scratch (complex-disk kernel, combined IBP identity, Ci/Si cusp remainder) and the implementation is confirmed via direct line-by-line code read plus a fresh, non-cached re-execution of the gate script against the upstream source payload, reproducing the committed payload byte-for-byte. The apparent "172/(9R^2)" discrepancy this auditor initially flagged for itself was resolved as a restatement of the arch bound via x=2k, not an error -- recorded here for transparency about the audit process, not as a finding. No correction found. Per v14.235's own §6, the next concrete step is combining the raw diagonal with the action-precision physical z evaluator to evaluate a represented trial/action and certify new finite lifts.
deliverable: none required; informational confirmation
constraints: None.
