"""External audit (Round 141) independent check of v13.931's large-negative-
shift trivialization formula:

  H_a(z) = (1-iz)/(1+iz) * sinh(a(1+iz)) / sinh(a(1-iz))

claimed to decay to 0 locally uniformly on C_+ as a -> infinity, at the
rate exp(-2a*min(1, Im(z))).
"""
import cmath


def H_a(z, a):
    return (1 - 1j * z) / (1 + 1j * z) * cmath.sinh(a * (1 + 1j * z)) / cmath.sinh(a * (1 - 1j * z))


if __name__ == '__main__':
    for z in [0.5 + 0.3j, 1 + 1j, 2 + 0.5j]:
        y = z.imag
        rate = 2 * min(1, y)
        print(f"z={z}  (predicted decay rate exp(-{rate}*a)):")
        prev = None
        for a in [1, 2, 4, 8, 16]:
            val = abs(H_a(z, a))
            ratio = f"  ratio from prev a: {val/prev:.4e}" if prev else ""
            print(f"   a={a:3d}  |H_a(z)|={val:.6e}{ratio}")
            prev = val
        print()
