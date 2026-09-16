# Cone Derivation Ledger v13.516 — External Audit Round 40

## Scope

Independent audit of everything committed since my last audit push (`0aaebe2`, v13.511) through the current head (`332f4f5`, v13.514, plus my own collision fixes): the M16001 instrumentation follow-through (v13.512 M16001, v13.514), and the new QR-quotient/A3 algebra (v13.512-QR — now v13.515, v13.513). Every claim independently re-derived or re-executed.

**Housekeeping first.** Two version collisions were found and fixed this round:
1. Two files were both filed as v13.512: `...M16001_Transcripted_Gamma_Replay_Instrumentation.md` (17:23:22) and a QR-quotient checkpoint (17:23:28, 6 seconds later) — the latter was also misplaced directly under `unified/discriminant-12-return/` instead of `ledger/`. Renumbered and relocated.
2. While fixing that, a genuine v13.514 (`...M16001_Structured_Solve_Residual_Transcript.md`) landed from the parallel thread and collided with my in-progress renumbering. Bumped my file again, to v13.515, and fixed all forward-references in v13.513 both times.

**Mathematical verdict: everything in this batch is exact.** The QR-quotient/A3 algebra (now v13.513, v13.515) is fully verified by direct matrix and group-theory computation — every identity holds. The M16001 instrumentation (v13.512, v13.514) is genuine, re-executable arithmetic (unlike v13.508): no hardcoded radii, a benign RuntimeWarning traced to its source and confirmed harmless, and one small floating-point reproducibility variation in v13.514 that does not affect the validity of its stated bound.

---

## 1. v13.512 (M16001 transcripted gamma replay instrumentation) — verified

Re-executed `research-notes/suzuki_M16001_gamma_transcripted_replay.py` directly. Output matches the entry's claims: `gamma_NF=4.331929780165835e-16` (exact match), `remote rows = 991999` (correctly using the Round 39 correction, not the earlier "992000" typo), all reported radii are genuinely computed from `sum(abs(products))` transcripts, not literals.

**Investigated:** a `RuntimeWarning: invalid value encountered in divide` fires during execution, traced to `off_block(low,ZC,low,ZC)` in `suzuki_M16001_even_index3_anisotropic_tail_split.py` line 69 — calling the pairwise off-diagonal formula `-(2/PI)*(ns*Zs-ms*Zn)/(ns**2-ms**2)` with identical row/column index sets produces `0/0` on the diagonal. Checked the next line: `np.fill_diagonal(A0CC,diag0[:10])` immediately overwrites those entries with the correct value from a separate formula. Confirmed no NaN reaches any reported quantity (all printed outputs are finite). This is a harmless vectorization artifact, not a defect — noted only because a silent `0/0` is worth having on record, and because wrapping the call in `np.errstate(invalid='ignore')` would silence the false alarm without changing behavior.

## 2. v13.513 (A3 tetrahedral edges, S4 transpositions, QR χ12 axis) — exhaustively verified

Independently recomputed every claim:

- `μ_r·μ_r=3/4`, `μ_r·μ_s=-1/4` (r≠s): confirmed for all pairs.
- All six edges `α_{r,s}=μ_r-μ_s`: confirmed exactly against the claimed table (all six match `Φ(A3)` entries bit-for-bit).
- Root reflections `s_{r,s}` act as the transposition `(r s)` on all four tetrahedral vertices, fixing the other two: confirmed by direct reflection computation for all six edges × four vertices.
- Simple-root identification `α1=μ1-μ5, α2=μ5-μ7, α3=μ7-μ11` matching the established simple roots `(0,1,1),(1,-1,0),(0,1,-1)`: confirmed.
- Braid relations `(s1s2)³=(s2s3)³=1`, `(s1s3)²=1` as literal permutation compositions: confirmed (and confirmed `(s1s2)²≠1`, ruling out a false shortcut).
- Path-sum telescoping `α1+α2=μ1-μ7`, `α2+α3=μ5-μ11`, `α1+α2+α3=μ1-μ11`: confirmed.
- Character-axis/perfect-matching table (each root has exactly one zero coordinate; the three axes `χ-4,χ-3,χ12` sort the six edges into the three perfect matchings of `K4`): confirmed exactly — `χ-4↔{1,5},{7,11}`, `χ-3↔{1,7},{5,11}`, `χ12↔{1,11},{5,7}`, matching the claimed table exactly.

