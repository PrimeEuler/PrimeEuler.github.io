"""XI FEASIBILITY (2026-10-22): sandbox return to the v14.700 HANDOFF.
Question: can ONE realistic rotor resolve beta1 and beta2 well enough
to measure Xi = (MlR/q)(beta2/beta1) = (1 - R Phi''/Phi')/3?
Apparatus/null-test study only. G appears ONLY to size engineering
signals (calibration-only, per the handoff constraint); no value of
G is derived or predicted.
Design anchors (program's own bench, v14.626-631 + seated balance):
source M_s = 2 kg at R = 0.10 m, position-modulated; rotor = solid
axisymmetric paraboloid pair (the V4/seated shape), radius a = 0.05 m,
height h = 0.05 m each, aluminium; deliberate axial unbalance
l = 1.0 mm (calibrated trim) supplies the rank-1 dipole moment."""
import numpy as np

G = 6.674e-11          # calibration-only: engineering signal sizes
hbar = 1.054571817e-34

# ---------- rotor geometry: paraboloid pair, exact integrals ----------
# Solid paraboloid (apex at origin, axis z, height h, rim radius a):
# A1 = int z^2 dm (about centre plane), B1 = int x^2 dm, via z-slicing:
# at height z the disc radius is a*sqrt(z/h), dm = rho*pi*a^2/h * z dz... use numeric.
rho_al = 2700.0
a, h = 0.05, 0.05
zs = np.linspace(0, h, 200001)
r2 = a*a*zs/h                       # disc radius^2 at z
dm_dz = rho_al*np.pi*r2             # mass per unit z
M1 = np.trapz(dm_dz, zs)
# moments of ONE paraboloid about its own apex plane, axis through apex:
A1 = np.trapz(zs**2*dm_dz, zs)                  # int z^2 dm (about apex plane z=0)
B1 = np.trapz(0.25*r2*dm_dz, zs)                # int x^2 dm (disc: <x^2> = r^2/4)
zcm = np.trapz(zs*dm_dz, zs)/M1
# pair: two paraboloids apex-to-apex at z=0 (bicone seating), COM at 0.
# A (about the centre plane, z along axis) and B for the pair:
A = 2*A1
B = 2*B1
Mrot = 2*M1
I_kin = A + B          # perpendicular moment (v14.700 S5)
q = A - B              # quadrupole coefficient (v14.700 S5)
print(f'ONE paraboloid: M = {M1:.4f} kg, z_cm from apex = {zcm*1000:.2f} mm')
print(f'PAIR: M_rot = {Mrot:.4f} kg   A = {A:.4e}   B = {B:.4e} kg m^2')
print(f'  I_kin = A+B = {I_kin:.4e}   q = A-B = {q:.4e}   q/I_kin = {q/I_kin:.3f}  (slender limit would be 1)')

# ---------- source field and couplings (calibration-only G) ----------
Ms, R = 2.0, 0.10
Phi1 = G*Ms/R**2            # Phi'(R)  [s^-2 * m = m/s^2]
Phi2 = -2*G*Ms/R**3         # Phi''(R)
l = 1.0e-3                  # deliberate COM offset (m)
Ml = Mrot*l
beta1 = (2*I_kin/hbar**2)*Ml*Phi1
beta2 = (2*I_kin/hbar**2)*(q/3)*(Phi1/R - Phi2)
Xi = (Ml*R/q)*(beta2/beta1)
print(f'\nsource: Phi\' = {Phi1:.3e} m/s^2,  Phi\'\' = {Phi2:.3e} s^-2,  gradient combo Phi\'/R - Phi\'\' = {Phi1/R - Phi2:.3e} s^-2')
print(f'beta1 = {beta1:.3e}   beta2 = {beta2:.3e}   Xi reconstructed = {Xi:.6f}  (Newtonian target: 1)')

