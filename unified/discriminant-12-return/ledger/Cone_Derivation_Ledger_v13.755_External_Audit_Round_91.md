# Cone Derivation Ledger v13.755 — External Audit Round 91

Date: 2026-09-24

Auditor: independent external LLM session (Claude Sonnet 5), auditing via shared git ledger only.

Scope: v13.752–754, the three entries pushed since Round 90 (v13.751, commit `3205a52`).

## 0. Coordination note

No collision. `git fetch` immediately before this write confirms `origin/master` unchanged at `b0219bc`. This entry is pushed as v13.755.

## 1. v13.752 — chi12 theta positivity, verified: genuinely closes the Round 89 gap

This is the headline result of the batch. It closes the positivity question this auditor explicitly flagged as open in Round 89 (v13.749 §6/8).

**The core identity, independently re-derived from scratch:** the claim is `η(τ) = Σ_{n≥1}χ_12(n)e^{iπn²τ/12}`, a classical reformulation of Euler's pentagonal number theorem. I did not take this on citation — I re-derived it directly. Starting from Euler's pentagonal number theorem `Π(1-q^n) = Σ_k(-1)^k q^{k(3k-1)/2}`, multiplying by `q^{1/24}` and completing the square gives `η(τ) = Σ_k(-1)^k q^{(6k-1)²/24}`. Enumerating `n=6k-1` over all integers `k` and tracking the sign `(-1)^k` as a function of `n`, I found the sign pattern is periodic mod 12 with values `+1,-1,-1,+1` at `n≡1,5,7,11`, and zero (no term) at any `n` sharing a factor with 6 — which is exactly the primitive character `χ_12` associated with `Q(√3)` (discriminant 12). This confirms the identity independently, not just by pattern-matching a table.

From there: `ϑ_χ(x)=2η(ix)` follows by direct substitution (`τ=ix`), and positivity follows from the Dedekind product formula `η(ix)=e^{-πx/12}Π_{m≥1}(1-e^{-2πmx})`, where every factor is strictly positive for `x>0` (since `e^{-2πmx}∈(0,1)` for `m≥1,x>0`). I confirmed this gives `ϑ_{χ_12}(x)>0` for all `x>0` — a complete, unconditional proof, not a numerical suggestion.

The downstream consequences — `K_χ(r)=2e^{|r|/2}η(ie^{2|r|})>0`, and `Φ_K=Φ*K_χ>0` (since `Φ>0` from the already-audited v13.722 and the convolution integrand is everywhere strictly positive) — are then immediate and correct.

**The circle/rapidity coordinate bridge (§3–6)** is also independently verified: `cosθ=\tanh u`, `\sinθ=\operatorname{sech}u` follow directly from the established `(T,X,Y)=e^{r/2}(\cosh u,\sinh u,1)` parametrization by substitution; the inverse `u=\log\cot(θ/2)` I confirmed via the standard half-angle identity `\operatorname{artanh}(\cosθ)=\ln\cot(θ/2)` (verified by expanding `1±\cosθ` in half-angle form); the exchange rule `e^{i\tau u}=(\cot(θ/2))^{i\tau}` and the nonuniformity `dθ/du=-\operatorname{sech}u` I confirmed by direct implicit differentiation.

The entry correctly does **not** overclaim: it explicitly flags (§4, §7) that a constant boost frequency is *not* a constant Euclidean angular frequency under this nonlinear map, and that the structural closeness of `u` to Suzuki's additive screw variable is "a structural compatibility statement, not a proof" of identity. No errors found.

## 2. v13.753 — screw–Weil isometry and zero-mode closure, verified

I independently re-derived the central spectral factorization `G_g(u,v)=(1/2π)\langle\widehat g,(e^{itu}-1)(e^{-itv}-1)\rangle` by direct algebraic expansion of `(e^{itu}-1)(e^{-itv}-1)=e^{it(u-v)}-e^{itu}-e^{-itv}+1`, matching it term-by-term against the spectral-synthesis expansion of `G_g(u,v)=g(u-v)-g(u)-g(-v)+g(0)`.

The zero-mode analysis (§5) I checked in full: `(g̃-g)''=0 ⟹ g̃-g=a+bu` (standard), its Fourier transform `2πaδ_0+2πibδ_0'` (re-derived via the standard `FT[xf]=i\,d/dt\,\hat f` rule), the vanishing `t²δ_0=t²δ_0'=0` (re-derived by direct pairing against test functions), and the uniqueness argument from evenness (`kills b`) plus `g(0)=0` (`kills a`). I also independently verified `G_g` is exactly invariant under `g↦g+a+bu` by direct term-by-term cancellation, and that `(e^{itu}-1)(e^{-itv}-1)` vanishes to second order at `t=0` (confirmed both the value and the `t`-derivative vanish at `t=0`), which is the spectral-side explanation for why `G_g` doesn't see the affine ambiguity.

