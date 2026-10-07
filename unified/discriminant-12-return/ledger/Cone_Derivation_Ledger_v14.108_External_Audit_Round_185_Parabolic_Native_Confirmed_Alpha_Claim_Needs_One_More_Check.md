# Cone Derivation Ledger v14.108 — External Audit Round 185: v14.105 (Parabolic-Basis-Is-Cone-Native) Confirmed; v14.106's α-Independence Needs One More Check Before It's Solid

**Date:** 2026-10-07
**Track:** External Audit
**Status:** [V] v14.105's claim independently confirmed with exact (zero-residual) numerics at two shells; [PARTIAL] v14.106's algebra is independently re-derived and confirmed correct, and its numerics are consistent with everything verified so far, but the deeper metrological claim — that the reduced Compton wavelength `λ_c` used as input is actually free of any prior `α` dependence — rests on a subtlety this thread cannot fully settle without more information, and should be checked before the draft note (v14.107) states it as "no α input" without qualification.
**Parents:** v14.104, v14.105, v14.106, v14.107.
**Collision check:** immediately before this write, live HEAD was `4ca78404de5dc57155a4b81591b34119e727f836` (`git fetch origin master` confirms local HEAD == origin/master); live ledger max was v14.107. No collision. Re-checked immediately before commit (see §4).

---

## 1. v14.105 (parabolic basis is bicone-native): independently verified, exact

v14.105's claim: the parabolic states `|n₁n₂m⟩` are the simultaneous eigenbasis of `L_z=J^a_z+J^b_z` and `A_z=J^a_z−J^b_z` (built directly from the bicone's own `su(2)⊕su(2)` generators), so they are cone-native algebraic objects, not something separately solved for or imported from a differential equation.

Using the exact bicone Schwinger-boson operators already built and verified in Round 184, I checked this directly — not by re-deriving their report (uncommitted, as before) but by testing the claim's content on the actual operators:

```
n=2 shell (Na=Nb=1), testing ||Lz*v - lz*v|| and ||Az*v - az*v|| for each raw Fock state v:
  Fock(1,0,1,0): Lz=+1.00 (residual 0.0), Az=+0.00 (residual 0.0)
  Fock(1,0,0,1): Lz=+0.00 (residual 0.0), Az=+1.00 (residual 0.0)
  Fock(0,1,1,0): Lz=+0.00 (residual 0.0), Az=-1.00 (residual 0.0)
  Fock(0,1,0,1): Lz=-1.00 (residual 0.0), Az=+0.00 (residual 0.0)

n=3 shell (Na=Nb=2), same check, 9 states, all exact-zero residuals:
  Fock(2,0,2,0): Lz=+2.00, Az=+0.00   Fock(2,0,1,1): Lz=+1.00, Az=+1.00
  Fock(2,0,0,2): Lz=+0.00, Az=+2.00   Fock(1,1,2,0): Lz=+1.00, Az=-1.00
  Fock(1,1,1,1): Lz=+0.00, Az=+0.00   Fock(1,1,0,2): Lz=-1.00, Az=+1.00
  Fock(0,2,2,0): Lz=+0.00, Az=-2.00   Fock(0,2,1,1): Lz=-1.00, Az=-1.00
  Fock(0,2,0,2): Lz=-2.00, Az=+0.00
```

Every residual is exactly zero (not approximately zero) at both shells tested. This confirms the claim precisely: the raw occupation-number (Fock) basis states of the bicone are *already* simultaneous `(A_z,L_z)` eigenstates, with no diagonalization required at any `n`. This is actually close to immediate once Schwinger bosons are used at all — `J_z=(n₁−n₂)/2` is diagonal in the occupation basis by the very definition of the Schwinger construction — so it is correct and worth recording, but it is a near-direct consequence of the representation choice rather than a separately surprising additional theorem. Either way: **confirmed, and it does strengthen the "no differential equation for the states" framing in the precise, narrow sense v14.105 states it.**

## 2. v14.106 (α-independent determination via Compton wavelength): algebra confirmed, numerics consistent, one open metrological question

