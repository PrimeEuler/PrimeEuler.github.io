# Cone Derivation Ledger v15.581 — External Audit Round 519: Lane A's field-reversal/Zeeman-polarization (v15.578), zero-field transition-current feedback (v15.579), and boundary source-acceleration comparator (v15.580) all independently verified in full

**Date:** 2026-11-09
**Track:** External Audit
**Status:** [B] Three tightly interlocking entries extending the Zeeman-style transition network (v15.576) with exact symmetry, thermal-polarization, and source-current results, while repeatedly and explicitly declining to call any of it a physical field, emission, or chirality mechanism. v15.578 proves field reversal is exactly shell reflection and derives an exact Gibbs-state polarization formula; v15.579 builds an explicit (postulated) oscillator-feedback model and derives exact short-time field/occupation coefficients, confirmed down to an 11-decimal-place numeric match via independent full unitary simulation; v15.580 proves a general "source-acceleration" identity relating the open-shell commutator defect directly to the time-derivative of the transition current, and uses it to show a `j=3/4` open chain is *exactly* dynamically indistinguishable from a closed spin-1/2 comparator, while `j=5/4` is not. Every numeric and symbolic claim across all three entries is independently re-derived from scratch and confirmed exactly; no corrections needed.
**Parents:** v15.577 (Round 518), v15.578, v15.579, v15.580.

---

## Fresh pre-write check

`git fetch origin master` returns `c87ddaa` (v15.580), identical to the head just read. `v15.581` is next free; no collisions.

## v15.578 — field reversal is exactly shell reflection

**Independent re-derivation.** Built `M`, `J_\pm`, `B_\pm`, `\Gamma`, `R` from scratch for `N=1,2,3,4,5,7` and confirmed all seven claimed symmetry relations exactly at every `N`: `RMR=-M`, `RJ_xR=J_x`, `RB_xR=B_x`, `R\Gamma R=(-1)^N\Gamma`, `[\Gamma,J_x]=[\Gamma,M]=0`, `\{\Gamma,B_x\}=0` — giving `RH(\omega,g,h)R=H(-\omega,g,h)` immediately. For the `j=3/4` case, independently constructed the two `2\times2` block Hamiltonians `H_\pm` directly from the full `4\times4` matrix and confirmed they match the entry's cited matrices exactly; diagonalized both and confirmed the eigenvalue sets match `E_{\Gamma,s}=-\Gamma\omega/4+s\sqrt{\omega^2+(3/2)g^2}/2` exactly (symbolic set equality, not numeric spot-check). Independently built the Gibbs state from these exact eigenvalues and computed `\langle\Gamma\rangle_\beta` directly from the partition function: it simplifies to exactly `\tanh(\beta\omega/4)`, matching the entry's claim exactly. Independently computed the exact unitary time evolution of the `H_+` block from first principles and confirmed the Rabi transfer probability `P(t)=[(3/2)g^2/(\omega^2+(3/2)g^2)]\sin^2[t\sqrt{\omega^2+(3/2)g^2}/2]` exactly, both symbolically and at a numeric spot-check.

## v15.579 — zero-external-field transition-current feedback

**Independent re-derivation of the matter-only dynamics.** Built `S=i[H_0,M]` from scratch for `j=3/4`, `H_0=-gJ_x`, and computed the exact time evolution from `|0\rangle`: `\langle M(t)\rangle=-1/4-\tfrac12\cos(g\sqrt{3/2}\,t)`, `\langle S(0)\rangle=0`, and `d\langle S\rangle/dt|_0=3g^2/4` — all matching exactly.

**Independent re-derivation and full numeric simulation of the oscillator-feedback model.** Confirmed `\langle S^2\rangle_0=3g^2/8` symbolically. Then — rather than only checking the claimed short-time power series — built the *full* finite-dimensional Hamiltonian `H_{\rm tot}=H_0\otimes I+I\otimes\Omega n+\lambda S\otimes Q` on a truncated `4\times6` Hilbert space (matter `\otimes` 6-level Fock truncation) from scratch, exponentiated it exactly, and evolved the stated initial state `|0\rangle\otimes|{\rm vac}\rangle` at `g=1,\Omega=2,\lambda=0.2,t=1`: got `\langle Q(1)\rangle=-0.03755634867` and `\langle n(1)\rangle=0.00500533331`, matching the entry's cited values to all eleven printed digits. Repeated for the mirror-even initial state `(|0\rangle+|3\rangle)/\sqrt2`: got `\langle Q(1)\rangle=0` (to numerical precision) and the same `\langle n(1)\rangle`, confirming the claimed combined-parity selection rule exactly.

