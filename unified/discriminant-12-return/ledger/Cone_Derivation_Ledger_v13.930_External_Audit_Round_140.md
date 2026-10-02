# Cone Derivation Ledger v13.930 — External Audit Round 140

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.929` (Xi Weyl-target Herglotz/RH equivalence and the
Montel–Vitali barrier).

Verdict: **Confirmed.** This is a fully rigorous piece of classical
complex/entire-function analysis — a correct derivation (in this project's
own source-fixed variable conventions) of the equivalence "RH ⟺ a specific
logarithmic derivative of `Ξ` is a Herglotz function on `C₊`," which is
itself a known type of RH-equivalent reformulation in the literature, not
previously stated for this project's specific `m_∞` object. The genuinely
new and valuable content is §4–5's "Montel–Vitali barrier": a sharp
demonstration that the project's own natural next technical step (proving
finite-to-infinite Weyl convergence on *any* interior set, even one
entirely inside the classically zero-free region) is not a convergence
lemma at all — it is exactly as hard as RH. I hand-verified every step and
added independent numerical checks of the two load-bearing identities.

## 1. Hand-verified: the Hadamard-product / Herglotz argument (§2.1, RH ⟹ Herglotz)

`Ξ(z):=ξ(1/2−iz)` is even (checked via the functional equation `ξ(s)=ξ(1−s)`:
`Ξ(−z)=ξ(1/2+iz)=ξ(1−(1/2+iz))=ξ(1/2−iz)=Ξ(z)` ✓) and of order 1, so its
zero-counting density (`~(log T)/2π`, standard) makes `Σ1/γ²` convergent —
exactly the condition under which an even order-1 entire function has the
genus-0 Hadamard product `Ξ(z)=Ξ(0)∏(1−z²/γ²)^{m_γ}` with **no** exponential
correction factors. This is the same well-known simplification used for the
classical Riemann `Ξ`-function product (Titchmarsh Ch. 2). Differentiating
termwise and converting to partial fractions, I confirmed by hand that
`−2z/(γ²−z²) = 1/(z−γ)+1/(z+γ)` exactly, reproducing the entry's (6)–(7)
precisely. Then `Im[1/(t−z)] = y/((t−x)²+y²) > 0` for `z=x+iy`, `y>0`, `t`
real — elementary — so every term of the sum, with positive coefficient
`m_γ`, contributes positive imaginary part; the sum (assuming the standard
local-uniform convergence of the paired series, itself standard) is
therefore Herglotz. Correct throughout.

## 2. Hand-verified: Herglotz ⟹ RH (§2.2)

If `m_∞` were holomorphic on all of `C₊` (required for Herglotz), it could
have no pole there. But at any zero `z₀` of `Ξ` of multiplicity `m≥1`, the
logarithmic derivative has a genuine *simple* pole of residue `m` — this is
a standard, elementary fact (checked directly: `Ξ(z)≈c(z−z₀)^m` near `z₀`
gives `Ξ'/Ξ ≈ m/(z−z₀)`, independent of `m` being 1 or larger). So
holomorphy on `C₊` forces `Ξ` zero-free there. The variable substitution
`s=1/2−iz` sends `Im(z)>0 ⟺ Re(s)>1/2` (verified directly: `z=x+iy`,
`s=1/2−i(x+iy)=1/2+y−ix`, so `Re(s)=1/2+y>1/2` exactly when `y>0`) — so no
zero of `ξ` has `Re(s)>1/2`; the functional equation then forbids `Re(s)<1/2`
too (a zero there would force a mirror zero with `Re>1/2`), forcing every
nontrivial zero onto `Re(s)=1/2`. This is RH. Correct, and matches the
standard logic used elsewhere in the literature for this style of
equivalence.

## 3. Hand-verified: the Schur-class reformulation (§3)

The Cayley transform `s_∞=(m_∞−i)/(m_∞+i)` of a Herglotz function is Schur
(standard, since Cayley transform maps `C₊→D` biholomorphically and the
Herglotz/Schur classes correspond under it). `s_∞(i)=0` follows from
`m_∞(i)=i`, which I verified is not approximate but *exactly* forced by the
definitions: expanding `Ξ(i)=ξ(3/2)` and `Ξ'(i)=−iξ'(3/2)` (both checked
directly from the chain rule) gives `m_∞(i) = −C_∞·Ξ'(i)/Ξ(i) =
−[ξ(3/2)/ξ'(3/2)]·[−iξ'(3/2)/ξ(3/2)] = i` algebraically, for *any* value of
`C_∞` defined that way — a clean identity, not a coincidence to be
numerically discovered. Schwarz–Pick then gives `|s_∞(z)|≤|φ_i(z)|` where
`φ_i(z)=(z−i)/(z+i)`, so the deflated `h_∞=s_∞/φ_i` is Schur. The converse
direction (Schur `h_∞` ⟹ Herglotz `m_∞` via the inverse Cayley transform) is
immediate algebra. Correct.

