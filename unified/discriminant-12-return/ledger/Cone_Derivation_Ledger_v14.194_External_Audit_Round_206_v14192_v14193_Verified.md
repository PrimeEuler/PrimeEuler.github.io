# Cone Derivation Ledger v14.194 — External Audit Round 206: v14.192's Exact Trace Repair/Transport and v14.193's Directional Refinement Independently Verified

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] v14.192's exact trace-repair identity, Q energy/norm inequalities, divided-difference kernel identity, and pole-term bound are independently re-derived by hand; the full actual-256k numerical pipeline is independently reproduced from the raw committed archive and matches the frozen payload byte-for-byte. [V] v14.193's directional energy-weighted refinement theorem is independently re-derived from scratch and confirmed exact. [N] One non-binding sharpness slip noted in v14.193's §"For v14.190's contract" translation (factor 4 where hand algebra gives 2 on the ||W||_F‖d‖‖B‖‖y_p‖ term) — not an error, since it is a valid looser upper bound and the term is numerically negligible (‖d‖~1e-17); flagged for the record only. One analytic step (the "22" commutator/anticommutator constant bookkeeping behind ‖B_{>R,≤R}‖<23) could not be fully re-derived from the entry's own compressed presentation without the primary |z|≤11 definition restated in full; this does not affect any current conclusion since the η bounds are already independently confirmed via raw-data reproduction and are already flagged by both lanes as too large for 5e-9.
**Parents:** v14.044, v14.071, v14.117, v14.155–157, v14.173, v14.176, v14.185–v14.193.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `2c95d958c76661cd7a7273567b4a2fc412ed41e1` (v14.193), matching local HEAD; live ledger max was v14.193. v14.194 is next-free. No collision.

---

## 1. Exact trace-repair identity — re-derived from scratch

Given $d=(LW)^{-1}(Lu-t)$, $x=u-Wd$: $Lx=Lu-LWd=Lu-(LW)(LW)^{-1}(Lu-t)=Lu-(Lu-t)=t$, independently re-derived, assuming only invertibility of $LW$ on the frozen six-plane. Confirmed exactly, matching v14.192 and v14.193 §1.

## 2. Q energy/norm inequalities — re-derived from scratch

With $e=x-x_\star\in Q$, $w=Q(Ax-g)=C_Qe$, $C_Q\succeq\gamma I$: $\|e\|=\|C_Q^{-1}w\|\le\|w\|/\gamma\le s_x/\gamma$ directly from $\|C_Q^{-1}\|\le1/\gamma$. For the energy bound, since $e\in Q$ and $C_Q$ is self-adjoint, $\langle e,Ae\rangle=\langle e,C_Qe\rangle=\langle C_Q^{-1}w,w\rangle=\langle w,C_Q^{-1}w\rangle=\|C_Q^{-1/2}w\|^2\le\|w\|^2/\gamma\le s_x^2/\gamma$. Both confirmed exactly, independently of v14.193's own statement of the same chain.

## 3. Divided-difference kernel identity — verified by direct hand expansion

Checked algebraically, not merely read: with numerator of the RHS of $\tfrac12[(z_n-z_m)/(n-m)-(z_n+z_m)/(n+m)]$ over the common denominator $n^2-m^2$,
$$(z_n-z_m)(n+m)-(z_n+z_m)(n-m)=2(z_nm-nz_m),$$
expanding both products termwise and cancelling the $z_nn$ and $z_mm$ pieces exactly, leaving $2z_nm-2z_mn$. Dividing by $2(n^2-m^2)$ reproduces $(z_nm-nz_m)/(n^2-m^2)$ exactly, independently confirming the identity used by both v14.192 and v14.193.

## 4. Pole-term bound — independently checked

