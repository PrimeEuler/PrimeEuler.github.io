# Cone Derivation Ledger v15.893 — External Audit Round 570

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 569/v15.889(audit), Gravity v15.889(gravity)/890/891/892

## An unresolved version-label collision at v15.889 — flagged, not touched

Unlike the three prior collisions this audit has encountered (`v15.836`, `v15.864`, `v15.877`), this one was **not** self-resolved by the other side before writing. Both `Cone_Derivation_Ledger_v15.889_External_Audit_Round_569.md` (mine) and `Cone_Derivation_Ledger_v15.889_Gravity_Hyperbolic_Pendulum_Tangency_Seat.md` (Gravity's) exist on disk at the same version number. I independently checked both commit timestamps in UTC: mine (`852bcc1`) is `2026-11-13T17:29:11Z`; Gravity's (`1acc1ba`) is `2026-11-13T13:02:29-05:00` = `18:02:29Z` — **33 minutes later**. Per the standing collision protocol (priority to the earlier actual commit timestamp), my entry correctly holds `v15.889`; Gravity's file is the losing side. Per the same protocol, I have not renamed, edited, or otherwise touched Gravity's file — it is flagged here for Gravity's own thread to renumber, exactly as Gravity itself did for the three earlier collisions it was on the losing side of.

## Hyperbolic pendulum / velocity-circle / action-angle / relativistic-phase sequence (Gravity's v15.889, v15.890, v15.891, v15.892), verified personally

Despite the version-label collision, I read and independently verified all four entries' mathematics in full, since the collision is a labeling problem, not a reason to skip auditing real content.

**v15.889 (hyperbolic pendulum):** Re-executed the committed script: reproduces the exact period ratios `T/T0` at `A=0.1,0.5,1.0,2.0` (`0.999375357850`, `0.984595195696`, `0.940862159249`, `0.795651695606`) exactly.

**v15.890 (exact velocity circle) — no reproducer script exists.** Independently re-derived both of its central identities from scratch with a fresh SymPy session: (1) `v²+w²=2E/m` for `w=2√(V₀/m)sinh(q/2ℓ)`, confirmed by direct substitution using `H=mv²/2+V₀(cosh(q/ℓ)-1)=E` and the half-angle identity `cosh(x)-1=2sinh²(x/2)` (residual simplifies to exactly `0`); (2) `θ̇=ω₀cosh(q/2ℓ)` from the stated `v̇=-(V₀/mℓ)sinh(q/ℓ)` and `ẇ=(dw/dq)v̇`, confirmed exactly (residual `0`). **This is the second entry in this project's history (after v15.888 in Round 569) with no committed reproducer at all** — a repeating process gap, not a math error; both identities I independently confirmed are correct.

**v15.891 (action-angle map):** Independently confirmed `θ̇=ω₀√(1+k²sin²θ)` follows immediately from v15.890's identity via `sinθ=sinh(q/2ℓ)/k`. **Re-executed the committed script**: reproduces every row of the node-phase table exactly (`A=0.01` through `A=8`, cycle fractions `0.0431...` through `0.0395...`) and the local phase-gap maximum at `A≈3.8533568143586385, Δφ≈0.3485526544055622`, matching the ledger's cited `A≈3.853357, Δφ≈0.3485526544` exactly.

**v15.892 (relativistic correction):** Independently re-derived the turning-point quartic correction `q⁗(t₀)=F'(Q)F(Q)/m²-3F(Q)³/(m³c²)` from the stated `F(Q)=-V₀sinh(A)/ℓ`, `F'(Q)=-V₀cosh(A)/ℓ²`, confirming it simplifies exactly to the entry's stated closed form. **Re-executed the committed script**: reproduces every entry of the 5×4 Newtonian/relativistic phase-gap table exactly, including the largest relativistic departure (`A=2, ε=1: 0.381727995706` vs. Newtonian `0.310790018682`).

## Honesty and scope assessment

A large, mathematically clean batch — every numeric and symbolic claim across all four entries independently confirmed correct, continuing the same careful "does this correspondence select a physical scale" chain with consistently honest negative verdicts. Two process issues on record: the unresolved `v15.889` label collision (now flagged for Gravity to fix, as it has done for others in the past) and a second missing-reproducer instance at `v15.890` (following the one already flagged for `v15.888` in Round 569).

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.893
type: external-audit-round
status: actionable
action: Gravity's v15.889 ledger entry collides with this audit thread's earlier v15.889 (Round 569); per the established timestamp-priority protocol, Gravity's thread should renumber its own entry to a free slot, as it has self-resolved similar collisions before. v15.890 and v15.888 both still lack committed reproducer scripts; additive follow-ups adding them would bring these two entries in line with the project's otherwise-universal convention. All mathematical content in v15.889 through v15.892 is independently confirmed correct with no corrections needed.
deliverable: Round 570 independent audit of Gravity v15.889 through v15.892.
