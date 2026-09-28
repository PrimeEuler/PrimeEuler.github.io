# v13.848 — Sandbox Bucket 2: the selection identity — SELECTS, conditionally

**Date:** 2026-09-28
**Lane:** Sandbox (our Lane B — Jeremy's exploratory track under LIttle Euler; disambiguated from the ledger's dormant norm-quotient Lane B)
**Status:** [I]/[O] — discovery + new analytic results, not certified
**Entry kind:** sandbox analytic verdict (text-faithful reconstruction + two new theorems about Suzuki's objects)
**Supersedes nothing. Refines:** v13.838 (the (8.5) gap — refined, not retracted), v13.840 (weak-form), v13.844 (judgment call #1), v13.846 (ker-minimization mechanism)
**Sibling:** the Wiener–Hopf lemma (v13.849) — this entry's verdict gates its transfer

**Headline:** SELECTS — conditionally. Suzuki's text determines its deficiency vectors by exact T_a-inversion (Lemma 6.2), with no minimum-norm anywhere in it. The kink-faithful weak-form T_a of v13.840 is PROVEN to compute exactly those vectors (for λ<λ_a), via the Friedrichs extension (Theorem 1.1) — so the reported Bucket 2 numbers (r₁⁺≈−8.75, |c|≈0.48, L₀+L₁=0) ARE Suzuki's true numbers, conditional only on λ_a>0. New analytic result: the continuum (8.5) problem, solved jointly for (v,A,B), needs NO selection — it is uniquely solvable. The 2D near-nullspace of v13.838 is a discretization artifact.

---

## 1. What Suzuki's text actually determines (real citations, v2)

- **Lemma 6.2 (§6.2, pp. 21–22):** for λ<λ_a, T_a is invertible on L²(−a,a); "(T_a v)(x) = C₊eˣ, (T_a v)(x) = C₋e⁻ˣ, **admit unique solutions**, and these functions span the eigenspaces corresponding to the eigenvalues ±i."
- **§6.3 (p. 22):** "(T_a f_z)(x) = C exp(−izx), **which uniquely determines f_z for each fixed C≠0, since T_a is invertible**."
- **§6.4 (p. 22) / Thm 1.5 (p. 6):** v_± = C_±v_{±i} "normalized so that ‖v₊(a,·)‖_{T_a} = ‖v₋(a,·)‖_{T_a}" — one real quadratic inter-channel condition; fixes |C₊|/|C₋| only.
- **§8 (p. 30):** (8.5) "formally equivalent" to (8.4) "in the sense that differentiating both sides twice with respect to x yields (8.4)"; "**Here we avoid expressing these equations in terms of the operators T_a or S_a, since the above argument ignores domain issues**"; "Since the kernel in (8.5) is continuous, it is an ordinary Fredholm integral equation of the first kind… **One may compute v_±(a,x) by solving this Fredholm equation numerically** and then test experimentally whether (1.12) holds."
- **Absent:** full-text grep of the v2 PDF — "minimum-norm"/"min-norm" never occur in §§6–8 (the only "minimum" is unrelated). No selection criterion for any (8.5) non-uniqueness is stated.

**Verdict on the text:** Suzuki's true selection is **exact T_a-inversion**: v_± = the unique T_a⁻¹(C_±e^{±x}), C_±≠0 free, |C₊|/|C₋| fixed by the norm equality. (A_±,B_±) are then forced as functionals of v_±.

## 2. New analytic result I — the continuum (8.5) needs no selection

Let U: L²(−a,a)→L²(−a,a), (Uv)(x) = ∫k(x,y)v(y)dy with k(x,y) = g(x−y) − λN(x,y).

- **U is injective:** (Uv)″ = −(T_a v) distributionally (since −k_xx is T_a's kernel, (8.4)); Uv=0 ⇒ T_a v=0 ⇒ v=0 by Lemma 6.2 (λ<λ_a).
- **Ran(U) has codimension 2:** f=Uv ⇒ f″=−(T_a v) ranges over all of L²; conversely f″∈L² ⇒ v:=−T_a⁻¹(f″) gives (Uv−f)″=0, i.e. Uv = f+Ax+B for a unique affine. So f∈Ran(U) iff two linear compatibility functionals vanish. The map (A,B)↦affine-remainder of (C e^{±x}+Ax+B) is the identity on (A,B) — hence **(A_±,B_±) are the UNIQUE pair with C_±e^{±x}+A_±x+B_± ∈ Ran(U)** (Fredholm compatibility; not stated in Suzuki, but a theorem about his objects given Lemma 6.2).
- **The augmented system is injective:** [U|X](v,a) := Uv+(Ax+B); if Uv+(Ax+B)=0 then Ax+B ∈ Ran(U)∩{affines} = {0} (twice-differentiating gives 0=−(T_a w) ⇒ w=0), so Ax+B=0, then Uv=0 ⇒ v=0. **(8.5) solved jointly for (v,A_±,B_±) has exactly one solution.**

## 3. Refinement of v13.838 — the gap was a discretization artifact

v13.838's characterization ("no two linear conditions in the text fix the 2D nullspace") stands, but is now understood: the text determines (I₀,I₁) **indirectly**, through the full T_a-inversion — and that is sufficient, because the continuum augmented problem is well-posed (§2). The 2D near-nullspace (affine ∈ Ran(K_A) to machine precision) is a **discretization artifact**: discretely affine falls into Ran(K_A), while in the continuum affine ∩ Ran(U) = {0}. The discretization does not preserve [U|X]-injectivity — the "domain issues are load-bearing" warning, made precise. **Tikhonov was regularizing an artifact, not a continuum freedom.**

## 4. New analytic result II — the kink-faithful weak-form IS the true selection

Theorem 1.1 (§1, p. 3): A_a is the **Friedrichs extension** of B_a, D(B_a)=H¹_0(−a,a). Then: H¹_0 ↪ D(Q_λ) continuously and densely (C_c^∞ ⊂ H¹_0; D(Q_λ) is the T_a-completion of C_c^∞); Lax–Milgram in (D(Q_λ),‖·‖_{Q_λ}) gives unique u with T_a u = e^{±x}; by Lemma 6.2 (λ<λ_a), u is THE unique solution — **u = v_±/C_±, Suzuki's true deficiency vector**. The H¹_0 P1 Galerkin method (v13.840) converges to u by Céa's lemma.

**Consequence:** the reported numbers — r₁⁺≈−8.75, r₀⁺≈+27.28 (A=3), |c|≈0.48, L₀+L₁=0 — **are Suzuki's true numbers, conditional only on λ_a>0** (λ=0 computations; λ_a>−1 for the λ=−1 track). The "Dom(A_a) ⊋ H¹_0" fact (Round 101) is consistent: the solution is approximable by H¹_0 functions.

## 5. Per-candidate verdicts

| Candidate | Verdict | Consequence |
|---|---|---|
| True selection (text) | **T_a-inversion**, unique (Lemma 6.2); no min-norm in text | the standard everything is judged against |
| (a) kink-faithful weak-form T_a | **SELECTS — proven** = true v_± for λ<λ_a | the numbers are Suzuki's true numbers, conditional on λ_a>0 |
| (b) analytic T_a-invertibility + Wiener–Hopf | **SELECTS by definition** (it *is* T_a⁻¹) | not a competing selector; open solely via λ_a>0 |
| (c) Thm 1.5 norm equality | **DOESN'T SELECT** within-channel | one quadratic inter-channel equation; ratios r_j^± = I_j^±/C_± scale-invariant, unaffected |
| (8.5)-LS Tikhonov ker-minimization | **SELECTS on numerical evidence** (via the (a)-bridge) | agrees with (a) to ~0.1%; BC-insensitive; refinement-stable. Analytic discrete→continuum transfer open but **no longer load-bearing** — (a) gives an independent proven-true route to the same numbers |

On the ker-minimization, honestly: in the continuum there is nothing to select, so it selects among discretization-artifact degrees of freedom — it is the discrete shadow of the Fredholm compatibility condition (§2): choose (A,B) to kill the cokernel component. Why it lands on the true (A_±,B_±) rather than being pulled by the 359-dim artifact directions is unproven — now a **numerical-analysis convergence question**, not a missing-selection-principle question. Cleanest airtight route: a compatibility-preserving discretization (e.g. Petrov–Galerkin with the two cokernel functionals as constraints) that never creates the artifact nullspace — then no Tikhonov is needed at all.

## 6. Transfer verdict for the Wiener–Hopf lemma (v13.849)

**CONDITIONAL TRANSFER.** Chain: discrete-Tikhonov ratios = weak-form ratios (numerical, ~0.1%, ledger) → weak-form = true v_±/C_± (**proven**, §4, for λ<λ_a). So v13.849's asymptotic-orthogonality mechanism transfers to the true deficiency vectors under **exactly one condition: λ_a>0**. **If λ_a≤0:** Lemma 6.2 does not apply at λ=0; the text defines no v_± at λ=0; the λ=−1 track (needs only λ_a>−1) is the fallback. The §7 RH-adjacent gap is not a new gap — but it is now the **only** gap between the Bucket 2 numerics and Suzuki's text. The value 0.48 remains unexplained under every reading.

## 7. Caveats

- A direct refinement probe (A=3, N=60/120) was OOM-killed under concurrent load and deferred; the ledger already records the needed stability (v13.840 gate 2.26→1.47e-6; v13.844 §2 gates; two-discretization agreement).
- No positivity, RH, or Hilbert–Pólya claim. The prime ramp is untouched.

## 8. Provenance

- Run: `~/workspace/d12/lane_b/sandbox/runs/20260928-210000-bucket2-selection-identity/` (report.md, STATUS.md, scripts/refine_select.py)
- Suzuki v2 PDF: `~/workspace/d12/cache/research-notes/2606.09096v2.pdf`; all quotes verified against pdftotext extraction, page numbers are PDF pages.
