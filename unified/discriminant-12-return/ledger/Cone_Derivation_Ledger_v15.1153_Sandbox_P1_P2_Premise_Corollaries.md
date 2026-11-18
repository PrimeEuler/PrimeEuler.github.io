# Cone Derivation Ledger v15.1153 — Sandbox: P1 and P2 tested — the weld's standing predictions are premise corollaries; the second-fixed-point hunt is closed

**Deposit type:** Sandbox exploration, independently checkable.
Tasked by Jeremy 2026-11-18 (gravity-thread remaining topics,
item 1): run down P1 and P2, the weld's falsifiable predictions,
standing untested since v14.910 (2026-10-26). Producers
re-executed at staging, both exit 0 (19 checks, all PASS).

**P1 (k-factor member scale h = 1/2 at every k): PREMISE
COROLLARY.** Counting form exact: on the half-grid the
product-counting function satisfies D_k^{1/2}(N) = D_k^1(2^k N)
identically (k = 1..4), so the radial shift is -k log 2 iff every
factor carries the sector spacing, and 0 on the EM grid. The
anomaly A_k(n) = D_k(2^k n) - 2^k D_k(n) carries the predicted
leading coefficient 2^k k log 2/(k-2)!: at k = 2 it is 4n log 4
(fit 5.5375 vs 5.5452 at n = 2000 — v14.857's Delta_4, the
original weld's own anomaly); at k = 3, 4 the fits decrease
monotonically toward prediction (1/log-extrapolated intercepts
16.80 vs 16.64 at k = 3; 19.5 vs 22.2 at k = 4; log-slow as
filed). Geometry form: NO shift exists — the k-factor Hessian
curvature R_k = -k(k-2)/(4P) (v14.820) is a power law in P,
rescaling by lambda^{-k} under x -> lambda x, so the geometry
defines no radial origin at any k (k = 2 the flat member):
v14.856's grid-blindness at every k. P1's content is therefore
exactly equivalent to the weld premise (member scale = sector
property); not falsified at any k, and not independently
confirmable from inside the record.

**P2 (W2 cutoff 4n): PREMISE COROLLARY.** The filed package
reproduces exactly: shell(12) = 113 (v14.858);
W2(4n)/W2(n) = 63.97 at n = 16000 (-> 64);
Delta_64/(n^2 ln n) = -9.88 (-> -12, the filed crawl). The
alternative is real and cleanly separated: the anomaly
log-coefficient for cutoff multiplier c is -c^2(c-1)/4, so a
seat Casimir built on the dyon product grid would give the
package (16n, 4096, -960) — computed Delta_4096/(n^2 ln n)
= -818.7 at n = 16000, nowhere near the filed package. What
selects 4n is that the seat Casimir counts states, states
live on the h-grid (2D density 1/h^2 = 4 at h = 1/2) — the
weld premise (h = 2q, node = state) itself. Every gravity-
side seat-Casimir derivation in the record (v14.858, v14.989)
uses the same integer-contact node set, so none is
independent in the sense P2 demanded. Not falsified; not
independently confirmable.

**Joint consequence:** the second-fixed-point hunt is
definitively closed. Both predictions are corollaries of
the premise, so no computation of their form can score the
weld an independent hit. The weld remains a one-application
dictionary (the Suzuki /4) whose premise — node = state —
is untested by anything in the current record; testing it
requires a genuinely new independent spectrum or counting
derivation (a k-sector operator diagonal built as Suzuki's
was at k = 2, or the K4 action's own mode spectrum), a
construction project, not a check. That is the same seam
as item 2 of the 2026-11-18 tasking (the pair-side hbar-Z /
radial-flux identification). No selector claimed;
G_derived = false; psi_selected = false. Lane A's Suzuki
R4 certification files untouched.

**Payload:** `payloads/p1_p2_premise_corollaries_v15_1153/` — P1_P2_Verdict.md `5a2d2cf2b2b2cb8d96a2cc89cf1ca3e452cdb1efd8d5acdc488890c9fc3621d9`, p1_kfactor.py `43b59cba9ef3307706ebb7918e2ca76d12c16395d3bda85354a496415ce2271b`, p2_w2_packages.py `04f2ddd88d78e187f8e972c349f935236196ebd3066a3c657b71f93482b4f7a3`.