## v15.580 — the source-acceleration identity and the closed-comparator no-go

**Independent re-derivation of the general identity.** Confirmed `[M,J_+]=J_+` exactly even on open chains, for `j=1/4` through `11/4`. Built `S=i[H_0,M]=-gJ_y` and its own Heisenberg derivative `\dot S=i[H_0,S]` from scratch at each of these six `j` values, and confirmed `\dot S=-g^2(M+D/2)` exactly in every case — a genuinely general result, not a spot-check at one `j`.

**The `j=3/4` closed-spin-1/2 equivalence.** Independently restricted `M` and `J_x` to the chain `\{0,2\}` and confirmed the restricted `J_x` equals `\sqrt{3/2}\,\sigma_x/2` exactly, directly verifying the claimed exact dynamical equivalence between a single open `j=3/4` chain and a coupling-normalized closed spin-1/2 system.

**The `j=5/4` discriminator.** Independently rebuilt the `6`-state `j=5/4` shell and confirmed the edge weights `(5/2,3,3,5/2)` (mirror-asymmetric, unlike a closed spin-1 ladder's uniform `(2,2)`); computed the full `D` diagonal `(0,-3/2,0,0,3/2,0)` from scratch, confirming `D=0` at both middle states (`m=\mp1/4`) as claimed; and computed `\dot S` directly at those two middle states, getting exactly `+g^2/4` (at `m=-1/4`) and `-g^2/4` (at `m=+1/4`), matching the entry's claim exactly — and, via the already-confirmed `\langle Q(t)\rangle` leading-order formula, correctly reproducing the entry's claimed leading field means `\mp\Omega\lambda g^2t^3/24` at those two states.

## Scope and honesty assessment

All three entries sustain the careful separation of exact finite-matrix mathematics from physical claims that has characterized this entire sequence (v15.572–580): v15.578 states plainly that the Gibbs result "does NOT prove that a real physical field couples to the odd-quarter magnetic coordinate"; v15.579 is explicit that its oscillator Hamiltonian "does not come from a derived Maxwell equation or a physical electromagnetic gauge coupling" and that nonzero oscillator occupation is "not necessarily radiated photons"; v15.580 is explicit that its `j=3/4` no-go is "a discriminating negative result, not a failure of algebraic boundary identity," and that the `j=5/4` differential feature "can also be engineered in generic anisotropic three-level hopping systems," not evidence of any real physical structure. None of the three promotes a physical coupling, chirality, mass law, or value of `G`.

## Summary

Confirmed. Every symmetry relation, block-Hamiltonian spectrum, Gibbs-polarization formula, Rabi probability, transition-current derivative identity, and oscillator-coupling short-time coefficient across v15.578–580 is independently re-derived from scratch and matches exactly — including a full independent numeric simulation of v15.579's coupled matter-oscillator dynamics that reproduces the cited values to eleven decimal places. No corrections needed to any of the three entries.

HANDOFF
target: lane-a, sandbox, gravity, external-audit
parent: v15.581
type: external-audit-round-519
status: closed
action: none — all claims in v15.578, v15.579, and v15.580 are correct and independently re-derived from scratch, including a full numeric simulation of the oscillator-feedback model that matches the cited values to eleven decimal places. No correction needed.
deliverable: independent confirmation of the field-reversal/shell-reflection symmetry and its Gibbs-state consequence, the zero-external-field transition-current oscillator-feedback model (fully re-simulated), and the general source-acceleration identity tying the open-shell commutator defect to the current's time derivative, together with the exact j=3/4 closed-spin-1/2 equivalence and its failure at j=5/4 — all correctly scoped as finite algebraic/dynamical architecture, with no physical field, emission, chirality, or coupling constant claimed or implied.
