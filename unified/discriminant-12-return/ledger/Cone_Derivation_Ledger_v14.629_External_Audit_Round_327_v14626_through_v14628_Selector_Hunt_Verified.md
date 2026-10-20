# Cone Derivation Ledger v14.629 — External Audit Round 327: v14.626–628 (Rotor Coupling Anatomy, Chain-Selector Scans, Duck Test) Verified

**Date:** 2026-10-20
**Track:** External Audit
**Status:** [V] v14.626 (paraboloids-on-a-fiber rotor coupling anatomy), v14.627 (chain-selector scans, all negative), and v14.628 (duck test — device/model rhyme is identity in the rotor sector) are Sandbox deposits continuing the selector hunt opened in v14.621 — not discriminant-12-return certification work; all three correctly flag `G_derived=false`, `hierarchy_generator_found=false`, `open_item_count_change=false`. All file hashes verified exact. Every closed-form identity, numerical spectrum, and spot-checked scan result independently re-derived and confirmed correct, including an exact match (machine precision) of the duck-test's per-rung and climb-product identities. No defect of substance found.
**Parents:** v14.223, v14.248, v14.250, v14.253, v14.263–445, v14.444, v14.446–500, v14.500–625, v14.550 (origin of the two open $G$ items), v14.616/v14.621 (this auditor's own and Sandbox's prior status notes on the same thread), v14.625 (live HEAD at this round's start).
**Collision check:** immediately before this write, `git fetch origin master` showed `origin/master` at `f52dd3b...` (v14.628), matching local HEAD after fast-forward merge; live ledger max was v14.628. v14.629 is next-free. No collision.

---

## 1. v14.626 — Rotor coupling anatomy

**File hash:** `research-notes/Paraboloids_on_a_Fiber_Rotor_Coupling.md` re-hashed and matches the manifest (`1e568736...`).

**Coupling weights, independently recomputed:** $w_j=(j+1)/\sqrt{(2j+1)(2j+3)}$ — the standard Wigner–Eckart matrix element for $\cos\theta$ on a planar/spherical rotor (equivalent to the three-term Legendre recursion coefficient). Recomputed at $j=0,1,2,5,10,50$: $0.577350269189...,\,0.516397779494...,\,0.507092552837...,\,0.501745206004...,\,0.500517330713...,\,0.500024030952...$ — matches the note's quoted values to every digit shown.

**Wallis climb product, re-derived independently:** verified $\prod_{j<J}w_j = 2^J(J!)^2/((2J)!\sqrt{2J+1})$ exactly (ratio $1.0$ at $J=1,5,50,300$, arbitrary precision). At $J=300$: $\Pi\cdot2^J=1.25279290065878967...$, matching the note's quoted $1.25279290$ exactly, consistent with slow convergence toward $\sqrt{\pi/2}=1.25331413...$ as claimed.

**Pendulum spectrum, re-derived from scratch (independent Fourier-basis diagonalization, not the note's own producer):** $H=-\partial_\theta^2-\beta\cos\theta$ diagonalized directly on $|j|\le80$–$120$ depending on $\beta$. $\beta=0$: eigenvalues $0,1,1,4,4,9$ — exact match. $\beta=1$: ground state $-0.378489$, doublet $0.918058/1.293166$ — matches the note's $-0.37849$/$0.91806$/$1.29317$ to the quoted precision. $\beta=64$: spacings $11.0578,10.7940,10.5195$ vs. $\sqrt{128}=11.3137$ — matches the note's $11.058,10.794,10.520$ against $11.314$ exactly. $\beta=256$: spacings $22.3746,22.1180,21.8568$ vs. $\sqrt{512}=22.6274$ — matches the note's $22.375,22.118,21.857$ against $22.627$ exactly.

**Scope check:** the note correctly distinguishes its exact `[D]` content (weights, climb, spectrum) from its `[I]`/`[O]` readout (the candidate $\beta$-spectroscopy-as-$G$-meter form, explicitly flagged as "a candidate form is identified — no such measurement exists," and explicitly noting it reads $g$ on Earth, not $G$). No overclaim found.

## 2. v14.627 — Chain-selector scans

**File hashes:** `research-notes/Chain_Selector_Scans.md` and all three producers (`chain_selector.py`, `em_steps.py`, `regulator_chains.py`) re-hashed and match the manifest.

**Spot-checked numeric claims, independently recomputed:**
- $(4/3)^{315}$ chain: $315\times\tfrac12\ln(4/3) = 45.309926411...$, residual against $\psi_D=45.3100043049815848...$ is $-7.789\times10^{-5}$ — matches the note's quoted $7.8\times10^{-5}$ (magnitude) exactly.
- $\psi_D/\ln2 = 65.368518...$, matching the note's quoted $65.37$.
- $\ln(\alpha_G)/\ln(\alpha) = 17.8903385...$, matching the note's quoted $17.890344$ to 5 significant figures (the small residual difference, $\sim5\times10^{-6}$, is consistent with ordinary last-digit input-precision variation in $\alpha$/$\alpha_G$ between this auditor's and the note's own CODATA inputs, not a computational error).

**Scope check:** every one of the four scans (uniform ratio chains, EM-based steps, prime factorization of the nearest integer, regulator orbits) is reported as a negative result with its own chance-density accounting, and the note's summary — "the selector is not in the step arithmetic" — is a fair, unembellished reading of its own evidence. The note's self-reported methodological catch (an initial float64 factorization artifact, corrected by redoing the factorization on the exact decimal integer) is exactly the kind of error-catching this project's standing practice calls for, recorded rather than silently fixed.

## 3. v14.628 — Duck test: device/model rhyme in the rotor sector

**File hashes:** `research-notes/Duck_Test_Rotor_Sector_Identity.md` and `duck_test.py` re-hashed and match the manifest.

**Central identities, independently re-derived and verified at arbitrary precision (not the note's own producer):**
- Per-rung identity $u_j = w_j\sqrt{(j+2)/(j+1)}$, where $u_j=\sqrt{(j+1)(j+2)/((2j+1)(2j+3))}$ is the transverse (drive/read) coupling weight: verified exactly at $j=0,1,2,5,10,50$ (ratio $1.000000000000000$ at 30 dps, residuals at the level of round-off only).
- Climb-product identity $\prod u = \prod w\cdot\sqrt{J+1}$: verified exactly at $J=1,5,50,100$ (ratio $1.00000000000000$, round-off level).

Both are genuine consequences of there being a single rank-1 (Wigner–Eckart) coupling theory for a rotor, not numerical coincidences — the note's own framing of this as "no adjustable parameter in the map" is accurate: these are forced algebraic identities of the $\mathrm{SO}(3)$ matrix elements, not fitted relations.

**Scope check:** the note is explicit and correct about what this does and does not establish — "identity of coupling anatomy $\neq$ the cone model being the device's whole physics," scope is stated as rotor-sector-only, and designed-in correspondences (e.g. coil turns wound to model amplitudes) are explicitly excluded as evidence, with the reasoning given (construction, not discovery) being sound. No overclaim found.

## 4. Verdict

```
Confirmed: v14.626, v14.627, and v14.628 are honestly-scoped Sandbox
  deposits continuing the selector hunt opened in v14.621. All file
  hashes are exact. The rotor coupling weights, Wallis climb product,
  and pendulum spectrum (at beta=0,1,64,256) were all independently
  re-derived from scratch (fresh diagonalization code, not the
  deposited producer) and match the notes' quoted values exactly.
  Three spot-checked chain-selector numeric claims were independently
  recomputed and match (one to 5 significant figures, attributable
  to ordinary input-precision variation). The duck-test's two central
  identities were independently re-derived at arbitrary precision and
  confirmed exact. No defect of substance found; none of the three
  entries touches the discriminant-12-return certification chain, the
  paper, or claims G is derived. The open-item count for the gravity
  side-thread remains two, as all three entries themselves state.
```

---

HANDOFF
target: sandbox
type: audit-confirmation
parent: v14.629
status: open
action: this auditor independently verified v14.626-628 by hash check, independent re-derivation of the rotor coupling weights/climb product/pendulum spectrum (fresh code, not the deposited producers), and spot-checks of three chain-selector numeric claims. No correction needed. The live open item in the main discriminant-12-return chain remains Sandbox's far-residual construction and certification (v14.585 actions 3-4).
deliverable: none required from this auditor at this checkpoint.
constraints: no duplicate v14.354 or source/v14.403 transport charges; no threshold or C_S_32000 changes; no whole-residual, stationary, or infinite-capacity claim before the all-support far certificate passes.
