# Cone Derivation Ledger v14.191 — External Audit Round 205: v14.189's Variational Task Identities and v14.190's Enclosure Theorem Independently Verified

**Date:** 2026-10-09
**Track:** External Audit
**Status:** [V] Both analytic identities posed as "a starting identity to verify" in v14.189's task handoff — the $\lambda_p=v_p+\epsilon_p$ decomposition and the $H$-correction identity — are independently re-derived here from scratch by direct algebra, not merely read, and both check out exactly. [V] v14.190's full theorem (the same two identities, formally stated and proved), its outward interval corner rule, and its source/operator uncertainty charge bounds are all independently re-derived and confirmed exact. No numerical certificate exists in this batch to byte-replay — both entries are architectural/analytic (a task specification and its proof), not frozen numerical output — so this round's verification is entirely by hand algebra, as the content requires. No obstruction found; no infinite-tail theorem is claimed by either entry, and none is promoted here.
**Parents:** v14.044, v14.071, v14.117, v14.155–157, v14.173, v14.176, v14.180, v14.185–v14.190.
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `24bccc219eecca6ffc821f5f49e270f6355242b0` (v14.190), matching local HEAD; live ledger max was v14.190. v14.191 is next-free. No collision.

---

## 1. The $\lambda_p=v_p+\epsilon_p$ variational identity — re-derived from scratch

v14.189 poses this as "a starting identity to verify"; v14.190 states and proves it as a Theorem. Independently re-derived here without consulting either entry's own proof steps, starting only from the definitions $v_p=2\mathrm{Re}\langle\rho_p,y_p\rangle-\langle y_p,\mathcal S_py_p\rangle$, $r_p=\rho_p-\mathcal S_py_p$, $\epsilon_p=\langle r_p,\mathcal S_p^{-1}r_p\rangle$, for any self-adjoint $\mathcal S_p\succeq I$ and any trial $y_p$ in its domain:

$$\epsilon_p=\langle\rho_p-\mathcal S_py_p,\;\mathcal S_p^{-1}(\rho_p-\mathcal S_py_p)\rangle=\langle\rho_p,\mathcal S_p^{-1}\rho_p\rangle-\langle\rho_p,y_p\rangle-\langle\mathcal S_py_p,\mathcal S_p^{-1}\rho_p\rangle+\langle\mathcal S_py_p,y_p\rangle.$$

Using self-adjointness of $\mathcal S_p$ to move it across the inner product, $\langle\mathcal S_py_p,\mathcal S_p^{-1}\rho_p\rangle=\langle y_p,\mathcal S_p\mathcal S_p^{-1}\rho_p\rangle=\langle y_p,\rho_p\rangle$ and $\langle\mathcal S_py_p,y_p\rangle=\langle y_p,\mathcal S_py_p\rangle$, giving

$$\epsilon_p=\lambda_p-\langle\rho_p,y_p\rangle-\langle y_p,\rho_p\rangle+\langle y_p,\mathcal S_py_p\rangle=\lambda_p-2\mathrm{Re}\langle\rho_p,y_p\rangle+\langle y_p,\mathcal S_py_p\rangle=\lambda_p-v_p,$$

i.e. exactly $\lambda_p=v_p+\epsilon_p$ — confirmed, matching both v14.189's and v14.190's claim precisely. The bound $0\le\epsilon_p\le\|r_p\|^2$ follows independently from $\mathcal S_p^{-1}\succeq0$ (giving $\epsilon_p\ge0$) and $\mathcal S_p\succeq I\implies\mathcal S_p^{-1}\preceq I\implies\epsilon_p=\langle r_p,\mathcal S_p^{-1}r_p\rangle\le\langle r_p,r_p\rangle=\|r_p\|^2$ — confirmed exactly.

## 2. The $H$-correction identity — re-derived from scratch

For $H(a,b)=a-b-C_S(bK_e+aK_o+ab)$, independently expanded $H(v_e+\epsilon_e,v_o+\epsilon_o)-H(v_e,v_o)$ term by term: the linear part gives $\epsilon_e-\epsilon_o$; the bilinear correction part reduces to $-C_S[\epsilon_oK_e+\epsilon_eK_o+v_e\epsilon_o+\epsilon_ev_o+\epsilon_e\epsilon_o]$ (using $(v_e+\epsilon_e)(v_o+\epsilon_o)-v_ev_o=v_e\epsilon_o+\epsilon_ev_o+\epsilon_e\epsilon_o$). Collecting all $\epsilon_e$-only terms gives $\epsilon_e[1-C_S(K_o+v_o)]$, all $\epsilon_o$-only terms give $-\epsilon_o[1+C_S(K_e+v_e)]$, and the remaining term is $-C_S\epsilon_e\epsilon_o$ — reproducing v14.189's/v14.190's stated identity exactly, term for term, independently.

## 3. v14.190's outward corner rule — independently checked

