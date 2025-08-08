import numpy as np

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
sigma = 10
sal = [int(a*anc[i] + b + np.random.normal(0, 10))*(1-.038*(sex[i]-1)) for i in range(N)]

# nombre d'années d'études après le bac
# entre 0 et 5
apbac = [int(np.random.rand()*6) for i in range(N)]


## 


np.savez("entreprise1", num=num, anc = anc, sex = sex, sal=sal, apbac=apbac)



