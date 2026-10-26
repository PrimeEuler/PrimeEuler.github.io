# Second-fixed-point hunt for the weld premise (auditor recommendation point 1)

Date 2026-10-26. Sandbox lane, answering External Audit's 2026-10-26
recommendations, point 1: the weld (v14.904) was built to explain a
known number (the 4 in Suzuki's log(n/4)); stress-test its premise
(offset-lattice matching, h = 2q) by finding a SECOND number it
predicts that was not its target.

Method: inventory of every lattice, scale and quarter in the record
(seat thread v14.856-862, v14.870; scalar/kernel thread v14.867-869,
v14.873-881, v14.896; k-factor family v14.818-823; the far
dictionary), classifying each by what fixes it. Full inventory:
INVENTORY.md in this payload.

## Verdict up front

**No independent second fixed point exists in the current record.**
The weld premise currently has exactly ONE application (the offset
lattice). Every other number in the surrounding structure is either
SU(2)/Casimir arithmetic (no free scale for the premise to fix),
downstream of c = 4 itself, the same counting-start in other
clothing, or a continuous postulated model parameter (outside the
premise's scope - it governs DISCRETE dictionary scales). The hunt
did close one open gate by computation (the W2 asymptotics,
sec. 3) and extracts two genuinely falsifiable predictions the
premise makes beyond its target (sec. 4) - both are predictions
about future computations, not numbers already on the books, and
are labelled as such.

## 1. The quarters, kept apart

Three distinct quarters circulate; the lanes already distinguish
the first two and the hunt confirms the distinctions are real:
- Q1 Casimir completion (j+1/2)^2 - j(j+1) = 1/4 (v14.859, v13.595),
  incl. the two-vector exchange values -lambda/4 / +3 lambda/4 at
  j = 1/2 (v14.862). Pure SU(2) arithmetic. No scale freedom.
- Q2 pair-product quantum q_G = 1/4 (v14.731) -> grid c = 4 (weld).
- Q3 Maslov action quarter (n - 1/4) (v14.592). Additive shift.
The weld is about Q2 only; Q1's quarters are NOT evidence for it.

## 2. Candidate-by-candidate

(a) Divisor counts D(4n) and the anomaly Delta_4 = 4n log 4 +
O(sqrt n) (v14.857): DOWNSTREAM of c = 4. Consequences, not tests.
(b) Schwinger occupation offset (n1,n2) = (a-1,b-1) (v14.858): the
(1,1) contact is the j = 0 state - the weld's counting-start in
occupation clothing. CONSISTENT, not independent (flag in the entry
itself: the offset is conventional, physical_contact_quantization
UNPROVED).
(c) Seat stiffness ratio (v14.856): not fixed by geometry at all
(A(u)-dependent; normalized sector difference NONE). The weld
premise is precisely the extra-geometric input here - no number
to predict.
(d) Kernel/exchange parameters (auditor point 2 overlap): lambda
(v14.862, POSTULATED), kernel coupling g = 2qR/u, blob size a,
orbit R, drive Omega, susceptibilities kappa_s, mu_s (v14.873-896).
All CONTINUOUS parameters of postulated models; offset-lattice
matching has no grip on continuous couplings. ONE contact point:
the kernel's seat scale u IS a dictionary scale - at the gravity
seat the weld forces u = 1/2 (and g inherits the factor 2 vs the
EM seat) - but u = 1/2 was already the kernel thread's seat
choice, so this is the same fact restated, not a second point.
Honest point-2 status: no pair-shaped kernel parameter found;
no bridge yet.

## 3. Closed by computation: the W2 gate (v14.858's open item)

v14.858 left open: exact asymptotics of the Casimir-weighted
contact sum W2(N) = sum_{ab<=N} j(j+1), j = (a+b-2)/2, and the
"correct scale-normalized 4n-versus-n comparison", warning that
4 might not be the right normalization. The hunt disentangles
two different numbers the entry conflated:
- CUTOFF: the weld fixes the gravity dictionary's contact cutoff
  at 4n (it counts the quarter-grid's nodes). Not a choice.
- NORMALIZATION: with the cutoff fixed, homogeneity forces the
  comparison constant: the weight j(j+1) is degree-2 in (a,b),
  the count degree-1, so W2 is degree-3 and the anomaly-free
  normalization is 64 = 4^3, not 4.
Exact asymptotics (shell decomposition: w(m) = [sigma_2(m) +
m tau(m) - 2 sigma_1(m)]/2; sum sigma_2 ~ zeta(3) N^3/3):
  W2(N) = (zeta(3)/6) N^3 + (1/4) N^2 ln N + O(N^2),
  W2(4n)/W2(n) -> 64,   Delta_64(n) = W2(4n) - 64 W2(n) ~ -12 n^2 ln n.
Verified in exact rational arithmetic (w2_check.py): shell(12)
= 113 (v14.858's value); cumulative closed form = brute force at
N = 12; at n = 64000: ratio 63.991211 -> 64, W2(n)/n^3 =
0.20038131 -> zeta(3)/6 = 0.20034282, Delta_64/(n^2 ln n) =
-10.18 crawling to -12 (log-slow, as the expansion dictates).
Falsifiable content: any independent gravity-side derivation of
the seat Casimir sum with cutoff other than 4n breaks the weld.

## 4. The premise's two standing predictions (not yet tests)

P1 (k-factor member scale): v14.818 ASSUMED h = 1/2 at every k by
analogy. The weld premise makes member scale a SECTOR property:
h = 1/2 (gravity) / 1 (EM) at every k, so the radial shift is
-k log 2 in the gravity sector and 0 in EM as a theorem of the
premise. Any independent k-sector computation landing elsewhere
falsifies it.
P2 (W2 cutoff/normalization, sec. 3): cutoff 4n, normalization
64, anomaly -12 n^2 ln n.

## 5. Bottom line for the auditor's challenge

The challenge stands unanswered in its strong form: the weld is
a one-application rule whose premise (node = state) has not yet
scored an independent hit. The hunt's negative is itself the
finding - the surrounding record offers no second lattice for the
premise to bite on, because its numbers are SU(2) arithmetic or
postulated couplings. P1 and P2 are where a second hit can come
from; both await computations the lanes have not yet done.

Flags: second_fixed_point=NOT_FOUND_IN_CURRENT_RECORD;
weld_applications=1; W2_gate=CLOSED; W2_C3=zeta(3)/6;
W2_normalization=64; predictions P1_kfactor_scale,
P2_W2_cutoff STANDING_UNTESTED; kernel_bridge=NOT_FOUND;
G_derived=false; alpha_G_derived=false; psi_selected=false;
NUT_observed=false.
