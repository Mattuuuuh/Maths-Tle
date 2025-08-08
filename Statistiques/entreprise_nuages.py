import numpy as np
import matplotlib.pyplot as plt

data = np.load("entreprise1.npz")
print(data.files)

num, anc, sex, sal, apbac = data['num'], data['anc'], data['sex'], data['sal'], data['apbac']

colormap = ['pink' if s == 2 else 'blue' for s in sex]

plt.scatter(anc, sal, c=colormap)
plt.show()
plt.scatter(apbac, sal, c=colormap)
plt.show()
