# Duck test: the device↔model rhyme, tested in the rotor sector

*Sandbox note (little Euler), 2026-10-19. Jeremy's bet (same
day): the correspondence — one axis, one field that shapes,
drives, and reads the paraboloids ↔ envelope (shapes), overlay
(drives phase), spectrum (reads out) — is "a very deep rhyme."
Test criterion, stated in advance: the rhyme is identity iff
the correspondence is forced — the same equations on both
sides with no free parameter in the map. Tested in the rotor
sector, the one place both sides are the same kind of object:
a rotor on one axis in rank-1 fields (the model's ladder
coupling, v14.626; the device's dumbbell/gyro in the coil
field). Producer: `duck_test.py`.*

## The three channels are one skeleton [D]

- **Shape/read (axial):** cos θ coupling, Δj = ±1, Δm = 0,
  weights w_j = (j+1)/√((2j+1)(2j+3)) (v14.626).
- **Drive (transverse):** the tipping field of the gyro build —
  sin θ e^{±iφ}, Δj = ±1, Δm = ±1 (the NMR/Rabi channel),
  weights u_j = √((j+1)(j+2)/((2j+1)(2j+3))) at m = 0.
- **Read:** by reciprocity the ring pickup sees the precessing
  transverse moment — the same Δm = ±1 channel as the drive.

The two weight systems are not merely alike. They obey, at
every rung,

**u_j = w_j · √((j+2)/(j+1))** (exact algebra; verified to
machine precision, ratio 1.000000000000000),

and the climb products obey **Πu = Πw · √(J+1)** exactly at
every J tested (1…100) — hence the drive climb is
√(π/2)·√(J+1)·2^{−J}, the axial climb's Wallis skeleton with
one exact factor. There is no adjustable parameter anywhere in
the map, because there is only one rank-1 coupling theory for
a rotor (Wigner–Eckart), and both sides are instances of it.

## Verdict

In the rotor sector, the rhyme is **identity of governing
structure**, not analogy: the model's ladder coupling and the
device field's coupling are the same object, provably, with
the shape/drive/read triple realised as the axial channel,
the transverse channel, and its reciprocal readout on one
ladder. Jeremy's duck passes its first DNA test.

## Boundaries (what the test does not cover)

- **Scope:** the rotor sector only. The fluid shaping profile,
  the acoustics, and the Suzuki/channel side of the model are
  untouched by this test.
- **Designed-in correspondences are excluded as evidence:** the
  coil turns were wound to the model's amplitudes by us, so
  their agreement is construction, not discovery. The weight
  identities above testify precisely because they were *not*
  chosen — SO(3) leaves no choice in them.
- Identity of coupling anatomy ≠ the cone model being the
  device's whole physics. It means: wherever the device is a
  rotor on the axis in a rank-1 field, its coupling anatomy is
  the ladder's anatomy — a theorem, not a resemblance.
