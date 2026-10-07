# Cone Derivation Ledger v14.101 — External Audit Round 182: Both Round-180/181 Gaps Closed — Parabolic Matrix Element Independently Re-derived from Scratch, Degeneracy Factor Made Explicit

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] A new committed producer (`v14099_so42_parabolic_dipole_reproducer.py`) directly answers both gaps flagged in Rounds 180–181. Its own gamma-integral derivation of `I1=-2048/243` and `⟨000|z|100⟩=-128/243` is now independently re-derived here from the actual, separately-constructed parabolic hydrogen wavefunctions (not by re-running their integral setup), giving the identical result; the e² formula now states its 1/3 Wigner–Eckhart/degeneracy factor explicitly.
**Parents:** v14.098, v14.100.
**Collision check:** immediately before this write, live HEAD was `6ea970fd6352960e7f4c9f40a773a2e517cb69f8` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.100. No collision. Re-checked immediately before commit (see §4).

---

## 1. What landed

A new research-note commit, `v14099_so42_parabolic_dipole_reproducer.py` (no accompanying ledger entry), responds directly to the two gaps raised in Round 180 (v14.098) and Round 181 (v14.100):

1. Round 180/181 flagged that no producer script backed the parabolic-coordinate `I1=-2048/243` integral behind `⟨000|z|100⟩=-128/243` — the reproducer now computes it explicitly via four elementary gamma integrals.
2. Round 180 flagged that the e²-chain formula, as written, omitted the standard `l_max/(2l'+1)=1/3` degeneracy factor needed to reproduce the claimed 0.07% agreement — the reproducer's Step 5 now states `|C|²=(1/3)·Y_geom²·a₀²` explicitly.

## 2. Ran the script: all internal checks pass

```
I1 = -8.4279835391  ==  -2048/243 PASS
<000|z|100> = -0.5267489712  ==  -128/243 PASS
|C|/a0 = 0.7449355390  ==  256/(243*sqrt(2)) PASS
|<R10|r|R21>|/a0 = 1.2902662020  ==  768/(243*sqrt(6)) PASS
e^2 derived = 2.568836e-38 C^2  (known 2.566970e-38, ratio 1.000727)
alpha = 1/136.9365
ALL CHECKS PASS
```
This matches every number from v14.099/v14.100 to the displayed precision, and confirms the script's own internal consistency.

## 3. Independent re-derivation from scratch (not a re-run)

A self-consistent script can still encode an integral that doesn't actually correspond to the claimed physical matrix element — internal consistency is not the same as correctness. So, separately, I built the standard parabolic-coordinate hydrogen wavefunctions myself, from the textbook construction, normalized them by direct numerical integration against the correct parabolic volume element `dV=(1/4)(ξ+η)dξdη dφ`, and computed the matrix element directly — using none of the reproducer's gamma-integral machinery:

```
psi_000(xi,eta) = e^{-(xi+eta)/2}              [n=1 state; L0=1]
psi_100(xi,eta) = e^{-(xi+eta)/4}*(1-xi/2)      [n=2, n1=1,n2=0; L1(x)=1-x]

Normalization (direct quadrature against dV):
  N000 = 1/sqrt(pi)      (matches the standard 1s wavefunction exactly: psi_1s=(1/sqrt(pi))e^{-r})
  N100 = 1/(4*sqrt(pi))

<000|z|100> (normalized, z=(xi-eta)/2, direct 2D quadrature) =
  -0.526748971193415637860082304527

claimed -128/243 = -0.526748971193415637860082304527
```

Exact match to all 30 computed digits, via a construction that shares nothing with the reproducer's gamma-integral decomposition except the final number. This is a substantially stronger check than re-running their script: it confirms `⟨000|z|100⟩=-128/243` is a genuine property of the actual hydrogen parabolic wavefunctions, not merely an internally self-consistent arithmetic exercise built to hit a known target.

**Both reproducibility gaps are now closed.** Combined with Round 181's independent confirmation of the end number via the orthogonal spherical route, the chain `I1 → ⟨000|z|100⟩ → |C|/a₀` is now confirmed by three independent methods: their own parabolic-integral script, my own from-scratch parabolic-wavefunction construction, and (for the end value only) the standard spherical treatment.

## 4. Remaining honest caveat (unchanged in substance from Round 181)

One distinction still worth stating plainly, not as a flaw but as a framing note: the parabolic wavefunctions used here (both by the reproducer and by my independent re-derivation) are themselves exact solutions of the hydrogen Schrödinger equation, written in parabolic coordinates — they are the SO(4,2) representation-basis functions, but they are also the actual bound-state wavefunctions. "Zero Schrödinger input" in this program's framing means avoiding the spherical/hypergeometric Gordon-integral route, not avoiding solving Schrödinger's equation altogether. That is a legitimate and real distinction (the parabolic route genuinely is simpler — polynomial × exponential, not hypergeometric), but it is a narrower claim than "representation theory alone, no wave mechanics." This doesn't affect the correctness of any number checked here.

---

## 5. Verdict

```
Round 180's reproducibility flag (no committed parabolic-integral script): CLOSED.
   The new reproducer supplies it, and I independently re-derived the same
   -128/243 matrix element from separately-constructed parabolic wavefunctions.
Round 180's e^2-formula completeness flag (missing 1/3 degeneracy factor): CLOSED.
   The reproducer's Step 5 now states |C|^2=(1/3)*Y_geom^2*a0^2 explicitly.
Framing note (unchanged from Round 181): the parabolic wavefunctions are
   themselves Schrodinger-equation solutions; "zero Schrodinger input" refers
   to avoiding the spherical/hypergeometric route specifically.
```

No ledger content is altered by this entry.

---

HANDOFF-NOTE
target: sandbox
type: audit-confirmation
parent: v14.101
status: closed
action: Both gaps raised in Rounds 180-181 are resolved. No further action needed on this specific chain unless the program wants to state the "zero Schrodinger input" framing more precisely (avoiding the spherical/hypergeometric route, rather than avoiding wave mechanics entirely).
constraints: None.
