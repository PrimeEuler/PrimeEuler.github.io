# Cone Derivation Ledger v15.922 — Exact legacy WebGL hyperbola/parabola intersections and divisor count

**Date:** 2026-11-13 US Eastern. **Track:** Gravity/EM geometric machine. **Parent:** v15.921 inspection of owner's original `webgl/index.html` plus earlier diameter-secant/divisor summatory notes (v14.550, v14.767, v15.906). **User correction:** Each constant-product hyperbolic height N should be intersected with each parabola row at **X=±(N−k²)/(2k)** rather than borrowing a horizontal coordinate from the separately sampled cone point. **Immediately prewrite live HEAD:** 8462acc1069228d5df9d43f2d84da3218f5ace10. Target path checked absent. Additive only; original historical WebGL page remains untouched, as do certified and other lanes' objects.

**Status:** [D] exact intersection formulas including ± branches; [D] explicit scaled t factor; [D] exact integer-divisor count of lattice intersections; [N] exact SymPy and finite divisor sweep; [O] dynamical/physical meaning of these intersection points, if any.

## Gate 643 — exact point placement

Original source's hyperbola branch is plotted by setting `Y=sqrt(N)`, `T=sqrt(X²+Y²)`. The cone mesh has fixed-factor parabolas `Y²=b²+2bX` with b the scaled row coordinate. On the mirror branch `Y²=b²−2bX`. Intersect either with the hyperbolic slice `Y²=N` to obtain **X_±=±(N−b²)/(2b)** and **T=(N+b²)/(2b)** (b>0). Define a=N/b: then

**X_±=±(a−b)/2, Y=sqrt(ab)=sqrt N, T=(a+b)/2**.

Consequently the intersection is not an arbitrary marker: it is exactly the AM–GM diameter–secant station, where `D=a+b`, `R=D/(a−b)` for the unmirrored noncentral branch, and the shared hyperbola imposes `ab=N`. The plus and minus points correspond to the two orientations of the same unordered factor pair, not two physically independent transitions. If a=b=sqrt N, X=0 and both mirror branches coincide: do not double count the central square-root seat.

## Gate 644 — legacy division scale and integer products

In the old WebGL cone constructor, `X=[(n+1)/2−k]/t`, `Y=sqrt[k(n+1−k)]/t`, and `T=sqrt(X²+Y²)`. The separately plotted hyperbolic height `sqrt N` does **not** divide by t. Therefore each legacy sector t has factor row **b=k/t**, and the *correct hyperbola/parabola intersection* is

**X_±=±[N−(k/t)²]/[2(k/t)]=±[Nt²−k²]/(2kt)**,
**Y=sqrt N**,
**T=[Nt²+k²]/(2kt)**.

If both original cone factors are integer mesh labels a0,k, then a0*k=N*t², with physical coordinates (a0/t,k/t). Hence **the integer lattice intersection criterion is `k divides Nt²`**, assuming N and t are positive integers. A physical hyperbola slice N at division t samples the divisor geometry for **Nt²**, not simply d(N), unless t=1. A continuum slice with noninteger N still has real intersections but not integer-lattice divisor points. This is the same normalization issue flagged in v15.921; mixing u=1/t and N would generate spurious counts.

At each fixed (N,t) integer-lattice slice, enumerate k≤sqrt(Nt²) with k|Nt², and reflect the resulting noncentral X to −X. You obtain **exactly d(Nt²) unique oriented X intersections**; at perfect square Nt² the central X=0 contributes once. This is an exact *arithmetic counting* theorem for the chosen lattice, **not a claim of new physical degeneracies or a particle spectrum**. For example N=12,t=1 gives pairs (12,1),(6,2),(4,3), with X=±11/2, ±2, ±1/2: six points =d(12)=6.

The old code's loops only include n up to tN and k≤n. Because a0+k−1=n, these historical finite loop bounds can omit otherwise valid intersections; a complete intersection plotting routine should enumerate divisors directly rather than presume the old sampling range enumerates all divisor pairs.

## Gate 645 — suggested additive visualization routine

In the existing Three.js renderer, after the original common pixel `scale` is chosen, replace the hyperbola's borrowed cone X position with a direct intersection calculation such as:

```javascript
function plotHyperbolaParabolaIntersections(particles, N, k, t, scale) {
    if (!(N > 0 && k > 0 && t > 0)) return;
    const b = k / t;
    const X = (N - b * b) / (2 * b);
    const Y = Math.sqrt(N);
    const T = Math.hypot(X, Y);
    GenerateParticles(particles,  X * scale, Y * scale, T * scale);
    if (Math.abs(X) > 1e-12) {
        GenerateParticles(particles, -X * scale, Y * scale, T * scale);
    }
}
```

`GenerateParticles` itself mirrors ±Y and ±T to show the upper/lower double cones, but **does not mirror X**, so the ±X call is needed. Calling it twice at X=0 would duplicate the seat. For non-square N or noninteger sector scaling, these are still valid real-coordinate intersections; use an explicit integer divisibility filter if the intent is to count only arithmetic factor lattice points.

## Gate 646 — physical status and next test

The owner-specified formula exactly connects each fixed-row parabola and a hyperbolic shell to the pairwise AM–GM circle station; it supplies a direct geometric interpretation for the divisor function and earlier `d_u(u²n)=d(n)` scale dictionary, subject to consistent N/t normalization. The functions `d` and `D` count arithmetic lattice points; physical EM radiative lifetimes remain connected to separately normalized cross-principal-shell dipole operators, and no SI acceleration/temporal evolution follows from static intersections alone.

**Reproducer:** `research-notes/k4_webgl_parabola_hyperbola_intersections_v15_922.py`, commit 8462acc1069228d5df9d43f2d84da3218f5ace10. Exact SymPy pair algebra and sweeps over N=1,4,12,16,25,36 and t=1,2,3 confirm all hyperbola/parabola intersections, ± central-seat treatment, and divisor count d(Nt²). External independent Audit pending.

**Next:** Plot the full divisor intersection lattice against a fixed-sum Schwinger shell and identify whether some *independently derived* cross-shell dipole matrix coefficient (not merely sqrt(ab)) can be expressed as a signed/weighted sum over the intersection points, preserving E1 selection rules, KS physical normalization, and the v15.920 2p/3p lifetime results. Record negative test if the geometric divisor weights fail.