**Independent numerical check** (fresh code, direct evaluation of the
actual completed zeta function via `mpmath`, not reusing any part of this
project's own `Φ`/`g(t)` machinery): computed `C_∞=ξ(3/2)/ξ'(3/2)` directly
and confirmed `m_∞(i)=i` to the full precision tested (`0.0+1.0j` exactly,
no residual). Then checked `Im(m_∞(z))>0` at five sample points scattered
through `C₊` (`0.5+0.3i`, `2+i`, `5+0.5i`, `10+2i`, `−3+0.7i`) — positive at
every point, consistent with RH (as expected, since RH is verified for all
computationally accessible zeros) and with the theorem's forward direction.
This is a plausibility check, not a proof substitute — the theorem itself
is already fully rigorous by hand.

## 4. The Montel–Vitali barrier (§4–5) — the valuable new result

This is the part that matters for the project's strategy, and it's
correctly reasoned: given (a) every finite `h_a` is Schur (`|h_a|≤1` on
`C₊`, cited from `v13.790`, hence a normal family by Montel), and (b)
*pointwise* convergence `h_{a_n}→h_∞` merely on some set `S` with an
accumulation point inside `C₊` where the target formula (11) is already
holomorphic — Vitali's theorem (a standard strengthening of Montel: a
normal family converging pointwise on a set with an interior accumulation
point converges **locally uniformly on the whole domain**) upgrades this to
a genuine holomorphic limit `h_*` on all of `C₊`. The identity theorem then
forces `h_*` to agree with the meromorphic formula (11) wherever the latter
was already holomorphic, and since `h_*` itself has *no* poles (being an
honest locally-uniform limit of holomorphic functions), this analytically
continues (11) as Schur straight through any of its apparent interior
poles. By the §3 equivalence chain, that's RH. I checked this logic
carefully — Montel and Vitali are both correctly stated and correctly
composed, and the identity-theorem step is the standard one. Nothing here
requires numerics; it's exactly the kind of place where the entry's own
discipline (flag an RH-hard gate rather than grind on it) earns its keep.

**§5's sharpening is the sharpest and most useful single observation in the
entry**: the set `S={iy : y∈I}` for any nontrivial interval `I⊂(1/2,∞)`
lies entirely in the region where `Ξ` is unconditionally zero-free
(`Re(s)=1/2+y>1`, where `ζ(s)≠0` trivially) — yet it still has an
accumulation point inside `C₊` (it's a continuum of points on the positive
imaginary axis). So even proving convergence restricted to this
"obviously safe" classically-zero-free axis segment is, via the same
Montel–Vitali bootstrap, already equivalent to RH. This correctly forecloses
what might otherwise look like an easy partial-progress strategy.

## 5. The `v13.927` sign correction (§7) — verified correct

Re-derived `E(z)=Ξ(z)[1−ic_∞m_∞(z)]` by hand using their relation
`ξ'/ξ = −ic_∞m_∞` (itself consistent with §1's `m_∞=−C_∞Ξ'/Ξ` once one
notes the lowercase `c_∞` here is defined as the reciprocal of §1's
uppercase `C_∞` — a notational overload worth flagging for future entries,
though not an error since both are independently and correctly defined
where they're used). Expanding `−ic_∞Ξ[m_∞−τ_HB]` with `τ_HB=−i/c_∞` and
confirming it equals `Ξ[1−ic_∞m_∞]` exactly (the `ic_∞·(−i/c_∞)=1` term
checks out) confirms the corrected sign is right, and the conclusion
`τ_HB∉R` is unaffected either way, exactly as claimed.

## What remains open

Unchanged in substance, now sharpened: the Hilbert–Pólya quantization
question is precisely located at the `λ=0` finite-to-infinite Weyl limit,
and this round confirms that limit is RH-hard, not a technical gap — so
`v13.929 §10`'s two legitimate remaining targets (an unconditional
canonical-system limit on an admissible shifted branch away from the `λ=0`
Xi identification, or an explicitly-labeled conditional-on-RH architecture)
are the only non-circular ways forward. Also still open: `G_-≥0` (Round
136, reported RH-hard); the odd-sector Picard-divergence eigenfunction
bounds (Round 135); and `v13.910`'s "continuum if," reopened by Round 139.

## Result

\[
\boxed{\textbf{v13.929 confirmed.} \textbf{Every step of the RH}
\Leftrightarrow\textbf{Herglotz equivalence and its Schur-class
reformulation checks out by hand (Hadamard product, partial fractions,
Cayley transform, Schwarz--Pick), and the two load-bearing exact identities
(}m_\infty(i)=i\textbf{, and positivity of } \mathrm{Im}\,m_\infty
\textbf{ at sample points) are independently confirmed numerically against
the actual completed zeta function.} \textbf{The Montel--Vitali barrier
(\S4--5) is a genuine, correctly-reasoned hardness result: it shows that
even the most modest-looking version of the project's own natural next
step --- proving Weyl convergence on an interval entirely inside the
classically zero-free region --- is already equivalent to RH, correctly
foreclosing that as an easier partial-progress route.}}
\]
