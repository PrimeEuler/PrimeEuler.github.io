# The nonlinear K4 corner, part 1 — the Z₂ veto is not a truncation artifact

Sandbox note (little Euler), 2026-11-18; item 3 of
Jeremy's 2026-11-18 tasking, first half (the full
nonlinear reduction and the ADM/boundary-with-
backreaction openings, v15.993 [O] and v15.1058's next
gate). Producer: `nonlinear_veto_closure.py` (sympy,
exact; all checks PASS). The scalar/vector ADM
constraint completion (v15.1085's next gate) is the
corner's second half and is filed separately.

## The question

v15.998's veto — isotropic K4 plus background cannot
correlate the two Maxwell polarizations into the
physical mixer; the odd-y vertex O4 = (a_x†)³a_y has
zero coefficient — was proved in the reduced system and
at the archived quadratic/quartic truncation. v15.1057
itself flags its J expansion as "quartic-truncation
only, not exact nonperturbatively." Does the full
nonlinear theory evade it?

## The closure, in three exact steps

1. **The invariant's argument decides everything.** The
   K4 elastic invariant is a scalar function of the TT
   strain block [[b, c], [c, −b]], whose trace is 0 and
   whose determinant is −(b²+c²) (eigenvalues
   ±√(b²+c²)). Every scalar invariant of the block —
   hence the isotropic solid's action, at every order —
   is a function of b²+c² alone: J = f(b²+c²). Its mixed
   Hessian is then structurally

       ∂²J/∂b∂c = 4bc·f″(b²+c²),

   for *any* f (verified symbolically for a general
   quartic polynomial in the argument). On the filed
   series (f through r⁶) this gives
   bc·[−64/9 + (896/45)(b²+c²)]: the r⁶ term v15.1057
   worried about corrects the *coefficient* — it is
   still proportional to bc, still zero on every
   reflection-symmetric background (c = 0), still odd
   under c → −c. Nonlinearity changes the size of the
   conditional response; it cannot change its selection
   rule, because the rule comes from the argument of f,
   not from the truncation of f.
2. **Monomial parity is order-independent.** Under P_y
   (v15.1057 Gate 867: A_y → −A_y, c → −c; A_x, b
   invariant), every monomial with odd y-count is odd —
   enumerated to degree 8 — and O4 has y-count 1. A
   P_y-invariant effective action therefore assigns it
   coefficient zero at *every* order, not just the
   orders so far expanded.
3. **Backreaction and self-sourcing stay inside the
   symmetric sector.** The full action (EH + solid
   invariants + Maxwell F²) is P_y-invariant; the ADM
   constraints and boundary terms are built from the
   same reflection-even scalars, so with
   reflection-symmetric data (background, state,
   boundary conditions) their solutions are
   reflection-even. v15.1058's mechanism is the
   algebraic core: the self-generated cross source is
   odd in the y-amplitude (V_c,2 = −3QU cos 4t), but
   integrating out the cross mode contributes V·G·V,
   which is even (∝ U²) — verified identically. Gravity
   stated this in the reduced system (Gates 867, 871);
   steps 1–2 promote the invariant side to all orders.

## Verdict and what remains open

**The nonlinear corner does not evade the veto.** The
full nonlinear K4 reduction, the ADM/boundary reduction
with backreaction, and graviton-exchange effective
vertices all inherit the same reflection selection rule,
because the rule is a symmetry of the full action, not
an artifact of linearization or truncation. The only
way the mixer becomes nonzero is parity-odd *input* —
a populated cross state (v15.1058's conditional drive),
a stipulated C ≠ 0 background (v15.1057's
susceptibility), or parity-odd boundary data. Those are
inputs, not derivations; and even granted one, the
output still owes the q2 matrix-element match
(T†T = 2E with the all-shell weight √((L+1)/4)) that no
entry has produced. The corner is therefore closed as a
veto-evasion route; what remains open inside it is
response theory in a broken-symmetry state, which is a
different and lesser claim.

Flags: veto = ALL_ORDERS (symmetry of the full action);
nonlinear_evasion = EXCLUDED for symmetric data;
parity_odd_input = REQUIRED for any mixer;
q2_matrix_match = STILL_OWED by any future positive;
G_derived = false; psi_selected = false.
