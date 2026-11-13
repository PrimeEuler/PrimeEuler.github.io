"""
The null channel (2026-11-13, sandbox; addendum to the HJ
inversion v15.857). Jeremy's observation: the cone's 45
degree null ray IS c (metres per second as the geometry's
own slope); with power (joules per second) and velocity
(metres per second) as axis quantities, F = P/v is
sitting in the geometry. Checked here in the pair
coordinates of the record (c = 1 units; E^2 - p^2 = m^2
on the boost hyperbola labelled by GM = m; the bicone's
surface is the m = 0 case).

1. Null states are the cone's surface: m = 0 gives
   E = |p| identically -- E = pc is the surface equation,
   not an imported law. In (ct, x) axes the null ray
   x = ct is the 45 degree diagonal (the seat direction
   u = v of the pair plane) by the equal scaling of the
   axes: the conversion factor between the time and
   space axes is a slope of the geometry.
2. A photon stream of power P carries momentum at rate
   P/c (absorption): per quantum E = pc, so momentum
   flux = energy flux / c. Force from energy data alone:
   F = P/c, reflection doubles it. No trajectory, no
   family, nothing supplied but P.
3. The massive contrast: a massive state at rapidity
   psi has v = tanh(psi) c, and the bookkeeping identity
   F_parallel = (dE/dt)/v = P/(c tanh psi) depends on
   psi -- trajectory data. At fixed P the force runs
   over (P/c, infinity) as psi runs over (infinity, 0):
   on the massive shells the same power buys any force,
   which is the HJ verdict (v15.857) in one line. Only
   the null limit psi -> infinity pins v to the cone's
   slope and closes the channel.
"""
import sympy as sp

psi, P, c = sp.symbols("psi P c", positive=True)

# massive shell: E = m cosh psi, p = m sinh psi (units c=1, m symbolic)
m = sp.symbols("m", positive=True)
E = m * sp.cosh(psi)
p = m * sp.sinh(psi)
print(f"shell identity E^2 - p^2 = {sp.simplify(E**2 - p**2)} (= m^2, the GM label)")
v_over_c = sp.simplify(p / E)
print(f"v/c = p/E = {v_over_c} (tanh psi: trajectory data on the shell)")
F_massive = sp.simplify(P / (c * v_over_c))
print(f"F_parallel = P/v = {F_massive} -- depends on psi at fixed P")
print(f"null limit psi->oo: F -> {sp.limit(F_massive, psi, sp.oo)} = P/c "
      f"(v pinned to the cone's slope)")

# null channel from the surface equation alone
Eph, Pstream = sp.symbols("E_ph P_stream", positive=True)
p_ph = Eph / c                      # E = p c on the m = 0 surface
mom_rate = sp.simplify(Pstream / Eph * p_ph)
print(f"photon stream: momentum rate = (P/E_ph)*(E_ph/c) = {mom_rate} "
      f"-> F_absorb = P/c, F_reflect = 2P/c. Nothing supplied but P.")
print("""
Reading (assembled in the note): the conversion layer
(c as slope, hbar as circle) is geometry, and exactly on
the null channel the force-from-energy bookkeeping
closes with no family input. The massive channel keeps
its psi. Door assessment in the note.""")
