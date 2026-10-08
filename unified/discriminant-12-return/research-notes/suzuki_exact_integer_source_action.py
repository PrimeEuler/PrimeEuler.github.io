#!/usr/bin/env python3
"""Exact signed convolution and dyadic Suzuki source action.

Kronecker substitution uses carry-free nonnegative coefficient blocks. GMP
only multiplies two integers; all packing, signs, scales and bounds are Python
integers. No floating FFT participates in the independently checked action.
GNU import/export docs: https://gmplib.org/manual/Integer-Import-and-Export
The guarded 64-bit GMP 6.x ABI is documented under Integer-Internals.
"""
import ctypes as C
import ctypes.util
from fractions import Fraction as F
from math import isqrt
import random


class MPZ(C.Structure):
    _fields_ = [('allocated', C.c_int), ('size', C.c_int), ('limbs', C.c_void_p)]


_gmp = None


def gmp():
    global _gmp
    if _gmp is not None:
        return _gmp
    lib = C.CDLL(C.util.find_library('gmp'))
    version = C.c_char_p.in_dll(lib, '__gmp_version').value.decode()
    bits = C.c_int.in_dll(lib, '__gmp_bits_per_limb').value
    if version not in ('6.1.2', '6.2.0', '6.2.1', '6.3.0') or bits != 64 or C.sizeof(C.c_void_p) != 8:
        raise RuntimeError(('unsupported GMP ABI', version, bits))
    for name in ('init', 'clear'):
        fn = getattr(lib, '__gmpz_' + name)
        fn.argtypes = [C.POINTER(MPZ)]; fn.restype = None
    fn = getattr(lib, '__gmpz_import')
    fn.argtypes = [C.POINTER(MPZ), C.c_size_t, C.c_int, C.c_size_t,
                   C.c_int, C.c_size_t, C.c_void_p]; fn.restype = None
    fn = getattr(lib, '__gmpz_export')
    fn.argtypes = [C.c_void_p, C.POINTER(C.c_size_t), C.c_int, C.c_size_t,
                   C.c_int, C.c_size_t, C.POINTER(MPZ)]; fn.restype = C.c_void_p
    fn = getattr(lib, '__gmpz_mul')
    fn.argtypes = [C.POINTER(MPZ)] * 3; fn.restype = None
    _gmp = lib
    return lib


def multiply_bytes(a, b):
    lib = gmp(); x, y, z = MPZ(), MPZ(), MPZ()
    init, clear = getattr(lib, '__gmpz_init'), getattr(lib, '__gmpz_clear')
    imp, exp, mul = (getattr(lib, '__gmpz_' + n) for n in ('import', 'export', 'mul'))
    for v in (x, y, z): init(C.byref(v))
    try:
        ab, bb = C.create_string_buffer(a, len(a)), C.create_string_buffer(b, len(b))
        imp(C.byref(x), len(a), -1, 1, 0, 0, ab)
        imp(C.byref(y), len(b), -1, 1, 0, 0, bb)
        mul(C.byref(z), C.byref(x), C.byref(y))
        output = (C.c_ubyte * (len(a) + len(b)))()
        count = C.c_size_t()
        exp(output, C.byref(count), -1, 1, 0, 0, C.byref(z))
        assert count.value <= len(output)
        return bytes(output)
    finally:
        for v in (x, y, z): clear(C.byref(v))


def prefix(values):
    p = [0]; total = 0
    for v in values:
        total += v; p.append(total)
    return p


def convolution(a, b, start=0, count=None):
    """Exact selected coefficients of the ordinary signed convolution."""
    n, m = len(a), len(b)
    assert n and m
    if count is None: count = n + m - 1 - start
    assert 0 <= start <= n + m - 1 and 0 <= count <= n + m - 1 - start
    ba = max(abs(v).bit_length() for v in a)
    bb = max(abs(v).bit_length() for v in b)
    ca, cb = 1 << ba, 1 << bb
    # Shifted inputs <2^(ba+1), <2^(bb+1). Each coefficient has <=min(n,m)
    # terms. The strict spare bit prevents inter-block carries.
    block_bits = ba + bb + 2 + min(n, m).bit_length() + 1
    block_bytes = (block_bits + 7) // 8
    packed_a = b''.join((v + ca).to_bytes(block_bytes, 'little') for v in a)
    packed_b = b''.join((v + cb).to_bytes(block_bytes, 'little') for v in b)
    product = multiply_bytes(packed_a, packed_b)
    pa, pb = prefix(a), prefix(b)
    result = []
    for k in range(start, start + count):
        low, high = max(0, k - m + 1), min(n - 1, k)
        blo, bhi = k - high, k - low
        shifted = int.from_bytes(product[k * block_bytes:(k + 1) * block_bytes], 'little')
        result.append(shifted - cb * (pa[high + 1] - pa[low])
                      - ca * (pb[bhi + 1] - pb[blo]) - ca * cb * (high - low + 1))
    return result


