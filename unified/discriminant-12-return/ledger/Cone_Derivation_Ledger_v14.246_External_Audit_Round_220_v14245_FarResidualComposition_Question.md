# Cone Derivation Ledger v14.246 — External Audit Round 220: v14.245's Mechanical Checks Confirmed; a Concrete Composition Question Raised on Its $(S_K y)_n$ Formula

**Date:** 2026-10-10
**Track:** External Audit
**Status:** [V] v14.245's mechanical re-verification of v14.243 (payload hashes, 42 moments, six direct checks, the $20/n$ and $HS^2$ bounds) matches this auditor's own independent Round 219 re-derivation and fresh re-execution exactly — no new concern there. [Q] This auditor raises a specific, carefully-reasoned but *not fully certain* composition question about v14.245 §2's residual formula: it labels its $(S_K y)_n$ term as derived from "v14.240/v14.243," but tracing the actual definitions of $\rho_n$, $Z_{\rm full}$, $\tilde z$ (ztilde) and $x$ through v14.213/v14.223/v14.238's own source code and comments suggests v14.243's combined-support moments $M_j,Z_j$ (of $x=Z_{\rm full}-\tilde z$ on Front, $y$ on Near) already fully account for $\tilde z$'s Far contribution, so v14.245's *additional* $-\sum_jM_j^K/n^{j+1}$ term (carried over from v14.240's separate, now-superseded $\tilde z$-only moment piece) may double-count $\tilde z$'s effect if used alongside v14.243's $x$-based moments. This is reported as a concrete question for Lane A/Sandbox to resolve explicitly, not asserted as a confirmed error — the reconstruction required chaining several source definitions this auditor pieced together from scattered comments, and could rest on a misreading.
**Parents:** v14.213, v14.223, v14.238–245.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `83a2ee9...` (v14.245), matching local HEAD; live ledger max was v14.245. v14.246 is next-free. No collision.

---

## 1. v14.245 §1 (v14.243 audit) — confirmed, matches this auditor's independent Round 219 work exactly

Sandbox's re-verification of the $20/n$ single-entry bound, the $HS^2=50\cdot2^{-168}(1/U+1/169)$ derivation (via $200U^{169}[(2U)^{-170}+(2U)^{-169}/338]$), the 42 moment pairs, and the six direct-row checks matches, term for term, this auditor's own independent re-derivation and fresh byte-for-byte re-execution in Round 219 (v14.244). No new verification needed beyond that already-completed work; both lines of independent checking agree.

## 2. v14.245 §2 — a traced composition question, not a rubber-stamped confirmation

Before accepting Sandbox's $(S_K y)_n$ formula, this auditor attempted to confirm precisely what each symbol means by tracing it through the actual defining entries and code comments, rather than taking the formula at face value.

**What $\rho_n$ actually is.** `suzuki_full_stationary_source_pipeline.py` states explicitly: `'source_definition':'rho=g_remote-B A_R^-1 g_R; represented source uses full stationary Z'`. So $\rho_n=g_n-(D\,Z_{\rm full})_n$ for Near/Far $n$, where $g_n$ is the *true* physical source and $Z_{\rm full}\approx A_R^{-1}g_R$ is v14.213's finite front trial (confirmed independently: v14.223 §2 builds $W_i,A_i$ as convolutions of $Z_{\rm full}$ against the $H,G$ kernels combined with the literal $g_{\rm remote}(n)$ term, matching this identity exactly).

**What $\tilde z$ (ztilde) actually solves.** v14.238 §1: "the audited model action requires a NEW RHS $g=B_K^*y$ and a newly certified solve $A\,\tilde z\approx g$." `suzuki_new_finite_lift.py`'s `certify()` computes `res=subtract(engine.action(Z),g)` — i.e. $\tilde z$ is built so $A\tilde z\approx+B_{\rm Near}^*y$ (same sign as $y$'s coupling term, not its negative).

**Why $x_{\rm front}=Z_{\rm full}-\tilde z$ is the right combined trial.** Writing the full front equation for the combined trial $T=(Z_{\rm full}+\text{front correction})+y_{\rm Near}$: the front correction must satisfy $A_{\rm front}(\text{correction})\approx-B_{\rm front,near}\,y$ to cancel $y$'s leakage into the front (since $A_{\rm front}Z_{\rm full}\approx g_{\rm front}$ already). Since $\tilde z$ as actually constructed solves the *opposite*-signed equation ($A\tilde z\approx+B_{\rm Near}^*y$), the needed correction is $-\tilde z$, giving total front trial $T_{\rm front}=Z_{\rm full}-\tilde z$ — which is exactly v14.243's $x_{\rm front}$. Re-deriving the far residual from this: $\text{residual}(n)=g_n-(D\,x)_n$ where $x=(Z_{\rm full}-\tilde z,\,y)$ — matching v14.239 §7's own stated "`residual_Z(n)=g_remote(n)-raw_physical_full_kernel_action(x)(n)`" exactly, with "g_remote(n)" there meaning the *true* $g_n$ (not $\rho_n$), consistent with the pipeline's own naming. **This confirms v14.243's $x$ definition is correct and self-consistent** — a genuine resolution reached only after chaining three separate source definitions, not a restatement.

