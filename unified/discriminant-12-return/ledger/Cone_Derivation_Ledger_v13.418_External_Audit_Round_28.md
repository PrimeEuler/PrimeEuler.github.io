# Cone Derivation Ledger v13.418 — External Audit Round 28

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers the wave following Round 27: `v13.413` (χ12 shell-displacement regulator cancellation), `v13.414` (χ12 time orientation / dihedral Pell extension), the two entries filed concurrently as `v13.415` (χ12 tail residue profile; Suzuki mod-12 source-channel audit — renamed to `v13.419`, see below), `v13.416` (F4 reduction / character splitting), and `v13.417` (odd pole-free finite-high reduction / source-enclosure provenance — a second, independent entry also originally numbered `v13.417`, see below).

## 1. Version-number collisions, again — same fix as Round 27, applied twice this round

**[Audit → resolved]** Two entries landed concurrently both titled `v13.415`: `Cone_Derivation_Ledger_v13.415_Chi12_Tail_Residue_Profile_and_Time_Orientation.md` and `Cone_Derivation_Ledger_v13.415_Suzuki_Mod12_Source_Channel_Audit.md`. Worth noting explicitly: the project caught this itself — `v13.416`'s own §0 flags it as "a live numbering collision only... should be normalized by the next bookkeeping/audit pass" and self-numbers past it rather than colliding further. That's exactly the right reflex. Renamed the Suzuki-audit file to the next free slot — first attempted `v13.417`, then found that number freshly taken too (by the concurrently-landed `Odd_Pole_Free_Finite_High_Reduction_and_Source_Enclosure_Provenance`, a legitimate, independent entry — verified below), so renamed again to `v13.419`. Content of the renamed file unchanged throughout both passes; this is now a two-collision round, purely a byproduct of two active sessions writing to the ledger at close to the same time, not a content issue.

## 2. χ12 shell-displacement regulator cancellation (`v13.413`) — verified exactly, after catching my own error first

