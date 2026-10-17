# Cone Derivation Ledger v14.550 — Sandbox deposit: the diameter–secant machine and the gravity road (synthesis note + interactive page)

**Timestamp:** 2026-10-17 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.366/v14.367 (unit-circle encoding note + pair form, ledgered), v14.414 (parabolic-dictionary literature scan: assembly not found), v14.441 (Cayley addendum), v14.549 (live HEAD at deposit; collision-checked immediately before allocation — next-free was v14.550).
**Status:** exploratory synthesis deposit under Jeremy's explicit 2026-10-17 authorization ("put it in the repo and mention it in the ledger"). This entry answers **no Lane A HANDOFF** and changes no paper, no staged draft, and no prior claim. It records a research note and its companion interactive page, both written 2026-10-17 from that day's conversation. The note's §1 identities are [D] (exact, numerically verified at deposit); §§2–3 are [I]/[O] as tagged in the note itself. **No derivation of $G$ is claimed** — the note's §3 is a status assessment whose two open items (hierarchy generator; factorised gravitational observable) are recorded as open.

## What was deposited

Research-notes, two files, commits `ce01f476b9e9b990eac3c0d91892e981d44b3f68` (note) and `64bb3cda7bdccc0ffc2864a298e6f6a0969ae842` (page):

- `Diameter_Secant_Machine_and_the_Gravity_Road.md` — SHA-256 `1c06226b5848e628de9a023f45dac898f52a3b2f32b912f852c374dfde179cd1`
- `Diameter_Secant_Machine.html` — SHA-256 `35e08c7849f4627dbd5947c92cff1e2cd2025a406dfe9c76d469aaaa85616b36`

Workspace originals remain in `d12/explorations/unit-circle-secant/` (`Diameter_Secant_Machine_and_the_Gravity_Road.md`, `secant_machine.html`).

## Content summary (as tagged in the note)

- **§1 The machine [D].** Jeremy's diameter/secant reading of the pair form: on the circle of diameter $n+k$, the secant splits the diameter $n\,|\,k$, sits at offset $(n-k)/2$, and has half-chord $\sqrt{nk}$ (altitude theorem); $(n+k)/(n-k)$ is sum-over-difference of the split $= \sec\varphi_{n,k} = \coth\psi_{n,k}$; $\mathrm{AM}^2 = \mathrm{offset}^2 + \mathrm{GM}^2$ (AM–GM as half-chord $\le$ radius); feet lie on $u^2 - v^2 = nk$ with light-cone coordinates $u \pm v = n, k$; fixed-$k$ endpoint locus is the parabola $h^2 = 2k(d + k/2)$, vertex $-k/2$ ($k=1$: vertex $-1/2$, $f=1/2$). Jeremy's compression recorded verbatim: "GM factor hyperbolas define the cone, their shadow is a chord on the circle, and the half chord centers the AM."
- **§2 The same cast in the laboratory [D/I].** Double-paraboloid meridian = dumbbell silhouette, torsion fibre = its axis [I, Jeremy]; symmetric-top/Wigner reading of the spun balance [I]; sourced facts [D]: Gundlach–Merkowitz rotating-turntable $G$ (14 ppm, fibre untwisted); the Vienna/TU Wien/Ulm levitated dumbbell nanorotor (two 150 nm silica spheres) cooled to its librational ground state in two axes (*Nature Physics*), ETH Zürich single-axis/three-mode results; Gravity Probe B. Design consequence [D mechanics]: gravity torques orientation only via a centre-of-mass offset — an asymmetric dumbbell is a quantum pendulum ($\sqrt{Mgl/I}$), the angular sibling of qBounce; the mass/frequency commensurability form of "precession over the nodes and antinodes" [I].
- **§3 The $G$ assessment.** $\alpha$ precedent (bicone elimination, $1/\alpha = 137.4 \pm 2.2$ from the H($2p$) lifetime; §3 KS-bridge repair remains a separate staged item); the dimensional wall for $G$ [D]; dimensionless targets $\alpha_G$ and Dirac's ratio $\approx 2.3\times10^{39}$; mass already housed in the machinery ($\log(m/4) = 2\psi_{m,4}$, hyperbola vertex); data map (Rosi atom-interferometric $G$, classical factor; qBounce Airy spectroscopy measures $g$, not $G$; torsion corpus discordant); the two missing pieces [O] — (i) hierarchy generator to $\psi \approx 45$, (ii) a factorised (cone/Wigner factor) × (gravitational coupling) observable, whose institutional search is QGEM/BMV. Verdict: unification of form mapped; unification of law open at exactly those two points.

## Verification

- §1 identities re-verified numerically at deposit over several $(n,k)$ (including $(3,1), (12,3), (1,1), (7,2.5), (11,1.25)$): $(n+k)/(n-k) = \sec\varphi = \coth\psi$ and $\mathrm{AM}^2 - \mathrm{offset}^2 = nk$ exact to machine precision in every case.
- The interactive page (dependency-free single file; $n$/$k$ sliders; circle/secant, hyperbola, and 3D-cone panels) was executed headlessly across the slider range with no errors, and all three panels were rendered locally and inspected before deposit (label collisions and a hyperbola frame clip found and fixed during that pass).
- Both deposited files were re-read from the repository after commit and byte-compared against the workspace originals (SHA-256 above).

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `new_physics_claim = false`; `G_derived = false`; `hierarchy_generator_found = false`; `factorised_G_observable_exists = false`. The note is a synthesis and status map of sandbox exploration plus sourced experimental facts, with Jeremy's formulations attributed and dated in its header.

## Disposition

Deposit complete. Ball remains where the note leaves it: the two open items of §3. Any future edit of the note (e.g., the gyroscope-in-coils forcing representation raised by Jeremy in the same conversation, after the note was frozen) is a new versioned deposit on his line, not a silent amendment.
