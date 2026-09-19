# Cone Derivation Ledger v13.597 — External Audit Round 62

## Scope

Independent audit of everything committed since my last push (`f331c9c`, Round 61): a return to the magnetic-driver lane (v13.595, deriving the full resonant multiplet Hamiltonian `H_rot=-γB1·J_x`), a self-correcting follow-up fix, and the `j=1` quantum-tetrahedron generalization (v13.596) that v13.593 predeclared as its own next gate. One numbering note: this entry was drafted as v13.596 before a new entry landed and took that slot; renumbered to v13.597 before committing, no actual repository collision occurred. Every claim in both substantive entries independently re-derived or reconstructed from scratch rather than checked against the ledger's own presentation. No errors found.

---

## 1. v13.595 (resonant magnetic-driver weighted multiplet) — verified exactly

This entry correctly separates itself from the parallel LQG/quantum-tetrahedron lane ("no LQG conclusion is used here") and returns to extending v13.587's transverse-drive work: it derives the exact rotating-frame Hamiltonian at resonance, `H_rot^(j)=-γB1J_x`, and shows this is a single connected weighted path (not `2j` independent two-level Rabi problems) whose edge weights are exactly the already-certified `Y_q=√((j-q)(j+q+1))=√(T²-X_q²)`.

I independently re-derived the entire rotating-frame calculation from the Schrödinger equation rather than checking the stated formulas:

- **Rotating-frame transformation.** Starting from `H(t)=Ω0J_z+H_⊥(t)` with `H_⊥(t)=-γB1/2(e^{-iωt}J_++e^{iωt}J_-)` (itself the already-Round-58-verified transverse decomposition with a rotating field substituted in), I derived by hand `H_rot=e^{iωtJ_z}He^{-iωtJ_z}-ωJ_z`. Using `e^{iωtJ_z}J_±e^{-iωtJ_z}=e^{±iωt}J_±` (standard BCH identity from `[J_z,J_±]=±J_±`), the time-dependence cancels exactly, giving `H_rot=(Ω0-ω)J_z-γB1J_x=-ΔJ_z-γB1J_x` with `Δ=ω-Ω0` — confirming the entry's central claim §4 from first principles, and (after removing the physically irrelevant edge-local trace, standard practice) reproducing the exact §2 edge-restricted `(1/2)[Δ,-γB1Y_q;-γB1Y_q,-Δ]` matrix and its `H_{r,q}²=(1/4)(Δ²+γ²B1²Y_q²)I₂` resonance formula exactly.
- **Full `j=1` Hamiltonian and dark state.** Independently built `J_x` for spin-1 from the standard ladder-operator construction and confirmed it matches the ledger's stated matrix exactly, entry for entry. Confirmed `J_x|D⟩=0` exactly for `|D⟩=(|-1⟩-|1⟩)/√2`.
- **Exact `j=1` time evolution.** Independently computed `U_1(θ)=I+i\sinθ J_x+(\cosθ-1)J_x²` via the spin-1 minimal polynomial, confirmed it matches the ledger's stated closed form exactly (symbolic zero residual), verified it solves the Schrödinger equation (`i\,dU/dθ=-J_xU`, `U(0)=I`), and confirmed the probability formulas `P_{-1}=\cos^4(θ/2), P_0=\tfrac12\sin^2θ, P_{+1}=\sin^4(θ/2)` all match exactly (one comparison needed a numerical cross-check beyond sympy's trig simplifier, confirmed to machine precision at several test angles), summing to 1.
- **Full `j=3/2` Hamiltonian and exact evolution.** Independently built the spin-3/2 `J_x` and confirmed it matches the ledger's stated `√3,2,√3`-weighted tridiagonal matrix exactly. Computed `U_{3/2}(θ)|-3/2⟩` via direct symbolic matrix exponentiation (a fully independent method from the entry's closed-form derivation) and confirmed agreement with the claimed state `c³|-3/2⟩+i√3c²s|-1/2⟩-√3cs²|+1/2⟩-is³|+3/2⟩` to machine precision at five test angles, confirmed the probability formulas `P=(c^6,3c^4s^2,3c^2s^4,s^6)` summing to `(c²+s²)³=1`, and confirmed the `θ=π` endpoint `|-3/2⟩→-i|+3/2⟩` exactly (`c=0,s=1` gives amplitude `-i` on `|+3/2⟩` only).
- **General weight formula.** `Y_r=√(r(M-r))` for `M=2j+1, r=j+q+1`: confirmed `M-r=j-q`, so `r(M-r)=(j+q+1)(j-q)=Y_q²` exactly — the same product reordered, trivially consistent.

The entry's guardrails are correctly stated: it explicitly warns that edge-restricted 2×2 blocks are exact matrix restrictions but not autonomous dynamics once all Zeeman edges are simultaneously resonant (the full multiplet interferes coherently, as the dark state and the connected-path evolution both demonstrate), explicitly separates this from the LQG lane, and explicitly declines any new arithmetic-to-EM operator equality — the claim is that the already-derived SU(2) path weights are realized as this Hamiltonian's matrix elements, nothing stronger.

