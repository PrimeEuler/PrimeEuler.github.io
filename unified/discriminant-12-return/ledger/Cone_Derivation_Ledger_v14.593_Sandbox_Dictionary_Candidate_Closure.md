# Cone Derivation Ledger v14.593 — Sandbox closure: the v14.592 dictionary candidate dissolved; J₁ signature ⟺ D_exp

**Timestamp:** 2026-10-18 (EDT, evening)
**Lane:** Sandbox (little Euler)
**Parents:** v14.592 (sandbox addendum deposit; its §3 recorded the dictionary candidate [O] this entry closes), v14.550 (gravity-road note), the sandbox standing-wave/archimedean reports of 2026-09-28 (`lane_b/sandbox/runs/20260927-175943-standing-wave-embedding/embedding.md` §18 and `20260928-010240-spherical-archimedean-2/archimedean_report_2.md` §2), v14.592 also being live HEAD at allocation (collision-checked immediately before — next-free was v14.593).
**Status:** closure entry under Jeremy's explicit 2026-10-18 authorization ("Ledger the closure"). Answers **no Lane A HANDOFF**; changes no paper, no staged draft, and no certified object (the ledger's analytic screw v13.258 is untouched, as in the parent reports). The candidate opened in v14.592 is **closed by dissolution** (computed negative), and the staged 2026-09-28 dictionary item is **closed by an exact equivalence**. One neighbouring item is explicitly **not** closed (§3 below).

## The obligation as staged (2026-09-28)

The archimedean channel's envelope is $\tilde A(t) = 6\sqrt{1-e^{-2t}}$ in Suzuki's variable $t$. A dictionary is a monotone $x(t):[0,\infty)\to[0,L]$, $L = 12/11$, with forced ends $x(0)=L$ (the channel's zero meets the envelope's only zero, at the edge) and $x(\infty)=0$ (centre concentration). D_exp, $x = Le^{-t}$, was found canonical *relative to the Lerch variable* $z=e^{-2t}$; the dictionary "as such" was left a choice, and the dual signature $(6\pi/\omega)J_1(12\omega/11)$ was staged as a prediction *pending the dictionary*. v14.592's candidate proposed closing the choice by an action/segment-area principle imported from the neutron bouncer (cone coordinate as action, warp $E\propto J^{2/3}$).

## Closure, part 1 — the candidate dissolves [D, computed]

Producer: `dictionary_closure_probe.py`, deposited in research-notes (commit `1734aff8a9648047de742c6618cc0d4eeb30203c`), SHA-256 `05de2225518bebbe82018615a4d4d8efa98a1edae51b257f743f59abc32aa1e2`. Workspace original in `d12/explorations/unit-circle-secant/`.

- The candidate built concretely — the deficit-area dictionary $x_S(t) = L\bigl(1 - S(t)/S(\infty)\bigr)$, $S(t)=\int_0^t \bigl(6-\tilde A(s)\bigr)\,ds$, $S(\infty) = 1.84111691664$ — is a legitimate dictionary (forced ends, monotone) but is **not** D_exp: $x_S/x_{D\_exp}$ runs $0.697 \to 0.00549$ over $t \in [0.25, 5]$, and $\log(L/x_S)/t \to 2$ (centre approached at the $e^{-2t}$ rate, not $e^{-t}$).
- Under $x_S$ the envelope is not the semicircle, so the dual signature is not $J_1$ and the Lerch affinity in the geometric coordinate is lost: the area principle competes with the canonical choice rather than selecting it.
- The candidate's motivating warp has **no foothold in this channel**: the verified channel asymptotics (archimedean_report_2, 30-digit) are $A_{12} \sim (t/2)[\log(1/(2t)) + K_0]$ at small $t$, $\tilde A \sim 6\sqrt{2t}$, and linear growth at large $t$; the signature zeros are arithmetic, $\pi(s+\tfrac14)$ (v14.592 §1). No $2/3$ power occurs. The action/segment-area principle requires a phase space (the bouncer's $(z,p)$); the archimedean channel has none. Its home remains the bouncer/rotor side, where it already closed in v14.592 §3.

## Closure, part 2 — signature ⟺ dictionary [D, exact + verified]

- The staged signature is exactly the Fourier transform of the semicircle envelope: $\int_{-L}^{L} 6\sqrt{1-(x/L)^2}\, e^{i\omega x} dx = (6\pi/\omega)\, J_1(L\omega)$, $L = 12/11$ — verified at dps 30, relative difference $0$ (≤ $9.3\times10^{-30}$) at $\omega \in \{0.7, 2.3, 5.0, 9.4\}$.
- The envelope is a semicircle in $x$ **iff** the dictionary is D_exp: $\tilde A(t) = 6\sqrt{1-e^{-2t}}$ equals $6\sqrt{1-(x/L)^2}$ iff $e^{-2t} = (x/L)^2$ iff $x = Le^{-t}$ (positive branch). Discriminating check: under D_tanh the transform misses the $J_1$ form by 14.4% ($\omega=2.3$) and 26.0% ($\omega=5.0$).
- Hence the J₁ signature and the D_exp dictionary are **one claim, not two**: retaining the overlay's predicted signature fixes the dictionary uniquely; the interior interpolation was never free once the signature is kept. The 2026-09-28 staging is discharged.

## Explicitly not closed

The helix-representation obstruction of archimedean_report_2 §3 — $\tilde T(x) = T(t(x)) \to -\infty$ like $-s\log(L/x)$ at the centre, $s = 0.24060639745313878\ldots$ — is a representation question, not a dictionary question, and it is dictionary-robust (under $x_S$ the log-rate doubles; under D_exp it is 1; the divergence persists). It remains open exactly as recorded there. Nothing in this entry touches it.

## Verification

Producer executed clean at deposit; all cited numbers are its output (Test 3 inputs are the cited 2026-09-28 verified asymptotics, not recomputed). Both deposited files (producer, this entry) re-read from the repository after commit and byte-compared against the originals.

## Scope flags (honest)

`answers_lane_a_handoff = false`; `papers_modified = false`; `certified_objects_modified = false`; `dictionary_candidate_status = CLOSED_DISSOLVED`; `staged_J1_dictionary_item = CLOSED_EQUIVALENT_TO_D_EXP`; `helix_representation_obstruction = STILL_OPEN`; `G_derived = false`.

## Disposition

The dictionary-candidate thread opened at v14.592 is closed. Live threads remaining from this arc: the §3 helix-representation obstruction (2026-09-28, restated above) and v14.550's two $G$ items. Further sandbox work on either is on Jeremy's line.
