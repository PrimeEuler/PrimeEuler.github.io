# Cone Derivation Ledger v13.850 — External Audit Round 119

Date: 2026-09-28

Auditor: External audit thread (Claude, independent instance).

Scope: v13.848 (the selection-identity verdict — "SELECTS, conditionally": Suzuki's true deficiency vectors are exact `T_a`-inversions with no minimum-norm anywhere in the text, and the `H^1_0` weak-form of v13.840 is proven to compute them, conditional on `λ_a>0`) and v13.849 (the Wiener–Hopf lemma attempt — an honest obstacle characterization, not a proof).

Verdict: **PASS on both. v13.848's two new theorems about Suzuki's objects were independently re-derived by hand from first principles (not just checked against the write-up) and hold. v13.849's central algebraic claim was independently re-derived by hand and separately confirmed with a synthetic numerical test unrelated to the sandbox's own code.**

## 1. v13.848 — citation check

Pulled the PDF text directly for every citation. Lemma 6.2's "admit unique solutions, and these functions span the eigenspaces..." (p.21) reproduces exactly. §6.3's "which uniquely determines `f_z` for each fixed `C≠0`, since `T_a` is invertible" (p.22) reproduces exactly. Theorem 1.1 — "the self-adjoint operator `A_a`... is the Friedrichs extension of the symmetric operator `B_a`" (p.4) — reproduces exactly. I did not independently redo the "`minimum-norm` never occurs in §§6–8" full-text-absence claim (that requires trusting their search rather than mine), but every positive citation I checked was exact, which is the pattern this sandbox track has held to since v13.838.

## 2. v13.848 §2 — "the continuum (8.5) needs no selection," re-derived from scratch

This is a new theorem about Suzuki's objects (not something the text states), so I did not accept the write-up's three bullets as given — I reconstructed the argument myself from Lemma 6.2 alone:

- **`U` injective.** `(Uv)''=-(T_av)` follows directly from (8.4)'s own definition (`-k_{xx}` integrated against `v` *is* `T_av`, and differentiating the convolution `Uv=\int k(\cdot,y)v(y)dy` twice pulls the derivative onto the continuous kernel). So `Uv=0 \Rightarrow T_av=0 \Rightarrow v=0` by Lemma 6.2's invertibility (`λ<λ_a`). Confirmed.
- **`\mathrm{Ran}(U)\cap\{\text{affines}\}=\{0\}`.** An affine function `Ax+B` has zero second derivative, so if it's `Uv` for some `v`, then `0=(Uv)''=-T_av`, forcing `v=0` (by the same injectivity) and hence `Ax+B=Uv=0`. This is a two-line consequence of the same fact, and it's the key lemma that makes the rest work.
- **The augmented map `[U|X](v,A,B):=Uv+Ax+B` is injective.** If `Uv+Ax+B=0`, then `Ax+B=-Uv\in\mathrm{Ran}(U)`, so by the previous bullet `Ax+B=0`, and then `Uv=0` forces `v=0`. Three lines, no gaps.
- **Existence.** Given `C_\pm e^{\pm x}` (whose second derivative is itself, hence in `L^2` on a bounded interval), set `v_0:=T_a^{-1}(\mp C_\pm e^{\pm x})` (using bijectivity of `T_a`, not just injectivity, which Lemma 6.2 also gives for `λ<λ_a`); then `Uv_0-C_\pm e^{\pm x}` has zero second derivative, i.e. is some specific affine function `A_0x+B_0`, giving exactly the pair `(A,B)=(-A_0,-B_0)` making `C_\pm e^{\pm x}+Ax+B\in\mathrm{Ran}(U)`.

Injectivity + existence together give unique solvability of (8.5) jointly in `(v,A,B)`. This is correct, and it's a real, freestanding piece of Fredholm-alternative reasoning built entirely on Lemma 6.2 — not asserted, derived.

## 3. v13.848 §4 — the Friedrichs-extension convergence argument, cross-checked against Suzuki's own proof

This is the entry's most significant claim: that the `H^1_0` Galerkin computation (v13.840) provably converges to Suzuki's true `v_\pm`, not just empirically agrees with a differently-discretized computation (which is as far as v13.842's falsification test went). I worked out independently why this should be true before checking their citation: since `H^1_0=D(B_a)` and the form domain `D(Q_\lambda)` is, by construction, the completion of `C_c^\infty` under the *energy* norm `\|\cdot\|_{Q_\lambda}$ — a different topology from the standard `H^1` norm — and since `C_c^\infty\subset H^1_0\subset D(Q_\lambda)`, density of `C_c^\infty` in `D(Q_\lambda)` (by definition) forces `H^1_0` to also be dense in `D(Q_\lambda)` under the energy norm, *provided* `H^1_0` isn't itself already energy-closed short of the full domain. I then read Suzuki's own §3.2 (the proof of Theorem 1.1, p.14) directly, expecting to have to take this on faith — and found the paper proves exactly this: "if `E\subset\overline{C_c^\infty(-a,a)}^{\|\cdot\|_Q}`, then `D(\bar Q_B)=D(Q)`. It follows that the Friedrichs extension of `B` coincides with `A`." That is the density argument, stated and proved by Suzuki himself as the mechanism for Theorem 1.1. Given that, Lax–Milgram (unique energy-norm solution) and Céa's lemma (Galerkin convergence under trial-space density in the energy norm) are standard and correctly invoked. This section holds up to independent scrutiny at the level I could reach without re-deriving Suzuki's own Lemma 3.1/Theorem 1.1 proof from scratch — and I didn't have to, because it's already there on the page.

**Consequence I want to be explicit about:** this changes the shape of the Horn A/B story from Rounds 115–116. The natural-BC falsification test showed *empirically* that Dirichlet and non-Dirichlet discretizations agree, which argued against a boundary-artifact explanation for the `Θ(e^A)` growth. v13.848 now gives an *analytic* reason the `H^1_0` computation should converge to the true object in the first place — a stronger and independent form of support for the same conclusion, not a re-run of the same test.

## 4. v13.849 — self-correction, then re-derived by hand

The entry opens by retracting its own initially-briefed lemma as trivial by Cauchy–Schwarz (`|\langle w_A,Pf\rangle|/(e^A\|w_A\|\|Pf\|)\le 1/e^A\to0` — correct, and correctly identified as content-free before being reported as a result). I independently re-derived the actual (non-trivial) claim, Lemma 2 of §2 — `\mathrm{corr}(w_A,Pf)=(t\rho_1+\rho_2)/\sqrt{t^2+1}` — from the definitions of `w_A`, `\rho_1,\rho_2,t` by hand, using only the parity fact `\langle Px,P1\rangle=0`, and got the identical formula. I then wrote a short independent script with synthetic random vectors (not the sandbox's D12 kernel, not their code) enforcing only the parity orthogonality constraint, and confirmed the formula numerically (`direct corr = 0.034810971642020294`, `formula corr = 0.0348109716420203`, exact match) — this is a general linear-algebra identity, correctly stated, true for *any* vectors satisfying the stated orthogonality, not something specific to their kernel that I had to trust.

The reported finding — that the cancellation is a delicate `O(1)` magnitude balance between two stably nonzero, oppositely-signed correlations (`\rho_1>0>\rho_2`), not a structural orthogonality — is exactly what Lemma 2 predicts given the reported `\rho_1,\rho_2` values staying `O(1)` rather than shrinking, and the entry's conclusion (the kernel is outside classical Wiener–Hopf theory because the D12 screw grows rather than being `L^1`) is a correct characterization of why the standard toolkit doesn't apply here. The honest disclosure of the OOM-killed scripts (`wh2/wh3`) and the resulting reliance on `wh1` data plus exact parity for the parity-split numbers is exactly the right way to report a partial run.

## 5. What remains open, and is stated as open

Both entries are explicit that: (a) the transfer chain to Suzuki's true `v_\pm` still requires `\lambda_a>0`, unresolved and correctly named as "the only gap between the Bucket 2 numerics and Suzuki's text"; (b) the value `0.48` itself is unexplained under every reading; (c) the medium Wiener–Hopf lemma (`\mathrm{corr}\to0`) remains a conjecture, not a theorem, with a precisely named obstacle (growing, non-`L^1` kernel) rather than a vague "still working on it."

## Self-audit note

No error of my own found this round. Both entries' central new mathematical claims were checked by independent derivation rather than by re-reading the write-up, and both held.

## Result

\[
\boxed{\textbf{PASS: v13.848 and v13.849 confirmed.} \textbf{v13.848's two new theorems (unique joint solvability of the continuum (8.5); Céa-lemma convergence of the }H^1_0\textbf{ Galerkin method to Suzuki's true }v_\pm\textbf{, via the Friedrichs-extension density argument Suzuki himself proves in §3.2) were independently re-derived from Lemma 6.2 and Theorem 1.1 and hold. v13.849's correlation-decomposition lemma was independently re-derived by hand and confirmed by an unrelated synthetic numerical test; its "no structural orthogonality, growing kernel outside classical theory" finding is honestly reported as an obstacle, not dressed up as progress. The single remaining gap in the whole Bucket 2 program is now sharply and consistently named across both entries: }\lambda_a>0\textbf{.}}
\]
