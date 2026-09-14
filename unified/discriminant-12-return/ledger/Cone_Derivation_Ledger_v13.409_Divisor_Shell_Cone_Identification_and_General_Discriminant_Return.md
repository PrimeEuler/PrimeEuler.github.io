# Cone Derivation Ledger v13.409 — Divisor-Shell/Cone Identification and General Discriminant Return

Date: 2026-09-14

Status labels: **[S]** source-established, **[D]** exact derived, **[I]** interpretation, **[O]** open, **[Audit]** correction/limitation.

## Provenance note

This entry records a synthesis reached in conversation with the external audit collaborator, cross-checking exploratory work done outside this ledger (a real-variable "mod 0.5" divisor-symmetry construction) against Paper A's cone and against `v13.179`. It is not an External Audit round (no new ledger updates were being reviewed) and not an autonomous derivation — it is recorded here specifically so the identification is not lost, per explicit request. Full derivations and the independent symbolic checks are in the companion research note.

## 1. The result

**[D, independently verified]** The real-variable construction $v_k=(n-k^2)/(2k),\ T_k=(n+k^2)/(2k)$ (with $v_k\bmod0.5=\tfrac12\{n/k\}$ recovering the classical divisor-summatory fractional-part sum) is **exactly** Paper A's cone $T^2-X^2=Y^2=uv$ restricted to the fixed shell $Y=\sqrt n$, under $u=k,\ v=n/k,\ X=-v_k,\ T=T_k$. Every $n$ has its own fixed height $Y=\sqrt n$ on the cone; this is an algebraic identity, checked symbolically, not an analogy.

**[Audit]** The $D(n)$-shell family's own discriminant (as a binary quadratic form) is fixed at $4$ for every $n$ — its asymptotes are always rational ($\pm1$ slope). Sweeping through $n$ never by itself produces an irrational ray. A candidate invariant (the angle at which a ray crosses the unit circle) was checked and found non-distinguishing: it is the same for rational, quadratic-irrational, and transcendental slopes alike, since it is a generic fact about any circle centered at the origin. Recorded so it is not later mistaken for a real connection.

**[D, re-verified]** `v13.179`'s discriminant-12 return, $g_{12}=\begin{pmatrix}3&1\\2&1\end{pmatrix}$ conjugate to the boost $B_{12}$ with eigenvalue $\varepsilon=2+\sqrt3$, satisfies $x'y'=xy$ for $x=T+X,y=T-X$ under the boost — i.e. it preserves **every** shell $xy=n$ simultaneously (not just $n=12$), acting as the uniform rapidity translation $s\mapsto s+\log\varepsilon$ on each shell's own $x=\sqrt n\,e^s,\,y=\sqrt n\,e^{-s}$ parametrization. Re-derived independently and confirmed symbolically.

**[D, new this session]** This is not special to $d=12$: (a) *any* Lorentz boost in the $(T,X)$ plane preserves every shell, for any real rapidity parameter — a generic fact, verified symbolically for arbitrary $R$; (b) what is special about $d=12$ is that $\varepsilon=2+\sqrt3$ arises from an *integer* matrix (a genuine arithmetic Pell-type return). Checked a second, independent discriminant, $d=5$: $g_5=\begin{pmatrix}2&1\\1&1\end{pmatrix}$ (trace 3, det 1, $\Delta=5$, eigenvalues $\varphi^{\pm2}$, $\varphi$ the golden ratio) gives the identical shell-preservation property under the same construction, verified symbolically. So the discriminant-12 return is one instance of a general pattern: for any non-square $d$ admitting an integer trace-$t$/det-1 matrix with $t^2-4=d$, the same shell-preserving, rapidity-translating boost exists, with rapidity step $\log\varepsilon_d$ for the corresponding unit of $\mathbf Q(\sqrt d)$.

## 2. What this does not establish

- No action on the *integer* divisor lattice — the boost(s) act on the continuous real shell only, exactly as `v13.179` already cautions for $d=12$; irrational $\varepsilon_d$ does not map integer factor pairs to integer factor pairs.
- No connection to the Suzuki screw-function/operator thread or to RH — this is real/algebraic cone geometry, independent of that separately-audited line of work.
- No unified proof covering all discriminants $d$ at once via Paper B's general $G_{a,b}$ generator — only two individual instances ($d=12,5$) are checked; the general statement is proposed but not proved here.

## 3. Companion research note

`research-notes/Cone_Shell_Rays_and_General_Discriminant_Return.md` — full derivations, all symbolic checks, and a suggested-next-steps list (prove the general $G_{a,b}$ case once rather than per-discriminant; characterize which $d$ admit an integer Pell return via classical theory; check whether $v13.179$'s "no finite integer orbit" limitation is generic or specific to $d=12$).

## Guardrails

- This entry makes no RH, GRH, or exact-zero claim.
- It makes no claim about the discrete/arithmetic divisor lattice, only the continuous real cone.
- The $d=5$ generalization is a single additional checked instance, not a proof for general $d$.
- The "same angle at the unit circle" observation is explicitly recorded as ruled out, not as supporting evidence.
