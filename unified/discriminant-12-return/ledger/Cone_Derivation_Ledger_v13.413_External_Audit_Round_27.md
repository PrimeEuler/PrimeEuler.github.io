# Cone Derivation Ledger v13.413 — External Audit Round 27

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Scope

This round covers the new thread that picked up `v13.409`'s discriminant-return synthesis: `v13.410` (shell-displacement moment hierarchy / V4 energy) and the two entries originally filed as `v13.406`/`v13.407` (Pell-return discretization and CRT half-return), which collided with existing filenames and have been renamed to `v13.411`/`v13.412` as part of this round.

## 1. Housekeeping: a real version-number collision, now fixed

**[Audit → resolved]** Two new files landed as `unified/discriminant-12-return/ledger/v13.406_Pell_Return_Discretization_OEIS_Regulator.md` and `v13.407_CRT_Half_Return_and_Ramified_Basis.md` — reusing version numbers already taken by `Cone_Derivation_Ledger_v13.406_Odd_Certificate_Provenance_Reconciliation.md` and `Cone_Derivation_Ledger_v13.407_Odd_Finite_High_Midpoint_Replay.md` from Round 26, and dropping the standard `Cone_Derivation_Ledger_` filename prefix used by every other entry in the directory. This looks like a fresh session that didn't check `git ls-tree` for the current highest version before choosing numbers — exactly the collision-avoidance step this audit relationship has performed before every push. Content in both files is mathematically sound (verified below), so this is a pure bookkeeping issue, not a retraction. Renamed them to `v13.411` and `v13.412` (next available numbers after `v13.410`), added the standard filename prefix, and added a one-line renumbering note plus fixed internal cross-references (their self-citations of "v13.406" now point to "v13.411"). Content otherwise unchanged.

## 2. Shell-displacement moment hierarchy and V4 energy (`v13.410`) — verified exactly

**[D, independently verified]** This entry builds directly on `v13.409`'s shell identification: $\Delta X_k=X_k-X_k^{(0)}=-\delta_k(n)/2$, giving an exact bridge from the cone-shell coordinate to the classical fractional divisor defect. I wrote an independent script computing $\Delta X_k$, $\delta_k$, the moments $\mathcal S_1,\mathcal S_2,\mathcal E_X$, and the four-residue energy channels $\mathcal E_r$ directly from their raw definitions (not from the entry's closed forms) and checked every boxed identity:

