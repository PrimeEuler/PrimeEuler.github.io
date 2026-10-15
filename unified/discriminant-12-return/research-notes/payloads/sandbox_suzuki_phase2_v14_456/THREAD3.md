# Thread 3 — The v13.753 §11 Gate: Basepointed Helix vs. Suzuki's de Branges Deficiency Carrier

**Date:** 2026-10-15. **Track:** sandbox ("our Lane B"), Thread 3 of the Suzuki×dictionary
exploration. **Workspace-only** — nothing here is ledgered or pushed.
**Task:** work the open gate of ledger v13.753 §11 — compare the basepointed rapidity-helix
carrier with Suzuki's de Branges deficiency carrier $E(z)$ and the paired characteristic
$T_{\rm pair}(z) = C_\xi\,\Xi(-iz)/E(z)$; give (or show the obstruction to) a boundary-triple
interpretation of the basepoint/zero-mode quotient.

**Sources read in full:** v13.753 (the gate), v13.285 (source calibration, (1.3) normalization),
v13.735, v13.737, v13.661, v13.667, v13.668, v13.670, v13.677, v13.706, v13.720, v13.754,
and `../EXPLORATION.md`. The direct continuation v13.754 already contains much of the
finite-$A$ answer; this note assembles it against the §11 question as posed, sharpens
exactly where the identification stops being helix data, and flags what the ledger
leaves implicit.

**Markings:** [D] derived/exact · [N] numerical · [C] conditional · [I] interpretation ·
[O] open. Nothing in this note is progress toward RH: the infinite-volume objects below
live inside Suzuki's §7 de Branges model, which is built on the screw-positivity
⇔ RH equivalence; the finite-$A$ identities are exact but are identities *about the
model*, not evidence for its positivity hypothesis.

---

## 0. Headline conclusion

The boundary-triple interpretation **exists and is exact at finite $A$** [D]. The
derivative transport $\bar D$ of v13.753 is a unitary conjugation of Suzuki's operator
realizations, so it transports the boundary triple itself, not merely the quadratic
form: $\widetilde\Gamma_j = \Gamma_j \bar D^{-1}$, $\widetilde\gamma_a = \bar D\gamma_a$,
and the Weyl function is *identical* on the helix side, $\widetilde m_a = m_a$
(v13.667, v13.754 §1). Consequently every characteristic defined invariantly from the
triple — Krein determinants, $W$-ratios, cross-ratios — is intertwined by the
screw–Weil unitary, and the paired characteristic is intertwined as an identity,
$\widetilde T_{\rm pair} = T_{\rm pair}$ (v13.754 §4).

