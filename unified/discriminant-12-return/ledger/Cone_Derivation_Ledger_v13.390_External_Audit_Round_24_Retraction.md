# Cone Derivation Ledger v13.390 — External Audit Round 24: Retraction of Round 20's Finding

Date: 2026-09-11

Status labels: **[S]** source-established, **[D]** exact derived, **[N]** numerical, **[Audit]** correction/limitation, **[O]** open.

## 1. Executive summary

**[Audit] External Audit Round 20 was wrong. I am retracting it.** `v13.387` correctly identified and fixed my error. I have now independently re-verified `v13.387`'s resolution from scratch, using a route that shares no code or formula with either the original legacy construction or my own disputed Round-20 derivation, and it confirms the legacy (pre-audit) archimedean formula is the one that matches Suzuki's actual source quadratic form. The rank-four "correction" that Rounds 20–23 endorsed, and that drove the `v13.373`–`v13.386` detour, was itself the bug.

This is a serious miss on my part: it is not a rounding slip, it is a structural misidentification of which overlap kernel the smooth archimedean weight is supposed to pair with, and it survived three of my own audit rounds (20, 21, 23) plus a full round (22) where I ran the project's own regression script and treated internal self-consistency as if it were validation against ground truth. I want to be precise about what went wrong and what does and doesn't survive.

## 2. Independent re-verification, from the actual source object

Rather than take `v13.387`'s resolution on the strength of its own writeup, I rebuilt the check from a different starting point than either side of the dispute had used: Suzuki's actual continuous screw function `g(t)` (pole + prime-ramp + archimedean, implemented in `research-notes/suzuki_riemann_screw_calibration.py`, established in `v13.285`, long before any of this controversy) and the exact 2-D-to-1-D reduction

\[
A_{mn}=\int_0^{2}g(t)\,[C_{mn}(t)+C_{nm}(t)]\,dt,
\qquad
C_{mn}(t)=\int_{-1+t}^{1}\psi_m'(x)\psi_n'(x-t)\,dx,
\]

established in `v13.290` — also from before the controversy. Both of these were common ground; my job was to evaluate the double integral directly, writing my own quadrature for `C_mn(t)` (an elementary, non-singular trig overlap) and integrating against `g(t)` (which has the known `t log t` cusp at the origin, handled by a `t=u^2` substitution near `0`) with no reference to anyone's closed-form archimedean formula, legacy or corrected.

**[N, independently computed]**

| `(m,n)` | my direct source-integral | `v13.387`'s reported source value | `v13.387`'s legacy formula | Round-20/rank-4 branch |
|---|---:|---:|---:|---:|
| `(1,3)` | `0.0003870693259522878` | `0.000387069325955204` | `0.000387069325951339` | `0.123796209246839` |
| `(1,21)` | `-0.0010495179195367183` | `-0.00104951791952813` | `-0.00104951791953675` | `+0.0164705769207731` |

My independently-written direct integral matches the legacy/source-faithful value to 8–10 significant figures at both test points, and is nowhere near the rank-four branch (which is off by roughly two orders of magnitude at `(1,21)` and even flips sign). This is not a close call.

## 3. What the actual mistake was

Having now traced it through, I can state the mechanism precisely. `v13.387`'s diagnosis is correct: the smooth archimedean weight `h` is meant to be paired against the **direct** overlap of the Dirichlet modes themselves, `S_{mn}(t)`, which arises from the identity `Q_g(v,w)=-\iint h(|x-y|)v(x)w(y)` obtained by integrating the original `\iint g(x-y)v'(x)w'(y)` by parts twice — once in each variable, moving both derivatives off the test functions onto `g` to produce `h=g''`. The overlap kernel that belongs with that manipulation has no extra frequency prefactor.

