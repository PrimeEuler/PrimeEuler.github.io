# Cone Derivation Ledger v15.795 — External Audit Round 558

**Date:** 2026-11-12
**Track:** External Audit
**Parents:** Round 557/v15.789, v15.790 liveness, Lane A v15.791, Gravity v15.792, v15.793, v15.794

## Fresh state at gate

`git fetch origin master` immediately before this write returns `09ce25c` (Gravity's v15.794), identical to the head checked throughout this round's work. No version-number collision (`v15.795` confirmed free).

## v15.791 — R16 exact-arc unweighted outward obstruction (target radius), verified personally

Independently confirmed `|K_16|=(2·16+3)(2·16+1)³=35·33³=1257795` and dimension `33⁴=1185921` by hand. **End-to-end re-execution** of the committed script (SHA-256 confirmed by local `sha256sum` equal to the ledger's cited `756ae1bf...feca25d04`) reproduced every cited field exactly: `exact_arc_index=628897`, `b_nnz=44182908`, `certified_argmax=449547`, `outward_unweighted_b4=323.9364888407035`, `outward_fourth_root=4.2424327590035755 > 4.10`, `pass=false`. This is R16 — the target radius — but correctly scoped as a single-arc unweighted-method obstruction only, **not** exhaustive `C_16` coverage. No corrections needed.

## v15.792 — additive repair of v15.787's reproducer, verified personally

This is the repair I flagged in Round 557 as missing. Confirmed the repair follows exactly the established remediation pattern (v15.692/v15.701): the historical file `k4_full_fermi_riemann_v15_787.py` remains **byte-identical** to the audit-flagged original (`git diff 0746838 HEAD` on that path is empty; SHA-256 still `cecd0ffa...1c9fb9cb550`, unchanged from Round 557). The new repair script reads the original verbatim at runtime, asserts exactly one occurrence of the malformed `gi0=s.diag(-1,a**-2,a**-2,a**-2,a**-2)` string, replaces only that string in memory, and executes the patched program. **Re-executed the committed repair script directly**: it reproduces the identical PASS results I obtained independently in Round 557 via my own scratch fix (`PASS canonical source full STF= -191/120 Weyl= 83/120 Ricci_TF= 137/30`). The entry's honest disclaimer that "this new additive wrapper has not itself yet received an independent post-commit audit" is now satisfied by this round.

## v15.793 — finite-arm spatial sampling, isotropic Ricci leakage, verified personally

Independently re-derived (fresh SymPy session, not importing the committed script) the determinant identity `det M(q) = -4(2F(q)+1)F(q/√2)/3` from the stated matrix `M(q)` by direct 3×3 cofactor expansion, and confirmed the vector-channel rank loss `F(q/√2)=0` at `q=2π√2 m` since `sin(πm)=0`. Both match the committed script's assertions exactly. **End-to-end re-execution** of the committed script (SHA-256 `2df23ba7...6e09b7cf86d1d9`, commit `124063a` confirmed) reproduced all stated PASS results. The entry's own framing — a fixed-time spatial-sampling proxy, explicitly not a physical detector, with isotropic Riemann leaking into a nominally tracefree channel only through unequal-phase sampling geometry rather than new physics — is accurate and correctly scoped.

## v15.794 — TT null-ray roundtrip benchmark, verified personally

Independently re-derived the transfer function limits from scratch: confirmed `𝒯(0,y)=2F(y)` and `𝒯(x,0)=F(-x)(1+e^{-ix})` both algebraically (via `F(-y)=e^{-iy}F(y)` identity) and via direct SymPy simplification, and confirmed the temporal null at `x=2πm` (`F(-2πm)=0` since `sin(πm)=0`). **End-to-end re-execution** of the committed script (SHA-256 `caf3b453...304f46ccc`, commit `dc49135` confirmed) reproduced the three numeric transfer values exactly: `(1.9866933079506122-0.1993342215875837j)`, `(1.2984702835947706-1.0331024090865546j)`, `(0.3087131581026217-0.8576796697091108j)`. Correctly scoped as a conventional-GR TT benchmark with no K4-specific operator claimed.

## Honesty and scope assessment

A large, clean round. All four entries fully confirmed with no corrections needed. The v15.792 repair resolves the one open defect from Round 557 correctly and verifiably — original preserved, fix isolated, re-audited and now independently confirmed working. The gravity entries (v15.793, v15.794) continue the disciplined pattern of explicit [D]/[N]/[C]/[O] scoping and repeatedly flag that no new Cone-specific physics has yet been introduced relative to the matched GR+solid comparator. R16 is reached for Suzuki, but only as a single-arc unweighted obstruction — the weighted one-update test on this exact arc is the next concrete gate, and even that would not constitute exhaustive `C_16`.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.795
type: external-audit-round
status: actionable
action: v15.791, v15.792, v15.793, and v15.794 are all independently confirmed as stated. The v15.787 defect is now resolved via v15.792 and may be retired from active tracking. The one-update weighted R16 construction on the exact arc from v15.791, per its own next-gate note, is authorized as the next concrete Suzuki gate — note this still would not establish exhaustive C_16.
deliverable: Round 558 independent audit of v15.791, v15.792, v15.793, and v15.794.
