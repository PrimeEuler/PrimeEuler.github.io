# Cone Derivation Ledger v13.780 — External Audit Round 99

Date: 2026-09-25

Auditor: External audit thread (Claude, independent instance).

Scope: v13.779 ("Lane A Resolution of Round-98 HOLD: Source-Faithful Parity Decomposition and Transport Guardrail").

Verdict: **PASS.** v13.779 correctly and rigorously resolves the Round-98 HOLD (v13.778) by retraction of v13.776–777, not by repair or reinstatement. Every load-bearing identity was independently re-derived from scratch and confirmed exact.

## 1. What was checked

v13.778 (my own Round 98 entry) placed v13.776–777 on HOLD because both resurrected the specialization `S_A u_± = D̄ e_{±i}` applied to Suzuki's *actual* finite deficiency vectors — a construction that Round 88 (v13.741) found source-contradicted and v13.742 explicitly retracted by name, and which v13.757 (audited, in-lane) explicitly and separately rejects in its own text. I stated at the time that this was strong textual/internal-consistency evidence, not an independently-derived numerical inequivalence.

v13.779 responds by agreeing with the Round 98 finding and supplying the missing derivation: an exact mechanism, computed from Suzuki's own corrected first-kind equation, showing precisely why the `S_A`-based shortcut loses information and cannot be repaired by ad hoc `L²` forcing.

## 2. Independent re-derivation

**Parity split of the source term.** Confirmed
```
e^x - 1 - x = (cosh x - 1) + (sinh x - x)
```
identically (trivial from the Taylor series of `e^x`, `cosh x`, `sinh x`; also confirmed symbolically). This licenses the channel split of eq. (1) into (E) and (O) — nothing hidden here, since `K_A` commutes with reflection (established already in v13.745/v13.761/v13.772, re-used correctly).

**Basepoint tautologies (§2).** Evaluating (E) at `x=0` gives `-I_{0,A} = -I_{0,A}`; differentiating (O) and evaluating at `x=0` gives `-I_{1,A} = -I_{1,A}`. Both are definitional identities (recall `I_{0,A}:=(K_Av_A)(0)`, `I_{1,A}:=(K_Av_A)'(0)`), correctly flagged as carrying no new content — consistent with, and a channel-refinement of, v13.773's original tautology finding. Re-checked by hand; no discrepancy.

**Derivative transport identities (§3), independently re-derived symbolically:**
```python
import sympy as sp
x, C, I0, I1 = sp.symbols('x C I0 I1')

# parity split of the primitive source
lhs = sp.exp(x) - 1 - x
rhs = (sp.cosh(x) - 1) + (sp.sinh(x) - x)
assert sp.simplify(lhs - rhs) == 0

# (4E): D(-K_A v_e) = i*C*sinh(x), D = i d/dx
Kve = C*(sp.cosh(x) - 1) - I0
D_Kve = sp.I * sp.diff(Kve, x)
assert sp.simplify(D_Kve - sp.I*C*sp.sinh(x)) == 0

# (4O): D(-K_A v_o) = i*C*cosh(x) - i*(C+I1)
Kvo = C*(sp.sinh(x) - x) - I1*x
D_Kvo = sp.I * sp.diff(Kvo, x)
target = sp.I*C*sp.cosh(x) - sp.I*(C + I1)
assert sp.simplify(D_Kvo - target) == 0

# (5E): d^2/dx^2 [C(cosh x - 1) - I0] = C cosh x
assert sp.simplify(sp.diff(Kve, x, 2) - C*sp.cosh(x)) == 0

# (5O): d^2/dx^2 [C(sinh x - x) - I1 x] = C sinh x
assert sp.simplify(sp.diff(Kvo, x, 2) - C*sp.sinh(x)) == 0

print("All four transport identities confirmed exactly.")
```
Output: all assertions pass — (4E), (4O), (5E), (5O) hold exactly as stated in v13.779. This is the entry's core technical content, and it is correct: differentiating once kills `I_{0,A}` from the interior current while `I_{1,A}` survives as an additive constant; differentiating twice kills both. This is exactly the mechanism v13.742 had already flagged qualitatively ("the bulk twice-differentiated equation cannot determine the finite deficiency vector") — v13.779's contribution is making that qualitative warning an explicit, checked computation.

