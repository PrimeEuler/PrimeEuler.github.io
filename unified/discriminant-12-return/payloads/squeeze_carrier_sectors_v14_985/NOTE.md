# Where does discreteness live on the two-factor carrier? (Sandbox exploration)

**Question.** The gravity lane's chain v14.944–950 closed every route from the
shape coordinate s = (1/2)ln(u/v) to a quantized source charge: on
H = L²(R_+², du dv) the squeeze generator is p_s = −iℏ∂_s with continuous
spectrum (v14.950), and no Casimir fixes a flux amplitude. This exploration
asks the carrier-level question behind that negative: on the two-factor
oscillator (Schwinger) carrier, which structures are discrete, and does the
shape-side generator preserve any of them?

**Setup.** Two bosonic modes (u, v), ℏ = 1. Two distinct su(1,1) algebras act:
(i) the *pair* algebra K0 = (N_u + N_v + 1)/2, K+ = a_u† a_v†, K− = a_u a_v;
(ii) the direct-sum squeeze generator p_s = D_u − D_v with
D = (i/2)(a†² − a²) per mode (the Fock face of v14.948/949's dilation).
Exact matrix arithmetic, Fock cutoff 7/mode; bracket identities checked on
states away from the cutoff edge (one Casimir value at the edge state
|3, 6> is a truncation artifact, identified as such in the output).

## Results [D], all machine-verified by the payload script

1. Pair algebra closes exactly: [K0, K±] = ±K±, [K−, K+] = 2K0 (residual 0).
   Its Casimir K0² − (K+K− + K−K+)/2 is diagonal in the sector
   d = n_u − n_v with eigenvalue **(d² − 1)/4** (d = 0: −1/4; d = 1: 0;
   d = 2: 3/4; d = 3: 2). K0 has the discrete ladder n + (|d|+1)/2 in
   sector d. K− lowers BOTH occupations together (coefficient √(n(n+d))),
   preserving d exactly: the pair algebra moves along the product/pair
   direction, never the shape direction.
2. **p_s preserves neither discrete label.** Its selection rules are
   (Δn_u, Δn_v) ∈ {(±2, 0), (0, ±2)} — it hops ONE factor at a time
   (e.g. |2,2> → |0,2>, |2,0>, |2,4>, |4,2>). Hence [p_s, N_u − N_v] ≠ 0
   and [p_s, K0] ≠ 0 (explicit nonzero matrix elements √6, √6/2): the
   squeeze flow crosses pair sectors (Δd = ±2) and changes pair number.
   Its only Fock-space invariants are the two parities n_u mod 2, n_v mod 2.
3. Casimir centering is shared: SU(2) gives C = j(j+1) = T² − 1/4 with
   T = (x+y)/2 (the pair AM); the pair SU(1,1) gives C = (d²−1)/4 =
   (|J_z| − 1/2)(|J_z| + 1/2) with J_z = (n_u − n_v)/2. Both are
   (m − 1/2)(m + 1/2) = m² − 1/4 for a half-integer lattice quantity m —
   the cone's centering form, on the pair side in both cases.

## Carrier trichotomy [D/I]

- **Factor-coordinate carrier** L²(R_+²): the s-flow is unitary, p_s is a
  boost, spectrum continuous (v14.949/950).
- **Schwinger Fock carrier**: discrete labels exist (pair ladder, sector d,
  both Casimirs), but they belong to the pair algebra; the s-generator
  preserves none of them (result 2).
- **Mesh carrier** (pairs (n, k) ∈ ℕ²): s takes discrete values on lattice
  points, but a fixed product shell is a finite divisor set carrying no
  translation group in s (only the flip s → −s). Discrete values ≠ a
  discrete conjugate charge.

**Verdict [I].** On every carrier, discreteness is a pair-side property —
pair number (conjugate to a pair phase, with the usual Susskind–Glogower
caveat), sector difference, Casimir centering — while the shape side
carries either a continuous boost or no group action at all. This is a
carrier-level explanation of the gravity lane's v14.944–950 negative: a
radial flux is a shape-side object, and the shape side has no discrete or
normalizable charge structure to fix its amplitude. A quantized source
charge, if one exists in this geometry, must be built from pair-side data
(K0 / d / Casimir) and coupled by an additional identification — it cannot
be the shape-side Noether flux. No such identification is claimed here.

**Scope.** Finite-mode exact algebra + the cited v14.949/950 analysis.
No gravitational source, coupling, or G is derived; the Suzuki-quarter
physical weld remains parked and untouched. Complementary to the gravity
lane's finite-strain constitutive line (different question: energy
functional vs. charge carrier).

**Reproducer:** `carrier_sectors.py` (payload). Prints every bracket,
Casimir eigenvalue, and selection rule quoted above.
