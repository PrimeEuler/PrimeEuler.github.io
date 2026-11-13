# Cone Derivation Ledger v15.860 — Sandbox addendum: the metres-per-second tag on the accel/decel parabolas

**Deposit type:** Sandbox exploration, independently checkable. Short
addendum to v15.859, on Jeremy's remark and direction (2026-11-13):
the accel/decel parabolas have a metres-per-second tag. Producer
re-executed at staging, exit 0, all forms symbolic and exact.

Each parabola belongs to one null ray and carries its ray's velocity
as a tag (+c the accel parabola's, −c the decel parabola's). In SI the
arms are u = E + pc = γmc(c + v) and v = E − pc = γmc(c − v) — the
state's energy-momentum read along each ray — so the v15.859 leverage
is e^{2ψ} = (c + v)/(c − v), the state's velocity measured against
each parabola's own m/s tag, with action shares (c+v)/2c and (c−v)/2c
(du/dt = F(v+c), dv/dt = F(v−c)). The 1 MeV electron rechecks exactly
(13.2421 : 1; shares 0.9298 / 0.0702). Null limit: v → c sends the
decel share to 0 and the accel share to 1 — the lever's extreme is
the null channel of v15.858, where the velocity stops being the
state's data and becomes the ray's tag itself.

**Payload:** `payloads/ms_tag_addendum_v15_860/` — Ms_Tag_Addendum.md `32df4cd6e0b1031bf5d431bd4b8d287f74b7a83fcc520bd66b6c932ec0801453`, ms_tag.py `785060fb9f922449473b43f5d6404b7f5f987914662116519927d93973e17a15`.
