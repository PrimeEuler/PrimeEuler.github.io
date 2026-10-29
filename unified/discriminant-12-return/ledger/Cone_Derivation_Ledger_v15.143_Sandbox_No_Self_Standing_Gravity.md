# Ledger v15.143 — Sandbox return: No-Self-Standing-Gravity theorem (table form)

**Kind:** Sandbox return; addendum to v15.135 / v15.140.
**Origin:** Jeremy's statement (2026-10-29): "because gravity is
unbounded, it has nothing to form a standing wave with other than
echoes from other mass" — formalised in the refined table's transition
algebra and proved.
**Producers:** `standing_wave_test.py` (new this entry; exact rationals,
clean exit), building on the chain audit of `rep_boundary_test.py`
(v15.140 payload, rechecked, unchanged).
**Payload:** `payloads/no_self_standing_gravity_v15_143/` —
THEOREM.md, standing_wave_test.py, standing_wave_output.txt.
**Verification:** all identities closed-form; producers audit every
shell T = 1/4 … 5/2 and 10 escape iterations, 0 violations.

## 1. Definitions
Refined table as in v15.135 §4 / v15.140: shell T ∈ (1/4)ℤ_{>0}, states
at offsets X ∈ {−T + i/2} on the Casimir circle (radius √(T(T+1)),
ladder radius R = T + 1/2), J± stepping X by ±1 with squared amplitudes
(T∓X)(T±X+1); chains are X mod 1 classes. A chain is a **standing wave**
if it is a finite unitary SU(2) multiplet: all squared amplitudes ≥ 0,
vanishing exactly at its two ends. An end failing this is **open**, its
last state's nonzero squared amplitude is the **escape weight**, and
the **missing state** X* sits one J-step beyond, |X*| = R.

## 2. Theorem [D]
(i) **Standing ⟺ closed ⟺ even.** A shell has a standing wave iff
T ∈ (1/2)ℤ, and then exactly one: the integer-table (Schwinger) chain.
(ii) **Odd chains are one-ended.** At odd-quarter T both chains hold
one endpoint and are open at the other (mirror conjugates); at
T ∈ (1/2)ℤ the non-table chain is open at both ends. Every open end
has escape weight exactly **T + 1/4**.
(iii) **No internal closure.** Adjoining X* gives it outward squared
amplitude **−(T + 3/4) < 0** under the home Casimir (a ghost: no
unitary chain with Casimir T(T+1) contains X*); truncating instead
leaves the commutator defect ±(T + 1/4) at the boundary state
(v15.140). Both fiat closures fail by universal amounts.
(iv) **Closure is another shell's data.** X* is a genuine endpoint
(outward amplitude exactly 0) of exactly one other shell, T′ = T + 1/2,
under that shell's own Casimir.
(v) **Unboundedness.** Iterating the escape stays in odd shells
forever (1/4, 3/4, 5/4, …; escape weights strictly increasing); at no
stage does a gravitational chain stand.

## 3. Proof
Closed forms, audited exhaustively by the producer. (i) A chain
contains +T iff its class ≡ T (mod 1) and −T iff ≡ −T; both iff
2T ∈ ℤ. (ii) An open end sits at m = ±(T − 1/2); escape weight
= (1/2)(2T + 1/2) = T + 1/4. (iii) At X* = ±(T + 1/2) the outward
factor under Casimir T is (−1/2)(2T + 3/2) = −(T + 3/4). (iv) Under
Casimir T′ = |X*| the same factor is (T′ − |X*|)(…) = 0. (v) |X*| =
T + 1/2 preserves odd quarters; apply (ii) at each stage. ∎

## 4. Reading [I]
In the record's pair language, the supplying shell is the other member
of the pair — another mass: a gravitational chain terminates only
against a second system carrying its own Casimir. Physical instances
of external closure already on the record: the neutron bouncer's
standing waves close against a material mirror (gravity supplies the
slope, matter the wall, v14.592); the Misner ε quantisation holds
because a global identification closes the fiber — a boundary
condition imposed on the geometry, not produced by it (v14.731); the
unclosed squeeze carrier has purely continuous spectrum (v14.950).
The identification of "different shell" with "other mass" is the
interpretation, recorded as such; the theorem itself is about the
transition algebra.

## 5. Scope
Classification unchanged (v15.069 taxonomy; G_derived = false).
Gravity's particle content is untouched: the graviton remains an
even-sector j = 2 chain state (v15.140 §3). Production files untouched.
Companion sandbox item (the phase-relation check, PHASE.md /
phase_relation_test.py: U-eigenstates as inter-sector phase relations)
remains unledgered pending Jeremy's word.
