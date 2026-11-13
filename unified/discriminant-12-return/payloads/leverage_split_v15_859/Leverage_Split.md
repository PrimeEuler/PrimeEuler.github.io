# The leverage split: the accel/decel parabolas as lever arms

*Sandbox note (little Euler), 2026-11-13. Jeremy: "look
at the accel/decel parabolas as different leverage for
our force" — verified and filed at his direction.
Producer: `leverage_split.py` (symbolic checks all
exact; one sign correction caught by the build's own
cross-check, disclosed in §1).*

## The split [D]

A state is the crossing of two opposite-sign parabolas,
the pair (u, v) = (E+p, E−p) on the shell uv = m², with
u = m e^{ψ}, v = m e^{−ψ}. A longitudinal force
(dp/dt = F, dE/dt = Fβ) slides the state along its shell
(v15.270). Its action divides between the parabolas as

du = F(1+β) dt,   dv = −F(1−β) dt:

the accel parabola grows at the (1+β) rate while the
decel parabola shrinks at the (1−β) rate — magnitudes in
the ratio **(1+β)/(1−β) = e^{2ψ} = u/v**, on the integer
mesh the pair ratio n/k itself. The response shares are
the arms normalized by their sum: |du| share =
u/(u+v) = (1+β)/2, |dv| share = v/(u+v), arm over twice
the AM. Equivalent slide form: dψ = F dt/E (the shell's
energy is the inertia per unit rapidity), du = u dψ,
dv = −v dψ — the boost's reciprocal action read
channel-wise. A transverse force has **no** first-order
action on (u, v) at all (rotation of p at fixed E leaves
both unchanged to first order): the lever is purely
longitudinal.

*Sign correction, disclosed:* the chat sketch preceding
this build wrote dv = +F(1−β) dt. The build's ψ-slide
cross-check (dv must equal −v dψ, since v = m e^{−ψ}
falls as ψ rises) returned False against that form and
True against the corrected one; the filed form above is
the corrected one. The leverage ratio and the seat
statement were unaffected; deceleration (F < 0) flips
both signs — u collapses at (1+β), v climbs at (1−β).

## Reading [D]

- **The seat is leverage 1.** At ψ = 0 the force's
  action is an even reciprocal split (du = F dt,
  dv = −F dt). Off the seat the leverage steepens
  without bound: at the record's 1 MeV electron
  (ψ = 1.2917) the split is **13.24 : 1**; at ψ = 3 it
  is 403 : 1. Accelerating a fast state, the decel
  parabola nearly freezes; decelerating it, most of
  the impulse goes into collapsing u while v climbs
  only at the (1−β) rate.
- **The lever creates nothing.** The fulcrum is the
  invariant uv = m²; the split redistributes the
  response at fixed product — work conserved, no
  amplification, exactly a lever's terms.
- **Kinship:** e^{2ψ} is also the head-on vs tail-on
  longitudinal Doppler ratio — the same lever read by
  light.
- **Use and scope:** this is the response coefficient
  the dynamics record was missing — it supplies the
  drive×reaction split (v15.275) with its ψ-dependent
  channel weights ((1+β)/2 drive-side share, (1−β)/2
  reaction-side share of any longitudinal impulse's
  action). It is the corridor's transport species: it
  says how a *given* force lands on a state, in exact
  terms, and selects no force — consistent with the
  map filed at v15.858.
