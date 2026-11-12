#!/usr/bin/env python3
"""v15.835: one Fourier mode cannot certify localized remote-source arrival.

Exact discrete translation theorem and inverse reconstruction of a compact
C7 spatial bump at a separate receiver. This is a *Fourier localization*
control, NOT a spacetime causal Green-function or distant K4 waveform.
"""
import numpy as np
N=512
L=16.
dx=L/N
x=np.arange(N)*dx
R=1.
shift=4.
points=int(shift/dx)
def cutoff(y):
    z=(y+L/2)%L-L/2
    return np.where(np.abs(z)<R,(1-(z/R)**2)**8,0.)
source=cutoff(x)
far=np.roll(source,points)
assert abs(source[0]-1.)<1e-14
assert far[0]==0
F=np.fft.fft(source)/N
G=np.fft.fft(far)/N
m=3
expected=np.exp(-2j*np.pi*m*points/N)*F[m]
assert abs(G[m]-expected)<1e-14
assert abs(abs(G[m])-abs(F[m]))<1e-14
assert abs(G[m])>1e-6
receiver_single=G[m] # one mode is globally nonlocal
assert abs(receiver_single)>1e-6
reconstructed=np.fft.ifft(G*N).real
assert np.max(abs(reconstructed-far))<2e-14
assert abs(reconstructed[0])<2e-14
assert np.max(abs(G-np.exp(-2j*np.pi*np.arange(N)*points/N)*F))<2e-14
print("PASS translated compact source: single K mode magnitude unchanged")
print("receiver x=0 actual local source:",far[0])
print("single nonlocal Fourier coefficient:",G[m])
print("full inverse transform at receiver:",reconstructed[0])
print("NEGATIVE single-mode K4 optical output cannot establish remote retarded arrival")
