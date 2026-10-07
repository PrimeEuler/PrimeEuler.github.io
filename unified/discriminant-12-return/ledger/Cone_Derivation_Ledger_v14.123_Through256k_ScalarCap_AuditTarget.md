# Cone Derivation Ledger v14.123 — Through-256k Exact-Source Scalar-Cap Transport Audit Target

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [AUDIT TARGET] The public exact-vs-LDDD scalar envelopes survive every new mode on the complete residual octave 128k<n<=256k in both parities. No infinite-tail theorem is inferred here.  
**Parents:** v14.058–v14.059, v14.111, v14.115, v14.120, v14.122.  
**Collision check:** immediately before this write, live HEAD was `931b8b00757661720febc6e0d8d4e2df368bc8a3`; live ledger max was v14.122. No collision.

---

## 1. Producer and workflow

Producer:

[
	exttt{research-notes/suzuki_M256000_scalar_interval_incremental_arch200.py}
]

Workflow:

[
	exttt{.github/workflows/suzuki-M256000-scalar-interval-incremental-arch200.yml}
]

Successful run:

[
	exttt{37634983075}.
]

The replay checks every new mode

[
128000<nle256000
]

against the same public scalar envelopes independently promoted through 128k by v14.120.

---

## 2. even-v

Worst exact-vs-LDDD z error:

[
oxed{
max |Delta z|
=
5.875530481105451	imes10^{-39}
}
]

at

[
n=152511.
]

Worst diagonal error:

[
oxed{
max |Delta d|
=
1.1754870223039474	imes10^{-38}
}
]

at

[
n=167073.
]

Worst pole-vector error:

[
oxed{
max |Delta p|
=
1.1209095552695028	imes10^{-44}
}
]

at

[
n=169879.
]

All public caps pass.

---

## 3. odd-v

Worst exact-vs-LDDD z error:

[
oxed{
max |Delta z|
=
5.8768155657218075	imes10^{-39}
}
]

at

[
n=230412.
]

Worst diagonal error:

[
oxed{
max |Delta d|
=
1.1754889462519052	imes10^{-38}
}
]

at

[
n=206292.
]

Worst pole-vector error:

[
oxed{
max |Delta p|
=
5.604394042151852	imes10^{-45}
}
]

at

[
n=169202.
]

Again all public caps pass.

---

## 4. Public z-cap margin

The public exact-source envelope is

[
|Delta z|<5.88	imes10^{-39}.
]

Thus the tightest observed ratio is

[
rac{
5.8768155657218075
}{
5.88
}
=
0.999458ldots
]

so the cap remains valid but is genuinely tight.

No tighter internal cap is substituted for the promoted public theorem interface.

---

## 5. Consequence

The exact-source scalar uncertainty infrastructure now reaches across the entire finite residual octave required by the frozen-128k architecture:

[
128k<nle256k.
]

Therefore the remaining certification problem on this octave is no longer scalar-source transport. It is the parity-correlated finite-Schur/resolvent calculation itself.

For the genuinely separated tail,

[
nge256k,
]

v14.118 supplies the closed K=10 signed-moment residual formula.

---

## 6. Verdict

[
oxed{
	ext{All public exact-source scalar caps survive through }256k.
}
]

This entry proposes promotion of that finite statement only.

---

HANDOFF
target: external-audit
type: through-256k-scalar-cap-audit
parent: v14.123
status: open
action: Independently rerun the incremental arch-200 scalar interval audit on every 128k<n<=256k mode in both parities. Verify the maxima and mode indices above against the already-promoted public caps. If all checks reproduce, promote through-256k scalar-cap transport.
deliverable: theorem-or-obstruction
constraints: Do not infer the infinite-tail sign. Preserve the public 5.88e-39 z cap rather than replacing it by a tighter internal maximum.
