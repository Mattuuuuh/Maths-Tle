import numpy as np

data = np.load("entreprise1.npz")

anc, sal = data['anc'], data['sal']
#anc, sal = list(anc), list(sal)

#header
#anc = ["anc"]+anc
#sal = ["sal"]+sal

np.savetxt("entreprise-anc-sal.dat", np.transpose([anc, sal]), fmt=['%d', '%.2f'], header="anc sal")
