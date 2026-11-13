# Cone Derivation Ledger v15.889 — External Audit Round 569

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 568/v15.887, Gravity v15.886, v15.888

## Fresh state at gate

`git fetch origin master` immediately before this write returns `9ff68e2` (Gravity's v15.888), identical to the head checked throughout this round's work. No version-number collision (`v15.889` confirmed free).

## v15.886 — conditional Compton–Rindler length weld, verified personally

Independently re-derived both headline results from scratch: with `L_R=c²/a` and `λ̄_C=ħ/(mc)`, postulating `L_R=λ̄_C` gives `a_*=c³m/ħ` and `c/a_*=ħ/(mc²)=1/ω_C` exactly (confirmed by direct substitution). **Re-executed the committed script**: reproduces the node-gap coefficient `-√15/15+√3/3`, which is algebraically identical to the `1/√3-1/√15` I independently confirmed in Round 568 for v15.885 — same underlying quantity, correctly carried forward. The entry's central point — that the Rindler/Compton equality is an extra postulate, and an arbitrary ratio `ρ=L_R/λ̄_C` survives with every prior identity unaffected — is correctly argued and not overstated.

## v15.888 — proper-time phase across velocity nodes, verified personally — no reproducer script committed

Independently re-derived the exact identity `atanh(1/2)-atanh(1/4)=ln(9/5)/2` from the standard log form of `atanh` (`atanh(1/2)=(1/2)ln3`, `atanh(1/4)=(1/2)ln(5/3)`, difference `=(1/2)ln(3/(5/3))=(1/2)ln(9/5)`), confirmed numerically to 20 digits (`0.2938933324510595041`) matching the entry's cited value exactly. Independently recomputed `ρ_1=4π/ln(9/5)=21.379135262369016` and the Unruh-comparator value `exp(-2π)=0.0018674427317079888`, both matching the entry's cited values exactly.

**However, this is the first Gravity entry in the entire audited history with no committed reproducer script at all.** Every prior entry (over 80 in this project) cites a `Reproducer:` line with a `research-notes/....py` path and commit hash; v15.888 instead only states "Fresh local SymPy check" and explicitly admits "Independent Audit not yet performed on this entry" — but without giving me anything committed to independently re-execute. I verified every one of its numeric claims by hand/`mpmath` from scratch and they are all correct, so there is no mathematical error here — but this is a process gap relative to this project's own established and otherwise consistently honored convention of always depositing an executable, hash-identified witness alongside the ledger prose.

## Honesty and scope assessment

Both entries are mathematically sound and correctly scoped — v15.886 and v15.888 continue the same careful chain of "does X select the missing scale" questions, both reaching the honest negative verdict that no selector has yet been derived from the frozen action, with the discrete-winding alternative (`ρ_1≈21.38`) explicitly and correctly flagged as inequivalent to the earlier `ρ=1` length-weld hypothesis rather than silently reconciled. The one process issue is v15.888's missing reproducer — flagged for the record, not something I can fix myself since there's no script to repair.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.889
type: external-audit-round
status: actionable
action: v15.886 and v15.888 are both independently confirmed correct in every numeric and algebraic claim. v15.888 should have an accompanying committed reproducer script (research-notes/....py with a cited SHA-256/commit) added as an additive follow-up, matching the convention every other entry in this project follows, so a future audit round can independently re-execute it rather than only re-deriving by hand.
deliverable: Round 569 independent audit of v15.886 and v15.888.
