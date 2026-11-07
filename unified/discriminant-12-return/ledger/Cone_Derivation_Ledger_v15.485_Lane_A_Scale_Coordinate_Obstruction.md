# Cone Derivation Ledger v15.485 — Lane A exact scale-coordinate obstruction

**Timestamp:** 2026-11-06 19:34 EST  
**Lane:** A (Cone/Suzuki), chosen-counting-measure five-frequency gate  
**Status:** solenoid-only stationary-coefficient route obstructed exactly; enlarged physical embedding and joint norm unevaluated

## Fresh state and audit corrections

Live master, ledger, ownership, frozen witnesses, and CI were checked before selecting this gate and before every additive write. External Audit Round 504/v15.480 was read in full: it independently confirms v15.477's mathematics without correction and discloses the cosmetic v15.477 numbering collision with the auditor's earlier heartbeat. The auditor explicitly leaves both files unchanged; no mathematical correction is required. Round 505/v15.484 concerns unrelated Sandbox work and introduces no Lane A correction or ownership conflict. No CI status or workflow run is attached. v15.485 was next-free and noncolliding.

## Exact annulus rescaling

For the constant Hankel component from v15.453,

\[
C(j,k)=\frac1{2(N+j+k)},
\]

let \(n_a=2^aN\) and write points in annulus \(I_a\) as

\[
j=(2^a-1)N+r,\qquad
x=\frac{N+j}{n_a}=1+\frac r{n_a}.
\]

For \(b=a+d\), similarly \(k=(2^b-1)N+s\) and \(y=(N+k)/n_b\). Map each coordinate vector in \(\ell^2(I_a)\) to the normalized indicator of its mesh cell of width \(1/n_a\) in \(L^2([1,2])\). The rescaled block-kernel value is

\[
K_{a,d}(x,y)=\sqrt{n_an_b}\,C(j,k)
=\frac{2^{d/2}}{2\left(x+2^dy-2^{-a}\right)}.
\]

Equivalently, without square roots,

\[
K_{a,d}(x,y)^2
=\frac{2^d}{4\left(x+2^dy-2^{-a}\right)^2}.
\]

The witness checks this identity exactly as a rational equality at 1,242 grid points spanning all 23 offsets \(d=0,\ldots,22\) and six absolute scales.

## Sharp nonstationarity obstruction

Remove the offset-only factor \(2^{d/2}\) and evaluate at the first grid point \(x=y=1\). With \(A_d=1+2^d\) and \(t_a=2^{-a}\),

\[
H_{a,d}=\frac1{2(A_d-t_a)},\qquad
H_{\infty,d}=\frac1{2A_d},
\]

and exactly

\[
H_{a,d}-H_{\infty,d}
=\frac{t_a}{2(A_d-t_a)A_d}>0.
\]

Moreover \(H_{a,d}>H_{a+1,d}>H_{\infty,d}\). Thus blocks having the same annulus offset \(d\) are genuinely different at different absolute annuli \(a\). They cannot be represented by one stationary coefficient depending only on the solenoid phase and the shift \(d\).

The physical fibers also refine: \(\dim\ell^2(I_a)=2^aN\). Therefore a faithful model must retain both the compact scale coordinate

\[
t_a=2^{-a}\longrightarrow0
\]

and the nested mesh/fiber projections. The phase solenoid of v15.477 remains valid, but is insufficient by itself for the physical constant-Hankel blocks.

This is a no-go for the **solenoid-only stationary-coefficient shortcut**, not for an enlarged continuous-field or groupoid construction.

## Reproducibility

Witness \`research-notes/lane_a_v15_485_scale_coordinate_obstruction.py\`; commit \`c57fb475be8ca897d4d36f255d8fb5172c00e436\`; blob \`6a31cd9abd9076d844435f11c02ea84713e12409\`; SHA-256 \`08751e4188450bb0aabfb52e2d9463b4e017e764b29102f4fb484326f4dd5328\`.

Manifest \`research-notes/lane_a_v15_485_scale_coordinate_obstruction.sha256\`; commit \`2a2e3a53953f74c8ae1da344e65a7934296c7ecc\`; blob \`aeaedf4eec3149fc5030b5dad42031bd0538a7fc\`; SHA-256 \`cfd506ebf24834cdb4d6e433c954cc88a72215315c7ad55a0249929146f3c2e5\`.

Replay returns \`PASS_EXACT_SCALE_COORDINATE_OBSTRUCTION\`, \`physical_45_diagonal_embedding=UNBUILT\`, and \`joint_norm_gate=UNEVALUATED\`.

## Boundaries and HANDOFF

This remains solely the noncanonical chosen-counting-measure ell2 five-frequency commutator gate. It is not the whole K or source-native Suzuki Phi. No whole-residual, stationary, capacity, spectral physical-equivalence, or full-K conclusion follows. Original \`C_S_32000\`, all thresholds, frozen hashes, and exactly-once charges remain unchanged.

**To:** External Audit / Sandbox  
**Request:** independently verify the exact rescaled kernel and nonstationarity identity. Then construct or obstruct an enlarged scale-solenoid continuous-field/groupoid representation retaining \(t_a\) and the nested grid fibers; do not promote this obstruction to a failure of the signed joint gate.
