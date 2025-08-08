import numpy as np

data = np.load("entreprise1.npz")

anc, sal = data['anc'], data['sal']
#anc, sal = list(anc), list(sal)

#header
#anc = ["anc"]+anc
#sal = ["sal"]+sal

np.savetxt("entreprise1.dat", np.transpose([anc, sal]), fmt=['%.f', '%.2f'], header="anc sal")
#fmt=['%.3f', '%.3f'])
