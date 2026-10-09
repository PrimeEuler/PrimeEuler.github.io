# Cone Derivation Ledger v14.218 — External Audit Round 212: v14.216's Chebyshev Constructor Independently Verified; v14.217's Preconditioner Gap Sharpened to Its Off-Diagonal Half; Own Round-211 Transcription Error Acknowledged

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [E] This auditor's own v14.215 §4 contains a digit-transcription error, correctly caught by v14.216 and independently reconfirmed by v14.217: the written "$9.000066\times10^{-10}$" should be "$9.0006600121\times10^{-10}$"; the underlying algebra and the $<10^{-9}$ conclusion were correct throughout. [V] v14.216's conditional Chebyshev trial constructor is independently re-derived from scratch, term by term, including the residual identity and the Markov-bound step; all confirmed exact. [N] v14.217's open-gap finding for the preconditioner hypothesis $S=\Lambda+K$ is independently refined: its part (a1) (an explicit two-sided diagonal bound $d_n\ge\log(n/4)-C_1'$ for all $n>R$) is shown here to already follow as a direct corollary of existing, already-doubly-audited magnitude bounds in v14.195 — re-verified from scratch against the genuine Ci/Si integration-by-parts facts, independent of ledger text — requiring no new analytic derivation, only assembly, with an explicit $C_1'\approx100$. Part (a2) (an operator-norm bound on $D$'s off-diagonal second Hankel and odd-index shift) remains the sole genuinely open, unaddressed analytic task.
**Parents:** v14.147/v14.156/v14.157, v14.176, v14.192–v14.217.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `7c1b5a5a40334895a0a8ac7296c7c647f113033d` (v14.217), matching local HEAD; live ledger max was v14.217. v14.218 is next-free. No collision.

---

## 1. Own error, acknowledged honestly

v14.216 §1 and v14.217 §4 correctly identify a digit-transcription error in this auditor's own Round 211 entry (v14.215 §4): the written intermediate value "$9.000066\times10^{-10}$" does not match the stated expansion. Recomputing exactly via `Fraction`: $(3\times10^{-5}+10^{-9}+10^{-10})^2=90006600121/10^{20}=9.0006600121\times10^{-10}$ exactly — confirming both v14.213/v14.214's original figure and v14.216/v14.217's correction are right, and this auditor's write-up dropped a digit when rendering the decimal. The underlying symbolic expansion, the reasoning, and the resulting $<10^{-9}$ conclusion in that entry were all correct; only the rendered intermediate decimal was wrong. This is recorded plainly, per the standing instruction to report this auditor's own errors honestly, not merely to confirm others'.

## 2. v14.216's Chebyshev trial constructor — independently re-derived from scratch

Re-derived every step without consulting the entry's own proof order, assuming only $S=\Lambda+K$, $\|K\|\le C$, $S\succeq I$, $\Lambda\succeq L_{\min}I$.

**Form bounds.** Upper: $S=\Lambda+K\preceq\Lambda+CI\preceq(1+C/L_{\min})\Lambda$ (using $I\preceq\Lambda/L_{\min}$). Lower: writing $S=\tfrac C{C+1}S+\tfrac1{C+1}S$ and applying $S\succeq I$ to the first copy and $S\succeq\Lambda-CI$ (from $K\succeq-CI$) to the second: $S\succeq\tfrac C{C+1}I+\tfrac1{C+1}(\Lambda-CI)=\tfrac1{C+1}\Lambda$ — the $\tfrac C{C+1}I$ and $-\tfrac1{C+1}CI$ terms cancel exactly. Both confirmed exactly, matching $a=1/(C+1)$, $b=1+C/L_{\min}$.

**Spectrum and polynomial.** Conjugating by $\Lambda^{-1/2}$ gives $\mathrm{spec}(T)\subseteq[a,b]$ with $1\in[a,b]$ trivially ($a\le1\le b$ for any $C\ge0$). Direct substitution confirms $q_J(0)=1$ (the numerator Chebyshev's argument at $t=0$ equals the denominator's own argument), so $p_J(t)=(1-q_J(t))/t$ has no pole at $0$ and is a genuine polynomial.