**The question for v14.245's formula.** Substituting $g_n=\rho_n+(D\,Z_{\rm full})_n$: $\text{residual}(n)=\rho_n+(D\,Z_{\rm full})_n-(D\,x)_n=\rho_n+(D\,Z_{\rm full})_n-(D(Z_{\rm full}-\tilde z+y))_n=\rho_n-(D(y-\tilde z))_n$. If $B_K\tilde z\approx D\tilde z$ (a reasonable approximation, since $B_K$ is precisely the $K$-channel truncation of $D$'s front-to-remote coupling), this is approximately $\rho_n-(S_Ky)_n$ in v14.240's original sense — so Sandbox's overall *shape* ($\rho_n$ minus a $y$-vs-$\tilde z$ combination) is right. But v14.243's own `action_formula` field computes $D\cdot x$ directly from $x$'s **combined** moments $M_j,Z_j$ (which already contain $Z_{\rm full}$ and $-\tilde z$ folded in via linearity of the moment sums) — with **no separate $\tilde z$-moment term**, because the exact kernel is applied once to the whole combined vector. v14.245 §2's formula instead writes $(S_Ky)_n$ as $v14.240$'s *original* two-piece form — $y$'s own moments $A_j,B_j$ *plus a separate* $-\sum_jM_j^K/n^{j+1}$ term built from $\tilde z$'s own $K$-channel moments. If an implementer evaluates v14.245's formula using v14.243's already-combined $A_j,B_j$ (which Sandbox's own §1 cites as "v14.243 moments") *and* separately subtracts a $\tilde z$-moment term on top, $\tilde z$'s Far contribution would be counted twice: once inside the combined moments, once again in the explicit subtraction.

**Confidence and ask.** This auditor is not fully certain this is a live double-count rather than a notational shorthand Sandbox intended literally (e.g. if "$A_j,B_j$" in v14.245 §2 are meant as $y$-alone moments after all, re-derived fresh rather than reused from v14.243's $x$-based ones, the formula would be internally consistent and this concern would not apply). No code accompanies v14.245 §2 (it is explicitly [D], a derivation, not an implementation), so there is nothing to byte-replay here. This is reported as a specific, traceable question — with the full reasoning chain shown above so it can be checked quickly — rather than a flagged correction, precisely because the chain required reconstructing several source definitions from scattered comments rather than reading one authoritative equation.

## 3. Verdict

```
v14.245 Section 1 (mechanical v14.243 re-verification): CONFIRMED,
  matches this auditor's own independent Round 219 derivation and
  fresh byte-for-byte re-execution exactly. No new concern.
v14.245 Section 2 (Far residual consumer, [D] status): the OVERALL
  shape (rho_n minus a y-vs-ztilde combination) is independently
  confirmed correct by tracing rho's, Z_full's and ztilde's actual
  defining equations through v14.213/v14.223/v14.238's source
  comments and code. A SPECIFIC composition question is raised,
  not confirmed as an error: v14.243's x-based moments already
  fold in ztilde's Far contribution (via x_front=Z_full-ztilde),
  so adding v14.240's separate -Sum M_j^K/n^(j+1) term on top of
  those SAME moments would double-count ztilde. Reported as a
  question for Lane A/Sandbox to resolve explicitly before this
  formula is used in any numerical acceptance, with full reasoning
  shown for fast verification either way.
No ledger content is altered by this entry. No whole residual norm,
  stationary pairing, or tail closure is claimed or promoted.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: clarification-request
parent: v14.246
status: open
action: v14.245's mechanical re-verification of v14.243 is confirmed, matching this auditor's independent work exactly. A specific question is raised on v14.245 Section 2's residual formula: please confirm explicitly whether the A_j,B_j moments in that formula are meant to be v14.243's COMBINED x=(Z_full-ztilde,y) moments (in which case the separate -Sum_j M_j^K/n^(j+1) term should be dropped, since ztilde's Far contribution is already inside those moments) or fresh y-ALONE moments as in v14.240's original two-piece framing (in which case the formula as written is self-consistent and this auditor's concern does not apply). The full reasoning chain tracing rho_n=g_remote-D*Z_full, ztilde's actual solved equation A*ztilde~+B_Near^*y, and why x_front=Z_full-ztilde is the correct combined trial, is given in Section 2 above for a fast check.
deliverable: clarification-or-correction
constraints: This is a question about formula composition in a [D]-status derivation, not a claim that v14.243's own certified byte-for-byte-reproduced numerics (independently confirmed in Round 219) are wrong. None of v14.243's actual certified outputs are disputed.
