#!/usr/bin/env python3
"""v15.693: inequivalent parity pullbacks of q=2 shell grading to factor pairs.

Neither mapping L=ab nor L=a+b is a physically selected Cone-to-factor
dictionary. Both define valid integer parities and give different results.
"""
def D(n):
    return sum(n//a for a in range(1,n+1))
def brute(n):
    return (
        sum((-1)**(a*b) for a in range(1,n+1) for b in range(1,n//a+1)),
        sum((-1)**(a+b) for a in range(1,n+1) for b in range(1,n//a+1)),
    )
def closed(n):
    d0,d2,d4=D(n),D(n//2),D(n//4)
    return -d0+4*d2-2*d4, d0-4*d2+4*d4
for n in range(1,151):
    assert brute(n)==closed(n)
for n in (4,8,16,32,64,256,1024,4096,65536):
    p,s=closed(n)
    print(n,D(n),p,s,p/D(n),s/D(n))
print("PASS: distinct exact parity pullbacks and divisor identities")
