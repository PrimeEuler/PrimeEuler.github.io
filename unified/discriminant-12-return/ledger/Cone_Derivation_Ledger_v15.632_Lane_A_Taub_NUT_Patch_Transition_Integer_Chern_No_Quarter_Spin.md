# Cone Derivation Ledger v15.632 — Lane A: Taub–NUT patch overlap selects integer monopole winding, not quarter-valued SU2 spin

**Date:** 2026-11-10. **Parents:** v14.731 gravitational dyon quarter product, independent Audit Round 338 v14.732, v14.913 gravitational lattice provenance clarification, v15.135 EM and quarter-only classes, v15.625–630 geometric Casimir and ordinary SU2 distinction, v15.631 explicit four-holonomy candidate and Misner-time Fourier label. **Status:** [D] exact patch transition, curvature/first-Chern winding and representation normalization; [O] independent gauge mechanism selecting the additional quarter-angular holonomy and a calibrated coupling. **Fresh prewrite live HEAD:** 8b71dd61af08629fc3cdbd89fc97aba3cfc930f8; v15.632 collision search empty. Additive only. Suzuki-quarter physical weld remains parked and frozen Suzuki production untouched.

## Gate 132 — exact global patching of the known Taub–NUT fibration

In the Taub–NUT regular patch conventions already recorded at v14.731, t_N=t+2l φ and t_S=t−2l φ (with t a length-coordinate, or t_phys=t/c). Their overlap has

**t_N−t_S=4l φ.**

An energy eigenmode has factor exp(−iEt/(ℏc)). Re-expressing that same mode in the north/south trivializations gives an overlap transition phase

**g_NS(φ)=exp(±i[4lE/(ℏc)]φ)=exp(±ikφ)**,

where the Misner period imposes **k:=4lE/(ℏc)∈Z**. The ± orientation depends on how the local wavefunction trivializations are defined; the integer magnitude of the winding is invariant. In the usual Dirac-monopole angular normalization (choosing the positive orientation), take

**A_N=(k/2)(1−cos θ)dφ,  A_S=−(k/2)(1+cos θ)dφ.**

Then **A_N−A_S=k dφ** and

**F=dA_N=dA_S=(k/2)sin θ dθ∧dφ,**
**(1/(2π))∫_{S²}F=k.**

Thus the angular bundle has an **integer first Chern number k**, not fractional k/4 winding. The induced monopole strength is s=k/2 in standard conventions, and the regular angular harmonics have j=|k|/2+n, n∈Z≥0. This reproduces the conventional half-integer/integer SU2 spin ladder and the v14.731 Poincaré angular-monopole term. At k=1: the product quantum is p=1/4, the pair-product square p²=1/16, but the minimum angular Casimir is j(j+1)=3/4, not the odd-quarter geometric C_geom(1/4)=5/16.

## Meaning for the separate geometric quarter-spin candidate

The formal quarter-shell spectrum and its Casimir character from v15.625–628 remain mathematically valid. v15.631 provides an explicit **chosen** four-twist U(1) angular carrier whose spectrum equals them. However, the **actual** north/south Taub–NUT patching yields e^(ikφ) and integral first Chern class; it does not supply an angular transition function e^(ikφ/4), nor does it select the ±i angular holonomy of the separate candidate. A fractional-winding map would fail to be an ordinary global U1 transition on this overlap for generic k, unless the base/gauge bundle and its covering structure were changed and physically justified. A proposed intertwiner sending the normalized Misner time momentum k to quarter angular shell j_geom=k/4 must therefore be stated as additional structure and checked against these exact patch equations; its absence is the present **precise obstruction**, not a disproof of all gravitational quantizations.

## Exact independent checks and audit

Companion archive `cone_holonomy_gates_128_132.zip` contains `reproduce.py` and `patch_check.py` (run successfully) and updated `REPORT.md`. `patch_check.py` verifies exact A_N−A_S=k, F_N=F_S, the curvature flux/(2π)=k, and the exact mismatch of standard minimum-angular and formal quarter Casimirs over k=1..7. No measured G or physical observable has been inserted. Parent v14.731 was independently audited by v14.732 and is **preserved**, not rederived or revised here.

**HANDOFF:** external-audit, gravity, sandbox; independently check patch phase sign/orientation, correct time-length versus physical-time factors of c, that integral c1 is integer k, standard angular monopole spectrum j=|k|/2+n, and the distinction between the pair-product quarter and a separate quarter-valued angular Casimir. Preserve Suzuki parked weld and all frozen far-tail material.

**Next meaningful gate:** specify an actual extended fibration or discrete gauge bundle with a nontrivial Z4 angular character, and test its compatibility with the existing Taub–NUT patching, global action, and physical excitations. Do not choose an independent quarter holonomy just to reproduce the desired result; require an independently fixed mechanism and an experimentally distinguishing response.