The basepoint quotient is **not** a boundary condition, and this is a theorem, not a
gap [D]: it is the quotient by $\ker D = \operatorname{span}\{1\}$ on the primitive
domain, and it *precedes* the boundary triple in the chain
$\text{primitive}/\mathbf 1 \xrightarrow{\bar D} \text{screw space}
\xrightarrow{\widetilde\Gamma_j} \mathbb C$ (v13.754 §2). On the de Branges side its
correspondent is the entire-gauge freedom of $E$ at fixed $m$: every characteristic
sees only $\mathscr W = -g''$, i.e. is annihilated by exactly the same
$\operatorname{span}\{\delta_0,\delta_0'\}$.

The identification becomes conditional at exactly three points, each locatable:
(i) the finite-$A$ Hermite–Biehler carrier $E_a$ is determined by the transported
triple only after importing one scalar from infinity, $c_\infty = \xi'(3/2)/\xi(3/2)$,
whose intrinsic finite-$A$ definition is open [O]; (ii) identifying the finite
transported pair with Suzuki's infinite-volume $T_{\rm pair}$ requires the
$A\to\infty$ convergence ($m_a \to m_\infty$ locally uniformly, $\gamma$-field and
gauge control) that remains open [O]; (iii) the completed Hilbert/de Branges picture
is conditional on screw positivity [C], as in v13.753 §§6–8. There is also one
*convention* (not mathematical) soft spot: the sign in $E_a \propto W_\pi(1 \mp i c_\infty m_a)$
is orientation data, stabilized in the ledger by matching Suzuki's §7.8 anchor
formula, not by the triple alone (§2.4 below).

---

## 1. What $E(z)$ and $T_{\rm pair}(z)$ are in Suzuki's setup

### 1.1 Conventions (two collisions in the ledger, flagged)

- v13.668/v13.670/v13.754 write $\Xi(z) := \xi(\tfrac12 - iz)$ and
  $D_\xi(z) := \xi'(\tfrac12 - iz)$, with $s = \tfrac12 - iz$.
- v13.737 writes $\Xi(w) := \xi(\tfrac12 + w)$, an *even* function of $w$.
  The $\Xi(-iz)$ in $T_{\rm pair}$ is this second convention at $w = -iz$:
  $\Xi(-iz) = \xi(\tfrac12 - iz)$, the same value as the first convention's $\Xi(z)$.
  The ledger uses both without a global warning. **[flagged: convention collision,
  harmless once stated]**

### 1.2 $E(z)$ [D, as Suzuki-model data]

$$
E(z) \;=\; \Xi(z) + D_\xi(z) \;=\; \xi(s) + \xi'(s), \qquad s = \tfrac12 - iz,
$$
i.e. $E(z) = \Xi(z)\,[1 + L(s)]$ with $L = \xi'/\xi$ (v13.668 §2, v13.754 §5).
$E$ is the **Hermite–Biehler function of Suzuki's §7 de Branges space**: with
$E^\sharp(z) := \Xi(z) - D_\xi(z)$ one has $E - E^\sharp = 2D_\xi$, and $E$ enters
Suzuki's boundary form for the defect vector $K(\bar z,\cdot)$ against the extension
vector $W_\theta$ as (v13.668 §2, v13.670 §1)
$$
\mathcal W(K(\bar z,\cdot), W_\theta)
= -\frac{e^{-i\theta/2}}{\pi i}\big[C_\theta E(z) - \overline{C_\theta} E^\sharp(z)\big],
\qquad
C_\theta = a\cos\tfrac\theta2 + i b\sin\tfrac\theta2,
$$
with anchor values $a = \xi(3/2)$, $b = \xi'(3/2)$.

Two layers must not be conflated (v13.668 §5): the raw $\theta=\pi$ boundary form is
proportional to $\Xi$, **not** to $\Xi/E$:
$B_\pi = (2ib/\pi)\,\Xi$, $B_0 = (2ia/\pi)\,D_\xi$. The denominator $E$ enters only
through the *normalization of the defect vectors in the Fourier/energy realization*
(the $\widehat f_{\pm i}$ below). So $E$ is not the characteristic of the reference
extension; it is the characteristic **denominator of a complex boundary parameter**:
with $c_\infty := b/a$ and the corrected Weyl function (v13.670 §2)
$$
m_\infty(z) = -i\,\frac{a}{b}\,\frac{D_\xi(z)}{\Xi(z)},
\qquad\text{one has}\qquad
\frac{\Xi(z)}{E(z)} = \frac{1}{1 + i c_\infty m_\infty(z)},
$$
i.e. $E(z) = i c_\infty\,\Xi(z)\,[m_\infty(z) - \tau_{\rm HB}]$ with
$\tau_{\rm HB} = i/c_\infty = ia/b \notin \mathbb R$ (v13.754 §6). $E$ is therefore
the denominator of the **maximal dissipative/accumulative** extension at
$\tau_{\rm HB}$, *not* of any self-adjoint member of Suzuki's real $\theta$-family.
(v13.669's claim of a real $\theta_*$ producing $E$ was retracted in v13.670 §4;
do not resurrect it.) Suzuki's Corollary-1.6 target $\Xi/E$ is the Möbius transform
$R_{\rm Suz} = [1 + ic_\infty m_\infty]^{-1}$ of the Weyl function (v13.668 §4 as
corrected by v13.670 §3).

**Ledger-implicit points [flagged]:**
(a) The unit coefficients in $E = \xi + \xi'$ are imported from Suzuki §7 as model
data. The ledger nowhere derives the coefficient of $\xi'$ from the screw side;
equivalently, $T_{\rm pair} = C_\xi/(1+L)$ with *no* extra constant before $L$ is a
normalization fact about Suzuki's $\widehat f_{\pm i}$, not a consequence of the
quadratic form. (b) The Hermite–Biehler property of $E$ (no zeros in the closed
upper half-plane sense, $|E| > |E^\sharp|$ for $\operatorname{Im} z > 0$) is part of
Suzuki's §7 model, i.e. it carries the positivity/RH-equivalent content [C]; the
ledger verifies it only through the model, never independently.

### 1.3 $T_{\rm pair}(z)$ [D, Suzuki §7 identity]

$$
T_{\rm pair}(z) \;:=\; (z-i)\widehat f_{+i}(z) - (z+i)\widehat f_{-i}(z)
\;=\; C_\xi\,\frac{\Xi(-iz)}{E(z)},
\qquad
C_\xi = \frac{2\xi'(3/2)}{\pi^2 i} = \frac{2b}{\pi^2 i},
$$
(v13.737 Gate 5, v13.735 §9, v13.754 §4). The $\widehat f_{\pm i}$ are Suzuki's
canonical deficiency functions at the spectral points $\pm i$ in their
Fourier/energy realization; $T_{\rm pair}$ is the $\theta=\pi$ *combination* of the
two channels. The finite-$A$ analogue is exact: with $A(z) = (z-i)F_+(z)$,
$B(z) = (z+i)F_-(z)$, Suzuki's characteristic is $W_\theta = A + e^{i\theta}B$
(v13.685, quoted in v13.706 §0), so the pair combination is $A - B = W_\pi$ at the
level of channel algebra — with the caveat of §1.2 that the *infinite-volume
normalized* $T_{\rm pair}$ is $W_\pi$-type data divided by $E$, the $E^{-1}$ being
the de Branges normalization of the $\widehat f_{\pm i}$, not boundary-triple data.

**Ledger-implicit point [flagged]:** the ledger quotes the $T_{\rm pair}$ identity
from Suzuki §7 (v13.737 Gate 5: "Suzuki Section 7 gives the exact boundary
combination") but never writes an independent definition of $\widehat f_{\pm i}$
(precise transform, precise scalar normalization). The identity
$E \cdot T_{\rm pair} = C_\xi\,\Xi$ is therefore, within the ledger, an imported
source identity [D/source], and all ledger-side content is in its *decomposition*
(§2.3) and its finite-$A$ transport (§2.1), not in a re-derivation.

### 1.4 The boundary triple (finite $A$) [D]

Suzuki §6, made exact in v13.661: deficiency vectors $\mathscr D_A^* v_\pm = \pm i v_\pm$
of equal norm $h_A = \|v_+\|^2 = \|v_-\|^2 > 0$; von Neumann coordinates
$f = f_0 + \alpha v_+ + \beta v_-$; ordinary boundary triple
$$
\Gamma_0 f = \sqrt{h_A}\,(\alpha + \beta), \qquad
\Gamma_1 f = i\sqrt{h_A}\,(\alpha - \beta),
$$
reproducing the Green form $\mathcal W(f,g) = \Gamma_1 f\,\overline{\Gamma_0 g}
- \Gamma_0 f\,\overline{\Gamma_1 g}$ exactly. Reference extension
$H_{A,\pi} = \ker\Gamma_0$; self-adjoint parameters $\tau_\theta = \tan(\theta/2)
\in \mathbb R \cup \{\infty\}$; $\gamma$-field
$\gamma_A(z) = (\Gamma_0|_{\ker(\mathscr D_A^* - z)})^{-1}$; Weyl function
$m_A(z) = \Gamma_1\gamma_A(z)$; Krein formula and normalized determinant
$\Delta^{\rm bdry}_{A,\theta/\pi}(z;z_*) = \frac{\tau_\theta - m_A(z)}{\tau_\theta - m_A(z_*)}$
(v13.661 §§2–3). Infinite-volume: the same coordinate formulas on the deficiency
basis $k_\pm(t) = K(\mp i, t)$ of Suzuki's §7 model (v13.668 §1) [C: model].

---

## 2. The identification: what plays the carrier role on the helix side

### 2.1 The triple transports; $m$ is the invariant [D]

$v13.753$'s derivative map is, at finite $A$, Suzuki's own §8 unitary
$\bar D : \mathcal H(T_A) \xrightarrow{\sim} \mathcal H(S_A)$ onto the
continuous-kernel (screw) realization. v13.667 proves the transported triple is
$$
\widetilde\Gamma_j = \Gamma_j \bar D^{-1}\ (j=0,1), \qquad
\widetilde\gamma_a(z) = \bar D\,\gamma_a(z), \qquad
\boxed{\ \widetilde m_a(z) = m_a(z)\ }
$$
exactly — Green identity, Krein formula, determinant, and Suzuki's characteristic
$W(a,\theta;z)$ all invariant. The helix side is the $S_a$ realization: its defect
vectors are $u_\pm = \bar D v_\pm$ and its defect equation is
$S_a u_z = \bar D e_z$ with helix exponentials $e_z(x) = e^{-izx}$ (v13.667 §6) —
i.e. **the deficiency data of the triple, on the helix side, is the $\bar D$-image
of the rapidity helix evaluated at the defect spectral points.** This answers the
second half of the §11 question directly: the screw–Weil unitary intertwines the
paired deficiency characteristic's *triple-determined part*, not merely its
quadratic form [D, finite $A$].

### 2.2 There is no single helix vector that is $E$ — the carrier role splits [D]

Per the v13.754 §4 guardrail, $T_{\rm pair}$ is not a bare helix vector, and neither
is $E$. The "deficiency carrier" role decomposes into three helix-side objects:

1. **The transported $\gamma$-field** $\widetilde\gamma_a(z) = \bar D\gamma_a(z)$
   carries the deficiency *space*: defect vectors $u_z = S_a^{-1}\bar D e_z$ in the
   screw increment space, generated from the basepointed helix
   $\Psi_u(t) = e^{itu} - 1$ by resolvent transport.
2. **The Weyl function** $m_a$ — identical on both sides — carries the *extension
   data*: every self-adjoint relative characteristic is $\tau - m_a$, every
   normalized determinant is a ratio of such (v13.661 §3).
3. **The gauge-dressed characteristic** carries $E$ itself. At finite $A$,
   v13.671/v13.673/v13.677 construct
   $$
   E_a = W_\pi - c_\infty W_0 = W_\pi\,\big(1 - i c_\infty m_a\big),
   $$
   and prove the exact kernel identity (v13.677 §§3–4)
   $$
   K_{E_a}(w,z) = \frac{c_\infty}{\pi}\, W_\pi(z)\overline{W_\pi(w)}\,
   \frac{m_a(z) - \overline{m_a(w)}}{z - \bar w}
   = q_a(z)\overline{q_a(w)}\,\langle\gamma_a(z),\gamma_a(w)\rangle,
   \quad q_a = \sqrt{c_\infty/\pi}\,W_\pi,
   $$
   so the de Branges space $\mathcal B(E_a)$ *is* the $\gamma$-field RKHS up to the
   analytic gauge $q_a$, and the simple sector of the Suzuki energy space is
   $\mathcal B(E_a)$ (v13.677 §5). On the helix side this says: **$E$'s reproducing
   kernel is the Gram kernel of the transported defect vectors, dressed by the
   $\theta=\pi$ characteristic as a gauge.** The helix supplies the Gram (through
   $G_g$-increments and the resolvent $S_a^{-1}\bar D$); $W_\pi$ and $c_\infty$ are
   the two scalar/gauge inputs discussed in §4.

### 2.3 The exact decomposition: what the helix current sees of $T_{\rm pair}$ [D]

From $E = \Xi(1+L)$ and $E\,T_{\rm pair} = C_\xi\Xi$ (v13.754 §5):
$$
T_{\rm pair} = \frac{C_\xi}{1 + L(s)}, \qquad
\frac{T_{\rm pair}'}{T_{\rm pair}} = i\,\frac{L'(s)}{1 + L(s)}, \qquad
\frac{E'}{E} = -iL(s) - i\,\frac{L'(s)}{1 + L(s)},
$$
hence the closed decomposition of the analytically regularized helix/Weil current
$$
\boxed{\ -iL(s) \;=\; \frac{T_{\rm pair}'}{T_{\rm pair}} + \frac{E'}{E}\ }
$$
(v13.737 Gate 7, v13.754 §§5, 8). Reading: the screw current supplies $-iL$
**exactly and completely** at the level of logarithmic derivatives; $E'/E$ is
precisely the complementary term, and $T_{\rm pair}'/T_{\rm pair}$ is the
rank-one resolvent-trace $\operatorname{Tr}[(H_{\rm HB} - z)^{-1} -
(H_\pi - z)^{-1}]$ in the v13.661 determinant convention (v13.754 §8). So the
helix sees $T_{\rm pair}$ through its logarithmic derivative with an explicitly
identified complementary term — the obstruction to seeing $T_{\rm pair}$ itself is
not analytic but *normalizational*: exponentiating back requires $\Xi$ (v13.737
Gate 3: integration + the value $\Xi(0) = \xi(1/2) \ne 0$) and the constant $C_\xi$.

### 2.4 The one convention soft spot: orientation of $E_a$ [flagged]

v13.670 §7's corrected finite candidate is $E_a \propto W_\pi[1 + i c_\infty m_a]$;
v13.677 §1's (later, audited via v13.676) is $E_a = W_\pi[1 - i c_\infty m_a]$, and
indeed $W_\pi[1 + ic_\infty m_a] = -E_a^\sharp$ in v13.677's convention: the two
candidates are the two members of the sharp pair, exchanged by the deficiency
reflection $\mathscr R$ ($m \mapsto -m$, $W_\pi \mapsto -W_\pi$; v13.706 §§1–2,
v13.754 §3, under which $s = (m-i)/(m+i) \mapsto s^{-1}$ — the Cayley inversion).
All structural content (kernel identity, $R_a$ a Möbius function of $m_a$ alone,
determinant identities) is identical for both. The sign is **orientation data**:
it is fixed only by matching Suzuki's source anchor $B_0/B_\pi = (a/b)(D_\xi/\Xi)$
(§7.8 of the source, via v13.670 §§1–2), not by the abstract triple. This note uses
the v13.670/v13.754 convention ($m_\infty = -i(a/b)D_\xi/\Xi$,
$\Xi/E = [1 + ic_\infty m_\infty]^{-1}$) throughout; the numerical check in §5.1
confirms that convention is internally consistent at 30-digit precision. Relatedly,
v13.647's literal-normalization gate (whether the project's Cayley coordinate
equals Suzuki's printed Schur candidate on the nose) remains open in the ledger
(v13.706 §8) [O]. A helix-side construction that ignores this sign will produce
$E^\sharp$ while calling it $E$ — the failure mode is silent and worth naming.

---

## 3. The basepoint quotient on the de Branges side

### 3.1 Continuum statement [D]

The quotient has three equivalent helix-side descriptions (v13.753 §5, v13.754 §2):
$\ker D = \operatorname{span}\{1\}$ on the enlarged primitive domain; the affine
gauge $g \mapsto g + a + bu$ of the screw function; Fourier-side
$\operatorname{span}\{\delta_0, \delta_0'\}$, annihilated by the $t^2$ that produces
$\mathscr W = -g''$. Its de Branges-side correspondent:

- **Every** boundary characteristic, Weyl function, Krein determinant, and the
  ratio $R = \Xi/E$ is built from $\mathscr W$ / $L$ alone, hence is exactly
  invariant under the gauge — the quotient is *invisible* to the triple, not
  encoded by it. In particular
  $\text{zero-mode quotient} \ne \ker\Gamma_0$ and $\ne \ker\Gamma_1$ (v13.754 §2):
  $\ker\Gamma_j$ are codimension-one conditions *inside* $\operatorname{dom}\mathscr D^*$,
  while $\operatorname{span}\{1\}$ is the kernel of the *intertwiner between
  realizations*. Asking "which boundary condition is the basepoint quotient?" is a
  category error, and the ledger's answer is the chain
  $\text{primitive}/\mathbf 1 \xrightarrow{\bar D} \text{screw space}
  \xrightarrow{\widetilde\Gamma_j} \mathbb C$: **the quotient is what makes the
  transport a map at all; the triple lives downstream of it.**
- What the gauge freedom *becomes* on the $E$ side: at fixed $m$, $E$ is determined
  only up to multiplication by zero-free real-entire gauge factors (the $q_a$ of
  §2.2; v13.677 §7 separates exactly this gauge convergence from spectral
  convergence). Suzuki's gauge-fix on the helix side (evenness kills $bu$/$δ_0'$;
  $g(0) = 0$ kills $a$/$δ_0$; v13.753 §5) corresponds to fixing $E$'s gauge by the
  anchor normalization: the specific representative $E = \Xi + D_\xi$ with
  constants $C_\xi$, $c_\infty$ read off $\xi, \xi'$ at the anchor point $s = 3/2$.
  The invisibility statement in this bullet is [D]; the correspondence of the two
  gauge-*fixings* is [I] — a structural parallel (a two-real-condition pin on the
  helix side; an anchor-value pin on the de Branges side, whose own gauge group —
  zero-free real-entire factors — is much larger), not a formula, and the ledger
  does not identify the two fixings with each other.

### 3.2 Station-lattice shadow [D about the construction; I for the reading]

The station Gram of `../EXPLORATION.md` is a Gram of the increments $\Psi_{u_n}$
under $G_g$ — post-quotient objects by construction. Station $n = 1$ is the
basepoint $u_1 = 0$, $\Psi_0 = 0$: its Gram row vanishes identically, giving the
single structural zero eigenvalue at every $N$ [N, EXPLORATION]. The discrete
model therefore *cannot represent the gauge at all*: there is no station-lattice
primitive whose ambiguity one could quotient. This is the finite shadow of
"quotient precedes triple" — if a discrete boundary triple on the station lattice
is ever built, its $\Gamma$'s will act on the $(N-1)$-dimensional increment space,
never on primitives. Likewise the zero-mass sector $\{f : \sum f_n = 0\}$ is the
discrete $D\mathcal D_W$ (derivatives have zero mass, v13.753 §7), and the measured
$K$-vs-$G$ discrepancy for nonzero-mass $f$ ($4.43$ at $N = 32$ [N]) is exactly the
affine-gauge/mass term — the discrete $\operatorname{span}\{1, u\}$ making itself
visible precisely where the quotient was *not* taken.

---

## 4. Where the identification stops: the residual gaps, precisely

1. **Imported scalar $c_\infty$ [O].** Finite-$A$ $E_a$ (v13.677 §1) is defined
   using $c := c_\infty = \xi'(3/2)/\xi(3/2)$, an infinite-volume anchor value.
   The transported triple at finite $A$ does not determine it. v13.668 §7 asks for
   an intrinsic finite $c_a$ (e.g. from finite deficiency data at $z = 0, \pm i$)
   with $c_a \to c_\infty$; unproved. Until then, "the helix determines $E_a$"
   carries the footnote "modulo one imported real scalar $\approx 0.0461359281$"
   [N value, §5.1]. Note $a = \xi(3/2)$ and $b = \xi'(3/2)$ themselves are values
   of the *theta-side* entire function $\Xi$ at the anchor — data the screw current
   reaches only after the integration of v13.737 Gate 3, i.e. after a choice of
   normalization constant. This is the same normalization gap as §2.3, seen from
   the other side.
2. **Finite-to-infinite convergence [O].** $\widetilde T_{{\rm pair},A} = T_{{\rm pair},A}$
   is finite-$A$ transport invariance [D]; $T_{{\rm pair},A} \to T_{\rm pair}$ is
   not proved. Needed (v13.754 §10, v13.677 §8, v13.737 Gate 10): the infinite HB
   operator as a strong/generalized resolvent limit of the finite transported
   extensions; $m_a \to m_\infty$ locally uniformly; $\gamma_a \to \gamma_\infty$
   on compacta of the resolvent set, with gauge factors controlled mod zero-free
   real-entire factors. A sharp sufficient-condition question is already posed in
   v13.754 §11: convergence of the finite HB determinants
   $\Delta_{{\rm HB},A/\pi}(z;z_*) =
   \frac{\tau_{\rm HB} - m_A(z)}{\tau_{\rm HB} - m_A(z_*)}$ with $\tau_{\rm HB}$
   defined at finite $A$. Additionally (v13.720 §§8, 11): promoting the paired-core
   recovery of $\Xi$ to the full Suzuki defect sources requires asymptotics of
   $\bar D_A$ and $S_A^{-1}$ on the exponential sources $e_z$ — the raw cores are
   exact, and the pairing is essential (a single channel grows like $e^A$ with
   folded half-line limits; only the renormalized pair minus the universal $2C_\theta$
   recovers $I(-iz)$) [D for cores; O for the transported version].
3. **Positivity/completion [C].** The Hilbert-space statements — $\bar D$ unitary
   between *completed* spaces, $\mathcal B(E_a)$ as the simple sector, the whole
   §7 de Branges model — are conditional on screw/Weil positivity (v13.753 §§6–7
   [G]). The form identities are unconditional; the operator model is not. Nothing
   in the boundary-triple interpretation weakens or strengthens this conditionality.

**The obstruction, stated positively:** there is no obstruction to the
boundary-triple interpretation of the quotient *as a pre-triple kernel quotient
with a gauge correspondent on the $E$ side* — that is proved [D]. The obstruction
is to the stronger (and, per v13.754 §2, ill-posed) reading in which the quotient
would itself be a boundary condition or in which a bare helix vector would equal
$E$ or $T_{\rm pair}$: $E$ is a gauge-dressed characteristic requiring
$(\gamma\text{-field}, m, W_\pi, c_\infty, \text{orientation})$, of which the last
two are not finite-$A$ helix data today.

---

## 5. Checks

### 5.1 Performed in this thread (sanity, not substitutes for §4's gates)

Symbolic (sympy, exact):
- v13.677 §2 bracket: $(1-icm_z)(1+ic\bar m_w) - (1+icm_z)(1-ic\bar m_w)
  = 2ic(\bar m_w - m_z)$ — verified, difference $0$.
- Möbius: with $m_\infty = -i(a/b)L$, $c_\infty = b/a$: $1 + ic_\infty m_\infty
  = 1 + L$ — verified identically.
- Log decomposition: $T'/T + E'/E = -iL(s)$ with $T = (1+L)^{-1}$,
  $E = \Xi(1+L)$, $\Xi'/\Xi = -iL$, $s = \tfrac12 - iz$ — verified identically.

Numerical (mpmath, 30-digit) [N]:
- Anchors: $a = \xi(3/2) = 0.508731038726\ldots$, $b = \xi'(3/2) =
  0.023470778605\ldots$, $c_\infty = 0.046135928060\ldots$
- At $z \in \{0.3 + 0.7i,\ -0.8 + 1.3i,\ 1.5 + 0.2i,\ 2i\}$:
  $|\Xi/E - [1 + ic_\infty m_\infty]^{-1}| \lesssim 10^{-31}$ and
  $|E\,T_{\rm pair} - C_\xi\,\Xi| \lesssim 10^{-34}$ with
  $T_{\rm pair} := C_\xi/(1+L)$ — the v13.670/v13.754 convention set is
  numerically coherent. The HB inequality $|E(z)| > |E^\sharp(z)|$ held at all
  four sample points (spot check only; inside Suzuki's model this is [C] content,
  not independent evidence).

### 5.2 What a real check of the identification would look like (not run)

1. **Finite-$A$ kernel check [N]:** in the existing §8 continuous-kernel
   machinery, compute $u_z = S_a^{-1}\bar D e_z$ at moderate $a$, extract
   $m_a(z) = \widetilde\Gamma_1 u_z / \widetilde\Gamma_0 u_z$, form
   $E_a = W_\pi - c_\infty W_0$, and verify the v13.677 kernel identity
   $K_{E_a} = \frac{c_\infty}\pi W_\pi\overline{W_\pi} K_{m_a}$ pointwise against
   the $\gamma$-Gram $\langle\gamma_a(z),\gamma_a(w)\rangle$ computed from defect
   solutions. This tests transport + gauge in one shot.
2. **Intrinsic-$c_a$ probe [N/O]:** compute candidate finite $c_a$ from deficiency
   norms/anchor values at $z = 0, \pm i$ across a ladder of $a$ and test
   $c_a \to c_\infty = 0.0461359281\ldots$ — a direct numerical attack on gap 1.
3. **Convergence probe [N/O]:** track $\Delta_{{\rm HB},A/\pi}(z;z_*)$ and
   $R_a = [1 + ic_\infty m_a]^{-1}$ (v13.670 §7 form) on compact $z$-sets as $A$
   grows, against the closed-form $\Xi/E$; locally uniform convergence of $R_a$
   would be the numerical shadow of gap 2 (and would *not* by itself prove it).
4. **Station-lattice version [O]:** discretize the defect equation on the station
   lattice $\{u_n = \log n\}$ (the $S_a$ Nyström machinery of v13.285 §5) and ask
   whether the discrete $\gamma$-Gram, restricted to the zero-mass sector, has the
   finite de Branges kernel of the sampled $E_a$ as its continuum shadow — the
   discrete analogue of §3.2's reading.

---

## 6. One-paragraph summary for the record

[D] The basepointed helix and Suzuki's de Branges deficiency carrier are related
by an exact finite-$A$ boundary-triple transport: $\bar D$ conjugates the triple,
$m$ is invariant, $E_a$'s kernel is the transported $\gamma$-Gram dressed by the
$W_\pi$ gauge, and $-iL = T_{\rm pair}'/T_{\rm pair} + E'/E$ decomposes the helix
current into the paired-characteristic trace term and the HB normalization term.
[D] The basepoint/zero-mode quotient is the pre-triple quotient by $\ker D$,
corresponding on the de Branges side to the entire-gauge freedom of $E$ at fixed
$m$ — not to any boundary condition. [O] The identification is completed only
modulo an intrinsic finite-$A$ $c_a \to c_\infty$ and the finite-to-infinite
resolvent/$\gamma$-field convergence. [C] All completed-space statements remain
conditional on screw positivity. The quotient has a boundary-triple
*interpretation*; it does not have a boundary-triple *identity*, and the ledger
(v13.754 §2) already contains the proof that it cannot.
