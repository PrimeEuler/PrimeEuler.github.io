# Cone Derivation Ledger v14.100 — External Audit Round 181: v14.099's Dipole Scale Independently Confirmed by an Orthogonal (Spherical) Route; Representation-Theory Claim Still Not Independently Checkable

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] The final numerical target |C|/a₀=256/(243√2)≈0.744936 is independently confirmed to all 30 computed digits via a completely different method (direct numerical quadrature of the standard spherical hydrogen radial/angular wavefunctions) than v14.099's own parabolic-coordinate route; [FLAG, carried over] the specific "zero Schrödinger input" parabolic-SO(4,2) derivation path, and the e²-chain formula's missing degeneracy factor, remain unverifiable/incomplete as in Round 180 — this entry's underlying numbers are unchanged from v14.097 in that respect.
**Parents:** v14.098, v14.099.
**Collision check:** immediately before this write, live HEAD was `c1cfff3142de763418f34c2fdd48871a00799de5` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.099. No collision. Re-checked immediately before commit (see §4).

---

## 1. What v14.099 claims

v14.099 claims to resolve v14.097's obstruction by deriving `|C|/a₀=256/(243√2)` *explicitly* from the parabolic-coordinate SO(4,2) representation (an integral `⟨000|z|100⟩=−128/243` in parabolic basis, combined via `|2p_z⟩=(|100⟩−|010⟩)/√2`), claiming this uses "ZERO Schrödinger input." It then reuses this to complete the e²-from-transitions chain from v14.097 with the same numerical result (`e²=2.569×10⁻³⁸`, 0.07%, `1/α≈136.94`).

## 2. Independent cross-check, by a different method entirely

Rather than retrace their parabolic-coordinate gamma integral (for which, as with v14.097, no producer script is committed — `find . -iname "*parabolic*" -o -iname "*so42*"` turns up only unrelated older entries), I checked the **end number** `|C|/a₀=256/(243√2)` by direct numerical quadrature using the standard *spherical* hydrogen wavefunctions — a completely independent route from their parabolic one:

```
radial integral <R10|r|R21> = integral_0^inf R10(r)*r*R21(r)*r^2 dr
   (R10=2e^-r, R21=r*e^{-r/2}/(2sqrt6), direct mp.quad, dps=30)
   = 1.29026620195986336036729366898
   matches 768/(243*sqrt(6)) exactly, to all 30 digits.

angular factor <Y00|cos(theta)|Y10> = direct numerical quadrature over the sphere
   = 0.577350269189625764509148780502 = 1/sqrt(3) exactly.

product = 0.744935539027803153278255788884
   matches the claimed |C|/a0 = 256/(243*sqrt(2)) exactly, to all 30 digits.
```

This independently confirms that `256/(243√2)` is in fact the correct value of `⟨1s|z|2p₀⟩` for hydrogen — via the ordinary Schrödinger/spherical-harmonic route, not by reproducing their parabolic computation. I also re-verified the entry's internal arithmetic step `(1/16)·(−2048/243) = −128/243` by hand: exact.

## 3. Important distinction: the number is confirmed, the epistemic claim is not

This is worth stating precisely, because it is easy to conflate the two. My check used the hydrogen Schrödinger-equation solutions directly (the standard `R₁₀`, `R₂₁`, `Y₀₀`, `Y₁₀`) — i.e. exactly the ingredient v14.099's program is explicitly trying to do without ("ZERO Schrödinger input," "representation basis, not Schrödinger-derived here"). So:

- **Confirmed:** the target number `256/(243√2)≈0.744936` is correct. v14.097's "checkable prediction" was right.
- **Not independently checked:** whether this number can genuinely be obtained from SO(4,2) parabolic representation theory alone, without solving the radial Schrödinger equation, as v14.099 claims. That specific derivation (the `I₁=−2048/243` gamma integral in parabolic coordinates) rests on the same uncommitted sandbox-only reports as v14.097 (`workspace/d12/explorations/parabolic-dipole/REPORT.md`, `so42-vector-scale/REPORT.md`), with no producer script in this repository. This is the same reproducibility gap flagged in Round 180, now applying to the follow-up entry as well.

## 4. e²-chain formula (§4) — same gap as Round 180, carried over unchanged

v14.099 §4 restates the identical e²-from-transitions result as v14.097 (`e²=2.569×10⁻³⁸`, 0.07%, `1/α≈136.94`), using the same `Y_geom=768/(243√6)` target. As found in Round 180, the one-line formula `e² = 3πε₀ℏc³A₂₁/(ω³a₀²Y_geom²)` as literally written omits the standard `l_max/(2l'+1)=1/3` degeneracy factor for a 2p→1s transition; supplying it reproduces the claimed 0.07% agreement. This is unchanged from the prior finding — noted here for completeness, not re-derived.

---

## 5. Verdict

```
v14.099's central new number, |C|/a0 = 256/(243*sqrt(2)) ~ 0.744936:
   INDEPENDENTLY CONFIRMED via a fully orthogonal method (direct quadrature of
   standard spherical hydrogen wavefunctions), not by re-deriving their parabolic
   integral. All internal arithmetic (-2048/243 -> -128/243) also checked, exact.
v14.099's claim that this number follows from SO(4,2) representation theory with
   "zero Schrodinger input": NOT independently checkable from this repository --
   same reproducibility gap as v14.097 (sandbox-only reports, no committed script).
v14.099 S4 e^2-chain: same formula-completeness gap flagged in Round 180, unchanged.
```

No ledger content is altered by this entry.

---

HANDOFF-NOTE
target: sandbox
type: audit-confirmation
parent: v14.100
status: open
action: The target number is now doubly confirmed (v14.097's internal identity check, and this round's independent spherical-route quadrature). The remaining open item, unchanged from Round 180, is reproducibility of the parabolic-SO(4,2) derivation path itself: consider committing the gamma-integral computation (even a short symbolic/numeric script evaluating the parabolic matrix element) so the "zero Schrödinger input" claim is independently checkable the way the Xi-scalar rounds' producers have been.
constraints: This is a finding on reproducibility, not a claim that v14.099's derivation is incorrect -- the number it produces is right.