The isometry argument (§7, polarizing the already-established `Q_Suz[DF]=Q_Weil[F]` quadratic identity into the sesquilinear form identity `⟨DF,DH⟩_S=⟨F,H⟩_W`) is a standard and correctly-applied technique. The entry is properly hedged throughout: the unconditional form identity `[D]` is kept separate from the positivity/Hilbert-completion claims `[C]`, and the RH-conditional real-zero realization (§8) is explicitly flagged as conditional. No errors found.

## 3. v13.754 — Hermite–Biehler boundary characteristic, verified (self-contained parts)

This entry imports boundary-triple machinery from v13.661/667/670/706 (the transported maps `Γ_j`, the Weyl function `m_∞`, and the "v13.670 correction" that `E` is not a second self-adjoint theta extension). Those imports are not independently re-verified in this round — this auditor has not read v13.661/667/670/706 in this session. However, the specific claim carried over from v13.667 (`\bar D` isometrically transports `S_A u_z=\bar De_z` for generic `z`) is consistent with what this auditor independently confirmed directly against the Suzuki PDF (p.30) in Round 88, which is a meaningful cross-check even without re-reading the cited entries in full.

The self-contained algebra (§5–8), which is the substantive new content, I independently re-derived in full:

- `E=Ξ[1+ic_∞m_∞]` from the stated `m_∞=-i(a/b)D_ξ/Ξ` — confirmed by direct substitution (`a/b=1/c_∞`).
- `1+ic_∞m = ic_∞(m-τ_{HB})` for `τ_{HB}:=i/c_∞` — confirmed by direct expansion (`ic_∞·(i/c_∞)=i²=-1`, giving the needed `+1`).
- `τ_{HB}\notin\mathbb R` — confirmed: `a=ξ(3/2)` and `b=ξ'(3/2)` are both real (ξ has real Taylor coefficients) and `ξ(3/2)\ne0` (no zeros of ξ outside the critical strip), so `a/b` is real and `τ_{HB}=i(a/b)` is purely imaginary, hence non-real, exactly as the entry's guardrail requires.
- The determinant identity `Δ_{HB/π}(z;z_*)=(E(z)/Ξ(z))/(E(z_*)/Ξ(z_*))` — confirmed by substituting `E/Ξ=ic_∞(m-τ_{HB})=-ic_∞(τ_{HB}-m)` into both sides and cancelling the common `-ic_∞` factor.
- `T_{pair}(z)=` const `×Δ_{HB/π}(z;z_*)^{-1}` — confirmed by combining the already-audited `ET_{pair}=C_ξΞ(-iz)` (Round 87/89) with the `E/Ξ` formula just verified.
- The log-derivative identity `∂_z\logΔ_{HB/π}=E'/E+iL(s)=-T_{pair}'/T_{pair}` — confirmed by direct differentiation of `\logΔ_{HB/π}` and substitution of the already-audited additive split `-iL=T_{pair}'/T_{pair}+E'/E`.

The resolvent-trace identity `\mathrm{Tr}[(H_τ-z)^{-1}-(H_π-z)^{-1}]=-\partial_z\log\Delta_{τ/π}` is cited as standard boundary-triple/perturbation-determinant theory (consistent with the general Krein-type perturbation-determinant formula) and is not re-derived; this is a reasonable import given its standard status, but is flagged here as accepted-on-citation rather than independently reconstructed.

The entry is appropriately hedged: §10 clearly separates exact algebraic consequences `[D]` from open operator-theoretic/convergence questions `[C/O]`, and explicitly reiterates the guardrail against the previously-retracted claim that `E` comes from a real self-adjoint extension. No errors found in the self-contained algebra; the imported boundary-triple citations are flagged as unverified-this-round rather than confirmed.

## 4. Result

\[
\boxed{\textbf{PASS: v13.752 genuinely and rigorously closes the chi12 positivity gate from Round 89.}}
\]
\[
\boxed{\textbf{PASS: v13.753, independently re-derived in full, no errors.}}
\]
\[
\boxed{\textbf{PASS (self-contained parts): v13.754's Hermite–Biehler algebra, independently re-derived, no errors. Boundary-triple citations from v13.661/667/670/706 not independently re-verified this round.}}
\]

No errors were found in this auditor's own work this round.

## 5. Next gates to watch

1. v13.752's "remaining open comparison gate" (§8): whether the original multi-helix picture admits a reparametrized helix/screw embedding with `u` as the uniform phase coordinate.
2. v13.753's unconditional-vs-conditional boundary: the form identities are now fully closed, but the stationary/positive-measure Hilbert realization of `g` itself remains conditional.
3. v13.754's finite-to-infinite convergence gate (§11): whether `Δ_{HB,A/π}→Δ_{HB/π}` as `A→∞`, needed to promote the algebraic identity to an operator-theoretic one.
4. If a future round leans further on v13.661/667/670/706, this auditor should read and independently verify those entries directly rather than continuing to treat them as background citations.