def family_from_pairs(high, low):
    entries = []
    bits = 0
    for h, l in zip(high, low):
        nh, dh = h.as_integer_ratio(); nl, dl = l.as_integer_ratio()
        assert dh & (dh - 1) == 0 and dl & (dl - 1) == 0
        bh, bl = dh.bit_length() - 1, dl.bit_length() - 1
        bits = max(bits, bh, bl); entries.append((nh, bh, nl, bl))
    return {'bits': bits, 'values': [(nh << (bits - bh)) + (nl << (bits - bl))
                                    for nh, bh, nl, bl in entries]}


def frac(value, bits):
    return F(value, 1 << bits)


def dot(a, b):
    assert len(a['values']) == len(b['values'])
    return frac(sum(x * y for x, y in zip(a['values'], b['values'])),
                a['bits'] + b['bits'])


def norm2(a):
    return dot(a, a)


def sqrt_upper(q, bits=128):
    assert q >= 0
    numerator = q.numerator << (2 * bits)
    r = isqrt(numerator // q.denominator)
    if r * r * q.denominator < numerator: r += 1
    out = F(r, 1 << bits)
    assert out * out >= q
    return out


def source_families(data):
    out = {name: family_from_pairs(getattr(data, name + '_hi'), getattr(data, name + '_lo'))
           for name in ('z', 'diag', 'pole')}
    out['c'] = family_from_pairs([data.c_hi], [data.c_lo])
    out['alpha'] = int(data.alpha)
    out['modes'] = [int(n) for n in data.modes]
    halves = {}
    for name in ('z', 'diag', 'pole', 'c'):
        for side in ('hi', 'lo'):
            a = getattr(data, name + '_' + side)
            if name == 'c': a = [a]
            halves[name + '_' + side] = family_from_pairs(a, [type(x)(0) for x in a])
    out['represented_source_halves'] = halves
    # The decimal reconstruction slack used to widen the audited scalar caps.
    out['component_magnitude_checks'] = {}
    for name, limit in (('z', 100), ('diag', 100), ('pole', 2)):
        ok = all(abs(F(*x.as_integer_ratio())) < limit
                 for a in (getattr(data, name + '_hi'), getattr(data, name + '_lo')) for x in a)
        assert ok; out['component_magnitude_checks'][name] = True
    assert abs(frac(out['c']['values'][0], out['c']['bits'])) < 1
    assert abs(data.c_hi) < 1 and abs(data.c_lo) < 1
    out['component_magnitude_checks']['c'] = True
    return out


class ExactSource:
    def __init__(self, source, kernel_bits=256):
        self.source = source; self.kernel_bits = kernel_bits
        modes = source['modes']; self.n = len(modes)
        self.start = modes[0]
        assert self.start in (1, 2)
        assert modes == list(range(self.start, self.start + 2 * self.n, 2))
        scale = 1 << kernel_bits; n = self.n
        self.toeplitz = [(-1 if k < 0 else 1) * (scale // (2 * abs(k))) if k else 0
                         for k in range(-n + 1, n)]
        self.hankel = [scale // (2 * (k + self.start)) for k in range(2 * n - 1)]

    def action(self, x):
        n, kb, s = self.n, self.kernel_bits, self.source
        z, d, p, c = (s[k] for k in ('z', 'diag', 'pole', 'c'))
        xv, zb = x['values'], z['bits']
        assert len(xv) == n
        zx = [a * b for a, b in zip(z['values'], xv)]
        tv = convolution(xv, self.toeplitz, n - 1, n)
        tz = convolution(zx, self.toeplitz, n - 1, n)
        hv = convolution(xv[::-1], self.hankel, n - 1, n)
        hz = convolution(zx[::-1], self.hankel, n - 1, n)
        conv_bits = c['bits'] + zb + x['bits'] + kb + 1
        diag_bits = d['bits'] + x['bits']
        pole_bits = 2 * p['bits'] + x['bits']
        yb = max(conv_bits, diag_bits, pole_bits)
        pole_dot = sum(a * b for a, b in zip(p['values'], xv))
        cv = c['values'][0]; y = []
        for i in range(n):
            # Removing the artificial Hankel diagonal keeps the diagonal
            # exactly diag_i + alpha*p_i^2 for this same symmetric point A.
            mixed = z['values'][i] * (tv[i] - hv[i]) - tz[i] - hz[i]
            mixed += 2 * z['values'][i] * self.hankel[2 * i] * xv[i]
            value = (cv * mixed) << (yb - conv_bits)
            value += (d['values'][i] * xv[i]) << (yb - diag_bits)
            value += (s['alpha'] * p['values'][i] * pole_dot) << (yb - pole_bits)
            y.append(value)
        return {'bits': yb, 'values': y}


def split_value(value, bits):
    """Nearest 64-bit high, then nearest 64-bit residual; ties to even."""
    import numpy as np
    def rounded(n):
        sign = -1 if n < 0 else 1; n = abs(n)
        shift = max(0, n.bit_length() - 64)
        q, r = divmod(n, 1 << shift)
        if shift and (r * 2 > 1 << shift or r * 2 == 1 << shift and q % 2): q += 1
        return sign * q, shift
    q, shift = rounded(value)
    high = np.ldexp(np.longdouble(str(q)), shift - bits)
    rem = value - (q << shift)
    ql, sl = rounded(rem)
    low = np.ldexp(np.longdouble(str(ql)), sl - bits)
    return high, low


class ExactBackend:
    def __init__(self, data, kernel_bits=256):
        self.source = source_families(data)
        self.engine = ExactSource(self.source, kernel_bits)
        self.last_inputs = self.last_outputs = None

    def action_arrays(self, high, low):
        import numpy as np
        columns = [family_from_pairs(high[:, j], low[:, j]) for j in range(high.shape[1])]
        actions = [self.engine.action(v) for v in columns]
        yh, yl = np.empty_like(high), np.empty_like(low)
        for j, y in enumerate(actions):
            for i, v in enumerate(y['values']):
                yh[i, j], yl[i, j] = split_value(v, y['bits'])
        self.last_inputs, self.last_outputs = columns, actions
        return yh, yl


def self_test():
    rng = random.Random(165)
    for n in (1, 2, 7, 31):
        for m in (1, 3, 12):
            a = [rng.randint(-10**30, 10**30) for _ in range(n)]
            b = [rng.randint(-10**25, 10**25) for _ in range(m)]
            expected = [sum(a[i] * b[k-i] for i in range(n) if 0 <= k-i < m)
                        for k in range(n + m - 1)]
            assert convolution(a, b) == expected
    checked = 0
    for start, alpha in ((1, 2), (2, -2)):
        n, sb, vb, kb = 13, 40, 35, 100
        source = {name: {'bits': sb, 'values': [rng.randint(-10**6, 10**6) for _ in range(n)]}
                  for name in ('z', 'diag', 'pole')}
        source.update({'c': {'bits': sb, 'values': [123456789]}, 'alpha': alpha,
                       'modes': list(range(start, start + 2*n, 2))})
        engine = ExactSource(source, kb)
        x = {'bits': vb, 'values': [rng.randint(-10**8, 10**8) for _ in range(n)]}
        y = engine.action(x)
        for i in range(n):
            expected = F(0)
            for j in range(n):
                zi, zj = (frac(source['z']['values'][k], sb) for k in (i, j))
                pi, pj = (frac(source['pole']['values'][k], sb) for k in (i, j))
                if i == j: a = frac(source['diag']['values'][i], sb)
                else:
                    kt = frac(engine.toeplitz[i - j + n - 1], kb)
                    kh = frac(engine.hankel[i + j], kb)
                    a = frac(source['c']['values'][0], sb) * ((zi-zj)*kt-(zi+zj)*kh)/2
                    true_t = F(1, 2*(i-j))
                    true_h = F(1, 2*(i+j+start))
                    true_a = frac(source['c']['values'][0], sb)*((zi-zj)*true_t-(zi+zj)*true_h)/2
                    assert abs(a-true_a) <= F(22, 1 << kb)
                a += alpha * pi * pj
                expected += a * frac(x['values'][j], vb)
            assert frac(y['values'][i], y['bits']) == expected
        checked += 1
    assert sqrt_upper(F(2))**2 >= 2
    return {'signed_convolution_cases': 12, 'dense_fraction_source_action_cases': checked,
            'rational_kernel_enclosure_cases': checked,
            'all_exact': True}


if __name__ == '__main__':
    import json
    print(json.dumps(self_test(), indent=2))