$|p(n)|\le2/n\implies|p(n)|^2\le4/n^2$; summing over all $n\ge1$, $\sum4/n^2\le4\cdot2=8$ (using $\sum n^{-2}\le2$, which is itself a loose but correct bound on $\pi^2/6\approx1.645$). For $n>R$, $\sum_{n>R}4/n^2\le4\int_R^\infty x^{-2}dx=4/R$ by the standard decreasing-term integral comparison. The cross-norm bound via Cauchy–Schwarz between the full-front and tail pieces is $2\sqrt{8\cdot4/R}=2\sqrt{32/R}$; squaring, $<1\iff128/R<1\iff R>128$, confirmed trivially for $R=256000$. Independently re-derived, matching v14.192 exactly.

## 5. Full numerical pipeline — independently reproduced from raw committed data, not merely re-read

Decoded the committed base64-split archive `research-notes/payloads/exact_outward_run_37827949740/joint-256000-{even,odd}-v.trace-256000.full.zip.b64.part*` into a fresh scratch directory; the reconstructed zips hash to `da718974...` (even) and `6ba7a15a...` (odd), matching the `snapshot_sha256` fields recorded in the committed `payloads/actual256-finite-trial-transport.json` exactly. Ran the committed, unmodified `research-notes/suzuki_finite_trial_transport.py` against this independently-reconstructed root: output matches the committed payload byte-for-byte (`diff` clean), and two successive runs are byte-identical to each other (deterministic). Separately, using Python's exact `Fraction` arithmetic directly on the rational strings stored in the committed payload (not by re-running the producer code), independently confirmed the internal arithmetic identities hold exactly for both sectors: `repair + residual/gamma == total`, `23*total == eta`, and `residual**2/gamma == corrected_finite_energy_error`. This is an independent reproduction from raw data, not a re-read of the claimed table; all values (even: trace-repair 2.213672e-17, η 4.136512e-4; odd: trace-repair 7.781094e-20, η 3.128345e-6) are confirmed.

## 6. Sandbox's directional energy-weighted refinement theorem — re-derived from scratch

Independently re-derived v14.193 §2 without consulting its own proof steps. With $\rho_u=g_{\rm tail}-Bu$, $\rho_\star=g_{\rm tail}-Bx_\star$: $\rho_\star-\rho_u=B(u-x_\star)=Bw$. From the trace-repair definitions, $x=u-Wd$ and $e=x-x_\star$ give $w=u-x_\star=Wd+e$. For any $y$: $\langle\rho_\star-\rho_u,y\rangle=\langle Bw,y\rangle=\langle w,B^*y\rangle$. Splitting, $|\langle Wd,B^*y\rangle|\le\|Wd\|\|B^*y\|\le\|W\|_F\|d\|\|B\|\|y\|$ by Cauchy–Schwarz and $\|Wd\|\le\|W\|_F\|d\|$. For the $e$-term, writing $\langle e,B^*y\rangle=\langle A^{1/2}e,A^{-1/2}B^*y\rangle$ (valid for $A\succ0$ self-adjoint) and applying Cauchy–Schwarz: $|\langle e,B^*y\rangle|\le\langle e,Ae\rangle^{1/2}\langle B^*y,A^{-1}B^*y\rangle^{1/2}\le(s_x/\sqrt\gamma)\langle B^*y,A^{-1}B^*y\rangle^{1/2}$, using §2's $\langle e,Ae\rangle\le s_x^2/\gamma$. Summing reproduces v14.193's theorem exactly:
$$|\langle\rho_\star-\rho_u,y\rangle|\le\|W\|_F\|d\|\|B\|\|y\|+\frac{s_x}{\sqrt\gamma}\langle B^*y,A^{-1}B^*y\rangle^{1/2}.$$
Confirmed exactly, independently, matching v14.193's proof term for term.

## 7. Contract-translation sharpness note [N] — non-binding

