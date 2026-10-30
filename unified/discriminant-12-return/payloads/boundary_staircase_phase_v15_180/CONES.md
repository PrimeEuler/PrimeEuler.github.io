# Cone within a cone: the null boundary as the measure

Sandbox exploration, 2026-10-30. Jeremy's prompt: the cone within a
cone (Casimir cone inside the ladder cone), with gravity; the null
light cone as a boundary to measure against. Producer `cones_test.py`
(exact rationals, clean run; shells audited to T = 5). NOT ledgered.

## The algebra already measures against the boundary [D]
Per shell T, three squared radii: floor AM² = T², states C² = T(T+1),
boundary (ladder) R² = (T + 1/2)². Every natural quantity of the
machinery is a difference against the boundary R²:
- transition amplitudes are boundary chords: amp² = R² − X′²
  (X′ the midpoint offset);
- **state depth is constant**: R² − C² = 1/4 at every shell — every
  state of every shell sits exactly a quarter (squared radius) inside
  the null boundary;
- **escape weight is the boundary-to-floor gap**: R² − AM² = T + 1/4.

## Boundary flux per shell [D]
Every shell T ≥ 1/4 has **exactly two open ends** (even shells: the
Casimir fragment's two; odd shells: one per fragment), each leaking
T + 1/4, so the **total escape per shell is 2T + 1/2**, carried
entirely by the non-table chains. The closed (particle) chain leaks
nothing. Verified T = 1/4 … 5, no exceptions.

## The boundary is a staircase, not a wall [D]
Shell T's boundary is shell T + 1/2's floor: R(T) = (T + 1/2) = AM
radius of the next shell. The next shell's state cone protrudes past
this shell's boundary by C(T + 1/2)² − R(T)² = T + 1/2 = R(T)
(squared radius). "Inside the light cone" is therefore shell-relative:
the only exact containment is within a shell (states 1/4 inside their
own boundary); across shells the cones poke out of each other in a
regular staircase, and the escape iteration of v15.143(v) is a climb
up that staircase that never tops out.

## Gravity walks the boundary [D steps / I reading]
Step intervals in the (X, T) plane (interval = ΔT² − ΔX², refined
steps (Δp, Δq), ΔX = (Δp − Δq)/4, ΔT = (Δp + Δq)/4):
- gravity's quarter steps, the single row step (1, 0) and column step
  (0, 1): Δ = (±1/4, 1/4), interval **0 — exactly null**, both null
  directions;
- EM shell ladder (2, 2): interval +1 (timelike); halfway step (1, 1):
  +1/4 (timelike); EM in-shell steps (2, −2) and (1, −1): −1, −1/4
  (spacelike).
Null ⟺ odd change in diagonal index ⟺ sector change. So in the
(X, T) plane, changing sector *is* moving on the light cone: matter
moves timelike (between shells) or spacelike (within a shell), and
only gravity's steps run along the null generators — the boundary
between the staircase levels. Combined with v15.143 (gravity's chain
ends are the next level's rim states) and v15.140 (its Casimir classes
are the ones the interior never takes): everything about the odd
sector is boundary data — its ends, its flux, its motion. [I] The
odd sector is not a region inside the cone; it is the cone's edge,
organised.
