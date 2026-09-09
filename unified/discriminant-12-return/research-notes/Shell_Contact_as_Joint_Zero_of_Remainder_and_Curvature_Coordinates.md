# Shell Contact as Joint Zero of Remainder and Curvature Coordinates

## Status
Exact continuation of v13.362--v13.368. This note isolates a two-coordinate criterion for divisor-shell contact inside each quotient block.

## 1. Quotient-block coordinates
Let
\[
q=\left\lfloor\frac nk\right\rfloor,
\qquad
R_q=\left\lfloor\frac nq\right\rfloor.
\]
Define the terminal remainder
\[
\boxed{s_q:=n-qR_q=n\bmod q}
\]
and the curvature/transport coordinate
\[
\boxed{C_{k,q}:=q(R_q-k)}.
\]
Then the shell defect is
\[
\boxed{\Delta_k=n-kq=s_q+C_{k,q}}.
\]
Both terms are nonnegative.

## 2. Separate zero loci
Because
\[
s_q=n\bmod q,
\]
we have
\[
\boxed{s_q=0\iff q\mid n.}
\]
Because \(q>0\),
\[
\boxed{C_{k,q}=0\iff k=R_q.}
\]
Thus the two coordinates detect different structures:
- \(s_q\): arithmetic divisibility of the quotient label \(q\);
- \(C_{k,q}\): geometric terminality of the column inside its horizontal quotient block.

## 3. Joint-zero contact criterion
Since
\[
\Delta_k=s_q+C_{k,q}
\]
with both terms nonnegative,
\[
\boxed{\Delta_k=0\iff s_q=0\ \text{and}\ C_{k,q}=0.}
\]
Equivalently,
\[
\boxed{kq=n\iff q\mid n\ \text{and}\ k=R_q.}
\]
At joint zero,
\[
R_q=\frac nq,
\]
so the endpoint is exactly
\[
\boxed{(k,q)=\left(\frac nq,q\right)}
\]
on the factor shell \(uv=n\).

## 4. Three strata in the two-coordinate plane
The nonnegative pair
\[
(s_q,C_{k,q})
\]
organizes the known strata:

### Contact
\[
s_q=0,\qquad C_{k,q}=0.
\]
Then \(\Delta_k=0\).

### Stable off-shell terminal
\[
s_q>0,\qquad C_{k,q}=0.
\]
Then \(k=R_q\) but \(q\nmid n\), so
\[
\Delta_k=s_q>0.
\]

### Strict descent/interior
\[
C_{k,q}>0.
\]
Then \(k<R_q\), and
\[
\Delta_k>s_q.
\]
The remainder coordinate may vanish or not, but the positive transport coordinate prevents shell contact.

Therefore the impossible quadrant for an actual quotient-block column is not \(s_q=0,C>0\); that case is possible and corresponds to an interior column in a block whose terminal endpoint is a true divisor contact. What is special is only the joint origin.

## 5. Geometric interpretation
By mixed curvature,
\[
C_{k,q}
=\sum_{C\subset[k,R_q]\times[0,q]}\Delta_u\Delta_v(Y^2).
\]
For unit lattice cells,
\[
C_{k,q}=4\sum M_F^2.
\]
Hence
\[
\boxed{
\Delta_k
=\underbrace{s_q}_{\text{terminal arithmetic remainder}}
+\underbrace{4\sum M_F^2}_{\text{accumulated mixed-curvature transport}}.
}
\]
Shell contact occurs precisely when both the terminal remainder and accumulated transport vanish.

## 6. Relation to the product-field gauge orbit
The transport coordinate gives only the product
\[
C_{k,q}=q(R_q-k).
\]
As v13.368 showed, product data does not separate the two factors without additional block information. Here that additional information is available because the quotient decomposition supplies \(q\) and \(R_q\) independently.

Thus the divisor staircase breaks the reciprocal product-field ambiguity by furnishing a canonical quotient label.

This should be read as a property of the arithmetic quotient decomposition, not as a universal breaking of the product-field rank-one degeneracy.

## 7. Prime/composite consequence
For every divisor \(q\mid n\), the quotient block has a joint-zero terminal endpoint. Therefore the number of joint-zero block endpoints is exactly
\[
\boxed{\tau(n)}.
\]
For \(n>1\),
\[
\boxed{\tau(n)=2\iff n\text{ is prime}.}
\]
This is the already-known divisor-count criterion, now expressed in the two-coordinate remainder/curvature geometry.

No stronger primality criterion is claimed.

## 8. Guardrails
- Zero transport alone means terminality, not divisibility.
- Zero remainder alone means \(q\mid n\), not that the current column \(k\) is the shell contact.
- Shell contact requires the simultaneous zero.
- This is an exact reformulation of quotient-block Euclidean division and mixed finite differences, not a factoring algorithm.
- The quarter mode enters only through the transport coordinate and does not replace the arithmetic remainder condition.
