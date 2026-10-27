# Canonical operator-origin projection gate (v14.942 handoff) — sandbox plan

**Gate:** ledger v14.942 (Lane A), HANDOFF — Sandbox, restated unchanged
in v14.961 (Lane A: the gate "remains the sole active Lane A
dependency"). Started 2026-10-26 on Jeremy's instruction
("continue with lanes as requests").

**Required return (v14.942):** either
(P) a canonical far-output projection/intertwiner derived from the
frozen operator/domain/spectral structure satisfying, without raw
row-wise cutoff or fitted zeros: (1) channel defined before
evaluation, output locality from an operator identity; (2) no
diagonal term; (3) exact structural annihilation of the frozen DM
output rows; (4) full F2 band [S, 2S); (5) audited drift/constant
cancellation + corrected O(1/ln N) remainder; (6) ℓ²; (7) exact
reproducible witnesses, manifests, hashes — or
(N) a proof of nonexistence in a precisely stated operator/channel
class, with no universal extrapolation.

## 1. Operative formalism (from ctgate/DERIVATION.md §0, audited)

Sector σ = ±1; input lattice m ≥ b (512001/512002), m ≡ start
(mod 2); first far row F0 = 4161533/4161534; DM rows N < F0.
Channel action of an input family y (no diagonal term):

  A_y(N) = (c/2)·(z_N·V_y(N) − U_y(N)) + 2σ·p_N·P_y,
  V_y(N) = Σ_{m≠N} 2m/(N²−m²)·y_m,
  U_y(N) = Σ_{m≠N} 2N/(N²−m²)·(zy)_m,
  P_y = Σ_m p_m·y_m,  p_m = ⌊L·m/(m²+t)·2^256⌋/2^256 > 0.

Row functional ℓ_N(y) = A_y(N); its coefficient of y_m (m ≠ N) is
k_N(m) = c·(m·z_N − N·z_m)/(N²−m²) + 2σ·p_N·p_m, and at m = N it is
exactly 2σ·p_N² (pole part only; V/U exclude m = N).
Audited facts used: |z_m| ≤ Zbar = 7.4232946911477145; z has
lattice (nonprime) mean π/2 — the mechanism of the audited drift
β = W_0/2 (v14.901, R356); κ_m := −c·z_m + 2σL·p_m satisfies
κ_{m₁} ≠ 0 at m₁ = b, certified exact Fractions (ctgate
constants.json: κ = −0.640872 even / −0.962386 odd);
N·k_N(m) → κ_m as N → ∞ (m fixed) and m·k_N(m) → κ_N as m → ∞
(N fixed). Three-band lemma (ctgate §1): the Λ coefficient of a
channel action is exactly −W*/2 for an affine family with leading
coefficient W*; in particular the CT⁰ profile (β = W_0/2 ≠ 0)
forces any realizing input to have the affine tail ŷ(m) =
W*/m + O(1/m²), W* = −W_0 ≠ 0, hence full support on the tail.

## 2. Inventory of frozen structures (candidate provenance sources)

- (a) The frozen mode basis and its diagonal operators: D_log
  ((D_log)_nn = ln(n/4)) and D2 (n²). Their Borel spectral
  calculus = exactly the diagonal operators in the mode basis.
- (b) The channel realization itself (V, U, pole) — Sylvester /
  divided-difference kernels in N² − m².
- (c) The freeze's region/block decomposition (v14.442/447/583):
  an evaluation partition — v14.942 already ruled it is not, by
  itself, operator provenance.
- (d) The moment class / inverse-moment DM algebra (85 moments):
  defines the domain; contains all finitely supported sequences.
- (e) NOT frozen data: the spectral decomposition of the full
  non-diagonal frozen operator; the stationary pair / capacity
  closure (open globally). Out of scope for this gate.

## 3. Route analysis (decided before write-up)

"Structural annihilation" is formalized as: the DM vanishing is
an identity holding for every input of an operator-defined class
(a property of the channel/class, not of one tuned input) — this
is the only reading under which item (3)'s "structural reason"
differs from the fitted zeros the gate excludes. Trichotomy on
where the annihilation comes from:

(i) Output side, B∘T with B diagonal (spectral calculus):
    - If B is a projection with range = far rows, B IS the hard
      indicator 1[N≥F0] as a linear map (Lemma A) — the object
      v14.942 excluded; a spectral-calculus redescription does
      not change the map.
    - Any diagonal B with β_N = 0 on DM rows is by construction
      an output-row cutoff (it discards the DM output
      coordinates for every input) — row-wise forcing in
      operator clothing, excluded by the gate's item (1), which
      requires locality from an operator identity of the
      channel, i.e. intertwining — route (iii).
(ii) Input side, restriction to 𝒴 = range(A), A diagonal, data
    class containing all finitely supported sequences:
    annihilation as an identity on 𝒴 forces k_N(m) = 0 at every
    DM row N and every live mode m (single-mode data). The
    profile forces supp(a) ⊇ tail (§1). Fixing one DM row N, the
    identity k_N(m) = 0 on the tail gives
    z_m = (z_N/N)·m + (2σp_N/(cN))·p_m·(N²−m²) for all large m;
    with p_m(N²−m²) = −L·m + O(1/m) + O(m²·2^−256) this reads
    z_m = S·m + o(1). Boundedness (|z| ≤ Zbar, half-line family)
    forces S = 0, hence z_m → 0 along the lattice — contradicting
    the audited lattice mean π/2 of z. Finite-support A is
    separately impossible (§8(a) of ctgate + the drift identity:
    no Λ term). [Theorem]
(iii) Intertwiners T∘A = B∘T, A, B diagonal: the pole diagonal
    coefficient gives β_N = a_N exactly (2σp_N² ≠ 0); pairing
    with the certified mode m₁ = b and N·k_N(m₁) → κ_{m₁} ≠ 0
    gives a_N = a_{m₁} for all large N; hence B = a·I on the far
    tail with a ≠ 0 (else the far profile dies). No diagonal
    intertwiner localizes output to the far band. [Lemma B]

Positive by-product (exact operator identities that DO hold):
the channels intertwine D2 up to global moment functionals:
  N²·V_y(N) − V_{Λy}(N) = 2·Σ_m m·y_m,
  N²·U_a(N) − U_{Λa}(N) = 2N·Σ_m a_m   (a = zy),
i.e. the commutator defect is a moment functional of the input,
never a row-support operator — the operator-level reason no
spectral-calculus manipulation manufactures output locality.

**Expected verdict: branch (N)** — scoped no-go in the class
𝒞_proj = {frozen V/U/pole kernel channels, no diagonal; input
classes, output operators and intertwiners confined to the
frozen mode-basis spectral calculus (a),(b); annihilation as an
operator identity on the input class}. Explicitly NOT excluded
(mirroring v14.942's own scoping): single tuned inputs with
fitted DM zeros (excluded by the gate on other grounds);
operators outside the frozen spectral calculus, e.g. built from
a spectral decomposition of the full non-diagonal operator
(not frozen data, item (e)); prescribed-zero infinite families
by non-frozen means; any future re-freeze with new structure.

## 4. Witness plan (projgate_witness.py)

W1. Exact Fraction verification of both Sylvester identities on
    random finite rational inputs (V-map and U-map separately).
W2. Exact recomputation of κ_{m₁} from ctgate constants.json
    (Fractions); assert ≠ 0, both sectors.
W3. Exact p_N > 0 spot checks (Fractions, incl. N at F0 scale)
    and the exact diagonal-pair coefficient 2σp_N² ≠ 0.
W4. Exact Fraction evaluation of the v14.936 spike's closed-form
    action CT_sp(N) at sample DM rows (≠ 0): the clause was
    load-bearing for at least the spike component.
W5. Float64 exhibit: the full v14.936 phantom's channel action
    (WITHOUT the support clause) at sample DM rows, direct
    chunked sums over the formula-defined input family to
    m ≤ 2·10^8 plus a rigorous affine tail enclosure
    (|ŷ_m| ≤ C_ŷ/m with C_ŷ from the channel constants) —
    nonzero by a wide margin vs the enclosure.
W6. Numerical confirmation of N·k_N(m₁) → κ_{m₁} and of the
    z-asymptotic identity's failure mode (z_m − (S·m + o(1))
    stays O(1) oscillatory for the best-fit S), as [N] support
    for the Theorem's contradiction step.

## 5. Deliverables

DERIVATION.md (class, Lemma A, Theorem, Lemma B, Sylvester
identities, scope), projgate_witness.py + witness.json,
CERTIFICATE.md, PACKAGE_MANIFEST.md with SHA-256 of every file;
ledger entry (negative branch) under the ledger-everything
policy after full review. No production run; no F1/F2
composition; thresholds and charges untouched.
