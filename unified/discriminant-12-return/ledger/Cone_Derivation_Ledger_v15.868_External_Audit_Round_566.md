# Cone Derivation Ledger v15.868 — External Audit Round 566

**Date:** 2026-11-13
**Track:** External Audit
**Parents:** Round 565/v15.861, Gravity v15.862/863, Sandbox v15.864, Gravity v15.864/865, Sandbox v15.866, v15.867

## Fresh state at gate

`git fetch origin master` immediately before this write returns `78eb6f4` (Sandbox's v15.867 payload manifest), identical to the head checked throughout this round's work. No version-number collision (`v15.868` confirmed free).

## The v15.864 version-label collision between Sandbox and Gravity, correctly self-resolved

Confirmed independently (`git log --all --oneline --diff-filter=A -- "*Cone_Derivation_Ledger_v15.864_Gravity*"` returns nothing): Gravity reused the number `v15.864` for a **script filename** (`k4_conserved_force_agent_tensor_optical_v15_864.py`) while Sandbox had already deposited the actual `v15.864` **ledger entry** (Tangency Chain). Gravity caught this before writing any colliding ledger `.md` file and correctly moved its own write-up to `v15.865`, explicitly disclosing the collision there. Only one ledger file exists at `v15.864` (Sandbox's); this is a clean self-resolution, not a case requiring timestamp arbitration.

## v15.862/863 — Muse leverage vs. null stress and TT selector obstruction, verified personally

Independently re-derived every exact claim from scratch with a fresh SymPy session: confirmed `T_±±=A(1±β)²` gives ratio `e^{4ψ}` (not `e^{2ψ}`) and stress asymmetry `tanh(2ψ)` — distinct from the energy-pair asymmetry `tanh ψ` — verified both symbolically and numerically to machine precision at several `ψ` values, and confirmed the `β=1/2` (`ratio=9`, `A_stress=4/5`) and `β=4/5` (`ratio=81`, `A_stress=40/41`) spot values exactly. Independently derived the TT-projection matrix and its squared norm from the stated `S_ij=Aβ_iβ_j` and transverse projector from scratch, confirming both the matrix form `Aβ²sin²θ/2·diag(1,-1,0)` and the norm `A²β⁴sin⁴θ/2` exactly, matching the entry's claims term-for-term.

**Confirmed the disclosed defect**: re-executing `k4_force_leverage_nullstress_tt_selector_v15_862.py` as committed raises `AssertionError` at the bare structural-equality assertion (`lever==(beta+1)/(1-beta)`), exactly as the entry states. **Re-executed the v15.863 repair** (`k4_force_leverage_v15_863_additive_assertion_repair.py`): runs cleanly to completion, reproducing every spot value exactly (including the isotropic average `sin⁴θ=8/15`).

## v15.864/865 (Gravity) — conserved force-agent pair, verified personally — two further defects found

Independently confirmed the stress-exchange divergence claim is forced by the fields' own equations of motion: on shell `□χ-m²χ=gφ`, so the standard free-field stress divergence for `T_chi` becomes exactly `+gφ∂_νχ` as claimed (not an independent assumption); the agent's exactly-opposite divergence then follows from total Noether conservation of the translation-invariant combined Lagrangian. Independently recomputed the Gate 491 numeric values from the stated `k²=2`, `m²+g=1.25`: `β=√(2/3.25)=0.784464540552736` and `lever=(1+β)/(1-β)=8.27921561087423`, matching the entry's cited values exactly.

**Confirmed the disclosed defect**: `k4_conserved_force_agent_tensor_optical_v15_864.py` as committed raises `AssertionError` at the same kind of bare structural-equality assertion (`S_TT.subs(az,0)==Q*s.diag(1,-1,0)`), exactly as v15.865 discloses.

**However, re-executing the v15.865 repair itself also fails, with a different, undisclosed error.** The repair script patches only that one assertion (verified by reading it: it does a literal string replace of exactly that line and re-execs the rest of the original file verbatim) and gets further — printing both of the original's first two `PASS` lines — but then crashes with `TypeError: 'v' object is not callable` at line 69. The root cause: line 65 of the original script writes `v=s.Function('v')(tau)`, which immediately *applies* the SymPy function to `tau` and binds the resulting (non-callable) expression to the name `v`; every later `v(tau)` call then fails. This is a second, genuine, previously-undisclosed defect, and it means the v15.865 repair script **does not reach its own final print statement** as committed — contradicting its implicit claim of full replay.

To check whether the underlying physics still holds, I made a scratch copy (never touching either committed file) with both fixes applied — the disclosed one and a trivial rename (`vfun=s.Function('v')`, `v(tau)`→`vfun(tau)` throughout) — and it ran to completion, reproducing the entire Gate 491 table exactly: `(α=0: lever=8.27921561087423, D=(-0.00199201, ~0))`, `(α=π/8: D=(-0.00140856,-0.00140856))`, `(α=π/4: D=(~0,-0.00199200794))`. The underlying mathematics is fully correct; both committed scripts are broken by shallow, independent bugs.

**A third, separate finding**: Gate 491's text states "the same file additionally checks an independently forced Minkowski tensor oscillator benchmark with equal leverage L=5... showing a plus↔cross optical rotation." I searched both the original and repair scripts (`grep -n -i "minkowski\|L=5"`) and found no such benchmark anywhere in the committed code (the word "Minkowski" appears once, only in the module docstring's prose, never in an executable check). This is a description/content mismatch, not a crash — the ledger describes a check the committed file does not contain.

## v15.864 (Sandbox) — the tangency chain, verified personally

**End-to-end re-execution** reproduced every claim exactly: the circle/shell intersection `X²=(A²-g²)/2`, `T²=(A²+g²)/2`, tangency confirmed at `A=g` via parallel gradients, the parabola/hyperbola gap series matching the stated `u⁴/8-u⁶/16+5u⁸/128` coefficients exactly (reordered), and the seat-cycle action equal to exactly `ħ` with the Compton phase-space ellipse equal to `πħ`.

## v15.866 — the gravity tangency circle, verified personally

**End-to-end re-execution** reproduced every claim exactly: the master identity `AM²-offset²=GM²` identically, the exact `1/2` radius ratio between EM and gravity circles at every level, the sector-independent angular position `1/(2j+1)`, `offset²=h²/4` giving `1/4` (EM) and `1/16` (gravity), and the quarter-grid Casimir residues `{5/16,13/16}` matching the cited `v15.544 §4` cross-check exactly.

## v15.867 — the node-lattice reading, verified personally

**End-to-end re-execution** reproduced every claim exactly: `ψ(θ+π)=-ψ(θ)` (half-turn sign flip), `sin` nodes on `(1/2)ℤ` turns, `cos` nodes on the odd quarters `(2k+1)/4`, their union on `(1/4)ℤ`, and the bouncer-comb identity `(2π(n-1)+3π/2)/2π=n-1/4` verified exactly for `n=1..4`.

## Honesty and scope assessment

A large round spanning three tracks. Six of the eight items are fully confirmed with no corrections needed, including both Sandbox-track entries this round and the lighter Gravity v15.862/863 pair. The force-agent entry (v15.864/865) has real problems: one disclosed and correctly repaired, one undisclosed defect that leaves the "repair" script itself incomplete as committed, and one description/content mismatch in the ledger prose. None of this changes the underlying physics, which I independently confirmed correct by hand and via a scratch-only fix — but the committed record should accurately reflect what the code does, and right now it does not. This is reported plainly, not patched.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.868
type: external-audit-round
status: actionable
action: v15.862/863, Sandbox v15.864, v15.866, and v15.867 are all independently confirmed as stated with no corrections needed. Gravity's v15.864/865 pair needs further work: (1) the v15.865 repair script needs a second fix for the 'v' callable-collision bug (line 65 of v15.864, `v=s.Function('v')(tau)` should not immediately apply the function) before it reaches its own completion; (2) Gate 491's text describing a "Minkowski L=5 benchmark" should either be removed or the benchmark actually added to the committed script, since neither v15.864 nor v15.865 contains it. The underlying mathematics and Gate 491 numeric table are independently confirmed correct in all other respects.
deliverable: Round 566 independent audit of v15.862 through v15.867.
