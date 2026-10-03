#!/usr/bin/env python3
"""4-panel figure for the sieve-flow companion paper.

(a) Composite-indicator spectrum with zeta-zero cyclic frequencies.
(b) Mobius spectrum with zeta-zero cyclic frequencies.
(c) Sieve coverage: marginal and cumulative fraction by prime.
(d) Carrier strength R across arithmetic functions.

Requires: paper_spectra.npz and lpf_cover.npz from the sieve-renorm
sandbox runs (see research-notes/sieve_flow_R_pipeline_reproducer.py).
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

D = np.load(
    '/home/hatch/workspace/d12/lane_b/sandbox/runs/20261002-sieve-renorm/'
    'paper_spectra.npz')
fc, mc, fm, mm, G = D['fc'], D['mc'], D['fm'], D['mm'], D['G']
C = np.load(
    '/home/hatch/workspace/d12/lane_b/sandbox/runs/20261002-sieve-renorm/'
    'lpf_cover.npz')
primes, marg, cum = C['primes'], C['marg'], C['cum']
GC = G / (2 * np.pi)

fig, ax = plt.subplots(2, 2, figsize=(12, 9))

# (a) composite spectrum
a = ax[0, 0]
m = mc / mc.mean()
a.plot(fc, m, lw=0.4, color='#1a1a1a')
for g in GC:
    a.axvline(g, color='#c0392b', lw=0.8, alpha=0.7)
a.set_xlim(0, 6)
a.set_ylim(0, 12)
a.set_title('(a) Composite indicator spectrum', fontsize=11)
a.set_xlabel('cyclic frequency')
a.set_ylabel('|FFT| / mean')

# (b) mu spectrum
a = ax[0, 1]
m = mm / mm.mean()
a.plot(fm, m, lw=0.4, color='#1a1a1a')
for g in GC:
    a.axvline(g, color='#c0392b', lw=0.8, alpha=0.7)
a.set_xlim(0, 6)
a.set_ylim(0, 25)
a.set_title('(b) Mobius spectrum', fontsize=11)
a.set_xlabel('cyclic frequency')
a.set_ylabel('|FFT| / mean')

# (c) coverage
a = ax[1, 0]
a2 = a.twinx()
a.bar(range(len(primes)), marg * 100, color='#7fa7cf', width=1.0)
a2.plot(range(len(primes)), cum * 100, color='#c0392b', lw=1.5)
a.set_xlabel('prime index (2 to 997)')
a.set_ylabel('marginal %', color='#7fa7cf')
a2.set_ylabel('cumulative %', color='#c0392b')
a.set_title('(c) Sieve coverage by prime', fontsize=11)

# (d) R bar chart
a = ax[1, 1]
labels = ['composite', 'mu', 'lambda', 'phi/n', 'omega', 'mu^2']
Rs = [2.165, 3.776, 3.761, 1.676, 1.20, 1.24]
cols = ['#2c3e50'] * 3 + ['#7fa7cf'] * 3
a.barh(labels, Rs, color=cols)
a.axvline(1.0, color='#c0392b', ls='--', lw=1)
a.set_xlabel('R')
a.set_title('(d) Carrier strength R', fontsize=11)

plt.tight_layout()
plt.savefig('companion_sieve_flow_4panel.pdf')
plt.savefig('companion_sieve_flow_4panel.png', dpi=150)
print('figure done')