# ---------- the quantum-readout reality check ----------
B_rot_Hz = (hbar**2/(2*I_kin))/6.62607015e-34   # rotational constant in Hz
print(f'\nrotational constant hbar^2/2I = {B_rot_Hz:.2e} Hz: quantum level spectroscopy')
print('of a macro rotor is not a readout. The observables are the CLASSICAL limits:')
# classical torques at unit angular factors
tau1 = Ml*Phi1                       # rank-1 (pendulum) torque amplitude, source part
tau2 = q*(Phi1/R - Phi2)/3*3        # rank-2 torque scale: q * (gradient combo) (angular factor O(1))
tau2 = q*(Phi1/R - Phi2)
print(f'  rank-1 source torque  Ml*Phi\'        = {tau1:.3e} N m')
print(f'  rank-2 source torque  q*(Phi\'/R-Phi\'\') = {tau2:.3e} N m')
print(f'  torsion-balance noise floors (state of art): 1e-15 .. 1e-17 N m/sqrt(Hz)')
print(f'  -> both channels sit {np.log10(tau1/1e-15):.0f}-{np.log10(tau2/1e-15):.0f} orders above a 1e-15 floor. NOT readout-limited.')

# ---------- Part 2: backgrounds and the Xi error budget ----------
print('\n=== backgrounds ===')
g = 9.81
tau1_earth = Ml*g
print(f'rank-1 Earth torque through the same unbalance: {tau1_earth:.3e} N m '
      f'({tau1_earth/tau1:.1e} x the source term; DC, removed by source modulation)')
for tilt in (1e-9, 1e-10):
    app = g*tilt
    print(f'  tilt noise {tilt:.0e} rad at f_mod -> apparent Phi\' noise {app:.2e} m/s^2/sqrt(Hz) '
          f'= {app/Phi1:.2f} x source Phi\'; 1e4 s lock-in -> beta1 to ~{app/Phi1/100:.1%}')
grad_earth = 3.1e-6
print(f'rank-2: Earth gradient {grad_earth:.1e} s^-2 vs source combo {Phi1/R - Phi2:.1e} s^-2 '
      f'({grad_earth/(Phi1/R - Phi2):.1f} x, static; source is modulated, gradient tensor signature rotates with source)')
tau_person = q*2*G*70/3.0**3
print(f'  70 kg person at 3 m: gradient torque {tau_person:.1e} N m ({tau2/tau_person:.0f} x below source torque)')

print('\n=== Xi error budget (relative, 1 sigma) ===')
terms = {
  'unbalance l calibration (5 um on 1 mm)': 0.005,
  'quadrupole q calibration (geometry + known-gradient cal)': 0.005,
  'source distance R (0.01 mm on 100 mm)': 0.0001,
  'angular geometry factor g2 (source-rotation cal)': 0.002,
  'stiffness ratio k2/k1 (rank-1 tilt statistics, 1e4 s)': 0.007,
  'rank-2 systematics (source position, Earth-gradient drift)': 0.003,
}
tot = np.sqrt(sum(v*v for v in terms.values()))
for k, v in terms.items(): print(f'  {k:58s} {v:.2%}')
print(f'  {"TOTAL":58s} {tot:.2%}')
print(f'\nXi = 1 (Newton) distinguishable from Xi = (p+2)/3 at |dp| ~ {3*tot:.3f}.')
print('VERDICT: POSITIVE as an apparatus/null-test study. Both channels are')
print('4-6 orders above torque readout floors; the measurement is won or lost')
print('on (i) sub-nrad tilt stability at the modulation frequency (rank-1')
print('channel, the design driver) and (ii) the unbalance/quadrupole')
print('calibrations. ~1% on Xi is a realistic bench target: a genuine')
print('single-device two-channel null test of the 1/R slope at 10 cm.')
print('NEGATIVE sub-verdicts: quantum level spectroscopy of the macro rotor')
print('(1e-33 Hz spacings) is not a readout; and this bench does not compete')
print('with dedicated inverse-square torsion balances on p itself. G entered')
print('only to size signals (calibration-only); nothing here derives G, and')
print('Xi=1 is the standard-gradiometry expectation (v14.700 novelty-negative).')
