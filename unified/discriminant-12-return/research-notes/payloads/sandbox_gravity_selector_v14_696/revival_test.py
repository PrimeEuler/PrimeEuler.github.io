"""RYDBERG REVIVALS (2026-10-22): packet on the cone-derived spectrum
E_n = -1/(2n^2) (v14.680 forced form+prefactor). T_cl = 2 pi nbar^3;
leading revival T_rev = (4 pi/3) nbar^4; discrete-difference time
T_disc = 4 pi / |D2 E(nbar)| from the ladder's own second difference;
packet-averaged n^4 law <n^4>/nbar^4 corrects the peak position."""
import numpy as np
for nbar, sig in ((40, 1.2), (40, 1.0), (60, 1.5)):
    ns = np.arange(nbar-15, nbar+16)
    w = np.exp(-(ns-nbar)**2/(2*sig**2)); w /= w.sum()
    E = -1.0/(2*ns**2)
    Tcl = 2*np.pi*nbar**3; Trev = (4*np.pi/3)*nbar**4
    E2 = -0.5*(1/(nbar-1)**2 - 2/nbar**2 + 1/(nbar+1)**2)
    Tdisc = 4*np.pi/abs(E2)
    avg4 = np.sum(w*ns**4)/nbar**4
    def A2(t):
        A = np.sum(w*np.exp(-1j*E*t)); return abs(A)**2
    ts = np.linspace(0.95*Trev, 1.05*Trev, 2001)
    vals = np.array([A2(t) for t in ts]); i = int(np.argmax(vals))
    print(f'nbar={nbar} sig={sig}: |A(T_cl)|^2={A2(Tcl):.3f} |A(2T_cl)|^2={A2(2*Tcl):.3f} '
          f'|A(T_rev/2)|^2={A2(Trev/2):.3f}')
    print(f'   revival peak |A|^2={vals[i]:.4f} at t/T_rev={ts[i]/Trev:.4f}; '
          f'T_disc/T_rev={Tdisc/Trev:.4f}; <n^4>/nbar^4={avg4:.4f}; |A(T_disc)|^2={A2(Tdisc):.4f}')
