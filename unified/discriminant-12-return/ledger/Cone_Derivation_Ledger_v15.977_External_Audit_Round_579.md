# Cone Derivation Ledger v15.977 — External Audit Round 579

**Date:** 2026-11-14
**Track:** External Audit
**Parents:** Round 578/v15.966, Gravity v15.967 through v15.976

## Fresh state at gate

`git fetch origin master` immediately before this write returns `daad402` (Gravity's v15.976), identical to the head checked throughout this round's work. No version-number collision anywhere in v15.967–976.

## v15.967/968 — the two Round 578 collisions correctly self-resolved

Both entries reissue the previously colliding v15.954/955 content verbatim under the free numbers v15.967/968, leaving the original colliding files untouched as historical aliases — the established self-resolution pattern. Diffed both reissued bodies against their originals: identical apart from header/provenance lines. No action needed.

## v15.969 through v15.976 — Casimir-as-kinetic-energy sequence, verified personally

An eight-entry sequence following a user hypothesis — that the formal EM/quarter Casimir difference might represent a physical kinetic energy — through to its systematic dismantling: three inequivalent "inertia" choices give three different energy-gap functions of D (none selected by geometry), a positive-mass counterexample kills any automatic splitting, the quarter sector's half-integer prequantization index rules out a naive closed ordinary-SU(2) reading, a relative Berry/Hopf connection has integer charge D but cannot serve as a scalar intertwiner, and finally an exact Clebsch–Gordan rank bound shows low-rank (dipole/quadrupole) EM-to-quarter couplings are representation-theoretically forbidden at all but a few small D.

Independently re-derived every concrete algebraic claim from scratch:

- **v15.969**: confirmed `C_q,formal − C_EM = (4D+1)/16` exactly by direct symbolic subtraction.
- **v15.970**: confirmed all three kinetic-profile functions exactly — `F_outer(D)=(4D+1)/(4D²)`, `F_Casimir-radius(D)=2/(2D+1)`, `F_inner(D)=(D+2)/4` — and their sample values at D=2,3,5 all matched.
- **v15.972**: confirmed the rest/product identity `R_rest,q²=P_q=j_q=(2D−1)/4` and the resulting constant normalized gap `(C_formal−C_scaled)/P_q=1/2` exactly, for symbolic D.
- **v15.974**: confirmed `Δk=k_q−k_e=D`, `C_q,norm−C_e=3D²/4` (growing with D), and the differently-normalized `C_q,scaled−C_e=3/16` (constant) — these are two genuinely different quantities, and the entry is careful not to conflate them.
- **v15.975**: confirmed the spin gap `Δj_phys=D/2` and, by direct enumeration, the exact pattern of when integer tensor rank 1 or 2 is representation-theoretically allowed between the two closed multiplets: rank-1 only at D=2, rank-2 only at D=2 and D=4, matching the ledger's claimed table exactly for D=2 through 6.
- **v15.976**: independently built the concrete 4-dimensional two-spin-½ bicone from scratch (not importing the script) and confirmed `L²+A²=3I` exactly, with eigenvalue pairs `(L²,A²)=(0,3)` on the singlet and `(2,1)` on the triplet — matching the ledger's claimed spectral structure exactly.

## Script execution and defect found

**Re-executed all eight new scripts** (v15.969 through v15.976). Seven ran to completion with `PASS`. **One genuine shallow defect found: `k4_casimir_difference_kinetic_sector_phase_v15_969.py` crashes with `AssertionError` at line 15 (`assert s.factor(Cq-Ce)==(4*D+1)/16`).** The left side is SymPy's factored form (a `Mul` object, `(4*D+1)/16`), while the literal right-hand expression `(4*D+1)/16` is auto-distributed by SymPy into an `Add` object (`D/4 + 1/16`); the two are mathematically equal but structurally different, so bare `==` returns `False` even though the claim is true — the same class of bare-structural-equality bug flagged repeatedly earlier in this project's history. Confirmed shallow: in an isolated scratch copy (never touching the committed file), replacing the comparison with `s.simplify(s.factor(Cq-Ce)-(4*D+1)/16)==0` lets the script run to completion with `PASS`, printing exactly the `ΔC` values at D=2,3,5 (`9/16, 13/16, 21/16`) that I had independently derived above.

## Honesty and scope assessment

This is one of the most disciplined negative-result sequences in the project to date: each entry takes the user's physically reasonable hypothesis seriously, builds the cleanest possible test of it, and reports exactly what survives and what doesn't — repeatedly distinguishing quantities that look similar but are not (formal vs. co-scaled Casimir, geometric Casimir-radius vs. actual SU(2) Casimir, relative Berry charge vs. ordinary spin gap). The explicit positive-mass counterexample in v15.970 (choosing `M_q/M_e` to force equal kinetic energies despite nonzero Casimir gap) is a particularly clean way to demonstrate that geometry alone cannot fix a physical coupling. No mathematical corrections needed anywhere in this round.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, sandbox
parent: v15.977
type: external-audit-round
status: actionable
action: v15.967/968 correctly resolve Round 578's two collisions. v15.969–976 all independently confirmed correct in their mathematics. `k4_casimir_difference_kinetic_sector_phase_v15_969.py` needs its line-15 assertion changed from bare `==` to a `simplify(...)==0` comparison; the underlying mathematics is correct.
deliverable: Round 579 independent audit of v15.967 through v15.976 (10 entries, 8 new scripts); two collision resolutions confirmed, one shallow script defect found and confirmed via scratch-copy fix.