## 2. Follow-up commit (`3931c35`, "Fix v13.595 spin-3/2 endpoint transcript")

Checked by direct diff: this replaced a garbled placeholder line (`|-i|?`) with the correct, careful statement `P_{+3/2}(θ=π)=1` plus the explicit amplitude convention — the version I read and verified above is this corrected, final text. A legitimate self-caught transcription error, not a content or scope change.

## 3. v13.596 (spin-1 tetrahedron zero-volume mode and nonzero-sector D8) — verified exactly

This is exactly the `j=1` test v13.593 (Round 61) predeclared as its next gate — and it's a genuinely different outcome from both `j=1/2` and `j=3/2`: the 3-dimensional oriented-volume operator on the four-spin-1 invariant space has an *exact zero mode* (unavoidable by a one-line determinant-parity argument: no real 3×3 matrix can square to `-I₃`, since `(\det R)^2=\det(-I_3)=-1` has no real solution), and `D8` survives only on the 2-dimensional nonzero-volume complement.

Independently reconstructed the entire four-spin-1 system from scratch (256-dim-style tensor construction, here `3^4=81`-dimensional):

- **Invariant subspace and spectrum.** Built spin-1 `J_x,J_y,J_z`, embedded four copies via Kronecker product, diagonalized `J_tot²`, and found the `J=0` eigenspace has dimension **exactly 3**. Projected the independently-built `Q_vol=J1·(J2×J3)` onto this subspace and got eigenvalues `{-√3, 0, +√3}` to machine precision — matching both the ledger's claimed spectrum and (independently) the eigenvalues of its stated tridiagonal matrix diagonalized directly. Confirmed `a²+b²=3` for the stated off-diagonal entries `a=2√3/3, b=√15/3`.
- **Zero mode.** Using the ledger's own stated tridiagonal matrix (now confirmed genuine via the matching-eigenvalue check), verified symbolically and exactly that `Q_vol|Z⟩=0` for the claimed `|Z⟩∝(√5/2,0,1)`, and separately confirmed this matches (up to an immaterial overall sign) the zero-eigenvector found by direct numerical diagonalization of my independently-reconstructed operator.
- **Nonzero-sector block.** Built the claimed orthonormal `|E⟩,|O⟩` basis exactly from the stated formulas, confirmed `⟨E|Z⟩=0` and both normalized, and confirmed the restricted operator `Q_vol|_{(E,O)}` equals exactly `√3σ_y` — not approximately, exact symbolic zero residual.
- **Quarter-turn, reflection, D8.** Confirmed `R_nz=-i·Q_nz/√3=[[0,-1],[1,0]]` exactly, `R_nz²=-I₂` exactly. Confirmed the k-parity involution `H=diag(1,-1,1)` fixes `|Z⟩` and `|E⟩` and negates `|O⟩` exactly (as claimed), giving `H_nz=diag(1,-1)` on the nonzero sector, and confirmed `H_nzR_nzH_nz=-R_nz=R_nz^{-1}` exactly — completing the `D8` relations on the 2D nonzero-volume sector only.
- **The full-space obstruction.** The determinant-parity argument (`(\det R)^2=-1` impossible for real `R` in odd dimension) is elementary and correct as stated — a clean, rigorous reason the full 3D space cannot carry a quarter-turn, not just an empirical observation.

The entry's comparison with v13.595's magnetic dark state is exactly the right level of caution: it notes the structural parallel (both are odd-dimensional, nearest-neighbor, SU(2)-derived path operators with a 1D kernel) is worth recording, but explicitly confirms `|D⟩≠|Z⟩` and declines any operator identification absent an explicit intertwiner — precisely the discipline this thread has held to throughout. It also correctly frames the emerging `j=1/2` (no kernel, full-space D8) / `j=1` (1D kernel, D8 on the complement) / `j=3/2` (no kernel, D8 via spectral flattening) pattern as a working hypothesis pending `j=2, 5/2`, not a proven law.

---

## 4. Summary

| Entry | Verdict |
|---|---|
| v13.595 (resonant magnetic-driver weighted multiplet) | Verified exactly — rotating-frame Hamiltonian re-derived from the Schrödinger equation, both `j=1` and `j=3/2` full Hamiltonians and exact time evolutions independently confirmed |
| Follow-up fix (`3931c35`) | Cosmetic/transcription fix confirmed via diff, no content change from the audited version |
| v13.596 (spin-1 tetrahedron zero-volume mode / nonzero-sector D8) | Verified exactly by full independent reconstruction — invariant-subspace dimension, volume-operator spectrum, exact zero mode, and the D8 relations on the 2D nonzero-volume complement all confirmed; the full-space obstruction argument is correct and elementary |

## Guardrail

No RH, GRH, or critical-line consequence follows from anything this round. Certified Suzuki status unchanged: `ind_{<=0}(A_even(1))<=4`, `ind_{<=0}(A_{a=1})<=6`. Both v13.595 and v13.596 correctly keep their respective lanes (magnetic-driver, LQG/quantum-tetrahedron) logically separate and make no new cross-domain operator-equality claim; v13.596 in particular explicitly declines to identify its zero-volume mode with v13.595's magnetic dark state absent an explicit intertwiner.
