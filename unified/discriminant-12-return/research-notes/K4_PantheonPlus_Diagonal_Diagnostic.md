# Direct Pantheon+ preliminary Hubble-diagram diagnostic, gravity k4
Date 2026-10-26. Parents v14.921, v14.922. Additive, Suzuki/quarter parked.
Official data: https://github.com/PantheonPlusSH0ES/DataRelease/blob/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat ; full covariance lives separately at Pantheon+SH0ES_STAT+SYS.cov. Read public table via GitHub connector.
Select m_b_corr, zHD>0.01, IS_CALIBRATOR==0, finite diagonal m_b_corr_err_DIAG>0, zHEL>0; N=1580 out of 1701 records. Use zHD for comoving distance integral, zHEL for photon flux prefactor: d_C=(1+zHEL)ln(1+zHD), d_LCDM=(1+zHEL)∫_0^zHD du/[.315(1+u)^3+.685]^1/2. Both dimensionless; nuisance magnitude offset A fitted independently to m_b_corr - 5log10(d) by minimizing Σ residual²/sigma_diag². χ²_C=786.1217145063, χ²_LCDM=697.6175999269, difference +88.5041145794; offsets A_C=23.88812561765, A_LCDM=23.80256473998. Simpson quadrature N=128 intervals for LCDM; reproducibility via code below.

**CRITICAL** This is a preliminary DIAGONAL-ERROR diagnostic only. The official 1701x1701 statistical-plus-systematic covariance was NOT ingested or inverted, so these values are not a publishable Pantheon+ likelihood, do not imply a significance/sigma, and do not constitute complete empirical falsification. The values of chi² per point are low and the error column is not a substitute for correctly marginalized full covariance. There is no full-covariance numerical result in this entry. Does demonstrate empirical-data input and shape tension for same nuisance count. Follow up with exact released covariance, full Gaussian likelihood and correct redshift/selection treatment, and independently audit.

Reproducer:
\`\`\`python
import numpy as np,pandas as pd
from scipy.integrate import quad
url='https://raw.githubusercontent.com/PantheonPlusSH0ES/DataRelease/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR/Pantheon%2BSH0ES.dat'
df=pd.read_csv(url,sep=r'\\s+')
a=df[(df.zHD>0.01)&(df.IS_CALIBRATOR==0)&(df.zHEL>0)&(df.m_b_corr_err_DIAG>0)]
def mu(z,zh,kind):
    I=np.log1p(z) if kind=='cone' else quad(lambda u: 1/np.sqrt(0.315*(1+u)**3+0.685),0,z)[0]
    return 5*np.log10((1+zh)*I)
for kind in ['cone','lcdm']:
    mm=np.array([mu(z,zh,kind) for z,zh in zip(a.zHD,a.zHEL)])
    y=a.m_b_corr.to_numpy()-mm;w=1/a.m_b_corr_err_DIAG.to_numpy()**2
    off=np.sum(w*y)/sum(w)
    print(kind,len(y),off,np.sum(w*(y-off)**2))
\`\`\`
Note notebook execution requires public network; official covariance-complete gate remains open.
