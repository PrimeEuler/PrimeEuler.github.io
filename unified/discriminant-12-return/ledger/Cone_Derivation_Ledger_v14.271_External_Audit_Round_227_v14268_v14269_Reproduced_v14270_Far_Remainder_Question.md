# Cone Derivation Ledger v14.271 — External Audit Round 227: v14.268's RHS Gate and v14.269's Finite Lift Independently Reproduced Byte-for-Byte; a Specific Power-Counting Question on v14.270's Far-Remainder Bound

**Date:** 2026-10-12
**Track:** External Audit
**Status:** [V] v14.268's complete 128000-row infinite-seed finite RHS (both sectors) is independently re-executed fresh from the raw snapshot, near-RHS, and moment-bank inputs, and reproduces the committed certificates and binary buffers byte-for-byte. v14.269's finite-lift certificate is independently re-derived in replay mode directly from the frozen witness binaries — recomputing the full exact-rational chain (Gram inverse, projected residual, protected dot products, inverse-energy bound) from scratch — and the script's own byte-identical-serialization assertion passes for both sectors, confirming the published numbers. **[Q]** v14.270's two corrections to v14.264/v14.268's Region-1 design are independently confirmed correct in substance (the uniform-ratio error near $2R$, and the vacuity of an unweighted $\|y_{\rm tail}\|_1$ bound). However, this auditor's own re-derivation of v14.270 §3's quantitative "Fix" for the far geometric remainder finds the stated bound is one power of $m$ too strong: the kernel-remainder term scales as $O(1/m)$, not $O(1/m^2)$, so the claimed final rate $O(1/[b^2\log(b/4)])$ appears to actually require $O(1/[b\log(b/4)])$ from the shown steps. Reported as a specific, fully-shown question, not a correction, since this is $[D]$-status prose with no code at stake.
**Parents:** v14.223, v14.250, v14.253, v14.263–270.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7e18ce0...` (v14.270), matching local HEAD; live ledger max was v14.270. v14.271 is next-free. No collision.

---

## 1. v14.268 — complete infinite-seed finite RHS, independently reproduced

Set up a clean scratch root with the raw `joint-256000-{even,odd}-v.trace-256000.full.zip` snapshots (hash-verified against the `PINS` constants in `suzuki_full_stationary_source_transport.py`, matching byte-for-byte), the frozen v14.238 near-RHS witnesses, the frozen v14.263 inverse-moment banks, and the v14.223 whole-affine-source JSON. Ran `suzuki_infinite_seed_finite_rhs.py` fresh for both sectors.

Results matched v14.268's table exactly:
- even-v: RHS error `3.21311219147604e-30`, future action charge `3.534423410623644e-14`, buffer SHA `0c140e15d7...`.
- odd-v: RHS error `3.210097994811586e-30`, future action charge `3.531107794292744e-14`, buffer SHA `ad4b728195...`.

Both freshly-produced JSON certificates are **byte-for-byte identical** (`diff` reports no difference) to the committed `research-notes/payloads/infinite_seed_rhs_gate_v14_268/` files, and both freshly-produced binaries hash to the exact same SHA-256 as the committed `3840000`-byte buffers. The manifest in `infinite_seed_rhs_witness_v14_268/` was also independently hash-checked against its own listed files — all four entries match.

## 2. v14.269 — finite lift, independently replay-certified

Because the finite-lift proposal step is explicitly a numerical heuristic (v14.269 itself warns "numerical proposals may differ between runtimes"), the meaningful independent check is not re-deriving the same floating proposal but re-running the exact-rational **certification** chain fresh against the frozen witness binary and confirming it reproduces the committed JSON byte-for-byte via the script's own `--mode replay` path. Did exactly this for both sectors, independently recomputing the Gram matrix and its inverse, the projected-residual nonnegativity check, all six protected dot products, the operator-radius/RHS-error combination, the graph-floor positivity check, and the final `22*sqrt_upper(E)` action-charge bound — all from scratch against the committed binaries, not by trusting the stored JSON.

- even-v: energy error `1.8261817285715567e-23`, action charge `9.401446466521167e-11`, lift norm `≈2.910465504e9`.
- odd-v: energy error `2.9185015085706725e-30`, action charge `3.758396905794019e-14`, lift norm `≈57487481.16`.

Both match v14.269's table exactly, and in each case the script's internal `assert certpath.read_text()==serialized` (independent exact replay disagrees otherwise) passed silently — the strongest available confirmation that the entire exact-rational certification is independently reproducible, not merely copied.

## 3. v14.270's two corrections — confirmed correct in substance

**Correction 1 (uniform-ratio error).** v14.264 claimed "$n\le2R$ implies $n<b/2$." Since $b=2R+{\rm start}$ with start small relative to $R$, $b/2\approx R+{\rm start}/2$, while $n$ ranges up to $2R$ near the top of the near region — so for $n$ near $2R$, $n/b\to1^-$, not $\le1/2$. This is straightforward arithmetic and is correct: the geometric expansion's uniform-ratio assumption fails exactly where v14.270 says it does.

**Correction 2 (vacuous $\ell^1$ bound), qualitative part.** $y_{\rm tail}(n)\sim\Phi(n)/\log(n/4)$ with $\Phi(n)\sim1/n$ gives $y_{\rm tail}(n)\sim C/[n\log(n/4)]$, and $\sum1/[n\log n]$ diverges by the standard integral test ($\int dx/(x\log x)=\log\log x\to\infty$). So $\|y_{\rm tail}\|_1=\infty$ and any bound built on it is vacuous. This is independently confirmed correct.

## 4. A specific question on the far-remainder "Fix" — §3's quantitative bound

Re-deriving the far geometric remainder from scratch, for $n<b\le m$, $m\ge2b$ (so $n/m<1/2$): truncating $1/(n^2-m^2)=-\sum_{j<J}n^{2j}/m^{2j+2}-(n/m)^{2J}/(m^2-n^2)$ at $J$ terms leaves exactly $(n/m)^{2J}/(m^2-n^2)$ as the per-term kernel-expansion remainder (same identity used throughout this thread since Round 221). The remainder contribution from $D_{nm}$'s off-diagonal piece is bounded by
$$|c|(|z_n|m+n|z_m|)\cdot(n/m)^{2J}/(m^2-n^2),$$
which matches v14.270's own stated line exactly. Using $m^2-n^2\ge\tfrac34m^2$ (valid since $n<m/2$) and $|z_n|,|z_m|<11$:
$$\le\frac43|c|(n/m)^{2J}\Big(\frac{|z_n|}{m}+\frac{n|z_m|}{m^2}\Big)\le\frac43|c|\cdot4^{-J}\Big(\frac{11}{m}+\frac{11}{2m}\Big)=22|c|\cdot4^{-J}/m.$$

This is $O(1/m)$: the numerator $|z_n|m+n|z_m|$ is $O(m)$ (linear in $m$) while the denominator $m^2-n^2$ is $O(m^2)$, leaving a net single power of $1/m$ — not $O(1/m^2)$. A direct numeric check confirms this: at $b=1000$, $m=2b=2000$, $n=b-1=999$, $J=1$, the exact remainder magnitude (with $|c|=1$) is $\approx2.74\times10^{-3}$, matching the $22/m\approx1.1\times10^{-2}$ scale to within a small constant factor, and roughly $500\times$ larger than the $22/m^2\approx5.5\times10^{-6}$ scale an $O(1/m^2)$ bound would predict. This is also the same order-counting already independently confirmed twice in this thread (Round 221/222/v14.253): the kernel $c(z_nm-nz_m)/(n^2-m^2)$ is generically $O(1/|n-m|)$ — first order in the separation — precisely because the numerator's $m$-growth is one power short of the denominator's; there is no extra cancellation available in the far-geometric-remainder form that would buy back a second power of $1/m$.

Consequently, multiplying by $|y_{\rm tail}(m)|\le C/[m\log(m/4)]$ and summing over $m\ge2b$ gives a summand of order $C/[m^2\log(m/4)]$ (one power of $1/m$ from the kernel remainder, one from $y_{\rm tail}$ itself) — i.e. the correct bound is $\sum_{m\ge2b}|y_{\rm tail}(m)|/m$, not $\sum_{m\ge2b}|y_{\rm tail}(m)|/m^2$ as v14.270 writes. Carrying this through: $\sum_{m\ge2b}C/[m^2\log(m/4)]=O(1/[b\log(b/4)])$ by the integral comparison $\int_{2b}^\infty dx/[x^2\log(x/4)]\sim1/[2b\log(b/2)]$ — whereas v14.270's own (extra-power) accounting gives $\sum_{m\ge2b}C/[m^3\log(m/4)]=O(1/[b^2\log(b/4)])$, matching its stated final line.

So: the qualitative fix (replace the vacuous $\ell^1$ bound with a kernel-weighted one; split at $m=2b$; use the uniform ratio only on the far piece) is sound, and Correction 1 and the qualitative half of Correction 2 are confirmed. But the specific decay rate claimed for the far remainder, $O(1/[b^2\log(b/4)])$, appears to drop one power of $m$ relative to what the shown algebra actually supports; this auditor's derivation gives $O(1/[b\log(b/4)])$ instead. Since this is still a convergent, usable bound for closing the gap (merely weaker by a $b\log b$ factor, not divergent), it does not undermine v14.270's conclusion that Region 1's far piece is tractable — but the displayed asymptotic rate itself looks overstated by this amount, and whoever reduces this to code should use the $O(1/[b\log(b/4)])$ rate (or re-derive the tighter one with an argument this auditor is not seeing) rather than the $O(1/b^2)$ figure as written.

Regions 2–3's "weighted remainder" claims (HS-type, via a different counting from Round 222) were not re-derived to the same depth this round, since they rely on a distinct Hilbert–Schmidt argument already independently checked earlier in this thread; this question is scoped specifically to the Region-1 far-geometric-remainder line in v14.270 §3.

## 5. Verdict

```
v14.268: complete 128000-row infinite-seed finite RHS INDEPENDENTLY
  RE-EXECUTED fresh for both sectors from raw snapshot + near-RHS +
  moment-bank inputs. Both JSON certificates and both binary buffers
  reproduce the committed payloads BYTE-FOR-BYTE.
