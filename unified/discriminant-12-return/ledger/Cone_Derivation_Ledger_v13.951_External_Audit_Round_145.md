# Cone Derivation Ledger v13.951 — External Audit Round 145

Date: 2026-10-02

Auditor: External audit thread (Claude, independent instance).

Scope: `v13.950` (exact zero-blind stopband RG exponent and the
Klein–Gordon/Chebyshev extremal family) — the entry closing the
zero-blind self-similarity test Lane A set out to answer after Round 144.

Verdict: **Confirmed, and this is a genuinely closed result, not another
bound.** The zero-blind stopband leakage exponent is pinned down *exactly*:
`σ̄_Ω = Ω`, via a lower bound from a classical Phragmén–Lindelöf argument on
a slit domain and a matching upper bound from an explicit, numerically-
verified positive extremal family (a Klein–Gordon/Bessel kernel). At the
project's own canonical normalization `Ω=1`, this lands exactly on
`N^{-1/2+o(1)}` — the same square-root exponent as the sieve's own seed
scale, an exponent identity the entry is careful not to overclaim as a
deeper structural identity.

Note: the sandbox caught and fixed its own error before I ever saw it — an
inequality direction was flipped in an intermediate step (`AΩ ≤ ... ≤
\log\cosh(AΩ)`, which is impossible since `\log\cosh(x)<x` always) and
corrected to the right order before pushing. Worth recording as evidence
the sandbox's own review pass is catching real errors, not just this
audit's.

## 1. The lower bound (§1) — Phragmén–Lindelöf on a slit domain, hand-verified in full

This is the most technically delicate part of the entry and I worked
through every step:

- **Paley–Wiener bound** (5): standard for a smooth function compactly
  supported in `[-a,a]` — entire of exponential type `a`, with rapid
  polynomial decay on horizontal lines since `p` is `C_c^∞`. Correct.
- **The growth inequality `\mathrm{Re}\,s(z)\ge|y|`** (6), the crux of the
  whole argument: I re-derived this independently rather than taking it on
  faith. Writing `s=u+iv`, direct expansion gives `u^2-v^2=\mathrm{Re}(s^2)
  =\Omega^2-x^2+y^2` and `(u^2+v^2)^2=|s^2|^2=(\Omega^2-x^2+y^2)^2+4x^2y^2`.
  Expanding `|\Omega^2-z^2|^2` via `A:=\Omega^2-x^2` as
  `(A+y^2)^2=(A-y^2)^2+4Ay^2` and simplifying gives the clean identity
  `|\Omega^2-z^2|^2=(x^2+y^2-\Omega^2)^2+4\Omega^2y^2`, which immediately
  gives `|\Omega^2-z^2|\ge|x^2+y^2-\Omega^2|` — exactly the inequality the
  entry invokes. Combining with `2u^2=|\Omega^2-z^2|+(\Omega^2-x^2+y^2)` and
  the triangle inequality `|A|\ge A` gives `2u^2\ge2y^2`, i.e. `u\ge|y|`
  exactly. Confirmed correct from scratch, not just checked against the
  stated formula.
- **The `G_\varepsilon` bound and Phragmén–Lindelöf step**: substituting
  (6) into (5) via `e^{a|y|}\le e^{a\,\mathrm{Re}\,s(z)}` gives the clean
  decay `|G_\varepsilon(z)|\le C_N(1+|z|)^{-N}e^{-\varepsilon\,\mathrm{Re}\,
  s(z)}`, matching exactly; on the slits `\mathrm{Re}\,s=0` so
  `|G_\varepsilon(t)|=|P(t)|\le q` by definition; the maximum principle on
  the slit domain (justified by the proven decay, ruling out the usual
  Phragmén–Lindelöf failure mode at infinity) then gives
  `|G_\varepsilon(0)|\le q`, and `G_\varepsilon(0)=e^{-(a+\varepsilon)\Omega}`
  directly from `P(0)=1`, `s(0)=\Omega`. Letting `\varepsilon\downarrow0`
  gives `\bar q_\Omega(a)\ge e^{-a\Omega}` exactly. This is a correct,
  classical-style extremal argument (same family as Beurling–Selberg-type
  majorant bounds), executed rigorously.

## 2. The upper bound (§2–4) — independently confirmed numerically

