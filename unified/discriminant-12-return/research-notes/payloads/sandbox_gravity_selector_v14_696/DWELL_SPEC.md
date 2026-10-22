# Dwell computation — spec (staged 2026-10-22, NOT run, NOT ledgered)

Prepared after the gravity-selector arc closed structurally
(RESULTS.md, final sections): the seat is at −1/2, the balance at
+1/2, the outstanding initial condition is the point at 0, and
G_derived remains false. In the main chat's own closing inventory,
one item was named as "a well-posed computation nobody has run":
the merged dwell claim. This spec fixes what that computation is,
so a one-line go can execute it without further design work.

## The claim to settle

DWELL (merged form): a census of the frame's phase-orbit states
weighted by DWELL TIME (orbital period) rather than by state count
is dominated by the near-separatrix states, and its effective log
equals the separatrix log K(e) — with e set by each state's own
Runge–Lenz / angular-momentum split on its shell, not inserted by
hand.

## What is already known (do not re-run)

- Identification [D, RESULTS.md]: on the bicone shell
  e² = A²/(L²+A²), so 1−e² is the angular share; e = 1 is the
  radial orbit L = 0.
- Separatrix machine [D]: K(e) ~ ½ ln(16/(1−e²)); ψ would need
  1−e² = 7.05e-39 inserted by hand — a relocation, not a selection,
  unless dwell supplies the weight.
- Frame-only fill [N, RESULTS.md]: quantizing the share (closest
  orbit on shell n carries (3/2)²/n²) and dwell-weighting shells
  to J = 42 returned K ≈ 4.2–4.7 — ln J scale. That computation
  weighted SHELLS. It did not do the state-level census below,
  and it did not test domination (what fraction of the total
  dwell weight sits in the top decile of e).

## The computation (state-level, pre-registered)

1. States: shells j = 1/2 … J (run J = 42 to match the earlier
   fills, then J = 200 as a scaling check), states (j, m) with
   the frame's Langer-shifted labels (j+½, m+½).
2. Per state: angular share s = L²/(L²+A²) from the shell split;
   e = sqrt(1−s); separatrix log K_state = ½ ln(16/s), using the
   exact elliptic K(e) (scipy.special.ellipk) where e is not
   asymptotically close to 1, the asymptotic form only as a
   cross-check.
3. Dwell weight: w_state ∝ period ∝ K_state (the separatrix
   period divergence is the dwell mechanism — this is the one
   modeling input, stated here in advance).
4. Outputs, all reported regardless of outcome:
   - effective log L_eff = Σ w·K / Σ w (dwell-weighted census log);
   - domination fraction: share of Σw carried by the top 10% of
     states ranked by e;
   - scaling of both with J (42 vs 200): does L_eff grow like
     ln J, like (ln J)², or saturate?
5. Verdict criteria, fixed in advance:
   - POSITIVE (dwell is a selection mechanism): domination
     fraction → 1 as J grows AND L_eff outgrows ln J.
   - NEGATIVE (dwell is bookkeeping): L_eff stays O(ln J) or the
     weight stays spread — the merged claim joins the frame-only
     fill as a clean negative, and the arc's closing inventory
     loses its last unrun computation.
   Prior, stated honestly: the frame-only result points negative.
   The value of running it is closure, not expectation of a hit.

## Non-goals / guardrails

- No cosmic version in this run: the inflation closed form
  K = N + ½ ln(16/(1−e²)_i) already stands in RESULTS.md; this
  computation is frame-internal only.
- Sandbox only; nothing ledgered, nothing staged for Lane A —
  this does not touch the far gate (v14.585 actions 3–4), which
  keeps right of way.
- Producer to be written as `dwell_census.py` beside RESULTS.md,
  scipy only, minutes-scale; report numbers first, interpretation
  second, per house rule.