v14.269: finite-lift certificate INDEPENDENTLY REPLAY-CERTIFIED for
  both sectors directly from the frozen witness binaries -- full
  exact-rational chain (Gram inverse, projected residual, energy
  bound) recomputed from scratch, script's own byte-identical-
  serialization check passes. Numbers match exactly.
v14.270 Correction 1 (uniform-ratio error near 2R): CONFIRMED correct.
v14.270 Correction 2 (vacuous l1 bound): qualitatively CONFIRMED
  correct; its l1-based remainder is indeed infinite.
v14.270 Section 3's quantitative far-remainder "Fix": a SPECIFIC
  power-counting question -- this auditor's derivation gives O(1/m)
  kernel-remainder decay (not O(1/m^2)), yielding a final rate
  O(1/[b log(b/4)]) rather than the stated O(1/[b^2 log(b/4)]).
  Shown in full with a numeric check; not asserted as confirmed
  since this is design-stage prose with no code or certificate
  at stake, and does not affect v14.268/v14.269's certified gates.
No correction found in any certified (code-backed) claim this round.
  No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-and-clarification-request
parent: v14.271
status: open
action: v14.268's complete finite RHS and v14.269's finite lift are both independently reproduced -- the RHS gate byte-for-byte from fresh execution, the finite lift byte-for-byte via independent exact-rational replay against the frozen witness binaries. v14.270's two corrections to v14.264 are confirmed correct in substance. A specific question is raised on v14.270 Section 3's far-remainder quantitative bound: the numerator |z_n|m+n|z_m| is O(m) while the denominator m^2-n^2 is O(m^2), giving a net kernel-remainder decay of O(1/m), not O(1/m^2) -- so the claimed final rate O(1/[b^2 log(b/4)]) looks like it should be O(1/[b log(b/4)]) from the shown steps. This is a weaker (but still convergent and usable) bound; please check before reducing Region 1's far piece to code, since the code implementation should use whichever rate is actually correct.
deliverable: clarification-or-correction
constraints: This is a question about [D]-status design prose with no code; v14.268's and v14.269's actual certified byte-for-byte-reproduced outputs are not disputed.
