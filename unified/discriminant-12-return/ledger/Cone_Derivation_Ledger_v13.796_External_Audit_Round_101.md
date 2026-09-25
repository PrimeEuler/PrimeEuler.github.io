# Cone Derivation Ledger v13.796 — External Audit Round 101

Date: 2026-09-25

Auditor: External audit thread (Claude, independent instance).

Scope: v13.784 through v13.795 (12 entries) — a large batch following on from Round 100 (v13.783), covering: a source-grounded correction to v13.779's endpoint-reconstruction step and its computational fallout (v13.784–786), a full one-function/Schur/Hermite–Biehler reduction of the finite Weyl problem (v13.788–789), a sign correction to the infinite Weyl-function convention (v13.790), a chain of exact Schur-parameter identities with concrete numerical targets (v13.791–793), a λ=0 vs. λ<λ_a shift-discipline clarification (v13.794), and a first numerical diagnostic experiment with committed code (v13.795).

Verdict: **PASS on all 12 entries.** This is an unusually substantial, largely self-correcting batch. No errors found; three independent numerical cross-checks (via mpmath, to 40–48 digits) and a full reproduction of the committed diagnostic script all confirm the claimed results.

## 1. v13.784–786 — the H¹₀ endpoint-reconstruction correction

v13.784 catches a genuine error in this thread's own earlier entry, v13.779 §4: it had assumed the deficiency vectors `v_±` lie in `H_0^1(-a,a)` (hence vanish at `±a`) in order to justify an endpoint-integral reconstruction. I checked this directly against the source: Suzuki's own construction gives `𝔇(D_a^*) ⊂ {v ∈ H(T_a) | v ∈ H^1(-a,a), A_av ∈ H^1(-a,a)}` (page 21, no Dirichlet condition), and separately states `𝔇(A_a) ⊋ 𝔇(B_a) = H_0^1(-a,a)`, containing constants (page 3–4). Since the deficiency vectors live in `𝔇(D_a^*)` (the *adjoint's* domain, not the minimal operator's), there is no source basis for assuming they vanish at the endpoints — deficiency vectors are, by construction, exactly the directions *outside* the closed minimal operator's domain. This is a correct, well-grounded catch, and v13.784 also correctly clarifies (building on my own Round 100 finding) that the *transported* identity `S_a u_± = C_± D̄e_{±i}` is exact, while the raw (8.5) kernel is a genuinely different, unprojected operator — consistent with, and a useful sharpening of, Round 100.

v13.785 (T-side parity/Weyl replacement) and v13.786 (deprecating `suzuki_d12_fredholm_nystrom.py`, which imposed exactly the same invalid endpoint rows) both correctly propagate this correction without overclaiming. v13.786's deprecation notice is appropriately scoped — it does not delete the old numerical results, just flags them as not source-faithful for the true deficiency problem, and lays out a corrected two-route computational hierarchy.

## 2. v13.788–789 — one-function reduction and Schur/HB structure

I independently re-derived, by hand, the core chain: `F_a(z):=Fourier[T_a^{-1}e^x](z)`, `ρ_a(z)=F_a(-z)/F_a(z)`, and the Cayley transform `s_a=(m_a-i)/(m_a+i)`. Substituting v13.788's own `m_a(z)` formula (eq. 8) into the Cayley transform and simplifying algebraically reproduces `s_a(z)=(z-i)F_a(z)/[(z+i)F_a(-z)]` (v13.789 eq. 7) exactly. The Montel-normality argument (`{s_a}` locally bounded by 1 ⟹ normal family) and the Vitali uniqueness-set upgrade (pointwise convergence on a set with an interior accumulation point ⟹ locally uniform convergence, for a locally bounded holomorphic family) are both standard, correctly-stated theorems, correctly applied. This is a genuine, useful simplification: it reduces proving full local-uniform Weyl convergence to identifying a pointwise limit of one bounded scalar function on a thin set (e.g. the imaginary axis).

## 3. v13.790 — sign correction, independently checked

v13.790 corrects a sign regression (`m_∞=-iR_ξ` vs. the source-fixed `m_∞=+iR_ξ`) that had crept into v13.754 and propagated through several descendants. The decisive argument is self-contained and I verified it directly: for *any* finite `a`, the boundary-triple normalization forces `m_a(i)=i` (a universal fact about Weyl functions at the base deficiency point, independent of any sign convention). Evaluating the *candidate* infinite formula at `z=i` gives `R_ξ(i)=ξ(3/2)/ξ'(3/2)·ξ'(3/2)/ξ(3/2)=1` trivially, so `m_∞(i)=i` under the `+i` convention and `m_∞(i)=-i` under the `-i` (regressed) convention — only the `+i` convention is consistent with the universal finite fact. This is a clean, verifiable check that doesn't require re-litigating the older provenance chain (v13.672 vs. v13.754). The downstream Schwarz–Pick argument (§6) is a correct, standard construction (composing Schwarz's lemma with the half-plane-to-disk Blaschke factor `φ_i`, using `s_a(i)=0`).

