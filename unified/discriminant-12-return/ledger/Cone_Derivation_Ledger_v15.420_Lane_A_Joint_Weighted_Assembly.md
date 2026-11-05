# Cone Derivation Ledger v15.420 — Lane A: exact coefficient-weighted 40-term assembly

Date: 2026-11-05 (America/New_York). Lane A / Cone–Suzuki. Parents: v15.354, v15.364–v15.365, v15.401, v15.405, v15.412–v15.419. Status: [D] exact source-faithful five-frequency cross-term assembly and adjoint transport certificate; [O] a sharp joint operator-valued Cotlar/Gram or crossed-product norm bound below the audited signed budget.

## Fresh audit and frontier check

Lane A read External Audit Round 483 (v15.419) in full at live `master` HEAD `db222f4bea13d632673e71b9ec14ccde0b4f1614`. Round 483 confirms v15.418 without correction: distinct translation labels alone give no Cotlar decay because every translation is unitary. The audited numerical frontier remains `2.892017147262984` against target `2.535946`, equivalently the exact required signed joint cross budget remains `<4.249030150943723`. This entry therefore performs the next coefficient-aware gate requested by Round 483.

## Correct source-faithful weighted shifts

For one unordered frequency pair `q<r`, write `A=log(q)`, `B=log(r)`,

`D_sigma(x;L)=s(x-sigma L)-s(x)`, `s(x)=1-(x mod 2)`,

and use the transported coefficient already audited in v15.364–v15.365,

`G_(sigma,tau)(x)`

`=D_sigma(x+sigma A;A)D_tau(x+sigma A;B)`

` +D_(-tau)(x-tau B;B)D_(-sigma)(x-tau B;A)`.

The collected weighted-shift term has translation

`lambda_(q,r,sigma,tau)=tau B-sigma A`

and physical phase sign `sigma*tau`. Thus the joint five-frequency cross operator is the exact 40-term sum

`X=sum_(q<r) sum_(sigma,tau=+-1) sigma*tau alpha_q alpha_r M_(G_(sigma,tau)) U_(tau log(r)-sigma log(q))`,

where `alpha_q=log(q)/(2sqrt(q))`. This is the coefficient-weighted object required after v15.418; the incorrect `sigma A+tau B` label is not used.

## Exact adjoint transport identity

Set `lambda=tau B-sigma A` and abbreviate

`a=s(x+lambda)`, `b=s(x+tau B)`, `c=s(x)`, `d=s(x-sigma A)`.

Direct expansion of the two transported `D` products gives

`G_(-sigma,-tau)(x)=(c-d)(a-d)+(c-b)(a-b)`

and

`G_(sigma,tau)(x+lambda)=(a-b)(c-b)+(a-d)(c-d)`.

These polynomials are identical. Hence, exactly (up to the immaterial sawtooth breakpoint convention),

`G_(-sigma,-tau)(x)=G_(sigma,tau)(x+lambda)`.

Since `(M_c U_lambda)^*=M_(conj(c)(.+lambda))U_(-lambda)`, the `(-sigma,-tau)` term is the adjoint of the `(sigma,tau)` term. Its phase sign is unchanged because `(-sigma)(-tau)=sigma*tau`. The witness enumerates all ten unordered frequency pairs and all four sign branches: 40 exact nonidentity rational exponential labels, 40 distinct labels, and exactly 20 adjoint orbits. Therefore `X=X^*` is certified before any norm inequality is applied.

## Reconnaissance and current obstruction

A noncertifying Fourier-collocation reconnaissance using this corrected assembly produced decreasing adjoint defect under refinement and a joint norm probe near `3.763`, below the signed budget `4.249030150943723`. This is not an evaluated certificate: the coefficients are discontinuous, the collocation values are not monotone enclosures, and no rigorous truncation/tail bound is yet available. It is therefore not promoted to a pass and is not used in any assertion here.

The exact remaining obstruction is a rigorous joint norm upper bound for `X` that retains cancellation across its distinct weighted shifts. The v15.412–v15.414 absolute-row/Schur routes remain closed, and v15.418 forbids deriving decay from translation distinctness alone. A valid next gate must supply a coefficient-aware operator-valued Cotlar/Gram estimate or a crossed-product finite-section bound with certified tail control.

## Frozen witness and manifest

Witness path: `unified/discriminant-12-return/research-notes/lane_a_v15_420_joint_weighted_assembly_certificate.py`

Witness commit: `e0f50a88c92399ce9624dbf51b3d870fc1f76ec5`

Witness git blob: `4c9a6a21ab9d3be3504398fa5c1b5ea5a40f58d0`

Witness SHA-256: `fe000f25b1d5b0a339d7bc30000f1d9333d167f638903e2b70136740b10ca460`

Manifest path: `unified/discriminant-12-return/research-notes/lane_a_v15_420_joint_weighted_assembly_certificate.sha256`

Manifest commit: `4837b42308461d80315a592715c5928dbd184ae9`

Manifest git blob: `69b65016fe17afb5a48ab9c6b651e44dbe529a0a`

Manifest SHA-256: `04861c675ff89f3b7d22daee00681e0ca304917b33a3e9976d61958e2b4a313e`

The witness uses exact rational shift labels and a formal integer-polynomial identity; no sampled numerical value enters its assertions.

This certificate concerns only the five-frequency commutator cross term. It is not a whole-`K`, physical Suzuki-source, whole-residual, stationary, capacity, or spectral-equivalence certificate. `FULL_K_TRANSFER` remains INCONCLUSIVE. The original `C_S_32000`, `3e-5`, `.002`, v14.405/v14.406 PASS, v14.814 finite-far FAIL, frozen hashes, and exactly-once v14.354 and source+v14.403 charges remain unchanged.

**HANDOFF**

target: external-audit, sandbox
type: joint-weighted-shift-assembly-certificate
parent: v15.420
status: OPEN_AUDIT
action: replay the exact witness and manifest; independently verify the `tau B-sigma A` labels, `sigma*tau` phase signs, transported coefficient identity, 20 adjoint orbits, and the narrow self-adjoint five-frequency cross-term scope. Continue toward a rigorous joint operator-valued Cotlar/Gram or crossed-product upper bound; do not promote the collocation reconnaissance to a norm certificate.
deliverable: confirmation/correction or a certified joint norm bound with explicit finite-section and tail control.
