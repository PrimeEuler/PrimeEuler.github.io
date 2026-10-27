# Cone Derivation Ledger v14.966 — Sandbox return to the v14.942 canonical-projection gate: scoped no-go in the frozen spectral calculus

**Date:** 2026-10-26. **Lane:** Sandbox (little Euler). **Parents:** v14.942 (Lane A output-support verdict and canonical-projection gate), v14.961 (Lane A: the gate remains the sole active Lane A dependency), v14.936 (sandbox counter-term return), v14.909 (counter-term design gate), v14.901 (far-coefficient return). **Status:** [D] scoped nonexistence proof (the gate's negative branch), with [N] exhibits. **Collision check:** immediately before writing, live master HEAD `52e14355bdb8` (v14.965); v14.966 next free. Payload: `payloads/sandbox_projection_gate_v14_966/` (DERIVATION.md, PLAN.md, projgate_witness.py, witness.json, CERTIFICATE.md, PACKAGE_MANIFEST.md).

## Answer

The gate asked for a canonical far-output projection/intertwiner derived from the frozen operator/domain/spectral structure, or a proof that no such object exists in a clearly stated certification class. The return is the negative branch: **in the class 𝒞_proj below, no auxiliary channel realizes the v14.909 counter-term profile with exact DM annihilation holding for a structural reason.** The obstruction of v14.936 §8 is thereby complemented on the operator-identity side: the support clause was not an artifact of phrasing — every operator-derived replacement for it inside the frozen calculus is either the clause itself, a row cutoff by construction, unable to annihilate, or unable to localize.

## The class 𝒞_proj (DERIVATION.md §1)

(K) Kernel species: the frozen channel action A_y(N) = (c/2)(z_N V_y(N) − U_y(N)) + 2σ p_N P_y (V/U/pole sums of the audited formalism), **no diagonal term**. (I) Input classes 𝒴 = A(𝒟) with 𝒟 linear, containing all finitely supported lattice sequences, and A diagonal in the frozen mode basis — the Borel spectral calculus of the frozen diagonal (D_log, equivalently D2); DM annihilation required as an identity on all of 𝒴. (O) Output operators/intertwiners: diagonal B in the same calculus, by composition or by intertwining T∘A = B∘T. (P) Profile: the constructed input in 𝒴 realizes CT⁰'s audited coefficients; by the three-band lemma (v14.936 §1) the nonzero drift β = W_0/2 forces its affine coefficient W* = −W_0 ≠ 0, hence full tail support — which in turn forces supp(A) ⊇ tail.

"Structural" is formalized as an identity on the operator-defined class — the only reading under which the gate's item (3) differs from the fitted zeros it separately excludes and from the evaluation declaration v14.942 already rejected.

## Results (DERIVATION.md §§2–5)

**Exact identities that hold (§2).** The frozen channels intertwine D2 up to global moment functionals: N²V_y(N) − V_{Λy}(N) = 2(M₁[y] − N·y_N) and N²U_a(N) − U_{Λa}(N) = 2N(M₀[a] − a_N), termwise, verified in exact Fractions (witness W1, 60/60 random trials). Every spectral-calculus manipulation of the channel re-expresses its action through input moments; none manufactures row support.

**Lemma A (§3).** A diagonal projection whose range is the far-row space is, as a linear map, exactly the hard indicator 1[N≥F0] — the object v14.942 excluded; a spectral-calculus redescription does not change the map. Any diagonal B vanishing on DM rows is a row-wise cutoff by construction, excluded by the gate's item (1).

**Theorem (§4).** Input-side annihilation as an identity on 𝒴 forces the row kernel k_N(m) to vanish at one fixed DM row for all large lattice m; the identity then reads z_m = S·m + o(1) with S = z_N/N − 2σp_NL/(cN). The audited bound |z_m| ≤ Zbar forces S = 0, and then the audited lattice mean π/2 of z — the mechanism behind the nonzero audited drift — is contradicted. Finite-support classes separately fail the profile (zero Λ coefficient; cf. v14.936 §8(a)).

**Lemma B (§5).** For diagonal intertwiners T∘A = B∘T, the pole diagonal coefficient gives β_N = a_N exactly (2σp_N² ≠ 0, p_N > 0 exact), and pairing with the certified spike mode m₁ = b (κ_{m₁} = −c·z_{m₁} + 2σL·p_{m₁} ≠ 0 in exact Fractions, both sectors) with N·k_N(m₁) → κ_{m₁} forces B = a·I on the whole far tail. No diagonal intertwiner localizes output to the far band.

## Exhibits (witness.json; DERIVATION.md §6)

- **W4:** the v14.936 spike's DM action is *certified* nonzero at eight sample DM rows — the z_N value that would force it to zero misses the certified z_N enclosure by 0.139–13.45 (enclosure radii ~1e-39).
- **W5:** the full v14.936 phantom evaluated without the support clause at four sample DM rows gives N·A_ph(N) = **+0.0350 / +0.0303 (even), +0.1173 / +0.1644 (odd)**, against rigorous affine tail enclosures ≤ 0.0036 — the clause carried the entire DM silence, at the same order as the far profile itself.
- **W6:** N·k_N(m₁) → κ_{m₁} confirmed numerically; the z-identity forced by the Theorem's hypothesis mispredicts z_m by up to 433 at m = 4·10^8 (forced +436.93 vs model +3.49, even sector).

## Scope (DERIVATION.md §7) — no universal extrapolation

Not excluded: (a) a single tuned input with fitted DM zeros (excluded by the gate's own no-fitted-zeros rule, not re-derived here); (b) objects built from data outside the frozen spectral calculus — above all a spectral decomposition of the full non-diagonal frozen operator, or the stationary-pair/capacity structures, none of which are frozen data; if such a decomposition is ever frozen, the gate can be re-asked in the enlarged calculus and §§3–5 do not prejudge it; (c) infinite families with prescribed discrete zeros by non-frozen means (v14.936 §8(c)). If Lane A rejects the §1 formalization of "structural", the live remainder of the gate is exactly the choice of formalization — the three routes closed here are the three the frozen calculus offers.

## Not claimed / untouched

No F1/F2 composition or certificate; no residual replay; `C_S_32000`, the 3e-5 and 0.002 thresholds, and the exactly-once v14.354 / v14.403 charges unchanged and unspent. v14.583 stands as certified; v14.936's frozen witness values stand as audited (its construction branch remains NOT ADMISSIBLE per v14.942 — this return explains, within 𝒞_proj, why no operator-derived variant of it can be admissible either).

**Flags:** `gate_branch=NEGATIVE_SCOPED_NOGO`; `class=C_proj_frozen_spectral_calculus`; `universal_nogo=NOT_ASSERTED`; `witnesses=W1..W6_in_payload`; `Suzuki_payloads_touched=false`; `far_tail_touched=false`; `production_run=NONE`.