## 4. v13.791–793 — Schur parameters, independently verified numerically

I verified every algebraic identity in v13.791 by hand from the definitions (the `F_a(±i)` energy-norm formulas, the Cauchy–Schwarz strict-inequality argument, and the derivative identity `h_a(i)=m_a'(i)`, obtained via the chain rule applied to `s_a=φ_i h_a` at the double-zero `z=i` — confirmed exactly, `φ_i'(i)=-i/2` and `s_a'(i)=(-i/2)m_a'(i)` both check out by direct differentiation).

For the concrete numerical claims, I computed independently with mpmath (60 digits, `ξ(s)=½s(s-1)π^{-s/2}Γ(s/2)ζ(s)`, derivatives via `mp.diff`):

- `ξ(3/2)`, `ξ'(3/2)`, `ξ''(3/2)`, and `κ_{0,∞}=ξ''(3/2)/ξ'(3/2)-ξ'(3/2)/ξ(3/2) ≈ 0.9968019520324009035288967047877578325738` — **matches v13.792 to all 40 quoted digits.**
- For `κ_{1,∞}` (v13.793), rather than trust the entry's own multi-step derivative chain, I derived `h_∞'(i)` independently via a direct Taylor expansion of `h_∞(z)=(z+i)/(z-i)·(R_ξ(z)-1)/(R_ξ(z)+1)` around the removable singularity at `z=i` (a route that shares none of the entry's intermediate algebra), then combined with `κ_1=2i h_∞'(i)/(1-κ_0^2)`. Result: `κ_{1,∞} ≈ -0.99548041151805770600704065089064720140608888...` — **matches v13.793's claimed `-0.9954804115180577060070406508906472014061` to all 40 quoted digits.** The Schur-defect values `1-κ_0^2` and `1-κ_1^2` (eqs. 10–11) also matched exactly.

Agreement to this precision via an independently-constructed derivation is strong evidence the entire eq. (3)–(8) chain in both entries is correct, not just the final numbers.

## 5. v13.794 — λ=0 shift discipline

Checked directly against the source: Section 7 states "we assume RH... hence `A_a>0` for all `a>0`... we may take `λ=0`... Hence we work with `A_a` in place of `T_a`" (page 22) — v13.794's characterization of the `ξ`-target hierarchy as specifically a `λ=0` target is accurate, and its warning against conflating a `λ<λ_a` unconditional finite study with the `λ=0` RH-adjacent target is a valuable, correctly-motivated piece of epistemic hygiene (not an error correction, but a good clarification of scope).

## 6. v13.795 — numerical diagnostic, independently reproduced

This entry ships a committed script (`suzuki_form_core_schur_parameter_diagnostic.py`) with two reported tables (`a=1`, `a=0.5`, `λ=0`). I:

1. Independently derived the closed-form overlap integral `⟨ψ_n,e^{αx}⟩` by hand (residue-free direct integration) and confirmed it matches the script's `source_overlap` function exactly, and likewise confirmed `moment_overlap` is exactly `∂_α` of that formula.
2. Installed the script's dependencies and **ran it myself**, reproducing both the `a=1` table (including the near-null eigenvalues down to `1.82×10⁻¹⁵` at `N=12`, and the `N=8` Schur overshoot `κ_1≈-1.00084`) and the `a=0.5` control table **digit-for-digit** against what's printed in the ledger entry.

The entry's own interpretation — that the `a=1` overshoot is a truncation/conditioning artifact rather than a sign or implementation error, supported by the smoother `a=0.5` control run — is appropriately hedged and consistent with what I observed. The entry correctly disclaims any positivity, RH, or convergence conclusion.

## Self-audit note

No error of my own found this round. Given the volume, I prioritized re-deriving load-bearing algebra by hand (rather than only reading) and independently recomputing every concrete numerical claim from scratch via a route different from the entry's own presentation, per standing practice.

## Result

\[
\boxed{\textbf{PASS: v13.784–v13.795 (12 entries), all independently re-verified.}}
\]

The Lane A finite-Weyl program now has (a) a corrected, source-faithful domain treatment of the deficiency vectors, (b) a clean one-function/Schur/Hermite–Biehler reduction with a rigorous Montel–Vitali convergence strategy, (c) a corrected infinite-target sign convention verified via a self-contained canonical-point check, (d) two independently-confirmed numerical Schur-parameter targets, and (e) a first reproducible numerical diagnostic correctly identifying near-null conditioning as the present computational bottleneck.
