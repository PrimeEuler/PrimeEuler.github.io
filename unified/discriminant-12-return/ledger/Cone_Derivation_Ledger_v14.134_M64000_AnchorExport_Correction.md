# Cone Derivation Ledger v14.134 — M64000 Protected-Anchor Export Bug Isolated and Fail-Closed Export Fix

**Date:** 2026-10-07  
**Track:** Lane A / no-twist Suzuki Xi scalar certification  
**Status:** [CORRECTION + OBSTRUCTION] The previously exported 64k protected-anchor artifacts are not the final LDDD protected matrices used by the certified M64000 producer. The finite K result itself is unaffected. The heuristic interception exporter is retired and replaced by an explicit final-anchor interface inside the producer with fail-closed self-consistency checks. Corrected replays are in progress.  
**Parents:** v14.120, v14.124–v14.133.  
**Fix commits:** producer `cf1a682e8f693c2c3bd05ce4288234a6d33a8bd6`; workflow `4e0ea5cf9f8892026c692f56359178f192e7f72f`.  
**Corrected replay:** `37659896312` (in progress at write time).  
**Collision check:** immediately before this write, live HEAD was `4e0ea5cf9f8892026c692f56359178f192e7f72f`; live ledger max was v14.133. No collision.

---

## 1. What failed

The first anchor-export workflow attempted to recover the final reduced data by monkeypatching

[
	exttt{dd_matrix_to_mp}
]

and then selecting the first captured matrices by shape:

[
6	imes6,qquad6	imes1,qquad1	imes1.
]

Those artifacts were internally consistent as matrices, but they were **not** the final protected LDDD objects used by the producer's own

[
K=h+b^*S^{-1}b.
]

This was detected before any theorem use by directly reconstructing the anchor scalar.

### even-v

The old artifact gives

[
h+b^*S^{-1}b
=
8.7807820378812117511	imes10^{-7},
]

whereas the same producer run reports

[
K_{m total}
=
8.8076337216742431370	imes10^{-7}.
]

Its exported matrix also has

[
lambda_{min}(S_{m old,artifact})
approx
-1.01	imes10^{-22},
]

while the producer itself reports the true final protected minimum

[
lambda_{min}(S)
=
5.66572498201128	imes10^{-30}>0.
]

### odd-v

The old artifact reconstructs

[
8.7980235467973339864	imes10^{-7},
]

instead of the producer's

[
8.8067153720271120085	imes10^{-7}.
]

Likewise its matrix minimum is (sim3.84	imes10^{-21}), not the producer's final

[
1.42821375294745	imes10^{-26}.
]

Therefore the old exported anchor files are withdrawn as consumers.

---

## 2. What is **not** affected

The audited M64000 finite-Schur computation is unchanged.

Inside the original producer, the final LDDD matrices are formed explicitly and the reported quantities

[
K_{m complement},quad
K_{m protected},quad
K_{m total},quad
lambda_{min}(S)
]

are computed directly from those final objects.

The defect is solely in the later workflow-side attempt to rediscover those objects heuristically.

Thus no promoted finite theorem or v14.120 audit statement is withdrawn.

---

## 3. Correct export interface

The producer now supports

[
	exttt{one(sector, export_anchor=True)}
]

and exports the exact final objects **at the point where they are used**:

[
S,qquad b,qquad h,qquad S^{-1}b.
]

The workflow no longer intercepts conversion calls.

It consumes the producer's named (	exttt{anchor_export}) payload and checks, in multiprecision,

[
oxed{
|K_{m reconstructed}-K_{m total}|<10^{-60}
}
]

and

[
oxed{
|lambda_{min}(S_{m exported})-lambda_{min}(S_{m producer})|
<10^{-45}.
}
]

If either check fails, the workflow aborts.

---

## 4. Consequence for the v14.130/v14.132 gate

The normalized protected formula

[
Lambda_parallel
=
u^*G(I-G)^{-1}u
]

and Sandbox's paired bound remain exact and unaffected.

Only their numerical evaluation must wait for the corrected final anchor.

The preliminary high-precision transport run `37658776275`, which consumed the withdrawn old artifacts, is diagnostic-invalid and must not be used downstream.

---

## 5. Verdict

[
oxed{
	ext{Old 64k anchor artifacts: WITHDRAWN.}
}
]

[
oxed{
	ext{M64000 finite K theorem input: UNAFFECTED.}
}
]

[
oxed{
	ext{Correct explicit anchor export: replaying fail-closed.}
}
]

---

HANDOFF
target: external-audit, sandbox
type: anchor-export-correction
parent: v14.134
status: open
action: Do not consume the old M64000 anchor artifacts or high-precision transport run 37658776275. When corrected replay 37659896312 completes, verify the two explicit self-consistency checks, then use the corrected anchor with v14.130/v14.132.
deliverable: verification-or-obstruction
constraints: No heuristic matrix capture by shape; only the producer's explicit final anchor payload is admissible.
