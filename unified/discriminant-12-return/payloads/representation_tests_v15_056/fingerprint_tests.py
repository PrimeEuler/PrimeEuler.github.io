"""Representation tests against the AM-triplet fingerprint (v14.996):
{background rho = C/a^2, w = -1/3} + {5 propagating dof: 2T + 2V + 1S} + {all sound speeds = 1}
+ {universal gap Qt^2 = 3k^2 + 4 with friction 3H} + {ghost-free}."""
import sympy as sp

print("ELASTIC FAMILY (v14.927 speeds): c_T^2 = 2 eta/3, c_L^2 = -1/3 + 8 eta/9")
eta = sp.symbols('eta', positive=True)
sol = sp.solve([sp.Eq(2 * eta / 3, 1), sp.Eq(-sp.Rational(1, 3) + 8 * eta / 9, 1)], [eta], dict=True)
print("   both speeds = 1  ->  eta =", sol, ": the fingerprint isolates the AM point eta = 3/2 uniquely in the family")
print("   (tensor mass check at the point: (8 eta/3) H^2 =", (8 * sp.Rational(3, 2) / 3), "H^2  = the record's 4 H^2 ✓)")

print("\nCURVED-TARGET SIGMA MODEL (labels on S^3 of radius l): target curvature gives phonons a mass")
print("   m^2 ~ (C/a^2)(1/l^2)  [kinetic coeff x strain^2 x target Riemann ~ 1/l^2]")
print("   gap ratio m^2 / (4/tau^2): with a^2 = tau^2/3 and kappa C = 1:  ratio = 3/(4 kappa l^2)")
print("   -> pure number ONLY if l is Planck-fixed by hand; l -> infinity recovers the flat triplet. FAIL at finite l.")

print("\nDOF LEDGER (propagating modes per sector; fingerprint = T2 V2 S1):")
rows = [
    ("AM triplet (reference)",        "2/2/1", "PASS - definition"),
    ("Stueckelberg / massive-grav phonons", "2/2/1", "PASS trivially - same fields, new notation"),
    ("General elastic medium",        "2/2/1", "PASS only at eta = 3/2 (= the AM point)"),
    ("Exponential scalar (v14.959)",  "2/0/1", "FAIL - no vector phonons; background-only match"),
    ("Perfect fluid w=-1/3, cs=1",    "2/0/1", "FAIL - vorticity non-propagating (decays, no phonon)"),
    ("k-essence / P(X) scalar",       "2/0/1", "FAIL - one scalar dof"),
    ("3-form field",                  "2/0/1", "FAIL - dual to a scalar"),
    ("Pair spinor chi (v15.014)",     "2/0/1*", "FAIL - tested: charge decouples; Q=0 tracker = scalar in dress"),
    ("f(R) effective source",         "2/0/2", "FAIL - scalaron adds a second scalar"),
    ("Vector triad (gauge-flation type)", "2/4+/2+", "FAIL - extra modes; known scalar-sector pathologies"),
    ("Cosmic-string network",         "active", "FAIL - incoherent active stress, no phonon eigen-spectrum"),
    ("Sigma model, S^3 target",       "2/2/1", "FAIL - dof pass, gap shifted by target curvature"),
]
for name, dof, verdict in rows:
    print(f"   {name:38s} dof {dof:7s} {verdict}")
