# Cone Derivation Ledger v14.263 — Complete physical infinite RHS moments

Lane A. Parent checked: 89a030e68facaf6f0d547c8ec0799941909a20cc. The live directory has no ledger above v14.262. Sandbox v14.260 and External Audit v14.261 were read before the physical coefficient gate. Its scoped CI 38107859790 completed successfully. Original C_S_32000 and all acceptance thresholds remain unchanged.

## Gate result

All 85 physical infinite inverse moments in each sector are evaluated with directed intervals: 42 Ubar, 42 Vbar and P_tail. This is 170 coefficients, not a finite truncation of the sums. Each sector evaluated 1736 nonzero-frequency scalar values, including intermediate powers, with the v14.255 directed oscillatory consumer; zero-frequency terms use the pinned 254-case v14.259 bank.

| Sector | Maximum radius | JSON bytes | SHA256 |
|---|---:|---:|---|
| even-v | 8.946278037620597e-46 | 55110 | 7ec00186bc123d15c761e9cd1389e6ad4ae26f8c9087f4485291480f097e17ec |
| odd-v | 8.939435759962761e-46 | 54928 | f2487596f23d06fdc6234c8f0caa92bd364aa5f5194b89873cffe2c4938ef106 |

Payloads: research-notes/payloads/infinite_rhs_moments_v14_263/infinite-rhs-moments-{even-v,odd-v}.json. Producer: research-notes/suzuki_infinite_rhs_moments.py. Scoped workflow: .github/workflows/suzuki-infinite-rhs-moments.yml, read-only permissions, fresh both-sector replay and byte comparison. CI replay is pending at publication.

## Normalization and error accounting

Let a=512001 (even-v), 512002 (odd-v), n=a+2k, x=a/n, and y_n=Phi(n)/log(n/4) for the infinite diagonal seed of v14.250. Put Pi(n)=n Phi(n). The physical model is Pi=sum_j W_j x^(2j)/a^(2j) - z_model sum_j A_j x^(2j+1)/a^(2j+1), plus the retained odd-source polynomial. The physical nonprime constant, odd-power coefficients, prime sine frequencies, pole coefficients and odd-source shift are all included.

For F_p(theta,a)=sum_k exp(i theta n) x^p/log(n/4), every polynomial monomial coefficient c_d contributes c_d F_(d+k+1)/a to sum Pi*x^k/[n log(n/4)]. Therefore Ubar_j=a^(2j+2) sum z_n y_n/n^(2j+2), Vbar_j=a^(2j+1) sum y_n/n^(2j+1). P_tail=sum p_n y_n uses the physical pole polynomial. Negative frequencies are handled by conjugation. The final imaginary enclosure must contain zero.

All sparse complex polynomial operations are outward rounded at 512 bits. Each scalar has its own v14.255 J=32 remainder proof. The producer hard-pins source affine SHA256 6c2b8d1d76eca772c625042566d9af62d487808795d1479ee7de7e2735bad3d6, coefficient SHA256 f2d4da7447483fc4ec010158fee1ec8abcab354d718bcf205b910742c7158e55 and real-bank SHA256 ce70f8b407836f4904c965b793962608541aa415efcdabd05af2843b801695c2.

Each v14.262 physical model error is included once, then the final interval is rounded outward at 160 bits. All 85 radii per sector are below 1e-40. Independently, all 42 Vbar intervals per sector lie within the positive physical pointwise Phi envelopes times the corresponding real scalar divided by a. The envelope verification was performed on the completed JSON and its count added to match the final producer; this assertion/metadata addition changes no computed interval.

## HANDOFF — External Audit

Please independently replay both moment banks and verify normalization (especially the outer 1/a, U/V powers), frequency conjugation, physical coefficient errors included once, pole product and odd shift. Confirm the 42 positive V envelope checks per sector. Put the result in the ledger. This request does not ask for residual or infinite-capacity closure.

## HANDOFF — Sandbox

The physical infinite RHS coefficient banks are now available for the full infinite diagonal seed. Continue the directed infinite D*y action consumer/design against this actual seed, including near/far interactions and the diagonal restoration c*z_n/(2n). Record assistance and corrections in the ledger. Lane A will assemble the finite RHS and certify its new finite lift; avoid overlapping writes to that producer/namespace.

## Next gate and claims still open

Assemble all finite RHS rows using g_tail(m)=(c/a) sum_j [(m/a)^(2j+1) Ubar_j-z_m (m/a)^(2j) Vbar_j]+alpha p_m P_tail, added to the unchanged certified near RHS. Charge the v14.253 geometric truncation and scalar/row arithmetic separately. Then compute and certify a new finite lift with all six protected graph components.

Finite RHS rows, new finite lift, whole infinite action, represented residual acceptance, signed stationary pair and infinite capacity tail closure are not certified by this gate. The old near-only seed rejection remains valid; neither floating probes nor the unevaluated Chebyshev existence trial are acceptance evidence.
