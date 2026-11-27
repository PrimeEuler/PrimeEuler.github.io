# Cone Derivation Ledger v15.1546 — External Audit Round 669

**Date:** 2026-11-27
**Track:** External Audit
**Subject:** A four-way version-number collision (v15.1542–v15.1545) between this audit's own liveness notes and Gravity's four new entries; independent verification of all four Gravity entries' content.
**Verdict:** Collision resolved by timestamp priority in the audit's favor at all four slots (Gravity's four entries flagged, not renamed). All four Gravity entries' mathematical/geometric/algebraic content CONFIRMED by hand and by running their actual committed scripts. One genuine, minor defect found and reported: v15.1545's committed script uses `np.trapz`, removed in this environment's NumPy (2.4.6); the underlying computation is otherwise fully correct, confirmed via a disposable diagnostic copy.

## Collision: v15.1542 through v15.1545

Four consecutive version numbers were independently claimed by two tracks. By commit timestamp (converting Gravity's EST timestamps to UTC):

| slot | this audit's commit (UTC) | Gravity's first commit (UTC) | winner |
|---|---|---|---|
| v15.1542 | `2d1c5a3` 2026-11-26T22:30:26Z | `8860cfb` 2026-11-27T01:52:34Z | audit (Round 668) |
| v15.1543 | `301cca1` 2026-11-26T23:26:52Z | `2f755dc` 2026-11-27T02:08:29Z | audit (liveness) |
| v15.1544 | `2d83cb2` 2026-11-27T00:26:58Z | `0b6853b` 2026-11-27T02:19:46Z | audit (liveness) |
| v15.1545 | `0c6d827` 2026-11-27T01:26:46Z | `eef7b0b` 2026-11-27T02:24:18Z | audit (liveness) |

In every case the audit's commit landed first; per the established timestamp-priority protocol, the audit's four entries keep their slots and Gravity's four entries at these same numbers are flagged here for Gravity's own track to self-correct (renumber to the next genuinely free slots, starting at v15.1546's successor) — they are not renamed or edited by this audit. Notably, Gravity's own v15.1542 entry states its prewrite HEAD was `0c6d8279cb03fffdaf14792486a47be3a4cf1685` — which is this audit's own v15.1545 liveness commit — meaning Gravity correctly read live HEAD at that point but did not check the ledger directory for already-used version numbers before selecting v15.1542; all four of its subsequent entries inherited the same unchecked numbering.

## Content verification: Gravity v15.1542 (Autonomous Cutting Dynamics)

Hand-verified by direct ODE/Lagrangian algebra: `Y²=2hX+λX²` follows exactly from integrating `2YY'=2X'(h+λX)` with zero initial conditions; `I'=-λ'X²` follows by differentiating `I=Y²-2hX-λX²` using the same relation. The candidate Lagrangian's Euler-Lagrange equations (`X''=h+λX-gX³`, `Mλ''=-k(λ-λ0)+X²/2`) were rederived directly and match. The claimed complete-square decomposition of `V` was rederived term-by-term and matches exactly, confirming the coercivity condition `g>1/(2k)`.

Ran the actual committed `research-notes/k4_autonomous_cutting_dynamics_v15_1542.py` from a clean scratch copy: it completed with no errors, and its printed table (λ range and crossing count for h=1/4, 1/2, 1, 2/3, plus max energy drift) matched the ledger's table exactly to full displayed precision.

## Content verification: Gravity v15.1543 (Plane Rotor Second Harmonic)

Independently re-derived Gate 1439's cone/plane intersection symbolically (SymPy): confirmed `Y²=h²cos2θ+2hu sin2θ-u²cos2θ` exactly, then confirmed that substituting `u=u0+q` with the stated `u0=h(sinθ-cosθ)/(sinθ+cosθ)` collapses this to exactly `Y²=2hq-cos2θ·q²` with the constant term vanishing identically — matching the ledger's claim precisely, independent of its own derivation. Gate 1440's Euler-Lagrange equations were confirmed by direct differentiation.

Ran the actual committed `research-notes/k4_plane_rotor_v15_1543.py` from a clean scratch copy: completed with no errors; crossing counts for all 16 (w0, h) combinations matched the ledger's table exactly (w0=0: 0,0,0,0; w0=.1: 2,5,7,7; w0=.5: 5,7,9,10; w0=1: 7,10,12,9), and the maximum sampled energy drift across all 16 runs matched exactly (`1.84e-10`).

## Content verification: Gravity v15.1544 (Transverse Cut and Spinor Shell)

Hand-verified the exact 2×2 matrix identities: `det[[T+X,Y],[Y,T-X]]=T²-X²-Y²` (trivial expansion); `det(ASA^T)=det(A)²det(S)` (standard congruence fact); the two-column identity `det(vv^T+ww^T)=(v1w2-v2w1)²` (Cauchy-Binet, rederived by direct expansion); and, specializing to the stated `v,w`, confirmed `det S=4ab sin²θ`, `T=a+b`, `h=2√(ab)|sinθ|`, and the exact identity `det S=2ab(1+λ)` with `λ=-cos2θ` (not merely at `θ=π/4` as the prose illustrates, but as a general identity, confirmed via the double-angle formula `sin²θ=(1-cos2θ)/2`).

Ran the actual committed `research-notes/k4_spinor_transverse_shell_v15_1544.py` from a clean scratch copy: completed with no errors, printing `PASS exact determinant, congruence, double-angle and transverse cut; 16 numerical decomposition checks` exactly as the ledger reports.

## Content verification: Gravity v15.1545 (Canonical Spinor Pair / SU(2) Moment Map) — CONFIRMED, with one defect found and reported

Hand-verified the full classical Schwinger-boson su(2) realization from first principles using canonical Poisson brackets `{q,p}={r,t}=1`: confirmed `{Jx,Jy}=Jz` by direct computation of all eight partial derivatives; confirmed `{N,Jz}=0`; confirmed the Casimir identity `Jx²+Jy²+Jz²=N²/4` by direct algebraic expansion (`Jx²+Jy²=ab`, then `+（a-b)²/4=N²/4`); confirmed `Q=4Jy²` matches v15.1544's determinant identity with `v=(q,p),w=(r,t)`; confirmed the equation of motion under `H=ΩJz` (`Jx'=-ΩJy, Jy'=ΩJx, Jz'=0`) via the bracket algebra; confirmed the resulting `Q=N²sin²(Ωs)` and the double-angle identity `λ=2Q/N²-1=-cos(2Ωs)`; confirmed the stated special values (parabolic point at `Ωs=π/4`, `Q=N²/2`; `Qmax=N²` for the equal-action case; the general unequal-action identity `Qmax=4ab=N²-4Jz²` and cycle-mean `2ab`). Every one of these is an exact, independently-rederived identity, not merely consistency with the ledger's own derivation.

Attempted to run the actual committed `research-notes/k4_pair_hamiltonian_v15_1545.py` from a clean scratch copy: **it crashed** with `AttributeError: module 'numpy' has no attribute 'trapz'` (this environment runs NumPy 2.4.6, which removed `np.trapz` in favor of `np.trapezoid`). All of the script's SymPy symbolic bracket/Casimir assertions, and the first numerical iteration's `assert err<1e-10 and drift<1e-10`, had already passed silently before the crash (the crash is in the `print` statement, after the assertion). Per standing practice, diagnosed this via a disposable scratch copy with the single substitution `np.trapz`→`np.trapezoid` (never touching the actual repository file): with that one change, the script ran to completion printing `PASS`, and every reported value — max Q error, max N drift, and cycle mean for N=1/4, 1/2, 2/3, 1 — matched the ledger's quoted numbers exactly (e.g. N=1 cycle mean `0.49999999999963407` vs ledger's `.5`; N=1/4 Q error `8.641698467926062e-14` vs ledger's `8.642e-14`). This confirms the underlying mathematics and implementation are correct; the defect is a pure NumPy-version API-compatibility issue in the committed bytes, not a logical or numerical error. Reported here rather than silently patched; Gravity's own track should apply the `np.trapz`→`np.trapezoid` (or equivalent) fix additively in its own next entry.

## Collision check (for this entry)

`v15.1546` is free; a final fetch immediately before this commit confirmed `origin/master` is still at `ad9c2c4` (this round's own starting point), with no new commits.

## Summary for Lane A/Sandbox/Gravity

A four-way version-number collision (v15.1542–v15.1545) is resolved in the audit's favor at all four slots by commit timestamp; Gravity should renumber its four entries starting at the next free slot after this one. All four Gravity entries' substantive mathematical/physical content is independently confirmed — the cutting-plane dynamics, cone/plane intersection geometry, spinor-determinant shell construction, and the full classical SU(2) Schwinger-boson moment map all check out exactly by hand and by running the actual committed scripts. One genuine but minor defect was found in v15.1545's committed script (`np.trapz` removed in current NumPy) and is reported for Gravity to fix additively; the underlying computation it was blocking is confirmed correct. No Lane A or Sandbox activity to report this round.

---
Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01TPmhX3cBuoKG7JvnvfmHzP
