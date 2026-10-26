"""SVT return part 4: assemble EH+matter scalar L2, Fourier-map (cos-mode
bookkeeping: d_z^n on a cos-field -> factor {1,-k,-k^2,k^3,k^4}), set E=0 gauge,
eliminate lapse Phi and shift B amplitudes via their (derivative-free) EOMs,
extract the reduced (psi, P) kinetic/gradient/mass structure."""
import sympy as sp
import pickle

a, adot, kappa, C, eta, k = sp.symbols('a adot kappa C eta k', positive=True)
Phi, B, psi, E, P = sp.symbols('Phi B psi E P')
psi_t, E_t, P_t = sp.symbols('psi_t E_t P_t')

Lm = sp.sympify(pickle.load(open('matter_scalar.pkl', 'rb'))['L2'])
Le = sp.sympify(pickle.load(open('eh_scalar.pkl', 'rb'))['L2'])

# real-space derivative symbols -> Fourier factors (cos-mode, averaged)
subs = {
    'Phi': Phi, 'psi': psi, 'Ezz': -k**2 * E, 'Bz': -k * B, 'Bzz': -k**2 * B,
    'psi_z': -k * psi, 'psi_zz': -k**2 * psi, 'psi_t': psi_t,
    'E_zzz': k**3 * E, 'E_zzzz': k**4 * E, 'E_zzt': -k**2 * E_t,
    'Pzz': -k**2 * P, 'Pzt': -k * P_t,
}
def fourier(expr):
    out = expr
    for name, val in subs.items():
        out = out.subs(sp.Symbol(name), val)
    return sp.expand(out)

Lf = fourier(Lm) + fourier(Le)
print("total Fourier L2 monomials:", len(Lf.args))
# gauge E = 0 (and E_t = 0)
Lf = sp.expand(Lf.subs({E: 0, E_t: 0}))
# auxiliary check: Phi and B appear without time derivatives
assert not Lf.has(sp.Symbol('Phi_t')) and not Lf.has(sp.Symbol('B_t'))
dPhi = sp.diff(Lf, Phi)
dB = sp.diff(Lf, B)
print("constraint eqs are linear in (Phi, B):",
      sp.Poly(dPhi, Phi, B).total_degree() <= 1, sp.Poly(dB, Phi, B).total_degree() <= 1)
sol = sp.solve([dPhi, dB], [Phi, B], dict=True)[0]
print("Phi* =", sp.simplify(sol[Phi]))
print("B*   =", sp.simplify(sol[B]))
Lred = sp.expand(Lf.subs(sol))
pickle.dump({'Lred': str(Lred), 'Phi_star': str(sol[Phi]), 'B_star': str(sol[B])},
            open('scalar_reduced.pkl', 'wb'))
# kinetic matrix in basis (psi, P): L = 1/2 [ psi_t, P_t ] K [psi_t, P_t]^T + ...
def coeff2(expr, x, y):
    return sp.expand(expr).coeff(x, 1).coeff(y, 1) if x != y else sp.expand(expr).coeff(x, 2)
Kpp = Lred.coeff(P_t, 2); Kss = Lred.coeff(psi_t, 2); Ksp = sp.expand(Lred).coeff(psi_t, 1).coeff(P_t, 1)
print("K(psi_t,psi_t) =", sp.simplify(Kss))
print("K(psi_t,P_t)   =", sp.simplify(Ksp))
print("K(P_t,P_t)     =", sp.simplify(Kpp))
print("saved scalar_reduced.pkl; total reduced monomials:", len(Lred.args))
