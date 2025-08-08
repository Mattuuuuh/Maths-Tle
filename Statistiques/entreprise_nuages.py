import numpy as np
import matplotlib.pyplot as plt

stats = np.load("entreprise1.npz")
print(stats.files)

num, anc, sex, sal, apbac = stats['num'], stats['anc'], stats['sex'], stats['sal'], stats['apbac']

colormap = ['pink' if s == 2 else 'blue' for s in sex]

plt.scatter(anc, sal, c=colormap)
plt.show()
plt.scatter(apbac, sal, c=colormap)
plt.show()