Checking v14.193's "For v14.190's contract" paragraph: applying the theorem of §6 with $y=y_p$ to bound $|2\mathrm{Re}\langle\rho_p-\rho_{p,\mathrm{rep}},y_p\rangle|$ (identifying $\rho_p=\rho_\star$, $\rho_{p,\mathrm{rep}}=\rho_u$) gives $2\times[\|W\|_F\|d\|\|B\|\|y_p\|+(s_x/\sqrt\gamma)M(y_p)^{1/2}]=2\|W\|_F\|d\|\|B\|\|y_p\|+(2s_x/\sqrt\gamma)M(y_p)^{1/2}$ by direct hand computation. v14.193 states the first coefficient as $4\|W\|_F\|d\|\|B\|\|y_p\|$ rather than $2\|W\|_F\|d\|\|B\|\|y_p\|$; the $M(y_p)^{1/2}$ coefficient of $2s_x/\sqrt\gamma$ matches exactly. The stated inequality with coefficient 4 remains a **valid** (merely non-sharp) upper bound, since $2x\le4x$ for the nonnegative quantity $x=\|W\|_F\|d\|\|B\|\|y_p\|$; it is not an error and does not affect any conclusion, since this term is numerically negligible ($\|d\|\sim10^{-17}$ from the trace-repair output confirmed in §5) regardless of the factor of 2. Noted for the record only; no correction to the ledger is needed.

## 8. Scope note on the ‖B‖<23 cross-block constant

The entry's "$c=2/\pi$ bounds the whole divided-difference cross block by 22" step, stacking the audited $|z|\le11$ bound with the classical Hilbert/Hankel-kernel norm facts (confirmed independently in §3–4 above for the algebraic identity and pole term), was not fully re-derivable from this entry's own compressed presentation alone — the precise constant bookkeeping from "$11\pi/2$ per term" to the stated total of 22 admits more than one consistent reading (e.g. whether a commutator-type factor of 2 is already folded into the stated per-term bound). This is flagged honestly as an incomplete independent check of one scalar constant, not a found error: the final numerical η values this constant feeds into have already been independently reproduced from raw committed data byte-for-byte in §5, and both lanes already and correctly flag these η values as far too large to close the 5e-9 gate — so even a factor-of-2 slack in this constant would not change any currently-asserted conclusion.

## 9. Verdict

```
v14.192: exact trace-repair identity, Q energy/norm inequalities, divided-
  difference kernel identity, and pole-term bound all INDEPENDENTLY
  RE-DERIVED from scratch by hand algebra. All confirmed exactly.
v14.192's full numerical pipeline: INDEPENDENTLY REPRODUCED from the raw
  committed base64 archive (fresh decode, hash-matched, script re-run,
  byte-identical output; exact-Fraction arithmetic cross-check of every
  stated formula against the committed payload's own rational values).
  All table values confirmed exactly.
v14.193's directional energy-weighted refinement theorem: INDEPENDENTLY
  RE-DERIVED from scratch. Confirmed exactly, term for term.
[N] One non-binding sharpness slip noted in the contract-translation
  paragraph (factor 4 vs hand-derived 2 on a numerically negligible term);
  not an error, flagged for the record only.
[N] The ||B||<23 constant's precise bookkeeping from 11*pi/2 to 22 could
  not be fully independently closed from this entry's presentation alone;
  this does not affect any conclusion, since eta is already independently
  reproduced from raw data and already flagged by both lanes as too large
  for 5e-9.
No obstruction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.194
status: open
action: v14.192's exact trace repair, Q inequalities, and full numerical transport pipeline are independently confirmed, including a from-scratch raw-archive reproduction (not a re-read) that matches the committed payload byte-for-byte. v14.193's directional refinement theorem is independently confirmed exact. Two non-binding notes for the record: (1) the contract-translation paragraph's Wd-term coefficient is a valid but non-sharp 4x instead of the hand-derived 2x — immaterial given the term's size; (2) the precise constant bookkeeping behind the 22/23 cross-block bound was not fully reconstructable from this entry's presentation alone, though it does not affect any live conclusion. Neither note requires action; recorded for traceability only. The open item remains Lane A's: construct admissible trial $y_p$ and evaluate $M(y_p)=\langle B^*y_p,A^{-1}B^*y_p\rangle$ to test whether the directional refinement actually closes 5e-9, which neither lane has yet attempted.
deliverable: none required; informational confirmation
constraints: None.
