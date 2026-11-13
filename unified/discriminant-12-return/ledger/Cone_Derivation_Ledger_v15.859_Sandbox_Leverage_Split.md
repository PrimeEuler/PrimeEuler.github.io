# Cone Derivation Ledger v15.859 — Sandbox: the leverage split (the accel/decel parabolas as lever arms; response shares e^{2ψ})

**Deposit type:** Sandbox exploration, independently checkable. Jeremy's
proposal and filing direction 2026-11-13: look at the acceleration /
deceleration parabolas as different leverage for the force. Producer
re-executed at staging, exit 0, all symbolic checks exact.

## (a) The split

For a state (u, v) = (E+p, E−p) on the shell uv = m² (u = m e^{ψ},
v = m e^{−ψ}), a longitudinal force (dp/dt = F, dE/dt = Fβ) acts as
du = F(1+β) dt, dv = −F(1−β) dt: the accel parabola grows at the
(1+β) rate, the decel parabola shrinks at the (1−β) rate, magnitudes in
the ratio (1+β)/(1−β) = **e^{2ψ} = u/v** — on the integer mesh the pair
ratio n/k itself. Response shares are the arms over their sum:
u/(u+v) = (1+β)/2 and v/(u+v) = (1−β)/2 (arm over twice the AM).
Slide form: dψ = F dt/E, du = u dψ, dv = −v dψ. A transverse force has
no first-order action on (u, v): the lever is purely longitudinal.
All identities verified symbolically; spot checks at ψ = 0 … 3 agree
to all printed digits (the record's 1 MeV electron, ψ = 1.2917: split
13.24 : 1).

## (b) Reading and scope

The seat is leverage 1 (even reciprocal split); off-seat the leverage
steepens without bound. The fulcrum is the invariant product — the
lever redistributes a force's action at fixed uv = m² and amplifies
nothing. The same e^{2ψ} is the head-on/tail-on Doppler ratio. Filed
use: the response coefficient supplying the drive×reaction split
(v15.275) with its ψ-dependent channel weights. Transport species per
the v15.858 map — it says how a given force lands on a state and
selects no force. (Disclosure: the pre-build chat sketch carried a
sign error on dv; the build's ψ-slide cross-check caught it, and the
entry files the corrected form, as detailed in the payload note.)

**Payload:** `payloads/leverage_split_v15_859/` — Leverage_Split.md `2392f782222b9455e923d7b02d0861dcb6589d94a2707c70fb09fd92c6bfa583`, leverage_split.py `ceab5a73b9546b5bf70025180c657aa7152e3bbd377686d20f87e0365e83de71`.
