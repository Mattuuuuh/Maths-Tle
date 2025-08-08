import numpy as np
import matplotlib.pyplot as plt

N=34
num = [i+1 for i in range(N)]

# ancienneté aléatoire.
# peut-être changer la distribution discrète pour discuter
# de la variable catégorique <=5 ans, >= 5 ans ; turnover ?
anc = [int(np.random.rand()*13) for i in range(N)]

# sexe
# 1 = homme, 2 = femme (sécurité sociale)
p = .4 # proportion de femmes
sex = [1+(np.random.rand()<p) for i in range(N)]

# salaires linéaires wrt. anc + perturbation normale
# INSEE: Pour le même emploi exercé dans le même établissement, 
# l’écart de salaire net en équivalent temps plein se réduit à 3,8 %.
a = 43
b = 1426 # SMIC net 2025
sigma = 50
sal = [int(a*anc[i] + b + np.random.normal(0, sigma))*(1-.038*(sex[i]-1)) for i in range(N)]

# nombre d'années d'études après le bac
# entre 0 et 5
apbac = [int(np.random.rand()*6) for i in range(N)]

# le CEO
# Rémunération dans les grandes entreprises: entre PDG et salariés, 
# les écarts se creusent. L'ONG Oxfam a calculé qu'en moyenne, 
# les dirigeants des 100 principaux groupes cotés en France perçoivent 
# une rémunération 97 fois plus élevée que le salaire moyen de leurs salariés
anc[-2] = 12
sex[-2] = 1
sal[-2] = 10*np.mean(sal)

# le neveu du CEO
anc[-1]=2
sex[-1]=1
sal[-1]=2*(b+2*a)

## 
x = anc
y = sal

plt.scatter(x,y)
plt.show()

##

#np.savez("fewpoints", num=num, anc = anc, sex = sex, sal=sal, apbac=apbac)
np.savetxt(
        "entreprise.dat",
        np.transpose([num, anc, sex, sal, apbac]), 
        fmt=['%d', '%d', '%d', '%.2f', '%d'],
        header="num anc sex sal apbac",
        comments='',
)

