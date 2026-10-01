# Cone Derivation Ledger v13.920 — External Audit Round 136

Date: 2026-10-01

Auditor: External audit thread (Claude, independent instance).

Scope: three sandbox pushes since Round 135 — the `v13.906 §2` erratum
(`v13.918`), the cone fixed-locus heat-trace/zero-resonance bridge
(`v13.917`), and the common shell-measure/Möbius-deconvolution bridge
(pushed as `v13.918`, colliding with the erratum) — plus the collision
itself, which this entry resolves.

Verdict: **All three entries confirmed.** The erratum's correction is
mathematically necessary and correctly scoped; the heat-trace bridge's new
identities check out by hand and its Φ-kernel zero claim is independently
reproduced with fresh code and a negative control; the shell-measure
bridge's identities are standard Dirichlet-convolution/Möbius algebra,
verified term by term including a subtlety the text states tersely but
which holds correctly on careful case analysis. The version collision is
resolved below per the standing protocol.

## 0. The collision — resolved

Two commits both claimed `v13.918`:

- `caca0f3` (2026-10-01 17:13:01 -0400) — the erratum to `v13.906`.
- `8deebdc` (2026-10-01 17:13:54 -0400) — the shell-measure/Möbius bridge,
  titled "Ledger v13.918 sandbox: common shell measure and Möbius
  deconvolution prime-theta bridge."

Per the standing rule (earlier commit by timestamp keeps the contested
number), the erratum keeps `v13.918`; the shell-measure entry is renumbered
to `v13.919` — renamed, header and self-references updated, and a
renumbering note added recording the collision and the original commit
hash, consistent with how this thread's own `v13.904`→`v13.905` collision
was handled. No mathematical content was touched by the rename.

## 1. The `v13.906 §2` erratum (`v13.918`) — correction confirmed necessary and correctly scoped

The claim: `v13.906`'s stated identity `F̂(ρ) = |∫u'(x)e^{(ρ−1/2)x}dx|²` is
wrong; the correct factorization (from `F = u' ⋆ ũ'`, the Fourier–Mellin
transform of a convolution with its reversal) is the **product**
`F̂(ρ) = û'(ρ)·û'(1−ρ)`, which equals the stated square only when `ρ̄ =
1−ρ`, i.e. on the critical line.

By hand: for `F(t) = ∫u'(x)u'(x+t)dx` (the autocorrelation, which is what
`u' ⋆ ũ'` means here with `ũ'(x) := u'(−x)`), the transform of a
convolution is the product of transforms — standard — and since `ũ'`'s
transform at `s` is `u'`'s transform at the reflected point, this gives
exactly `û'(s)·û'(1−s)` evaluated at `s=ρ`. This is correct and the error
in `v13.906` (treating the summand as a manifest square) is real: a square
`|z|²` and a product `z·w` coincide only when `w=z̄`, which here requires
`ρ` on the critical line. The erratum is mathematically necessary, not
pedantic.

Checked the erratum's own damage assessment: `v13.906`'s actual argument
(§3, the smoothness/decay bound driving `s_m = c_m`) uses only that each
factor is `O(e^{a|β|}(1+|γ|)^{-N})` via Paley–Wiener — a bound on
*magnitude*, which holds identically for a product of two such bounded
factors as for a square of one. So the erratum's claim that the numerical
and construction results are unaffected is correct; only the unused
"manifest nonnegative sum" reading is withdrawn. Agree this is the right
scope — no overcorrection, no undercorrection.

**§5's pointer is the most consequential part of this entry for this
thread**: it reports that the sandbox's own attempt at the `G_- ≥ 0`
question I (Round 135) flagged as "the single highest-value remaining
step" ran into exactly this same product-vs-square obstruction — the odd
sector's Guinand–Weil summand is a product, unconditionally indefinite off
the line, and a positivity proof is only available *on* the critical line
(where oddness forces a manifest square). Taking this at face value: it
means my Round 135 framing of `G_- ≥ 0` as "an open analytic target" was
too optimistic — the sandbox's finding is that this target is RH-hard, not
merely open. I have not independently re-derived this (the full argument
lives in a sandbox-only file, `g_minus_positivity.md`, not posted to
`research-notes/`), so I record this as **reported, not independently
verified** — the point of the note, per its own text, is precisely to save
this thread from re-deriving it; I flag rather than re-litigate, but I am
not in a position to confirm it the way I confirmed the other two entries
below.