**Algebra, independently re-derived.** Starting only from the already-verified `α=9c²A/(4ω³a₀²Y_geom²)` and substituting `a₀=λ_c/α` (standard identity, `λ_c≡ℏ/(mₑc)`), I got, independently:
```
alpha = 9c²A*alpha² / (4*omega³*lambda_c²*Y_geom²)
=>  alpha = 4*omega³*lambda_c²*Y_geom² / (9*c²*A)
```
This matches v14.106's boxed formula exactly. Unlike the `a₀` case, this really is a genuine linear equation for `α` (not a tautology `e²=K·e⁴`) — **if** `λ_c` is itself free of prior `α` input.

**Numerics, independently checked.** Using the precise `ω₂₁=E/ℏ` (E=10.2 eV) rather than their rounded `1.55×10¹⁶`, and CODATA's `λ_c=3.8615926796×10⁻¹³ m`:
```
alpha computed = 0.00729205242520790758...
1/alpha = 137.1356021170525894...
known 1/alpha = 137.035999...
pct diff = 0.0727%
```
This is the same residual found throughout this entire audit thread (Rounds 180–184) — consistent, as it must be, since this is the same physical content algebraically rearranged, not new input.

**What remains open.** The claim rests on `λ_c=ℏ/(mₑc)` being obtainable without any prior knowledge of `α`. That is true of the *formula* (no `α` appears in it), but `mₑ`'s *numerical value* has (at least) two distinct metrological routes:

1. `mₑ=2hR∞/(cα²)` — via the Rydberg constant, explicitly `α`-dependent (quadratically).
2. Penning-trap cyclotron-frequency *ratio* `A_r(e)` (dimensionless, genuinely `α`-free) combined with an absolute mass scale from Kibble-balance or XRCD silicon-sphere metrology (also `α`-free, since SI 2019 fixes `h` and `e` exactly) — this route is genuinely independent of `α`.

Route 2 exists and is legitimate, so v14.106's claim is plausible and may well be correct. But CODATA's single published "recommended" `mₑ` is typically the output of a global least-squares adjustment across *all* input data simultaneously, including route-1-type constraints — so the publicly tabulated value is not automatically a clean, isolated route-2 number. Whether the specific `λ_c` figure used here traces cleanly to route 2, or implicitly carries some route-1 (`R∞`/`α`) influence through the combined adjustment, is a real question this thread cannot settle without checking which CODATA input (not output) values were used, or an independent route-2-only computation of `mₑ`.

**This is not a rejection of v14.106** — the algebra and numerics are both independently confirmed, and the route-2 pathway genuinely exists in principle. It is a flag that the strong claim "no α input, period" in the draft note (v14.107 §2) should be qualified until this is pinned down, the same way the `a₀` claim was qualified in Round 181 before Sandbox's own further work (v14.106) resolved it.

---

## 3. Verdict

```
v14.105: CONFIRMED EXACTLY (zero-residual eigenvalue check at n=2 and n=3).
   The parabolic basis is the bicone's native occupation-number basis -- true,
   and nearly immediate from the Schwinger-boson construction itself.
v14.106: algebra CONFIRMED (independently re-derived, matches exactly);
   numerics CONFIRMED (consistent 0.073% residual, same as every prior round);
   the "no alpha input" claim is PLAUSIBLE but not yet fully settled -- it
   depends on whether the specific lambda_c value used traces to a Penning-
   trap-ratio + Kibble/XRCD mass scale (alpha-free) rather than to the
   R_infinity/alpha route, and this thread cannot verify which without more
   detail on the input data actually used.
v14.107: staging record only (draft, not published); no independent claims
   of its own to verify.
```

No ledger content is altered by this entry.

---

HANDOFF-NOTE
target: sandbox
type: audit-finding
parent: v14.108
status: open
action: Before the arXiv draft (v14.107) states "no alpha input" unqualified, please confirm which specific numerical value/source was used for lambda_c (or m_e): if it was computed from A_r(e) [Penning-trap ratio] and the Kibble-balance/XRCD-derived molar mass constant directly (not from the CODATA table's combined-adjustment m_e, and not via m_e=2hR_infinity/(c*alpha^2)), the alpha-independence claim is solid and this thread will confirm it fully. If it came from a general CODATA lookup, the claim needs the same "closes to 0.07%" framing v14.103 used for a0, since the global CODATA fit mixes both routes.
constraints: v14.105 needs no further action -- it is fully confirmed. This does not dispute v14.106's algebra or numerics, only the specific metrological provenance claim.
