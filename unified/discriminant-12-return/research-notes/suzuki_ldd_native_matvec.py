"""Strict-arithmetic native acceleration of the existing LDDD midpoint action."""
import ctypes
from functools import lru_cache
from pathlib import Path
import subprocess
import tempfile
import numpy as np

@lru_cache(maxsize=1)
def _library():
    if np.finfo(np.longdouble).nmant != 63:
        raise RuntimeError("native kernel requires a 64-bit longdouble significand")
    root=Path(tempfile.mkdtemp(prefix="cone-lddd-kernel-"))
    output=root/"kernel.so"
    source=Path(__file__).with_suffix(".cpp")
    subprocess.run(["g++","-std=c++17","-O3","-fno-fast-math","-ffp-contract=off",
                    "-shared","-fPIC",str(source),"-o",str(output)],check=True)
    lib=ctypes.CDLL(str(output));f=lib.cone_lddd_matvec
    pointer=ctypes.c_void_p
    f.argtypes=[ctypes.c_int64,ctypes.c_int64]+[pointer]*12
    f.restype=ctypes.c_int
    return lib

def native_matvec(data,xh,xl):
    xh=np.ascontiguousarray(xh,dtype=np.longdouble)
    xl=np.ascontiguousarray(xl,dtype=np.longdouble)
    if xh.ndim!=2 or xh.shape!=xl.shape or len(xh)!=len(data.modes):
        raise ValueError("native matvec input shape mismatch")
    yh=np.zeros_like(xh);yl=np.zeros_like(xl)
    arrays=[np.ascontiguousarray(data.modes,dtype=np.int64)]
    arrays.extend(np.ascontiguousarray(a,dtype=np.longdouble) for a in
                  [data.z_hi,data.z_lo,data.diag_hi,data.diag_lo,data.pole_hi,data.pole_lo])
    arrays.append(np.array([data.c_hi,data.c_lo,data.alpha],dtype=np.longdouble))
    arrays.extend([xh,xl,yh,yl])
    result=_library().cone_lddd_matvec(*xh.shape,*(a.ctypes.data for a in arrays))
    if result:
        raise RuntimeError(("native matvec rejected input/runtime",result))
    return yh,yl