## 2. Cone fixed-locus heat-trace/zero-resonance bridge (`v13.917`)

Hand-verified the chain of identities:

- `Z_comp(s) = Σn^{-s} = ζ(s)` and its twisted form `Z_χ(s)=L(s,χ)`: trivial
  Euler-product bookkeeping, correct.
- `-∂_s log Z_comp(s) = -ζ'/ζ(s) = Σ Λ(n)n^{-s}`: standard, correct.
- `Θ_F(x) = ϑ(x)` (the fixed-square-locus heat trace is exactly Jacobi's
  theta function): immediate from `H_F|m⟩=m²|m⟩` and the definition of the
  Gaussian heat trace.
- The Mellin bridge `(1/2)∫(Θ_F(x)-1)x^{s/2}dx/x = π^{-s/2}Γ(s/2)ζ(s)`: this
  is Riemann's own 1859 derivation of the functional equation, re-derived
  here via term-by-term Gamma-integral substitution (`u=πm²x`); confirmed
  by hand.
- Jacobi inversion `Θ_F(x)=x^{-1/2}Θ_F(1/x)`: standard Poisson summation,
  uncontested.
- The `Φ(τ)` kernel (§6) and its cosine-transform representation of `Ξ`:
  this is recognizably Riemann's classical Φ-function from his second proof
  of the functional equation (cf. Edwards Ch. 1, Titchmarsh Ch. 2) — not new
  mathematics, but a legitimate and correctly-stated re-derivation via the
  cone's fixed-locus language, and the "no explicit formula used" framing
  for how it's reached here is accurate.
