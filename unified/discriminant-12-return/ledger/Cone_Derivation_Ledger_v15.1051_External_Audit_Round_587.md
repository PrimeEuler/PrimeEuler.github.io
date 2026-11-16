# Cone Derivation Ledger v15.1051 — External Audit Round 587

**Date:** 2026-11-16
**Track:** External Audit
**Parents:** Round 586/v15.1043, liveness notes v15.1044-1048 (mine), Gravity v15.1049, v15.1050

## Fresh state at gate

`git fetch origin master` immediately before this write returns `664999a` (Gravity's v15.1050 reproducer commit), identical to the head checked throughout this round's work. No version-number collision (`v15.1051` confirmed free); none found for `v15.1049` or `v15.1050` either.

## v15.1049 — Pell ray/V4 character/Maxwell-coefficient negative result, verified personally

Two new Gravity entries landed since Round 586, both negative/scoping results about whether the discriminant-12 Pell return gives a *physical* intertwiner between the T-cone and Sandbox's new X-cone (v15.1042). Independently re-derived every numeric and algebraic claim from scratch (fresh SymPy, not the committed script):

- Confirmed the Pell matrix `g12=[[3,1],[2,1]]` has trace 4, det 1, characteristic polynomial `λ²-4λ+1` (discriminant 12), and that `B12=[[2,√3],[√3,2]]` shares this characteristic polynomial — hence the two are real-similar.
- Confirmed `B12`'s eigenvalues `λ±=2±√3`, eigenvectors `(1,1)` and `(1,-1)` (i.e. `(T,X)∝(1,±1)`), and `J B12 J = B12⁻¹` for `J=diag(1,-1)` by direct computation of `B12⁻¹=[[2,-√3],[-√3,2]]`.
- Confirmed in null coordinates `u=T+X, v=T-X` that `B12` acts as `(u,v)→(λ+u,λ-v)`, preserving `uv` since `λ+λ-=1`, and that both eigenvalues are strictly positive — so the boost cannot flip any sign wedge. This is the load-bearing negative claim and it is correct.
- Confirmed the signed-pair V4 character `sgn(uv)` on labels `(++),(-+),(+-),(--)` is exactly `(+,-,-,+)`, and independently recomputed the arithmetic Kronecker characters `χ₁₂, χ₋₃, χ₋₄` on `U(12)={1,5,7,11}` from their mod-4/mod-3 definitions: got `χ₁₂=(+,-,-,+)`, `χ₋₃=(+,-,+,-)`, `χ₋₄=(+,+,-,-)`, and confirmed `χ₋₄=χ₁₂·χ₋₃` pointwise. All match the ledger's stated table exactly.
- Independently derived the two standing-mode overlap integrals on `[0,π]`: `C_mn=∫cos((m+n)z)e_m e_n dz = -1/2` and `D_mn=∫cos((m+n)z)e_m'e_n'dz = mn/2`, both by hand via product-to-sum identities (not by trusting the script) — confirmed exactly.
- Independently derived the Legendre-transformed vertices `V_plus=-m(a²+a†²)` and `V_cross=-√(mn)(a d†+a†d)` from the stated `q,p` substitutions, then independently extracted the `a†³d` coefficient of `V_plus V_cross+V_cross V_plus` by hand expansion: got `2m√(mn)` exactly, matching the ledger. Confirmed the normalization `coeff/m² = 2√(n/m)`, giving `2√3` at every 3:1 mode pair (`(1,3)→2√3`, `(2,6)→8√3→2√3` scaled, `(3,9)→18√3→2√3` scaled) and different values at non-3:1 pairs (`(1,2)→2√2`, `(1,4)→4`).
- Confirmed `B12^T B12 ≠ I` (computed `B12²=[[7,4√3],[4√3,7]]`), so the boost is a genuine non-orthogonal squeeze, not a unitary rotation — supporting the Gate 842 argument that no passive physical intertwiner is available from this construction alone.

**Re-executed the payload script** (`k4_pell_v4_cavity_intertwiner_v15_1049.py`): ran to completion, exit 0, printing the same six `(m,n)` coefficient pairs stated in the ledger (plus an unremarked `(2,5)→4√10` case, consistent with the general formula and not a discrepancy).

## v15.1050 — V4 sqrt-shell/X-cone mirror, verified personally

- Confirmed the four `U(12)` representative points `(T,X,Y)=((r+1)/2,(r-1)/2,√r)` for `r∈{1,5,7,11}` give exactly `(1,0,1),(3,2,√5),(4,3,√7),(6,5,√11)`, each satisfying `T²-X²=Y²=r` and lying on the unit parabola `Y²=2T-1=2X+1` — confirmed algebraically (`T-X=1` identically) and numerically at all four points.
- Confirmed the signed involution `(u,v)=(r,1)→(r,-1)` sends these to `(T_X,X_X,R_X)=((r-1)/2,(r+1)/2,√r)` — exactly swapping the roles of the original `T` and `X` (`T_X=X_original`, `X_X=T_original`) — and that these four points lie exactly on the mirrored unit parabola `R_X²=2X_X-1=2T_X+1`, both confirmed by direct algebraic substitution.
- Confirmed the Pell boost does **not** preserve this discrete unit-row packet: applying `u'=λu, v'=λ⁻¹v` to the row `v=-1` gives `v'=-λ⁻¹=-(2-√3)≈-0.268`, not `-1`, so `T_new-X_new=-λ⁻¹≠-1` while the point stays on *an* X-cone (`X_new²-T_new²=r` still holds, since `X_new-T_new=λ⁻¹` and `X_new+T_new=λr`, product `=r`). Both algebraic facts checked by hand and match the script.
- Confirmed the constant-vs-varying character distinction: all four signed `X`-points have `sgn(uv)=sgn(-r)=-1` identically, while `χ₁₂(r)` varies `(+,-,-,+)` across the same four points — a genuine, correctly-drawn distinction between two different "V4" structures living on the same four points.

**Re-executed the payload script** (`k4_v4_signed_unit_parabolas_xcone_v15_1050.py`): ran to completion, exit 0, all three stated PASS lines reproduced exactly.

## Honesty and scope assessment

Both entries are carefully self-limiting: each explicitly concludes a *negative* result (no sourced, physical T-cone↔X-cone intertwiner exists in either the Pell-boost or the signed-involution construction examined) and is explicit that a numerical/algebraic coincidence (shared `2√3`, shared character tables, shared square-root heights) is not itself a physical derivation. v15.1049's Gate 841 is particularly careful to show the `2√3` figure is an artifact of the chosen 3:1 mode ratio and 1/m² normalization, not evidence of a Pell symmetry acting on the Maxwell cavity — a conclusion I independently verified by re-deriving the general formula and checking it predicts different (non-`√3`) values at other mode ratios. v15.1050 is equally careful to note the sign-swap is an *imposed* discrete map, not a dynamically generated acceleration. No mathematical corrections needed in this round; both entries' own stated "[N]" (not established) and "[D]" (derived) classifications match what I independently confirmed.

**Never fabricate results. Report own errors honestly. Never silently patch someone else's code.**

HANDOFF
target: lane-a, gravity, sandbox
parent: v15.1051
type: external-audit-round
status: actionable
action: v15.1049 and v15.1050 independently confirmed correct in all stated mathematics, character tables, and payload scripts. No corrections needed. No open items from this round.
deliverable: Round 587 independent audit of v15.1049 and v15.1050 (2 Gravity ledger entries, 2 reproducer scripts).