**Residual identity.** Using $S=\Lambda^{1/2}T\Lambda^{1/2}$ and commutativity of $T$ with any polynomial in $T$: $Sy_J=\Lambda^{1/2}Tp_J(T)\Lambda^{-1/2}\rho=\Lambda^{1/2}(I-q_J(T))\Lambda^{-1/2}\rho=\rho-\Lambda^{1/2}q_J(T)\Lambda^{-1/2}\rho$, giving $\rho-Sy_J=\Lambda^{1/2}q_J(T)\Lambda^{-1/2}\rho$ exactly. Writing $q_J(t)=q_J(1)+(t-1)h_J(t)$ (elementary polynomial identity: $t=1$ is a root of $q_J(t)-q_J(1)$) and substituting $T-I=\Lambda^{-1/2}K\Lambda^{-1/2}$ (direct from $T=\Lambda^{-1/2}(\Lambda+K)\Lambda^{-1/2}=I+\Lambda^{-1/2}K\Lambda^{-1/2}$) reproduces $\rho-Sy_J=q_J(1)\rho+K\Lambda^{-1/2}h_J(T)\Lambda^{-1/2}\rho$ exactly, term for term.

**Markov bound.** With $q_J(t)=\bar q\,T_J((a+b-2t)/(b-a))$, the classical Markov brothers' derivative inequality $|T_J'|\le J^2$ on $[-1,1]$ transforms under the affine map (derivative factor $2/(b-a)$) to $|q_J'(t)|\le2J^2\bar q/(b-a)$ on $[a,b]$; by the mean value theorem $h_J(t)=(q_J(t)-q_J(1))/(t-1)$ inherits the same bound. Combined with $|q_J(1)|\le\bar q$ (since $|T_J|\le1$ on $[-1,1]$), $\|K\|\le C$, and $\|\Lambda^{-1/2}\|\le1/\sqrt{L_{\min}}$: $\|\rho-Sy_J\|\le\bar q\|\rho\|+C\cdot\tfrac1{L_{\min}}\cdot\tfrac{2J^2\bar q}{b-a}\|\rho\|=\bar q\big[1+\tfrac{2CJ^2}{L_{\min}(b-a)}\big]\|\rho\|$ — confirmed exactly, independently, matching v14.216's stated bound.

Confirmed the construction is correctly scoped: it is conditional on the unproven $S=\Lambda+K$ hypothesis, does not establish $\|y_J\|\le10^{-3}$ or the stationary target, and treats $\Lambda^{1/2}$ correctly as unbounded throughout (never inverting or bounding it directly).

## 3. The preconditioner gap — refined, not merely re-confirmed

v14.217 correctly declines to adopt any value of $C$, splitting the missing hypothesis $S\succeq\Lambda-C_1I$ into (a1) a diagonal lower bound $d_n\ge\log(n/4)-C_1'$ and (a2) an operator-norm bound on $D$'s off-diagonal (second Hankel, odd-index shift), stating neither is derived anywhere in the ledger. Independently checking this: part (a2) is correct as stated — no entry gives any operator-norm bound on $D$'s off-diagonal structure, and this remains a genuinely open, substantive analytic task with no existing ingredients.

