"""STARK = THE CONE'S OFFSET (2026-10-22). dE = (3/2) n (n1-n2) F (a.u.);
offset = (n1-n2)/2 is the diameter-secant offset of the (n,k) machine,
so dE = 3 n F * offset. States (n1,n2,m), n1+n2+|m|+1 = n, weight 1
for m=0 else 2. Reproduces the textbook first-order Stark tables."""
from collections import Counter
for n in (2, 3):
    tab = Counter()
    for n1 in range(n):
        for n2 in range(n):
            for am in range(n):
                if n1 + n2 + am + 1 == n:
                    tab[3*n*((n1-n2)/2)] += (1 if am == 0 else 2)
    print(f'n={n}: total {sum(tab.values())} states (= n^2 = {n*n});  table:',
          {f'{k:+.1f}': tab[k] for k in sorted(tab, reverse=True)})
print('Textbook: n=2 {+3:1, 0:2, -3:1};  n=3 {+9:1, +4.5:2, 0:3, -4.5:2, -9:1}.')
