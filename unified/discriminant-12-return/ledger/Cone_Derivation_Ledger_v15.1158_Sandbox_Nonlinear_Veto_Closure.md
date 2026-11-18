# Cone Derivation Ledger v15.1158 — Sandbox: the nonlinear K4 corner (1) — the Z2 veto is all-orders, not a truncation artifact

**Deposit type:** Sandbox exploration, independently checkable.
Item 3 of Jeremy's 2026-11-18 gravity-thread tasking, first
half: the full nonlinear K4 reduction (v15.993 [O]) and the
ADM/boundary reduction with backreaction (open from
v15.1058). Producer re-executed at staging, exit 0 (9 checks,
all PASS). The scalar/vector ADM constraint completion
(v15.1085's next gate) is the corner's second half, filed
separately.

Question: v15.998's reflection veto (isotropic K4 cannot
correlate the two Maxwell polarizations; the odd-y vertex
O4 = (a_x^dag)^3 a_y has zero coefficient) was proved in the
reduced system at archived truncation, and v15.1057 flags
its J expansion as quartic-truncation only. Does the full
nonlinear theory evade it? No — the rule is a symmetry of
the full action, in three exact steps. (1) The K4 elastic
invariant is a scalar function of the TT strain block
[[b, c], [c, -b]] (trace 0, determinant -(b^2+c^2),
eigenvalues +-sqrt(b^2+c^2)), so at every order
J = f(b^2+c^2) and the mixed Hessian is structurally
d2J/dbdc = 4 bc f''(b^2+c^2) for any f (verified for a
general polynomial in the argument). On the filed series
through r^6: bc[-64/9 + (896/45)(b^2+c^2)] — the r^6 term
corrects the coefficient, never the selection rule; the
Hessian is zero on every reflection-symmetric background
(c = 0) and odd under c -> -c at all orders. (2) Under P_y
(v15.1057 Gate 867), every odd-y-count monomial is odd
(enumerated to degree 8) and O4 has y-count 1, so a
P_y-invariant effective action gives it zero coefficient
at every order. (3) Backreaction stays in the symmetric
sector: the full action (EH + solid invariants + Maxwell
F^2) is P_y-invariant and the constraints/boundary terms
are built from the same even scalars; v15.1058's mechanism
is the algebraic core — the self-generated cross source
is odd in the y-amplitude (V_c,2 = -3QU cos(4t)) but its
integrated contribution V G V is even (proportional to
U^2), verified identically. Gates 867/871 stated this in
the reduced system; this entry promotes the invariant
side to all orders.

Verdict: the nonlinear corner does NOT evade the veto.
The mixer becomes nonzero only with parity-odd INPUT — a
populated cross state (v15.1058), a stipulated C != 0
background (v15.1057), or parity-odd boundary data — which
are inputs, not derivations; and even then the output
still owes the q2 matrix-element match (T^dag T = 2E,
all-shell weight sqrt((L+1)/4)) no entry has produced.
The corner is closed as a veto-evasion route; what
remains inside it is response theory in a
broken-symmetry state, a different and lesser claim. No
selector claimed; G_derived = false. Lane A files
untouched.

**Payload:** `payloads/nonlinear_veto_closure_v15_1158/` — Nonlinear_Veto_Closure.md `93c3b4e00efb0e8b9362d70706411c21ea720084c87802e00636cc124a646450`, nonlinear_veto_closure.py `57ba9af4dd24d1d50a608d850ddbc33371e1ad23ec47c4c684ae006572f7a6f6`.
