#!/usr/bin/env python3
"""Gravity v15.1416: coupled A_z,u,v nonlinear H2 sigma action in 1+1D,
with simplified frozen tidal-component interaction g*F_tz*Omega_uv*B_tx.
This is a local variational truncation, NOT the complete covariant
Weyl tensor with all components or dynamical metric Einstein gravity.
JAX automatic Hamiltonian gradients (x periodic, Fourier spectral).
"""
import os
os.environ["JAX_ENABLE_X64"]="True"
os.environ["XLA_FLAGS"]="--xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=1"
import jax
import jax.numpy as jnp
import numpy as np
from scipy.integrate import solve_ivp
jax.config.update("jax_enable_x64",True)
def run(N=16,g=.12,T=1.6):
 x=jnp.arange(N)*2*jnp.pi/N
 k=jnp.fft.fftfreq(N,d=1/N)
 def Dx(v):return jnp.fft.ifft(1j*k*jnp.fft.fft(v)).real
 def getmetric(u,v):
  D=1+u*u+v*v
  return 1-u*u/D,-u*v/D,1-v*v/D,1/jnp.sqrt(D)
 def Hamiltonian(q,p):
  Az,u,v=q;pa,pu,pv=p
  ax,ux,vx=jax.vmap(Dx)(q)
  guu,guv,gvv,omega=getmetric(u,v)
  one=jnp.ones_like(u)
  M=jnp.stack([
   jnp.stack([one,g*omega*vx,-g*omega*ux],axis=-1),
   jnp.stack([g*omega*vx,guu,guv],axis=-1),
   jnp.stack([-g*omega*ux,guv,gvv],axis=-1)],axis=-2)
  PP=p.T
  velocities=jnp.linalg.solve(M,PP[...,None])[...,0]
  return jnp.mean(jnp.sum(PP*velocities,axis=1)/2+
      ax*ax/2+(guu*ux*ux+2*guv*ux*vx+gvv*vx*vx)/2)
 grad=jax.jit(jax.grad(Hamiltonian,argnums=(0,1)))
 energy=jax.jit(Hamiltonian)
 q=np.zeros((3,N))
 q[1]=.16*np.sin(np.array(x))
 q[2]=.13*np.sin(2*np.array(x)+.3)
 q=jnp.array(q)
 _,ux,vx=jax.vmap(Dx)(q)
 u,v=q[1:]
 guu,guv,gvv,omega=getmetric(u,v)
 ut=.16*jnp.cos(x);vt=-.13*jnp.cos(2*x+.3)
 p=jnp.array([g*omega*(ut*vx-ux*vt),guu*ut+guv*vt,guv*ut+gvv*vt])
 y0=np.asarray(jnp.concatenate((q.ravel(),p.ravel())))
 def rhs(t,y):
  Q=jnp.asarray(y[:3*N]).reshape(3,N)
  P=jnp.asarray(y[3*N:]).reshape(3,N)
  dQ,dP=grad(Q,P)
  # H is a spatial MEAN, so lattice Hamilton equations use N*grad.
  return np.r_[np.array(N*dP).ravel(),np.array(-N*dQ).ravel()]
 sol=solve_ivp(rhs,(0,T),y0,rtol=2e-9,atol=3e-11,
               method="DOP853",dense_output=True)
 assert sol.success
 def split(y):
  Q=jnp.asarray(y[:3*N]).reshape(3,N)
  P=jnp.asarray(y[3*N:]).reshape(3,N)
  Az,u,v=Q
  Ax,ux,vx=jax.vmap(Dx)(Q)
  guu,guv,gvv,omega=getmetric(u,v)
  one=jnp.ones_like(u)
  M=jnp.stack([
   jnp.stack([one,g*omega*vx,-g*omega*ux],axis=-1),
   jnp.stack([g*omega*vx,guu,guv],axis=-1),
   jnp.stack([-g*omega*ux,guv,gvv],axis=-1)],axis=-2)
  At,ut,vt=jnp.linalg.solve(M,P.T[...,None])[...,0].T
  EA=jnp.mean((At*At+Ax*Ax)/2)
  ES=jnp.mean((guu*(ut*ut+ux*ux)+
       2*guv*(ut*vt+ux*vx)+gvv*(vt*vt+vx*vx))/2)
  EM=jnp.mean(g*At*omega*(ut*vx-ux*vt))
  return float(EA),float(ES),float(EM),float(jnp.min(jnp.linalg.eigvalsh(M)))
 snapshots=[sol.sol(t) for t in np.linspace(0,T,14)]
 E=np.array([float(energy(jnp.asarray(y[:3*N]).reshape(3,N),
                      jnp.asarray(y[3*N:]).reshape(3,N))) for y in snapshots])
 eA,eS,eM,min_eig=split(sol.y[:,-1])
 rmsA=float(np.sqrt(np.mean(sol.y[:N,-1]**2)))
 residual=float(np.max(abs(E-E[0]))/E[0])
 assert residual<1e-7 and min_eig>0.9
 assert abs(eA+eS+eM-E[-1])<1e-12
 result=dict(N=N,g=g,T=T,total_initial=float(E[0]),relative_energy_drift=residual,
    A_rms=rmsA,EM_energy=eA,H2_energy=eS,interaction_energy=eM,
    minimum_kinetic_eigenvalue=min_eig)
 print(result,flush=True)
 return result
if __name__=="__main__":
 a=run();b=run(g=.06);c=run(g=0);d=run(N=24)
 assert a["A_rms"]>0 and c["A_rms"]==0
 assert 1.95<a["A_rms"]/b["A_rms"]<2.05
 assert abs(a["A_rms"]-d["A_rms"])<2e-7
 print("PASS reduced curved-H2 coupled Hamiltonian energy, positive kinetic and zero coupling")
 print("OPEN complete covariant Weyl curvature, Einstein metric and quarter-grid selector")