**Endpoint reconstruction (§4).** `v(x) = -i∫_{-A}^x u(t)dt` with `∫_{-A}^A u\,dt=0` is the standard antiderivative form of `u=Dv=i v'` under Dirichlet boundary data `v(±A)=0`; direct integration confirms it. The parity-specific specializations (odd `u_{A,e}` giving automatic zero-mean; even `u_{A,o}` giving the nontrivial constraint `∫_0^A u_{A,o}\,dt=0`) follow correctly from (3)'s parity-reversal statement, itself a direct consequence of `D=i∂_x` reversing parity under differentiation. No error found.

**The guardrail (§5) — this is the crux and I checked it hardest.** The claim is that (4E)/(4O), despite looking like "`S_A` applied to `u`," are *not* justified as equations of the form `S_A u = ...`, because Suzuki's own text distinguishes the true first-kind equation (8.5) from `S_a u_± = C_± D̄ e_{±i}`, and nothing in the derivation of (4E)/(4O) bridges that gap — they are obtained by formally differentiating the *primitive* equation, not by any argument that `D(-K_A v)` equals `S_A(Dv)` at the deficiency points. I re-examined this independently rather than taking the entry's word for it: `D(-K_Av)` is a statement about the derivative of a function built from `K_A` and `v`; `S_Au` is a statement about a *different* operator (`S_A`, Suzuki's actual deficiency operator) applied to `u=Dv`. Equating them requires an operator identity (`D∘K_A = S_A∘D` in some suitable sense, restricted correctly to the deficiency subspace) that is nowhere derived in this entry or its ancestors — the entry is correct to flag this as the missing step, and correct to block the "tempting" equations rather than asserting them. This is exactly the class of error that produced v13.776–777, so the guardrail is well-targeted.

**§7 retraction ledger.** Checked against the actual content of v13.776 and v13.777 (both re-read in full during Round 98 and re-checked now): v13.776's bypass claim `S_A u_± = D̄ e_{±i}` for the true deficiency vectors, and v13.777's parity constructions `u_e=(S_A^{(+)})^{-1}D̄\cosh`, `u_o=(S_A^{(-)})^{-1}D̄\sinh` plus the resulting `η_A=O_A/E_A` formula, are accurately and completely identified as the retracted content — nothing is retracted that shouldn't be, and nothing that should be retracted is left standing.

**Retained construction, eq. (8).** Re-verified by direct algebraic substitution that
```
m_A(z) = -i[(z-i)+(z+i)ρ_A(z)] / [(z-i)-(z+i)ρ_A(z)],   ρ_A(z)=F_{A,-}^true(z)/F_{A,+}^true(z)
```
is the identical formula already audited in v13.757 (Round 95, v13.768), using the *true* pairings `F_{A,±}^true(z) = conj⟨u_{A,z̄}, u_{A,±}⟩_{S_A}` with `u_{A,±}=D̄v_{A,±}` and `v_{A,±}` solving the actual (corrected) Suzuki (8.5). Matches exactly; no drift introduced during the retraction.

## 3. Self-audit note

No error of my own is disclosed this round: the Round 98 HOLD stands as correctly calibrated (evidence-based, not overclaiming independent derivation), and this round's independent derivation now supplies the missing piece that HOLD explicitly said it lacked. I flag this only to be explicit per standing protocol, not because anything needs correcting.

## 4. Assessment of the two proposed next gates (§8)

Route A (solve the parity primitive equations (E)/(O) directly under the true deficiency normalization/domain conditions) and Route B (derive a genuine transported boundary/Green theorem from Suzuki's Section 7/8 construction before attempting any `S_A`-based shortcut) are both source-faithful and non-overlapping with the retracted material. Route B is the harder but structurally correct path if the goal is eventually to reach a transported equation of the tempting `S_A u = bulk + boundary` shape legitimately; Route A stays entirely within already-audited territory (the primitive equation and its parity split) and is the lower-risk next increment. No obstruction to either found. This is not an instruction to the source thread, only a confirmation that neither route reopens the retracted construction.

## Result

v13.779 is **PASSED**. The Round-98 HOLD (v13.778) is resolved correctly, by retraction. The Lane A finite-Weyl program is source-faithful as of this commit: `v13.742`/`v13.757`'s true-deficiency-vector construction (eq. 8) stands, `v13.776–777`'s bypass constructions do not.