- $\Delta X_k=-\delta_k(n)/2$ and $\mathcal S_1(n)=nH_n-D(n)=-2\sum\Delta X_k$: exact, all tested $n$.
- $\mathcal S_2(n)=4\mathcal E_X(n)$ and the inequality chain $4\mathcal E_X(n)=\mathcal S_2(n)\le\mathcal S_1(n)\le n-\tau(n)$: exact/holds, tested at $n\in\{12,30,60,100,144,221,360\}$.
- The V4 Hadamard energy transform $\tfrac14(Q_1^\times,Q_{-4},Q_{-3},Q_{12})^T=H_4(\mathcal E_1,\mathcal E_5,\mathcal E_7,\mathcal E_{11})^T$ and its inverse $E=\tfrac1{16}H_4Q$: matched exactly at $n\in\{12,30,60,100,144,221\}$ (my first attempt at this check had a bug in my own test script — an extra spurious factor of 4 — caught and fixed before concluding; noting this so the fix isn't mistaken for a finding against the entry).

The entry's own honesty is worth calling out: §5 explicitly flags that $E_\chi,Q_\chi$ do **not** inherit Euler-product multiplicativity from $n$'s prime exponents, unlike the zero-set data $D_\chi$ — a correct and appropriately modest limitation, not glossed over.

## 3. Pell-return discretization (`v13.411`, formerly `v13.406`) — verified exactly

**[D, independently verified]** Reconstructed the Pell sequences from scratch via the integer recurrence $x_{n+1}=2x_n+3y_n,\ y_{n+1}=x_n+2y_n$ (from $(2+\sqrt3)(x_n+y_n\sqrt3)$) rather than trusting the entry's stated values: got $x_n=1,2,7,26,97,362,1351,\ldots$ and $y_n=0,1,4,15,56,209,780,\ldots$, matching OEIS A001075/A001353 exactly as claimed, with $x_n^2-3y_n^2=1$ holding at every term. Confirmed $g_{12}^n=\begin{pmatrix}x_n+y_n&y_n\\2y_n&x_n-y_n\end{pmatrix}$ exactly via direct matrix powers for $n=0,\ldots,6$, and $\operatorname{tr}(g_{12}^n)=2x_n=2,4,14,52,194,724,2702,\ldots$ matching OEIS A003500. Confirmed the mod-12 claims directly: $g_{12}^6\equiv7I\pmod{12}$, $g_{12}^{12}\equiv I\pmod{12}$, order exactly 12.

The regulator identity $L(1,\chi_{12})=\log(2+\sqrt3)/\sqrt3$ follows from the class-number-formula value already on record in `research-notes/Divisor_Summatory_V4_Mod12_Findings.md` ($L(1,\chi_{12})=2h(12)\log(2+\sqrt3)/\sqrt{12}$) with $h(\mathbf Q(\sqrt3))=1$ substituted in — arithmetic check only, not re-derived from the class-number formula itself this round.

**Worth flagging as good practice**: §4–5 explicitly warn against conflating the cyclic Pell-return subgroup with the geometric $V_4$ shell action ("powers of $g_{12}$ do not produce $5I$ or $11I$... the Pell cyclic return must not be identified with $U(12)\cong V_4$"), and §6 explicitly prefers the more modest "same regulator, two distinct roles" framing over a stronger identification claim. This is exactly the discipline this ledger has needed at several points earlier in this audit relationship (most notably the Casimir-quarter guardrail), applied proactively here rather than after a correction.

## 4. CRT half-return (`v13.412`, formerly `v13.407`) — verified exactly

**[D, independently verified]** Checked every claimed congruence directly by modular matrix exponentiation, not by trusting the entry: $g_{12}^3\equiv-I\pmod3$ (computed $g_{12}^3\bmod3=2I$, and $2\equiv-1\pmod3$ ✓), $g_{12}^6\equiv I\pmod3$ (order 3 is exactly 6 ✓); $g_{12}^2\equiv-I\pmod4$ (computed $3I$, $3\equiv-1\pmod4$ ✓), $g_{12}^4\equiv I\pmod4$ (order 4 exactly 4 ✓). The CRT solve ($r\equiv1\pmod3,\ r\equiv-1\pmod4\Rightarrow r=7$) checked directly: $7\bmod3=1$, $7\bmod4=3\equiv-1$ ✓. The full $U(12)\leftrightarrow(\mathrm{sign}\bmod3,\mathrm{sign}\bmod4)$ table in §6 ($1\leftrightarrow(+,+),5\leftrightarrow(-,+),7\leftrightarrow(+,-),11\leftrightarrow(-,-)$) reproduced exactly.

This entry's own guardrail discipline is again worth noting explicitly: §6 states the CRT correspondence is "only an intersection of symmetry layers," not an identification, and §7 poses the natural next question (do 5 and 11 arise from combining the Pell return with an existing involution) as something to "test at the operator level before assigning geometric meaning" — precisely the right posture for a genuinely new observation.

## 5. Overall verdict

Strong round. Every boxed claim across all three entries was independently reconstructed from raw definitions (not copied and merely re-run) and checked exactly — divisor-defect moments, Pell/OEIS sequences, matrix powers mod 3/4/12, and the CRT table all matched. No mathematical errors found. The one real issue was the version-number collision, now fixed. The new thread's own guardrail language (repeatedly distinguishing "same regulator, different roles" from "identification," and flagging its own open questions as open) shows the project's self-correction discipline propagating correctly into freshly-started sessions, not just surviving within a single continuous one.

## 6. Scope note

Not independently re-derived this round: the class-number formula itself (used, not proved, for the $L(1,\chi_{12})$ identity); the mod-2 Frobenius identification in `v13.412` §4 (cited from earlier audited material, not re-checked here).

## Guardrails

All guardrails from prior rounds remain in force. No new guardrail needed — this round's entries already state the relevant ones themselves.

**External audit round 27: CLOSED. `v13.410`–`v13.412` (the latter two renumbered from a `v13.406`/`v13.407` collision, content unchanged) independently verified exactly: shell-displacement/V4-energy moment hierarchy, Pell/OEIS sequence identities, and CRT half-return structure. No mathematical errors found; one filename collision fixed.**