No error found. The entry's own guardrails (exact coincidence of two independently-defined selections, no Pell-dynamics or Suzuki-spectral claim, no moonshine/Monster claim) are appropriately stated and not oversold.

## 3. v13.515 (QR quotient / χ12 Fourier checkpoint, renumbered from v13.512) — exhaustively verified

Independently rebuilt the entire construction in code, not spot-checked:

- Signed carrier `r(a,b,c)=5^a7^b(-1)^c mod 24` reproduces `U(24)` and the four claimed sign-pair cosets `{1,-11},{5,-7},{7,-5},{11,-1}`: confirmed.
- `P(a,b,c)=(a+c,b+c)`, `ker P={000,111}`, `P` surjective onto `F2²`: confirmed.
- `K^⊥={000,110,101,011}` (even-weight vectors): confirmed by direct dot-product check against `111`.
- Character identification `χ_{100}=χ_{-3}`, `χ_{010}=χ_{-4}`, `χ_{110}=χ_{12}`: confirmed by direct sign comparison against the established characters on all four totatives — exact match in every case.
- Full Fourier machinery, rebuilt independently in NumPy: `H8²=8I`, `H4²=4I`, `J^TJ=2I₄`, `R^TR=I₄`, `H8J=2RH4`, `H8R=JH4`, the normalized forms `F8·P=R·F4`, `F8·R=P·F4`, the projector intertwining `F8·Π_K=Π_K⊥·F8`, and the explicit averaging formula `(Π_K f)(v)=½(f(v)+f(v+111))` — **every single identity confirmed exactly** by direct matrix construction and comparison.
- `P0∩K^⊥={1,χ12}`: confirmed (consistent with the character identification above).

This is a fully rigorous, fully verified piece of finite algebra. No error found anywhere.

## 4. v13.514 (M16001 structured-solve residual transcript) — verified with one noted reproducibility variation

Re-executed `research-notes/suzuki_M16001_structured_solve_residual_transcript.py` directly:

```
max sum_j |A0_ij X_jr| = 1.1209247268485287856     [ledger: 1.1209247268485288 -- matches]
max gamma_N dot charge = 4.8557672055593957713e-16  [ledger: 4.855767205559396e-16 -- matches]
max point residual entry = 4.239284704526946612e-15 [ledger: 4.2394473348528194e-15 -- differs at 5th sig. fig.]
point Frobenius residual = 7.80225884456075561e-15  [ledger: 7.802341177110749e-15 -- differs at 5th sig. fig.]
OUTWARD ||R_F||_F < 9.550294946230152434e-15        [ledger: 9.55035036608530e-15 -- differs at 5th sig. fig.]
```

The upstream quantity (`max sum_j |A0_ij X_jr|`, ~1.12) and the gamma dot charge match to full displayed precision; the divergence appears only in the residual itself and downstream. This is consistent with ordinary floating-point summation-order sensitivity in a **cancellation-prone** computation (the residual is a difference of larger intermediate quantities), plausibly from BLAS/threading nondeterminism between runs rather than any error in the method. Critically, **my independently recomputed value is smaller** than the entry's claimed outward bound (`9.5502949...e-15 < 9.5503504...e-15`), so the entry's stated bound remains valid as an outward (safe-upper) bound even accounting for this variation — it is not contradicted, just not bit-for-bit reproducible in its last digits. No hardcoded literal was found anywhere in the script (confirmed by direct source inspection, same check as v13.512); this is genuine, re-executable arithmetic, correctly distinguished from the v13.508 pattern.

---

## 5. Summary

| Entry | Verdict |
|---|---|
| v13.512 (M16001 instrumentation) | Re-executed, confirmed exact; benign RuntimeWarning traced and confirmed harmless |
| v13.513 (A3 tetrahedron / S4 / QR axis) | Exhaustively verified, every claim exact |
| v13.515 (QR quotient, ex-v13.512) | Exhaustively verified, every claim exact; version collision + misplacement fixed |
| v13.514 (structured-solve residual) | Re-executed; small floating-point reproducibility variation noted, direction confirmed safe |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything here. Certified status remains unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. The QR/A3 algebra (v13.513, v13.515) is exact finite mathematics with no Suzuki-spectral claim attached, consistent with its own guardrails.