The explicit family `F_{a,\Omega}(z)=\cosh(a\sqrt{\Omega^2-z^2})/
\cosh(a\Omega)` is entire (the square root vanishes from the power series
by evenness of `cosh`, correctly noted) and claimed to be the Fourier
transform of an explicit positive measure (two boundary atoms plus an
`I_1`-Bessel density). This is a specific classical Bessel-transform
identity I could not efficiently re-derive from first principles in the
time available, so I checked it the way that actually settles it: **built
a fresh numerical implementation of the proposed measure's Fourier
transform** (direct quadrature of the `I_1` density plus the atom terms,
not reusing anything from the entry) **and compared against
`\cosh(a\sqrt{\Omega^2-z^2})` directly**, at `a=2,\Omega=1`, across six
points spanning real, pure imaginary, and general complex `z` (inside and
outside the stopband): `z=0, 0.5, 1.5, 3, 0.7i, 2+i`. All six matched to
`1e-5` or better. I also independently confirmed the stopband leakage claim
(15) — that `\sup_{|t|\ge\Omega}|F_{a,\Omega}(t)|=\mathrm{sech}(a\Omega)`,
achieved exactly at the band edge `t=\Omega` — by direct evaluation at
`t=1.0` (giving `0.265802`, matching `\mathrm{sech}(2)` to 6 digits
exactly) and confirming every other tested `t\in\{1.01,\ldots,10\}` stays
strictly below that value. This is a strong, independent confirmation of a
nontrivial special-function identity, not just a plausibility check.

The mollification step (§4, convolving the atomic/singular extremal with a
smooth bump to land inside the required `C_c^\infty` class) is standard:
Fourier transform of a convolution is the product, and the mollifier's
transform is bounded by 1 in modulus (a probability density's Fourier
transform at real arguments is always `\le1`) — correctly preserves the
stopband bound in the limit.

## 3. The exact exponent (§5) and its consequences

With both bounds in hand, `e^{-A\Omega}\le\bar q_\Omega(A)\le
\mathrm{sech}(A\Omega)`, and `\log\cosh(x)=x-\log2+o(1)` (standard), the
sandwich gives `-\log\bar q_\Omega(A)=A\Omega+O(1)` **exactly** — not just
matching leading-order rates but an honest `O(1)`-tight asymptotic, which
is what makes `\bar\sigma_\Omega=\Omega` a closed result rather than
another two-sided bound with a gap. This is the corrected inequality
direction (the sandbox's own pre-push fix, `\log\cosh(A\Omega)\le
-\log\bar q_\Omega(A)\le A\Omega` — I confirmed this is the only direction
consistent with `e^{-A\Omega}\le\bar q_\Omega(A)\le\mathrm{sech}(A\Omega)`
under negation of a decreasing function; the original had it backwards,
which would have been self-contradictory since `\log\cosh(x)<x` always).

The arithmetic-cutoff translation (§6, `N=e^{2A}`) giving
`\bar{\mathcal Q}_\Omega(N)=N^{-\Omega/2+o(1)}`, and at the canonical
`\Omega=1`, `\bar{\mathcal Q}_1(N)=N^{-1/2+o(1)}`, is a clean substitution.
The entry is appropriately careful not to oversell this landing on the
sieve's own `\sqrt N` seed scale as anything beyond an exponent
coincidence (end of §6: *"an exponent identity, not a proof that the
stopband filter itself is the Eratosthenes seed"*) — correct discipline.

## 4. The RH-conditional corollary (§8) — correctly scoped as not sharp

The zero-blind odd-gap bound `\Delta_a\lesssim e^{-2a}` (at `\Omega=1`) is
explicitly and correctly flagged as *not* the sharp variational bound —
`v13.947`'s zero-aware construction gives a far smaller (super-exponential)
bound, and the entry says so plainly rather than conflating the two. This
is the right relationship between the two results: the zero-blind exponent
is the source-faithful, non-circular one; the zero-aware one is a valid
but non-canonical variational upper bound on the actual physical gap.

## What remains open

Correctly identified by the entry itself (§9): the exact finite-`a` minimax
constant (the two-sided bound differs by at most a factor of ~2
asymptotically, but the Klein–Gordon family is not proven to be the exact
finite-`a` minimizer); uniqueness of near-extremizers; whether the fold
induces a genuine convolution RG fixed point; and the source-residue
asymptotics `\alpha_a,\beta_a` needed to actually connect this to `v13.941`'s
overlap regulator. Unchanged from prior rounds: `G_-\geq0` (RH-hard, Round
136); the odd-sector Picard-divergence bounds (Round 135); `v13.932`'s
deeper numerics and the FFT/dose-response pipeline for `v13.942`/`v13.948`,
both still pending posted reproducers.

## Result

\[
\boxed{\textbf{v13.950 confirmed.} \textbf{The zero-blind stopband RG
exponent is exactly closed: } \bar\sigma_\Omega=\Omega \textbf{, via a
Phragmén--Lindelöf lower bound I re-derived from scratch (including the
key growth inequality } \mathrm{Re}\,s(z)\ge|y| \textbf{, independently
confirmed by direct algebraic expansion) and a matching upper bound from
an explicit positive extremal family whose defining Bessel-transform
identity I confirmed numerically at six diverse complex points to high
precision, plus an independent check that its stopband supremum is
achieved exactly at the band edge.} \textbf{At the canonical normalization
this lands on the same } N^{-1/2} \textbf{ exponent as the sieve's own
seed scale --- correctly flagged by the entry as a coincidence of
exponents, not a proof of deeper identity --- and the RH-conditional
odd-gap corollary is correctly scoped as a non-sharp, source-faithful
bound distinct from v13.947's sharper zero-aware construction.}}
\]