My Round-20 `S_{mn}(t)=\frac{2ab}{a^2-b^2}[b\sin(bt)-a\sin(at)]`, `a=m\pi/2,b=n\pi/2`, carries an explicit `ab`-type prefactor structure. That is the signature of a **derivative**-mode overlap (each derivative of a sine mode brings down a factor of its own frequency), i.e. it is `C_{mn}(t)`-shaped, not `S_{mn}(t)`-shaped. I paired the twice-differentiated weight `h=g''` with an overlap kernel that itself still carried one undischarged layer of differentiation. That mismatch is exactly what produces a formula that is dimensionally and numerically wrong by the amount seen above — not a sign error, not a coefficient typo (which is why, at the time, I could not find a simple variant that fixed it; there wasn't one, because the error was in which object to integrate against, not in the arithmetic of the integration itself).

## 4. Why Round 22 did not catch this

**[Audit — methodological lesson]** In Round 22 I "independently verified" the rank-four fix by writing my own script and running the project's new `suzuki_canonical_A0_matrix_assembly.py`, and confirmed both reproduced consistent numbers, including reproducing the historical `v13.348` value exactly when switched to the legacy formula. That was a real check, but of the wrong thing: it verified that the *implementation* was a faithful, bug-free realization of the *formula as re-derived*, and that the formula was internally self-consistent (agreed with a product-to-sum expansion of itself). It never checked the formula against Suzuki's actual source quadratic form, because I did not go back to `g(t)` and the raw double integral — I stayed inside the disputed derivation the whole time. Internal consistency between two things I derived from the same mistaken starting point cannot catch an error in the starting point itself.

**New guardrail, and the important one this round:** when a disputed formula traces back to an integration-by-parts or other exact-transformation step, a from-scratch re-derivation that repeats the same transformation is not independent of it. The decisive check has to go back to the pre-transformation source object (here, Suzuki's `g(t)` and the raw derivative-mode double integral) and reconstruct the disputed quantity by a route that shares no manipulation with either side of the dispute. Re-running or re-deriving inside the same framework, however carefully, only tests self-consistency.

## 5. Consequences

- **Round 20's finding is retracted.** The legacy archimedean formula `K_{\rm arch}(m,n)=-\frac4\pi\frac{nH_m-mH_n}{n^2-m^2}` was correct all along.
- **Rounds 21 and 23, which built on treating Round 20 as resolved-in-my-favor, inherit this retraction.** Round 21's confirmation that `v13.365`/`v13.366` "still needed" the fix is moot — they never needed it. Round 23's verification of `v13.376`–`v13.379` stands on its own arithmetic merits (that work was independent of the arch-formula dispute and I re-confirm it below), but its framing of the dispute as settled toward the rank-four branch does not.
- **`v13.362`, `v13.365`, `v13.366`** — which Round 20 caused to be marked superseded/reopened — are restored along with `v13.387`'s statement of their status; I have no further objection to them beyond what was already on record before Round 20.
- **The `v13.373`–`v13.386` rank-four detour** is correctly marked by the project as superseded. This represents real, sustained effort spent chasing a formula that was never wrong. I take responsibility for triggering that detour and I'm glad the project's own source-form regression check caught it as cleanly and quickly as it did.

## 6. What I re-confirm is unaffected

The V4/divisor-contact arithmetic verified in Round 23 (`v13.378`, `v13.379`) is genuine finite combinatorics and Dirichlet-character algebra, entirely independent of the Suzuki archimedean-formula question. It is unaffected by this retraction and I do not withdraw it.

## 7. Guardrails

All guardrails from prior rounds remain in force except that any language in Rounds 20/21/23 treating the rank-four archimedean formula as correct, or the legacy formula as erroneous, is superseded by this entry and by `v13.387`.

- **New guardrail (restated from §4):** a disputed formula that arose from an exact but easy-to-misapply transformation (integration by parts, change of overlap basis, etc.) must be checked against the pre-transformation object by an independently-derived route, not merely re-derived again inside the same transformation.
- **New guardrail:** running someone else's regression script and getting a matching number is evidence of implementation fidelity, not evidence that the underlying formula is correct. Say so explicitly in future audit entries rather than letting "I ran their script and it matched" imply more than it does.

**External audit round 24: Round 20's archimedean-overlap finding is retracted as incorrect, following independent re-derivation directly from Suzuki's source function that confirms `v13.387`'s resolution. The legacy rank-two formula is correct; the rank-four branch was the error. Apologies to the project for the detour this caused — the catch and fix in `v13.387`/`v13.388` were well done.**
