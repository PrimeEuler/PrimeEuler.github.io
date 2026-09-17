# Cone Derivation Ledger v13.566 — External Audit Round 50

## Scope

Independent audit of everything committed since my last push (`9a87633`, Round 49): the phase-bridge thread's self-directed redirect after its Level-1 failure (v13.555-new lane closure, renumbered v13.564; v13.556-new expanded-sample follow-up, renumbered v13.565), and the group-theory lane's continuation into a no-go theorem and its automorphism classification (v13.562, v13.563). One version-collision pair found and fixed (two collisions, same as the previous three rounds' pattern: new work landing in the same v13.555/v13.556 slot already occupied by earlier-audited entries). Every numerical and algebraic claim independently re-derived. Everything checks out; no errors found this round.

Note on timing: this batch is the phase-bridge thread's own response to its Level-1 failure. I had intended to write a redirect note myself per the user's instruction ("no go on the phase lane with a redirect"), but a fetch immediately before writing showed the thread had already redirected itself — cleanly and correctly, as verified below. No redirect note from me was needed or written.

---

## 1. Housekeeping

- `Cone_Derivation_Ledger_v13.555_Chi12_Lane_Closure_and_5_13_Ray_Lane_Open.md` (commit `77fb9d9`, 2026-09-17T16:44:40-04:00) collided with the already-audited `Cone_Derivation_Ledger_v13.555_M16001_Remaining_Outward_Certification_DAG.md` (which kept its number in Round 49). Renumbered to **v13.564**.
- `Cone_Derivation_Ledger_v13.556_Expanded_Blind_Ray_Geometry.md` (commit `aebd658`, 16:46:06-04:00) collided with the already-audited `Cone_Derivation_Ledger_v13.556_Three_Pair_Quotient_S4_to_S3.md` (kept its number in Round 49). Renumbered to **v13.565**, fixing the internal cross-reference to the lane-closure entry (now v13.564) in section 1.
- No other files referenced either colliding file by number (checked via grep across the ledger directory); the pre-existing entries that mention "v13.555"/"v13.556" all refer to the DAG/Three-Pair-Quotient entries that kept their numbers.

## 2. v13.564 (ex-v13.555, χ12/Suzuki lane closure and 5/13 ray lane open) — verified exactly

This is the thread's own closure of the phase-bridge lane following its Round-49-verified Level-1 failure (v13.559). Independently re-extracted `F_5, F_7, F_11, F_13` from `suzuki_chi12_phase_bridge_level1_blind.py` at M=1999 and recomputed every geometric quantity claimed for the q=5,13 pair:

- angle `theta(5,13)`, cosine similarity, radial separation, angular chord, and the identity `||x-y||^2 = Delta_rad^2 + Delta_ang^2` — all matched.
- the common-ray bisector projection `d_parallel`/`d_perp` decomposition — `||d_perp(5,13)||=0.23516218858913948` reproduced exactly, confirmed smaller than `||d_perp(5,11)||=0.5328671893957349`.
- the four per-center cosine values (r=1,5,7,11) and the percentage breakdown of the residual squared distance — reproduced exactly.

This is honest, well-scoped work: it correctly declines to promote the closed χ12 lane, correctly identifies the q=5,13 proximity as a *directional* (not scale) phenomenon global across all four unit-core centers, and opens a genuinely neutral new lane rather than silently retrying the failed hypothesis under a new name.

## 3. v13.565 (ex-v13.556, expanded label-blind ray geometry) — re-executed directly, verified exactly

Re-ran `suzuki_ray_alignment_expanded_blind.py` directly (not just inspected) at both cutoffs:

**M=499:** all six top-pair angles matched to the digit — `13,31→1.165022173665994°`, `5,37→3.0162283061610489°`, `5,13→8.4607265519466903°`, `nearest(5)=37`, `nearest(13)=31`, `seed_gate=FAIL-SEED`.

**M=999:** all six matched — `13,31→1.1667742670591184°`, `5,37→3.0227574037049889°`, `5,13→8.4791918571045919°`, `5,31→8.754907167245241°`, `31,37→9.3849738715687057°`, `13,37→9.4520916618271489°`, `FAIL-SEED` reproduced.

Also confirmed by direct source inspection (`grep` for hardcoded-looking literals, none found) that the twelve-prime sample `Q={5,7,11,13,17,19,23,29,31,37,41,43}` and the B0 whitening are exactly as predeclared, with no χ12/label lookup anywhere in `fingerprints()`.

This is the predeclared seed-persistence gate applied honestly against the thread's own seed observation from v13.564, and it fails cleanly: q=5 and q=13 are not mutual nearest neighbors once the sample is expanded (`nearest(5)=37`, `nearest(13)=31`, both well inside `theta(5,13)`). The entry correctly avoids retrofitting an arithmetic explanation onto the newly visible 13↔31 and 5↔37 alignments and instead proposes a geometry-first next gate (characterize the full angular-distance matrix before consulting any candidate labels). This is the second consecutive self-falsified hypothesis from this thread in as many entries — good discipline.

## 4. v13.562 (no-go for simultaneous marked V4 and complex-structure intertwining) — independently re-derived exactly

Set up the exact linear system symbolically (sympy, general 3×3 `Q`) for the identity relabeling `sigma=(5)(7)(11)` with the stated `K5,K7,K11`, `D5,D7,D11`, and `J`, solving `Q K_r = D_r Q` for r=5,7,11 jointly with `QJ=JQ`. The only solution is `Q=0` — confirming the no-go exactly, independent of the ledger's own coordinate computation and its separate coordinate-free `Fix(J)` argument (which I also checked by hand: `Fix(J)=span(e3)`, and the marked intertwining forces `Q(span(e3))=span(e2)≠span(e3)`, a direct contradiction).

## 5. v13.563 (V4 automorphisms and J-compatible relabelings) — independently re-derived exactly, all six cases

Extended the same symbolic sympy setup to all six permutations `sigma∈Aut(V4)≅S3` and solved each system independently (not by trusting the ledger's case labels):

| sigma | my result | ledger claim |
|---|---|---|
| (5)(7)(11) | zero only | no-go |
| (5)(7 11) | `Q=diag(a,a,c)` | solutions exist |
| (5 7)(11) | zero only | no-go |
| (5 7 11) | zero only | no-go |
| (5 11 7) | `Q=[[0,-a,0],[a,0,0],[0,0,c]]` | solutions exist |
| (5 11)(7) | zero only | no-go |

All six match exactly, including the precise two-parameter solution families for the two compatible cases (`sigma_A=(7 11)` giving `diag(a,a,c)`; `sigma_B=(5 11 7)` giving `diag(a,a,c)·J`). The conceptual argument (J-compatibility forces `sigma(11)=7` because K7 and D11 are the unique elements of their respective triples fixing the J-normal axis `e3`) is correct and matches the exhaustive computation.

---

## 6. Summary

| Entry | Verdict |
|---|---|
| v13.564 (ex-v13.555, lane closure) | Verified exactly |
| v13.565 (ex-v13.556, expanded ray geometry) | Re-executed at M=499 and M=999, every value matches; FAIL-SEED confirmed |
| v13.562 (marked V4/J no-go) | Independently re-derived via sympy, confirmed |
| v13.563 (J-compatible automorphism classification) | Independently re-derived all six cases via sympy, confirmed exactly |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The phase-bridge thread has now produced two consecutive honest negative results (Level-1 clustering failure, then seed-persistence failure) without retrofitting either — this is the correct way to run a falsifiable exploratory lane.