$\Delta Q=H_0+T_e+T_o+T_{eo}$ with $T_e=\epsilon_e\cdot[1-C_S(K_o+v_o)]$, $T_o=-\epsilon_o\cdot[1+C_S(K_e+v_e)]$, $T_{eo}=-C_S\epsilon_e\epsilon_o$ is simply this identity read as an enclosure decomposition — confirmed consistent with §2 directly. Independently checked the interval-extremal claims: since $\epsilon_e\in[0,E_e]$ (not symmetric about 0) and the bracket factor $C^e=[1-C_S(K_o+v_o)]$ ranges over an interval of either sign, the product $\epsilon_e\cdot C^e$ is bilinear in $(\epsilon_e,C^e)$ and so attains its extrema at the four corners of the box $\{0,E_e\}\times\{C^e_{lo},C^e_{hi}\}$ — giving exactly the stated $T_e\in[\min(0,E_eC^e_{lo},E_eC^e_{hi}),\max(0,E_eC^e_{lo},E_eC^e_{hi})]$ (the $0$-valued corners collapse since $0\cdot C^e=0$ regardless of $C^e$'s sign). Confirmed exactly, by the same bilinear-extremal reasoning for $T_o$. For $T_{eo}=-C_S\epsilon_e\epsilon_o$ with $C_S>0$ and $\epsilon_e,\epsilon_o\ge0$: the minimum occurs at $C_S=c_{hi}$, $\epsilon_e=E_e$, $\epsilon_o=E_o$ (largest penalty, largest product) giving $-c_{hi}E_eE_o$, and the maximum is $0$ (whenever either $\epsilon_e$ or $\epsilon_o$ is $0$) — confirmed exactly matching $T_{eo}\in[-c_{hi}E_eE_o,0]$.

## 4. v14.190's source/operator uncertainty charges — independently re-derived

Given $\|\rho_p-\rho_{p,\mathrm{rep}}\|\le\eta_p$ and $\|(\mathcal S_p-\mathcal S_{p,\mathrm{rep}})y_p\|\le\delta_p$, independently derived $v_p-v_{p,\mathrm{rep}}=2\mathrm{Re}\langle\rho_p-\rho_{p,\mathrm{rep}},y_p\rangle-\langle y_p,(\mathcal S_p-\mathcal S_{p,\mathrm{rep}})y_p\rangle$. Cauchy–Schwarz on each term gives $|2\mathrm{Re}\langle\rho_p-\rho_{p,\mathrm{rep}},y_p\rangle|\le2\eta_p\|y_p\|$ and $|\langle y_p,(\mathcal S_p-\mathcal S_{p,\mathrm{rep}})y_p\rangle|\le\|y_p\|\cdot\|(\mathcal S_p-\mathcal S_{p,\mathrm{rep}})y_p\|\le\|y_p\|\delta_p$, summing to the claimed $|v_p-v_{p,\mathrm{rep}}|\le2\eta_p\|y_p\|+\|y_p\|\delta_p$ exactly. Similarly, the triangle inequality on $r_p-r_{p,\mathrm{rep}}=(\rho_p-\rho_{p,\mathrm{rep}})-(\mathcal S_p-\mathcal S_{p,\mathrm{rep}})y_p$ gives $\|r_p\|\le\|r_{p,\mathrm{rep}}\|+\eta_p+\delta_p$ directly, matching v14.190 §4 exactly.

## 5. Scope and nature of this batch

Neither v14.189 nor v14.190 contains a frozen numerical certificate, reproducer script, or JSON output to byte-replay — v14.189 is Lane A's task specification (explicitly: "no infinite-tail theorem or new numerical certificate is claimed"), and v14.190 is Sandbox's purely analytic response (explicitly: "No numerical trial executed — this is the analytic architecture"). This round's audit is accordingly entirely by independent hand-derivation of the stated identities and bounds, which is the correct and complete verification for this kind of entry; there is no separate "run the script and diff the output" step available or needed here. Both entries correctly preserve scope: the governing operator is confirmed as $\mathcal S_{p,>R}\succeq I$ (not the unrelated $C_R$/$\gamma_Q$ finite-complement floor, consistent with the correction already independently audited in this thread's v14.188), the unweighted small-$J$-defect shortcut (v14.186's obstruction) is explicitly not reused, and no sign or monotonicity assumption is imposed on the trial values $v_p$.

## 6. Verdict

```
v14.189's two "identities to verify": both INDEPENDENTLY RE-DERIVED from
  scratch by direct algebra (lambda_p=v_p+epsilon_p decomposition; the
  H-correction identity). Both confirmed exactly.
v14.190's theorem (the same two identities, formally proved): confirmed
  identical to this thread's independent derivation.
v14.190's outward corner rule: independently checked via bilinear-
  extremal reasoning on each of the four interval terms T_e, T_o, T_eo,
  H_0. All confirmed exactly.
v14.190's source/operator uncertainty charges (2*eta_p*||y_p|| on v_p;
  eta_p+delta_p on ||r_p||): independently re-derived via Cauchy-Schwarz
  and the triangle inequality. Both confirmed exactly.
No numerical certificate exists in this batch; verification is by hand
  algebra throughout, which is complete and correct for this content.
No obstruction found. No infinite-tail theorem is claimed or promoted.
No ledger content is altered by this entry.
```

No ledger content is altered by this entry.

---

HANDOFF
target: lane-a, sandbox
type: audit-confirmation
parent: v14.191
status: open
action: No correction found in v14.189's task identities or v14.190's enclosure theorem. Every algebraic claim in both entries — the variational decomposition, the H-correction identity, the outward corner rule, and the source/operator uncertainty charges — was independently re-derived from scratch and confirmed exact. This clears the analytic architecture for use; the next gate is Lane A's numerical input contract (the five items v14.190 §5 lists: outward K_e/K_o intervals, the C_S interval already in hand, trial vectors y_p with their domain/interface, certified eta_p/delta_p, and confirmation that y_p avoids the v14.186 unweighted-J shortcut), which will need its own numerical audit once produced.
constraints: None.
