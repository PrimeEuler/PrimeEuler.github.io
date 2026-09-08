# Cone Derivation Ledger v13.314 — Exact Fixed-Core Prime-Tail Decay

## Status

This checkpoint converts the numerical fixed-core decoupling seen in v13.313 into an analytic statement for the prime-shift operator in Suzuki's a=1 even-v sector.

The key distinction remains:

- a **fixed finite core** decouples from the remote prime tail at an explicit Hilbert-Schmidt rate;
- a **moving buffer/tail interface** need not decouple, because the prime shift operator is bounded but noncompact.

No RH/GRH, kernel, or lambda_1(a=1)=0 conclusion is made.

---

## 1. Odd Dirichlet basis and one truncated shift

For odd n, the even-v Dirichlet basis may be written, up to the harmless sign convention,

\[
\psi_n(x)=\pm\cos\frac{n\pi x}{2},\qquad -1\le x\le1.
\]

Let

\[
(S_\ell f)(x)=f(x-\ell)+f(x+\ell),
\]

with zero extension outside [-1,1].

For odd m\neq n, set

\[
a=\frac{m\pi}{2},\qquad b=\frac{n\pi}{2}.
\]

A direct product-to-sum integration over the truncated overlap gives

\[
\boxed{
\langle\psi_m,S_\ell\psi_n\rangle
=
(-1)^{(m-n)/2}\frac{\sin(b\ell)-\sin(a\ell)}{a-b}
-
(-1)^{(m+n)/2}\frac{\sin(b\ell)+\sin(a\ell)}{a+b}.
}
\]

This is exact.

---

## 2. Explicit 1/n decay for fixed m

For n>m,

\[
\left|\langle\psi_m,S_\ell\psi_n\rangle\right|
\le
\left(1+|\sin(a\ell)|\right)
\left(\frac1{|a-b|}+\frac1{a+b}\right).
\]

Since

\[
\frac1{|a-b|}+\frac1{a+b}
=
\frac{2}{\pi}
\left(\frac1{n-m}+\frac1{n+m}\right),
\]

we obtain

\[
\boxed{
\left|\langle\psi_m,S_\ell\psi_n\rangle\right|
\le
\frac{2}{\pi}\left(1+|\sin(a\ell)|\right)
\left(\frac1{n-m}+\frac1{n+m}\right).
}
\]

Thus every fixed low mode couples to remote prime-shift modes like O_m(n^{-1}).

---

## 3. Suzuki prime operator

At a=1,

\[
B_{\rm prime}
=-\sum_{q\in\{2,3,4,5,7\}}w_qS_{\log q},
\qquad
w_q=\frac{\Lambda(q)}{\sqrt q}.
\]

For a fixed odd core mode m define

\[
\boxed{
C_m
=
\sum_qw_q
\left(1+\left|\sin\left(\frac{m\pi}{2}\log q\right)\right|\right).
}
\]

Then for odd n>=N>m,

\[
|(B_{\rm prime})_{mn}|
\le
\frac{2C_m}{\pi}
\left(\frac1{n-m}+\frac1{n+m}\right).
\]

Using

\[
\frac1{n-m}+\frac1{n+m}
=
\frac{2n}{n^2-m^2}
\le
\frac{2}{n\left(1-(m/N)^2\right)},
\]

we get

\[
\boxed{
|(B_{\rm prime})_{mn}|
\le
\frac{4C_m/\pi}{1-(m/N)^2}\frac1n.
}
\]

---

## 4. Fixed core n<=19 is Hilbert-Schmidt into the remote tail

Take

\[
\mathcal C
=\operatorname{span}\{\psi_1,\psi_3,\ldots,\psi_{19}\}.
\]

For the odd tail n>=N>19,

\[
\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|
\le
\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|_{\rm HS}.
\]

The previous entrywise estimate yields

\[
\boxed{
\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|_{\rm HS}^2
\le
\sum_{\substack{m\le19\\m\;\rm odd}}
\left(\frac{4C_m/\pi}{1-(m/N)^2}\right)^2
\sum_{\substack{n\ge N\\n\;\rm odd}}\frac1{n^2}.
}
\]

Using the already employed tail majorant

\[
\sum_{\substack{n\ge N\\n\;\rm odd}}\frac1{n^2}
\le
\frac1{N^2}+\frac1{2N},
\]

we obtain the fully explicit analytic rate

\[
\boxed{
\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|
=O(N^{-1/2}).
}
\]

The O(N^-1/2) is a Hilbert-Schmidt estimate for the whole ten-dimensional core-to-tail block. Individual fixed matrix entries decay like O(n^-1).

---

## 5. Ordinary floating evaluations

For m=1,3,...,19, the constants C_m are approximately

\[
\begin{array}{c|c}
m&C_m\\\hline
1&4.7487176492\\
3&4.5190524830\\
5&4.4453251925\\
7&4.9250051132\\
9&4.4588182605\\
11&4.5178176314\\
13&5.0714392943\\
15&4.8370156450\\
17&5.1988409903\\
19&5.5001332022
\end{array}
\]

The resulting analytic Hilbert-Schmidt upper bounds are approximately

\[
\begin{array}{c|c}
N&\|P_{\ge N}B_{\rm prime}P_{\mathcal C}\|_{\rm HS}\ \text{upper bound}\\\hline
151&1.13474\\
237&0.90010\\
301&0.79719\\
401&0.68962\\
501&0.61646\\
1001&0.43549\\
2001&0.30783
\end{array}
\]

These decimals are ordinary floating evaluations of exact closed forms, not interval-certified enclosures.

They are intentionally conservative. Direct finite summation of the exact entries is much smaller, as already observed numerically in v13.313. The purpose of this checkpoint is not sharpness; it is to establish the **infinite-tail decay mechanism analytically**.

---

## 6. What this proves and what it does not

This proves:

\[
\boxed{
\text{every fixed finite low-mode core decouples from the remote prime tail.}
}
\]

It does **not** prove that the moving boundary between a growing finite block and the tail decouples. Modes immediately below and above a cutoff can retain O(1) shift coupling.

Therefore the correct architecture remains

\[
\boxed{
\text{near-null core}
\oplus
\text{finite high-mode buffer/interface}
\oplus
\text{coercive tail}.
}
\]

The buffer must absorb the noncompact shift interface.

---

## 7. Audit continuity

The live ledger was checked before this checkpoint. Parallel work has continued beyond v13.313, including the defect-descent / stable-closure-strata line. Nothing in those updates invalidates the Suzuki tail analysis here; they remain complementary structural inputs to the broader unified framework.

The round-15 Hilbert-Schmidt objection remains resolved by the revised v13.303 estimate and the independent round-16 verification.

---

## 8. Next target

The present bound is rigorous but loose. The next high-leverage step is to exploit the **exact oscillatory matrix formula** rather than taking absolute values shift-by-shift.

There are two natural routes:

1. Parseval/Fourier-tail control for each truncated shift, obtaining exact tail energy after subtracting finitely many low coefficients;
2. direct combined-prime tail sums using the exact matrix formula, with a separately bounded asymptotic remainder.

Either route should move the analytic core-to-tail constant much closer to the numerical values from v13.313 and make a quantitative core-buffer-tail Schur estimate practical.
