# Cone Derivation Ledger v14.592 — Sandbox deposit: Airy comb and the two powers (addendum to the v14.550 gravity-road note)

**Timestamp:** 2026-10-18 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.550 (sandbox deposit: diameter–secant machine + gravity road note; this entry is its addendum), v14.366/v14.367/v14.441 (encoding note, pair form, Cayley addendum), v14.591 (live ledger max at allocation; collision-checked immediately before — next-free was v14.592).
**Status:** exploratory addendum deposit under Jeremy's explicit 2026-10-18 authorization ("Ledger it plus a short research-note addendum"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no prior claim. All numbers are the output of the deposited producer script, run clean at deposit. **No derivation of $G$ is claimed**; the hierarchy item of v14.550 §3 remains open.

## What was deposited

Research-notes, two files, commits `85f0bda5168a8c997278e4e674b14fa7b37956e7` (addendum) and `ba862aa9ba278738d7868329c53a276d6e6f2daf` (producer):

- `Airy_Comb_and_the_Two_Powers_Addendum.md` — SHA-256 `fdce569a15ce2d956bbe31190d9b9781d8a83fcb49dc26de08e0df7af6194fa9`
- `airy_powers_probe.py` — SHA-256 `3e920d24387b6cf758a40ff2786557e38513d52edd42d096237918e133cd0b1f`

Workspace originals remain in `d12/explorations/unit-circle-secant/`.

## Content summary (as tagged in the addendum)

- **§1 The Airy comb [D, computed].** The neutron bouncer's pure-number factor is Airy-zero differences: from $\hbar, m_n, g$ alone, $\varepsilon_0 = (\hbar^2 m_n g^2/2)^{1/3} = 0.6016$ peV and the comb $\nu_{13} = 463.0$ Hz, $\nu_{1\to7} = 1120.5$ Hz, $\nu_{2\to9} = 1141.7$ Hz, against qBounce-reported $\sim$1120 / $\sim$1142 Hz — the factorised (pure number) × (scale) shape exists in running gravitational spectroscopy, with Earth as source (returns $g$, not $G$). Quarter alignment: $|a_n| \approx [(3\pi/2)(n-\tfrac14)]^{2/3}$ (0.76% at $n=1$ → 0.003% at $n=12$; Maslov/Langer quarter, same family as the 1/4 Casimir and $(j+\tfrac12)^2$) and $j_{1,s} \approx \pi(s+\tfrac14)$ for the project signature function (2.49% → 0.056%). **Clean negative:** small-rational (denominator ≤ 36) matches to Airy transition ratios are at chance level (0.03–0.15%).
- **§2 The GM-wrap [D, computed].** Jeremy's geometric restatement of the unwrap — every diameter-$(n+k)$ circle wrapped onto the unit circle by its AM, point carried by the GM half-chord — reproduces the Cayley pair form exactly (worst discrepancy $1.7\times10^{-16}$, random pairs). The unwrapping power 1/2 *is* the geometric mean of the AM divisions.
- **§3 The two powers [D exact/computed; dictionary remark O].** Archimedean inventory (symbolically verified): cone's share 1/3 (cone : sphere : cylinder $= \tfrac13:\tfrac23:1$); parabolic segment exactly 2/3 of its circumscribing parallelogram, area $(8/3)\sqrt f\, h^{3/2}$ — the 3/2 decomposes as $1 + \tfrac12$ (height × GM-width). Evolute of the $f=\tfrac12$ parabola is semicubical, $27X^2 = 8(Y-1)^3$, cusp at $(0,1)$: a second exact 2/3 on the curve. Mechanism: the bouncer phase-space boundary is a parabola, its action is a segment ($\propto E^{3/2}$), Bohr–Sommerfeld + Maslov quarter gives $E_n \propto (n-\tfrac14)^{2/3}$ — so the spectral warp $2/3 = 1/(1+\tfrac12)$ and the GM unwrap are the same square root. Measured slopes: $\varphi_n \sim n^{-0.4997}$, $|a_m| \sim m^{0.6668}$. The composed constant $|a_n|\varphi_n^{4/3} \to (36\pi^2)^{1/3}$ is recorded as forced exponent arithmetic (bookkeeping, not signal). **Dictionary candidate [O]:** the pending Suzuki $t \leftrightarrow x$ entry gains a candidate form — cone coordinate read as action / parabolic-segment area, warp $E \propto J^{2/3}$ as its spectral shadow. Unbuilt.

## Verification

- Producer `airy_powers_probe.py` executed clean at deposit (exit 0, `DONE`); all cited numbers are its stdout.
- All three files (addendum, producer, this entry) re-read from the repository after commit and byte-compared against the workspace originals (SHA-256 above for the two research-notes files).

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `new_physics_claim = false`; `G_derived = false`; `hierarchy_generator_found = false`. The addendum records a computed probe, two exact classical identities, and one tagged-open dictionary candidate.

## Disposition

Deposit complete. The $t \leftrightarrow x$ dictionary candidate (cone coordinate as action/segment area) is the live thread this entry leaves open, alongside v14.550's two $G$ items. Further work on it is sandbox-side on Jeremy's line.