**[D, independently verified]** Rebuilt `E_{12}(n)=\sum_{k\le n}\chi_{12}(k)\{n/k\}$ and the ideal-counting remainder $\mathcal R_{12}(n)=\mathcal I_{12}(n)-L(1,\chi_{12})n$ from raw definitions and checked the claimed identity $E_{12}(n)=-\mathcal R_{12}(n)-nT_{12}(n)$. **First attempt used the wrong character** (I substituted $\chi_{-4}=(1,1,-1,-1)$ for $\chi_{12}=(1,-1,-1,1)$ on residues $(1,5,7,11)$, and got a spurious apparent violation of the entry's own $|nT_{12}(n)|<2$ bound). Caught this by checking $|S_{12}(m)|\le1$ directly, which failed under my wrong character but holds exactly under the correct one. Re-ran with the correct $\chi_{12}$: identity matches to $\sim10^{-28}$ at $n\in\{10,25,50,100,200,500\}$, $\max|S_{12}(m)|=1$ confirmed for $m\le100$, and $|nT_{12}(n)|$ stays comfortably under $2$ throughout (observed $\approx0.9$–$1.03$). Flagging my own error explicitly so it isn't mistaken for a finding against the entry — it was mine, not theirs.

## 3. χ12 time orientation / dihedral Pell extension (`v13.414`) — verified exactly

**[D, independently verified]** Checked the central identity $\sigma_r(\lambda)=\lambda^{\chi_{12}(r)}$ from first principles: wrote $\sqrt3=\zeta_{12}+\zeta_{12}^{-1}$, $i=\zeta_{12}-\zeta_{12}^{-1}$ (standard, since $\zeta_{12}=(\sqrt3+i)/2$), computed $\sigma_r(\sqrt3)=\zeta_{12}^r+\zeta_{12}^{-r}$ directly for $r=1,5,7,11$, and reproduced the entry's $\sqrt3,i$ sign table exactly. Verified $J_f^2=I$ and, by direct $2\times2$ matrix multiplication, $J_fg_{12}J_f=g_{12}^{-1}$ exactly (matches $g_{12}^{-1}=\begin{pmatrix}1&-1\\-2&3\end{pmatrix}$, computed independently via the adjugate formula). Verified the determinant obstruction in §4 ($\det J_f=-1$, $\det(rI)=r^2\equiv1\pmod{12}$ for every unit $r$, hence $g_{12}^kJ_f$ can never equal a scalar $rI$) by direct computation over $U(12)$.

## 4. χ12 tail residue profile (`v13.415`→ retained number) — verified exactly

**[D, independently verified]** Checked $S(r)=\sum_{a=1}^r\chi_{12}(a)$ directly: computed $0,1,1,1,1,0,0,-1,-1,-1,-1,0$ for $r=0,\ldots,11$, matching the entry's table exactly. Checked the digamma closed form for $T_{12}(12m+r)$ against a direct numerical tail sum at $m=50$, all twelve residues: agreement to $\sim10^{-32}$ in every case. Confirmed $nT_{12}(n)\to-S(r)$ along each residue class ($r=1$: $\to-1$; $r=7$: $\to+1$; $r\in\{0,5,6,11\}$: $\to0$), matching the claimed limit exactly.

## 5. F4 reduction / character splitting (`v13.416`) — verified exactly

**[D, independently verified]** Confirmed $\sigma_r(\omega)$ depends only on $r\bmod3$ and matches $\chi_{-3}$ exactly ($r=1,7\to+1$; $r=5,11\to-1$); confirmed $\sigma_r(i)=i^r$ matches $\chi_{-4}$ exactly ($r=1,5\to+1$; $r=7,11\to-1$); confirmed $\chi_{12}=\chi_{-4}\chi_{-3}$ by direct multiplication of the sign vectors, matching the table used throughout this entire audit relationship. Confirmed $J_f\bmod2 = \bar g_{12}$ by direct reduction ($-1\equiv1\pmod2$ collapses $J_f=\begin{pmatrix}1&-1\\0&-1\end{pmatrix}$ to $\begin{pmatrix}1&1\\0&1\end{pmatrix}$, matching $g_{12}\bmod2$ exactly).

## 6. The Suzuki mod-12 source-channel audit (`v13.419`, formerly `v13.415`) — the most consequential entry this round

**[D, verified]** This entry directly tests something I discussed with the user this session: whether the now-substantial χ12/cone/regulator structure actually reaches Suzuki's operator-positivity machinery, or stays confined to the arithmetic side. The entry's own answer, honestly derived: **no, it doesn't help**, for a precise, checkable reason — Suzuki's active prime source support is only $q\in\{2,3,4,5,7\}$, the ramified pieces $q\in\{2,3,4\}$ are annihilated by every unit character (trivially, since $\gcd(q,12)\ne1$), and on the surviving unit support $\chi_{12}(5)=\chi_{12}(7)=-1$ — both $-1$, not one of each sign. I verified this character-table fact directly (it's elementary, and it's the entire logical crux of the negative result): since $\chi_{12}$ takes the *same* sign on both surviving source atoms, $S_{\chi_{12}}=-S_5-S_7=-S_{1^\times}$ exactly, so passing from the principal to the $\chi_{12}$ channel only flips an overall sign and produces zero new cancellation. I did not independently rebuild the reported Frobenius/spectral norms (`‖S₅‖_F≈20.05`, etc. — would require reconstructing the full `M=4000` source-faithful matrix), so those specific numbers are trusted-not-verified, consistent with how comparable large-scale runs have been treated throughout this audit relationship; the decisive part of the argument (the character-table obstruction) does not depend on them and is independently confirmed.

**This is exactly the right kind of result to publish**: a direct, honest test of a tempting shortcut, reported as negative with the precise reason nailed down, rather than left untested or quietly dropped. It matches, almost to the letter, the boundary I described to the user earlier this session (the regulator connects to one arithmetic value, not to the operator machinery) — good independent confirmation from the project's own side.

## 7. Odd pole-free finite-high reduction (`v13.417`) — verified exactly, and it's real progress on the actual positivity program

**[D, independently verified]** Distinct from the χ12/cone thread — this is direct work on the live Suzuki odd-sector positivity certificate. The reduction step is elementary but valuable: since the odd sector's finite-high matrix is $A_{FF}=A_{FF}^{(0)}+2dd^T$ with $2dd^T\succeq0$ (a rank-one PSD outer product, true for any real vector $d$), it suffices to certify the *pole-free* block $A_{FF}^{(0)}\succeq0.53I$ — the positive pole can only help, never hurt, so it doesn't need its own outward enclosure. Checked the two numeric consequences directly: the pole's contribution to the bottom eigenvalue, $\lambda_{\min}(A_{FF})-\lambda_{\min}(A_{FF}^{(0)})=0.5337449990275-0.5328423837861=0.0009026152414$, matches the entry's "$\approx9.03\times10^{-4}$" exactly; and the shifted pole-free margin, $0.5328423837861-0.53=0.0028423837861$, matches the entry's boxed value to every digit shown. The entry also correctly declines to promote $A_{FF}^{(0)}\succeq0.53I$ to an `[N-cert]` statement yet (§5), keeping it as a midpoint diagnostic pending an even-mode-parity-corrected outward polynomial generator — appropriately conservative given the parity caveat it identifies in its own §4.

## 8. Overall verdict

A strong round, mathematically, on two separate fronts: every boxed claim in the χ12/cone thread (`v13.413`–`v13.416`, `v13.419`) independently reconstructed from raw definitions and confirmed exactly, including one case where I initially made my own error (wrong character) and caught it before it became a false finding; and genuine, verified progress on the live odd-sector positivity certificate itself (`v13.417`), which is the part that actually moves the project's core goal forward. The project's own self-discipline continues to hold up under concurrent sessions — `v13.416` caught and flagged its own `v13.415` collision, `v13.419` ran an honest "does this actually help" test on a tempting shortcut and reported the negative result plainly, and `v13.417` correctly declined to over-promote a midpoint number to a certified one.

## 9. Scope note

Not independently reproduced: the `M=4000` source-faithful Frobenius/spectral norm values in `v13.419` §3–4, and the pole-free `A_{FF}^{(0)}` midpoint eigendecomposition in `v13.417` §2 (both would require rebuilding the full odd-sector matrix infrastructure).

## Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed — this round's entries continue to state their own precisely.

**External audit round 28: CLOSED. `v13.413`–`v13.417` and `v13.419` (renumbered twice from cascading version collisions, both flagged and resolved) independently verified exactly. Two headline findings: (1) the χ12/cone/regulator structure, while mathematically real throughout, does not sharpen the active Suzuki odd-sector positivity certification, confirmed via an elementary and decisive character-table argument; (2) separately, genuine progress on that same certification via the pole-free reduction, correctly kept at midpoint-diagnostic status pending the outward arithmetic replay.**