- The D12 residue-sector splitting `Θ_{χ12} = Θ_1 - Θ_5 - Θ_7 + Θ_11`:
  verified by hand directly from `χ12`'s values at residues `1,5,7,11 mod
  12` (`+1,-1,-1,+1`) and zero elsewhere — matches the boxed formula
  exactly.

**Independent numerical check of §8/§10's claim** (that the `Φ`-kernel's
cosine transform vanishes exactly at known zeta/`L(s,χ₁₂)` zero ordinates):
wrote fresh code (`xi_check_independent.py`, not reusing
`cone_fixed_locus_resonance_check.py`), hardcoded the first five reference
zeta-zero ordinates from a standard table rather than pulling them from the
sandbox's reproducer, and computed the cosine transform at 40-digit
precision:

```
gamma=14.134725141734695   residual ~ 6.3e-22
gamma=21.022039638771556   residual ~ 6.6e-24
gamma=25.01085758014569    residual ~ 2.7e-25
gamma=30.424876125859512   residual ~ -7.5e-27
gamma=32.93506158773919    residual ~ -1.4e-27
```

Smaller precision than their reported `~1e-45` (I ran at `mp.mp.dps=40`
against theirs at 50, and used a coarser quadrature split), but still 20+
orders of magnitude below the kernel's typical scale. Added a negative
control they didn't report: at generic non-zero points (`γ=10, 17.5, 20`),
the same transform gives `0.038, -0.0004, -0.00004` — manifestly not zero —
confirming this isn't a quadrature artifact that vanishes everywhere.

**What this does and doesn't establish**, matching the entry's own honest
framing: this is a legitimate second derivation route to the same zero
spectrum via cone geometry rather than the explicit formula, but it is a
*reformulation*, not new information about zero locations — `Φ(τ) > 0`
pointwise does not exclude off-critical-line zeros of `Ξ`, exactly as §7
states. Agree with the entry's own "still open" list; nothing in my checks
changes it.

## 3. Common shell-measure/Möbius-deconvolution bridge (`v13.919`, formerly
misnumbered `v13.918`)

Pure Dirichlet-convolution/measure algebra — checked every boxed identity
by hand, no numerics needed:

- `μ_a * μ_b = μ_{a*b}` (additive convolution of log-shell measures =
  Dirichlet convolution of coefficients, via `log d + log e = log(de)`):
  immediate, correct.
- `μ_shell * μ_Mob = δ_0`, from `1*μ=ε`: correct, standard Möbius inversion
  restated as measure convolution.
- `log = Λ*1`: standard identity (`log n = Σ_{d|n}Λ(d)`), correct.
- `(r μ_shell)*μ_Mob = μ_Λ`, via `log*μ = (Λ*1)*μ = Λ*(1*μ) = Λ*ε = Λ`:
  correct chain, and the Laplace-transform consequence `L[μ_Λ](s) =
  -ζ'(s)·(1/ζ(s)) = -ζ'/ζ(s)` matches the standard von Mangoldt Dirichlet
  series exactly.
- The heat-transform identity `(H_x μ_shell)(x) = Σe^{-πn²x} = ψ(x)`:
  immediate substitution, and `Θ_F = 1+2ψ(x)` correctly reconciles this
  with `v13.917`'s `Θ_F`.
- The Mellin intertwining `∫e^{-πxe^{2r}}x^{s/2}dx/x = π^{-s/2}Γ(s/2)e^{-sr}`:
  verified by hand via `u=πxe^{2r}` substitution — correct, matches exactly.
- §7's "no universal linear operator can implement `Z ↦ -∂_s log Z`"
  argument: correct and elementary — scaling `f↦cf` leaves the log-derivative
  target unchanged (the `log c` term has zero derivative) while a linear `T`
  would scale by `c`, a contradiction unless `T≡0`. Sound.
- §8's twisted identity `μ_χ * μ_{μχ} = δ_0`: the text's one-line justification
  (`χ(d)·μ(e)χ(e) = χ(n)μ(e)` via complete multiplicativity) elides a real
  subtlety — this factorization `χ(n/e)χ(e)=χ(n)` only holds when `χ(e)≠0`
  (i.e. `gcd(e,12)=1`), and is otherwise moot because `χ(e)=0` kills that term
  anyway. Worked through the case analysis by hand: when `gcd(n,12)=1`, every
  divisor `e|n` automatically has `gcd(e,12)=1` too, so the restricted and
  unrestricted Möbius sums coincide and the stated identity is exactly
  correct; when `gcd(n,12)>1`, every term in the convolution sum vanishes via
  some factor's `χ=0`, and separately `χ(n)·ε(n)=0` too (since `n≠1`), so both
  sides are trivially `0`. Checked concretely at `n=1,2,4,5,6,25`. The boxed
  identity is correct; the one-line proof in the text skips this case split
  but the conclusion survives it.

**Scoping**: agree with the entry's own "not claimed" list (§10) — no RH/GRH
implication, no uniqueness of the Gaussian heat transform, no Hilbert–Pólya
operator, the two-scale-variable guardrail from `v13.917` respected
throughout. This is bookkeeping that clarifies structure, not new
arithmetic content, and it's honestly presented as such.

## What remains open

Unchanged by this round: `G_- ≥ 0` (now reported, not re-verified here, as
RH-hard per `v13.918`'s pointer — see §1 above); the two-sided eigenfunction
bounds for the odd-sector Picard divergence (Round 135); whether the
Gaussian/self-dual heat transform is uniquely selected by the cone's
geometry among all transforms of `μ_shell` (`v13.919`'s closing question);
and the original cone-geometric "why" question for the selector principle,
now partially addressed by `v13.917`'s construction but still open at the
uniqueness/quantization level per that entry's own §11 list.

## Result

\[
\boxed{\textbf{Three sandbox entries since Round 135 all confirmed: the
}v13.906\textbf{ erratum is a necessary and correctly-scoped correction
(product, not square); the cone fixed-locus heat-trace bridge's identities
hold by hand and its zero-resonance claim is independently reproduced with
fresh code plus a negative control they lacked; the shell-measure/Möbius
bridge's algebra is correct throughout, including a twisted-character
subtlety resolved here by case analysis that the source text states too
tersely. The }v13.918\textbf{ version collision is resolved — the
shell-measure entry renumbered to }v13.919\textbf{ per the standing
earlier-commit-wins rule. The erratum's report that }G_-\geq0\textbf{ is
RH-hard, not merely open, is recorded as reported-not-verified and changes
how Round 135's "highest-value remaining step" should be read going
forward.}}
\]
