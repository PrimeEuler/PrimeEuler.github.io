// Column-order implementation of suzuki_ldd_source_operator.matvec.
// Compile without fast-math or contraction. This is midpoint arithmetic,
// not a directed-rounding source-operator certificate.
#include <cstdint>
#include <cstddef>
#include <limits>

using L = long double;
struct DD { L h, l; };
constexpr L split = 4294967297.0L;

static inline DD two_sum(L a, L b) {
    L s=a+b, bb=s-a;
    return {s,(a-(s-bb))+(b-bb)};
}
static inline DD two_prod(L a, L b) {
    L p=a*b, ca=split*a, ah=ca-(ca-a), al=a-ah;
    L cb=split*b, bh=cb-(cb-b), bl=b-bh;
    L e=((ah*bh-p)+ah*bl+al*bh)+al*bl;
    return {p,e};
}
static inline DD add(DD a, DD b) {
    DD s=two_sum(a.h,b.h);
    L t=a.l+b.l+s.l;
    return two_sum(s.h,t);
}
static inline DD sub(DD a, DD b) { return add(a,{-b.h,-b.l}); }
static inline DD mul(DD a, DD b) {
    DD p=two_prod(a.h,b.h);
    L e=p.l+a.h*b.l+a.l*b.h+a.l*b.l;
    return two_sum(p.h,e);
}
static inline DD mul_d(DD a, L b) {
    DD p=two_prod(a.h,b);
    return two_sum(p.h,p.l+a.l*b);
}
static inline DD div_d(DD a, L b) {
    L q1=a.h/b;
    DD r=sub(a,two_prod(q1,b));
    L q2=(r.h+r.l)/b;
    return add({q1,0},{q2,0});
}

extern "C" int cone_lddd_matvec(
    std::int64_t n, std::int64_t r, const std::int64_t* modes,
    const L* zh, const L* zl, const L* dh, const L* dl,
    const L* ph, const L* pl, const L* parameters,
    const L* xh, const L* xl, L* yh, L* yl) {
    if (n<1 || r<1 || std::numeric_limits<L>::digits!=64) return 1;
    const DD c={parameters[0],parameters[1]};
    const L alpha=parameters[2];
    for (std::int64_t q=0;q<n*r;++q) { yh[q]=0;yl[q]=0; }
    for (std::int64_t j=0;j<n;++j) {
        bool active=false;
        for (std::int64_t k=0;k<r;++k)
            if(xh[j*r+k]!=0 || xl[j*r+k]!=0) {active=true;break;}
        if (!active) continue;
        const L nj=static_cast<L>(modes[j]);
        const DD zj={zh[j],zl[j]}, pj={ph[j],pl[j]};
        const DD diag=add({dh[j],dl[j]},mul_d(mul(pj,pj),alpha));
        for (std::int64_t i=0;i<n;++i) {
            DD a;
            if (i==j) { a=diag; }
            else {
                L ni=static_cast<L>(modes[i]);
                DD num=sub(mul_d({zh[i],zl[i]},nj),mul_d(zj,ni));
                DD off=mul(c,div_d(num,ni*ni-nj*nj));
                a=add(off,mul_d(mul({ph[i],pl[i]},pj),alpha));
            }
            for (std::int64_t k=0;k<r;++k) {
                const std::int64_t pos=i*r+k;
                DD product=mul(a,{xh[j*r+k],xl[j*r+k]});
                DD y=add({yh[pos],yl[pos]},product);
                yh[pos]=y.h;yl[pos]=y.l;
            }
        }
    }
    return 0;
}
