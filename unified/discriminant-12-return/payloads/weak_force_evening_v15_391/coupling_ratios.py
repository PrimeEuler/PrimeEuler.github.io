"""
Coupling-structure constants of the completed frame (2026-11-04,
sandbox). In the spirit of the acceleration-parabola coupling
experiments (drive x reaction; the rotor duck test): those never
derived a coupling constant's VALUE -- every one imported it (e^2 in
tau_0, g in beta) -- but they produced parameter-free IDENTITIES and
RATIOS between coupled quantities. The gauge analog: a vertex factor
is (one number g) x (a representation-theoretic matrix element). The
frame supplies all the matrix elements; what it can therefore give
for free are the coupling-STRUCTURE constants -- quadratic Casimirs
and Dynkin indices of its (p,q) irreps, and their ratios, which are
what real coupling measurements (jet rates, four-jet angles) see.

C2(p,q) = (p^2 + pq + q^2 + 3p + 3q)/3 ;  T(R) = C2(R) dim(R) / 8.
"""
from fractions import Fraction

def dim(pq):
    p, q = pq
    return (p + 1) * (q + 1) * (p + q + 2) // 2
def C2(pq):
    p, q = pq
    return Fraction(p * p + p * q + q * q + 3 * p + 3 * q, 3)
def T(pq):
    return C2(pq) * dim(pq) / 8

print("Frame irreps: Casimir C2 and Dynkin index T")
for pq, name in [((0, 0), "singlet"), ((1, 0), "quark 3"), ((0, 1), "antiquark 3bar"),
                 ((1, 1), "gluon 8"), ((2, 0), "sextet 6"), ((3, 0), "decuplet 10"),
                 ((2, 2), "27")]:
    print(f"  {str(pq):>7} {name:>15}: dim={dim(pq):>2}, C2={C2(pq)}, T={T(pq)}")
CF, CA, TF = C2((1, 0)), C2((1, 1)), T((1, 0))
print()
print(f"QCD coupling-structure constants from the frame's irreps alone:")
print(f"  C_F = {CF}  (quark Casimir -- sets quark radiation strength)")
print(f"  C_A = {CA}  (adjoint Casimir -- gluon self-coupling strength)")
print(f"  T_F = {TF}  (quark loop weight in the running of alpha_s)")
print(f"  C_A / C_F = {CA / CF}  -- the ratio four-jet angular analyses at LEP")
print(f"      measured, consistent with 9/4: gluons radiate 9/4 as strongly")
print(f"      as quarks, a number with no free parameter in it.")
print(f"  T_F / C_F = {TF / CF}")
print()
print("Weak side, same species (already in the record, pass 1): the")
print("charged-current vertex on the frame's j=1/2 doublet carries the")
print("J+ matrix element exactly 1 -- the vertex's shape is frame-fixed;")
print("only the overall g is not.")
print()
print("RESIDUE, stated plainly: the dynamics door compresses to one")
print("number per gauge factor (g1, g2, g3), plus the Higgs/Yukawa")
print("sector. Every coupling experiment in the record -- parabolas")
print("included -- imported its number; the geometry has only ever")
print("returned ratios, identities, and matrix elements.")
