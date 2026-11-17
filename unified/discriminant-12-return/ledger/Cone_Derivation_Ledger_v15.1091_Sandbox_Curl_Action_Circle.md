# Cone Derivation Ledger v15.1091 — Sandbox: the curl and the action circle (B is purely azimuthal; the charge on the seat's circle is the Zitterbewegung loop)

**Deposit type:** Sandbox exploration, independently checkable; fourth
in the charge-at-the-seat run (v15.1082, v15.1084, v15.1086,
cross-reference v15.1088). Jeremy 2026-11-17: "an accelerating charge
creates curl which seems like the action circle." Producer
re-executed at staging, exit 0 (8 checks, all PASS).

(1) The curl is literal: the slid seat's magnetic field (v15.1084)
is purely azimuthal around the motion axis — no radial component
(B.rho = 0), no axial component (B_x = 0), (B.phi)^2 = |B|^2 rho^2 —
so its field lines are circles about the trajectory and
oint B.dl = 2 pi rho B_phi != 0 around the axis. The boost's shadow
of E is a circulation. (2) The charge on the seat's own circle: the
seat's action data (v15.864) define one distinguished circulation,
the Dirac Zitterbewegung circle r = hbar/(2mc),
omega = 2mc^2/hbar, v = omega r = c (verified), whose invariants
land on the filed seat numbers exactly: circuit action
oint p dx = (mc)(2 pi r) = pi hbar — the v15.864 Compton-ellipse
action; period tau_ZB = pi tau_C, i.e. the ZB circuit is the pi hbar
object, NOT the hbar seat cycle (E_rest tau_C = hbar, a separate
smaller datum); circulation angular momentum L = mvr = hbar/2.
(3) The loop's moment: the circulating charge is a current loop
I = q omega/(2 pi) with mu = I pi r^2 = q hbar/(4m) = mu_B/2 — the
loop gives g = 1 against Dirac's g = 2. The missing half is
imported Dirac structure (Gordon decomposition): the Dirac current
splits into a convection part (this loop) and a polarization part
proportional to the curl of the spin density. "The charge creates
curl" has two floors, each worth g = 1: the circulation of the
charge, and the curl of its spin density; this entry gates the
first and imports the second.

Scope: dictionary level. Zitterbewegung is a mathematical feature
of the Dirac equation — interference between the +E and -E sectors
(the seat and its crossed partner; a pure one-sector state does not
circulate) — not a literal classical orbit. The gated content is
the azimuthal purity of B and the scale coincidences (pi hbar,
hbar/2, pi tau_C) with the seat's action data. No coupling
selected; Doors I-III untouched.

**Payload:** `payloads/curl_action_circle_v15_1091/` — Curl_Action_Circle.md `441e9c530e462de8383e5db753f8fe33ce4fde5f14a2491c0cba8c55f54af40e`, zb_circle.py `07cbca212fbad93509aaa2d989b9ef3daede27357a1bd352a003fdd8a97a3112`.
