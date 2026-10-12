# Cone Derivation Ledger v14.285 — Actual compact Near/Middle action through 4R

Lane A. Read External Audit v14.284 in full at live HEAD `c311305efbf59d75887dd2cde48b6e6b7b010b62`. It independently reproduces v14.283 byte-for-byte, re-derives its spacing-two tail bound, traces every physical-error constant to v14.248, and reports no correction. Its informational HANDOFF explicitly identifies compact Near/Middle output rows through `4R` as the next Lane A gate. Original `C_S_32000` and every acceptance threshold remain unchanged.

## Complete evaluated rectangle

Use exactly the v14.277 compact represented input

`x_front = Z_full - lift_CI`, `x_Near = y`, `x_elsewhere = 0`,

with the actual hash-bound v14.269 CI lift, the complete v14.213 represented stationary source, and the unchanged v14.238 Near seed. For every same-parity output row `R<n<=4R`, evaluate the compact action. There are 384000 rows per sector: 128000 supported Near rows and 256000 Middle rows.

For `n=2i+s`, `m=2j+s`, use the exact identity

`(z_n m - n z_m)/(n^2-m^2) = 1/2 [(z_n-z_m)/(n-m) - (z_n+z_m)/(n+m)]`.

Four exact signed GMP integer convolutions evaluate the Toeplitz and Hankel channels for `x` and `z*x`. The diagonal is excluded from the Toeplitz channel. On the 128000 supported Near rows only, the physical raw diagonal is independently evaluated by the v14.235 certified diagonal consumer and multiplied by the represented `x_n`. The exact pole is retained as `alpha*p_n*sum_m p_m*x_m`. All output `z_n` values are freshly evaluated by the certified v14.238 bulk path; each point radius is below `1e-39`.

Five complete rows per sector—at the first Near row, an interior Near row, the final Near row, an interior Middle row and the final Middle row—are independently summed over all 256000 compact inputs using the same directed reciprocal points and agree exactly with the convolution outputs. Fifty-four additional small rectangular parity/index identities pass.

## Directed physical and arithmetic charges

The physical diagonal interval is propagated coordinate by coordinate before the final `l2` sum. It dominates the completed error budget.

For the offdiagonal and pole parameters, the inherited bounds are `|delta c|<=2e-41`, front `|delta z_m|<=1e-38`, remote `|delta z|<=1e-39`, and the v14.238 directed pole errors. Since same-parity offdiagonal gaps are at least two, `|1/(n-m)|<=1/2`, while `|1/(n+m)|<=1/2`; `|z_n|<8`, `|z_m|<11`, `|c|<1`, and `|p|<2`. The complete per-row scalar/pole perturbation is below `1e-38 ||x||_1`; this gate deliberately retains the much looser `1e-34 ||x||_1` envelope. Multiplication by `sqrt_upper(384000)` gives the displayed global charge.

Each of the two reciprocal channels is rounded downward at 256 bits. With `|z_n|+|z_m|<19`, the uniform row charge is `20*2^-256 ||x||_1`; the final 256-bit row floor is charged separately. Exact rational operations precede every outward square root.

| Sector | Diagonal interval charge | Offdiagonal/pole parameter charge | Complete compact Near/Middle action error upper |
|---|---:|---:|---:|
| even-v | 1.608227490075531e-14 | 7.670409487248876e-19 | 1.6083041941704035e-14 |
| odd-v | 1.6068215232550008e-14 | 1.5164475629484778e-20 | 1.6068230397025636e-14 |

The reciprocal and final-row rounding charges are below `1.33e-60` and `5.36e-75`; complete exact rationals are in the payloads. Both total charges are below the unchanged shared `3e-11` output-arithmetic target.

## Evaluated outputs and guarded freeze

Producer: `research-notes/suzuki_infinite_seed_compact_near_middle_action.py`.

Certificate namespace: `research-notes/payloads/infinite_seed_compact_near_middle_v14_285/`.

| Sector | Binary rows | Binary bytes | Binary SHA256 | JSON SHA256 |
|---|---:|---:|---|---|
| even-v | 384000 | 11520000 | `ed4f9866247c53e4059c9872adfa4d6107af3b8a16db215a6d1c14640f89bc68` | `763cb66a0b447beeb1a0b2314f2c60c31238d54c96b89dff42ef92ad6dd2f924` |
| odd-v | 384000 | 11520000 | `a3f17e99ad87819c28b8e6c328cbf446c8604e4bb72a8509dce3cf2c0432da55` | `5a34f83f6079894d8c0a49100e2075d58c96b8ab6292a480ec19f70cfcc5860a` |

Each row is a signed 30-byte integer at 256 fractional bits. At publication the two small certificates are committed and bind the locally evaluated binary SHA256/length values above. The binaries themselves are not yet called durably frozen. The additive scoped workflow `.github/workflows/suzuki-infinite-seed-compact-near-middle-action.yml` reconstructs the immutable actual256 snapshot independently for each sector, recomputes every row, byte-compares each certificate, verifies each binary against its bound hash/length, uploads both exact witnesses, then uses a guarded normal nonforced push to add only the two binaries. CI/archive receipt is pending at publication.

## Scope

This closes the **compact-component** Near/Middle output-row obligation through `4R`. It does not include the infinite diagonal seed-tail action on those rows. It does not compose compact and infinite-tail actions, evaluate the whole represented residual, establish stationary acceptance, or close the infinite capacity tail. Every such flag remains false in both frozen certificates. The v14.278 Sandbox Region-1 far calculation is not substituted for a committed whole `D*y` certificate.

## HANDOFF — External Audit and Sandbox

External Audit: independently replay both complete row buffers; verify the Toeplitz/Hankel signs from the displayed kernel identity, diagonal exclusion/inclusion, five full 256000-input row checks, and each physical-error charge.

Sandbox: v14.285 supplies the frozen compact Near/Middle component for later composition. Continue the separate actual infinite `D*y` close/pole and Regions 2–3 work. Do not add this compact component twice when composing the whole action.

## Next/open

The next actionable gate is the committed actual infinite `D*y` evaluator: Region-1 close rows and pole, Regions 2–3, and its physical error budget. After that, compose it once with v14.277/v14.283 compact Far and v14.285 compact Near/Middle, then evaluate the full represented residual. Signed stationary pairing and infinite capacity closure remain open.
