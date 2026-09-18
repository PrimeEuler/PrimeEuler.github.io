# Cone Derivation Ledger v13.584 — External Audit Round 56

## Scope

Independent audit of everything committed since my last push (`cf376df`, Round 55): a substantial new entry bridging the AM-GM cone/factor-hyperbola coordinates to SU(2)/SU(1,1) angular-momentum ladder algebra via the project's own pre-existing "Paper C" quantum-realizations paper, plus a pure formatting fix to that same entry. No version collisions this round. Every algebraic identity independently re-derived symbolically; the cited external source was checked against the actual file rather than taken on trust. No errors found.

---

## 1. Housekeeping

`e700179` ("Fix v13.583 ledger math formatting and retain audited bridge") is a pure LaTeX-escaping fix to v13.583 (the committed version had broken `\frac`/`\boxed` markup, e.g. `rac` instead of `\frac`) — confirmed by diff that no mathematical content changed, only rendering. No version collision this round (v13.583 was free).

## 2. Source citation check

Before trusting any of v13.583's claims, checked whether its cited source, `foundations/PaperC_QuantumRealizations_v1.1.tex`, actually exists and actually contains the dictionary the entry attributes to it — given this project's history (v13.508) of a fabricated numerical claim, an unverified external citation is exactly the kind of thing worth checking directly rather than assuming.

The file exists, and its own text (lines 31–48) independently confirms, verbatim, the dictionary v13.583 cites: `x=n_1+1, y=n_2`, `X=(n_1-n_2+1)/2`, `T=(n_1+n_2+1)/2`, and the Schwinger SU(2) identification `j=N/2=T-1/2, J_z=X-1/2, J^2=j(j+1)`. The citation is genuine and accurate, not fabricated or misattributed.

## 3. v13.583 (centered half-lattice, Casimir core, precession-phase bridge) — verified exactly

This is a substantial, internally consistent piece of exact algebra: it shows that the AM-GM cone's factor-gap family `N=m(m+k)` gives `X=±k/2` and `T²-Y²=k²/4`, that the SU(2) raising/lowering ladder amplitudes `A_±²=(j∓q)(j±q+1)` are literally the same factor products under an explicit substitution `m,k↔j,q`, and that the pronic (`k=1`) family is exactly the zero-weight (`J_z=0`) Casimir core where `Y²=j(j+1)`.

Independently re-derived every claim in the entry's own "quick algebra audit" (§13) plus the underlying constructions, using sympy for the symbolic identities and direct numerical function composition (mod `2π`) for the phase-group relations, rather than accepting the stated algebra:

- `T=j+1/2`, `X=J_z+1/2`, `T²-j(j+1)=1/4` — confirmed exactly.
- `m(m+k)=(m+k/2)²-(k/2)²` — confirmed exactly.
- `(j-q)(j+q+1)=(j+1/2)²-(q+1/2)²` and `(j+q)(j-q+1)=(j+1/2)²-(q-1/2)²` — both confirmed exactly (these underpin the raising/lowering amplitude-to-cone-radius identities in §5–6).
- `Z_+(q)=Z_-(q+1)` and `A_+²(j,q)=A_-²(j,q+1)` (shared transition centers, §7) — confirmed exactly.
- `R_prec²-Y²=X-1/2`, hence `R_prec²=Y² ⟺ X=1/2` (§9) — confirmed exactly by substituting `j=T-1/2`, `q=X-1/2`, `T²-X²=Y²` into `R_prec²=j(j+1)-q²`.
- The phase-group relations (§11): `A²=S²=1`, `AS=SA`, `R²=A`, `R⁴=1`, `SRS=R⁻¹` for `A:φ↦φ+π`, `S:φ↦-φ`, `R:φ↦φ+π/2` — all six confirmed by direct function composition mod `2π` at multiple test points, giving `V_phase≅C2×C2` extending to `⟨R,S⟩≅D8` exactly as claimed.
- The reflection/rotation-reversal claim in §10 (`G L_XY G⁻¹=-L_XY` for `G=J_fol C_T`, i.e. the foliation swap reverses the sense of the `XY`-rotation generator while ordinary `T`-reversal preserves it) — independently re-derived by explicit conjugation of the rotation flow `Rotation_θ(X,Y)` by the coordinate swap and confirmed `G∘Rotation_θ∘G⁻¹=Rotation_{-θ}` exactly; this is the standard fact that a reflection reverses angular orientation, correctly applied here.
- The sphere construction (§8): `X²+Y²+T²=2T_j²` intersects the double cone exactly at `T=±T_j, X²+Y²=T_j²`, with radius `R_S=√2·T_j` — confirmed by direct substitution.

The entry is careful about scope throughout: it explicitly separates `[D]` (exact derived), `[G]` (geometric interpretation), and `[O]` (open/not promoted) claims, and §12's connection between the phase-group's central involution and the earlier-certified incidence-V4's `T_7↔FS` central element is correctly left as an unpromoted structural analogy ("not an operator equality... an explicit intertwiner is required"), consistent with this project's standing discipline against conflating isomorphic-but-unrelated group actions (the same discipline seen in v13.562/563's no-go work and v13.576's careful non-conflation of `J_fol` with `F`).

---

## 4. Summary

| Entry | Verdict |
|---|---|
| v13.583 (centered half-lattice / Casimir / phase bridge) | Verified exactly — every algebraic identity in the audit section independently re-derived (sympy + direct composition), source citation checked against the real file and confirmed accurate |
| Formatting-fix commit | Cosmetic only, confirmed by diff — no content change |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. v13.583 is a self-contained exact bridge between the elementary AM-GM cone and SU(2)/SU(1,1) ladder algebra via the project's own pre-existing Paper C; it does not touch the Suzuki operator or any certified index bound, and it correctly declines to promote its open structural analogy (§12) to an operator-level identification.