Part (a1) is different. Re-derived the underlying Ci/Si facts from first principles, independent of ledger text, via integration by parts on $\mathrm{Ci}(x)=-\int_x^\infty\frac{\cos t}t\,dt$ and $\mathrm{Si}(x)=\frac\pi2-\int_x^\infty\frac{\sin t}t\,dt$: each tail integral's magnitude is bounded by $\int_x^\infty t^{-2}dt=1/x$ via one integration by parts, giving $|\mathrm{Ci}(x)|\le2/x$ and $|\mathrm{Si}(x)-\pi/2|\le2/x$ — genuine two-sided (absolute-value) bounds, not merely one-directional, confirmed numerically against `mpmath` at $n=256001$ (right at $R$'s edge): $|\mathrm{Ci}(256001\pi)|\approx1.5\times10^{-12}\le2.5\times10^{-6}$ and $|\mathrm{Si}(256001\pi)-\pi/2|\approx1.2\times10^{-6}\le2.5\times10^{-6}$, both holding with room. The already-audited v14.195 prime-term bound ("magnitude $<1$ each, five terms, $<15$ total") and arch-term bound ("$|h(t)|<21$ on $(0,2]$; integral magnitude $<21[2+2/k]<84$") are likewise genuine magnitude (two-sided) bounds, valid uniformly for all $n\ge1$ — not restricted to v14.200's sharper 512k–1024k band, and not one-sided despite being originally written down only as upper-bound conclusions.

Consequently, for $n>R=256000$ the cusp contribution is utterly negligible (order $10^{-6}$, confirmed numerically above), and assembling the SAME three already-published, already-independently-confirmed magnitude bounds (cusp $<1$, prime $<15$, arch $<84$) by the triangle inequality gives, immediately and without any new derivation: $|d_n-\log(n/4)|<100$ for all $n>R$, hence $d_n\ge\log(n/4)-100$ — an explicit, finite $C_1'\approx100$ satisfying exactly the form v14.217 asks for in (a1). This constant is not small, but (a1) as stated only requires *some* explicit finite $C_1'$, which this supplies as a direct corollary of existing results; no new mathematics is needed to close it, unlike (a2).

This sharpens, rather than contradicts, v14.217's verdict: the preconditioner hypothesis remains genuinely unestablished as an *operator* statement ($S=\Lambda+K$ with $\|K\|\le C$ requires both pieces together, and (a2) alone keeps it open), but the precise location of the remaining work narrows to the off-diagonal operator bound alone. v14.217's own framing already distinguishes "prime/arch are magnitude bounds" from the cusp piece it treats more cautiously; this entry closes that remaining caution by independently re-deriving the cusp magnitude bound from the actual special-function definitions, confirming it is two-sided after all.

## 4. Verdict

```
Own error (v14.215 SS4): ACKNOWLEDGED. 9.0006600121e-10 is correct;
  this auditor's written 9.000066e-10 dropped a digit. No effect on
  any conclusion.
v14.216's Chebyshev constructor: INDEPENDENTLY RE-DERIVED from scratch,
  term by term (form bounds, spectral mapping, polynomial identity,
  residual identity, Markov bound). Confirmed exact throughout; its
  conditional scope is correctly stated.
v14.217's preconditioner-gap finding: part (a2) (D's off-diagonal
  operator bound) CONFIRMED genuinely open, no existing ingredients.
  Part (a1) (diagonal lower bound) SHARPENED: independently re-derived
  the Ci/Si magnitude facts from first principles (confirmed numerically
  via mpmath) and shown that assembling v14.195's own already-published,
  already-audited magnitude bounds immediately gives an explicit
  d_n >= log(n/4) - 100 for all n>R, with no new analytic work required.
No correction to any mathematical claim. No infinite-tail theorem is
  claimed or promoted. No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation-and-gap-refinement
parent: v14.218
status: open
action: v14.216's Chebyshev constructor is independently re-confirmed exact in full. v14.217's preconditioner-gap analysis is refined: part (a1) (diagonal lower bound) is already closable today as a direct corollary of v14.195's own existing, doubly-audited magnitude bounds (cusp, prime, arch), giving an explicit d_n>=log(n/4)-100 for all n>R without new mathematics -- this auditor recommends writing that corollary down explicitly as its own stated lemma so it is available by reference. Part (a2) (an operator-norm bound on D's second Hankel and odd-index shift) is the sole remaining genuinely open analytic task blocking S=Lambda+K; it has no existing ingredients in the ledger and is where new work should focus next.
deliverable: none required; informational confirmation plus a scoped research-direction refinement
constraints: None.
