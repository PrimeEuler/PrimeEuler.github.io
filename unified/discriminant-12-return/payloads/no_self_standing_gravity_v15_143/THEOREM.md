# Theorem — No Self-Standing Gravity (table form)

Sandbox, 2026-10-29. Formalisation of Jeremy's statement: "gravity is
unbounded; it has nothing to form a standing wave with, other than
echoes from other mass." Producers: `rep_boundary_test.py` (v15.140
payload) and `standing_wave_test.py` (this addendum; run log
`standing_wave_output.txt`, clean exit, exact rationals throughout).
NOT ledgered.

## Definitions
Refined table as in v15.135 §4 / v15.140. A **shell** T ∈ (1/4)ℤ_{>0} has
states at offsets X ∈ {−T + i/2 : i = 0 … 4T} on its Casimir circle
(radius √(T(T+1)); ladder radius R = T + 1/2). J± transitions step X by
±1 with squared amplitudes (T∓X)(T±X+1); a **chain** is a maximal
X mod 1 class within a shell. A chain is a **standing wave** if it is a
finite unitary SU(2) multiplet: every squared amplitude ≥ 0, vanishing
exactly at the chain's two ends. An end failing this is **open**; the
nonzero squared amplitude from its last state, the **escape weight**,
points at the **missing state** X* one J-step beyond the end,
|X*| = T + 1/2 = R.

## Theorem [D]
(i) **Standing ⟺ closed ⟺ even.** A shell has a standing wave iff
T ∈ (1/2)ℤ, and then exactly one: the integer-table chain (class
X ≡ T mod 1). Every other chain in every shell is open.
(ii) **Odd chains are one-ended.** For T an odd quarter, both chains
hold exactly one endpoint each (mirror conjugates) and are open at the
other; for T ∈ (1/2)ℤ the non-table chain is open at both ends. Every
open end has escape weight exactly **T + 1/4**.
(iii) **Closure cannot be supplied from inside.** Adjoining the missing
state X* to its chain gives X* the outward squared amplitude
**−(T + 3/4) < 0** under the shell's own Casimir — a ghost: no unitary
chain with Casimir T(T+1) contains X*. Truncating the chain instead
leaves the commutator defect diag([J+, J−] − 2Jz) = ±(T + 1/4) at the
boundary state (v15.140). Both fiat closures fail, by universal amounts.
(iv) **Closure is another shell's data.** The missing state X* is a
genuine endpoint — outward amplitude exactly 0 — of exactly one other
shell, T′ = T + 1/2, under that shell's own Casimir. A one-ended chain
can therefore be terminated only by data belonging to a different
shell: external to the system that carries the chain.
(v) **Unboundedness.** Iterating the escape (follow X* to its own
shell, take that shell's same-class chain, repeat) remains in odd
shells forever (T = 1/4, 3/4, 5/4, …; verified 10 steps, weights
T + 1/4 strictly increasing, no step closed). The cone's shell ladder
is unbounded above, and at no stage does a gravitational chain stand.

## Proof
All steps are closed-form in the squared amplitudes; the producers
audit them exhaustively over T = 1/4 … 5/2 (parts i–iii) and 10 escape
iterations (part v), 0 violations.
(i) A chain contains +T iff its class ≡ T (mod 1) and −T iff its class
≡ −T (mod 1); both in one chain iff 2T ∈ ℤ. The class X ≡ T chain at
T ∈ (1/2)ℤ is the integer table's Schwinger chain.
(ii) An open end sits at m = ±(T − 1/2); its escape weight is
(1/2)(2T + 1/2) = T + 1/4.
(iii) At X* = ±(T + 1/2), the outward factor under Casimir T is
(−1/2)(2T + 3/2) = −(T + 3/4) < 0 for all T > 0.
(iv) Under Casimir T′ = |X*| the same factor is (T′ − |X*|)(…) = 0.
(v) |X*| = T + 1/2 maps odd quarters to odd quarters; by (ii) the
receiving chain is again one-ended with larger escape weight. ∎

## Reading [I]
In the pair language of the record, the supplying shell is the *other
member of the pair*: a gravitational chain terminates only against a
second system carrying its own Casimir — another mass. Physical
instances of external closure already on the record: the neutron
bouncer's standing waves close against a material mirror (gravity
supplies the slope, matter the wall, v14.592); the Misner fiber's ε
quantisation holds because a global identification closes the fiber —
a boundary condition imposed on the geometry, not produced by it
(v14.731); the open squeeze carrier, closed by nothing, has purely
continuous spectrum (v14.950). The theorem is a statement about the
refined table's transition algebra; the identification of "different
shell" with "other mass" is the interpretation, stated as such.
