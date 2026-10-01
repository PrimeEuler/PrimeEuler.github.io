# Handoff bundle: prime ordinates on the cone — binary compression machinery

Posted 2026-10-01 at the project owner's direction, for the worker taking up the
**prime-ordinates-on-the-cone** program. Sandbox provenance throughout; status
tags: [D] derived, [N] numerical/provisional, [I] interpretation, [O] open.

## What this bundle is

The binary-compression framework detects L-function zero ordinates as frequencies
in a prime-side signal. The ledger chain below built it, closed 5/5 explicit-formula
loops, and derived *why* the detection works. The open question — the worker's
program — is **why the cone geometry realizes the selector**: placing the
prime-side ordinates onto the cone.

## The ledger chain (all under `unified/discriminant-12-return/ledger/`)

- v13.882 — Binary decompression: the zeta zero wave in the prime-side signal.
- v13.883 — Binary mod-24 analysis: where the zeros are, how much DSUM sees.
- v13.884 — Twisted binary: the χ₁₂ zero spectrum.
- v13.885 — Twisted explicit-formula loop closed (χ₁₂ tracking).
- v13.887 — Two selection axes of the twisted mod-12 probe.
- v13.888 — Universality probe: χ₃, χ₄, χ₅ spectra.
- v13.889 — β (χ₄) explicit-formula loop closed.
- v13.890 — **5/5 loops closed** + trivial-zero sign corrections.
- v13.891 — **Selector principle derived (capstone).**
- v13.892 — Quantization exploration: map, not flag (no H–P construction yet).
- v13.894 — Suzuki stability test: decisive negative for the spring-through-Suzuki
  positivity bridge (indicator weights break positivity immediately).

## The 5/5 loops [N]

Block-500 explicit-formula tracking correlations (zeros used):

| L-world | zeros | corr |
|---------|-------|------|
| ζ       | 100   | 0.9995 |
| χ₄ (β)  | 50    | 0.9976 |
| χ₃      | 46    | 0.9959 |
| χ₅      | 53    | 0.9925 |
| χ₁₂     | 67    | 0.9840 |

Pattern: cleaner spectral detection → tighter loop. χ₄ was the cleanest binary
probe and is the tightest loop per zero.

## The selector principle [D]

b(n) = 1 − 1_P(n) − δ_{n,1} gives B(x) = ⌊x⌋ − π(x) − 1 exactly; the
Riemann–von Mangoldt / Guinand–Weil explicit formula then puts Li(e^{ρt}) terms
at frequency Im(ρ) on log scale t = log x. The observed prime-side zero spectrum
is a standard explicit-formula theorem — RH/GRH not required (Re(ρ) controls the
envelope; Im(ρ) sets the tone). Full derivation: `selector_theory_derivation.md`.

Related but distinct: `selector_principle_exploration.md` — the "positivity
selects" heresy (Weil positivity over all test functions as the selector of the
zero set itself, not of oscillator frequencies). Different selector, different
selected object; do not conflate.

## The open cone question [O]

Why does the cone geometry realize the selector? The frequencies live on log
scale; the cone's helices lift via x + it. The worker's program: put the
prime-side ordinates onto the cone — nodes, helices, the 12-node/V₄ apparatus —
and find the geometric form of the selection. The ψ = log lcm identity
(v13.895, Λ as the jump function) is the natural arithmetic input.

## Files in this bundle

- `selector_theory_derivation.md` — the [D] derivation (Guinand–Weil frequency
  selection). Start here.
- `selector_principle_exploration.md` — the positivity-selector heresy exploration.
- `compression_cone_handoff_README.md` — this file.
