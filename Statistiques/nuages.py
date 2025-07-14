import numpy as np
import matplotlib.pyplot as plt

# machine learning curve is log(y) = alog(x) + b, ie. y = Bx^a.
def f(x):
    a = -.5
    b=10
    B = 2**b
    return B*x**a

# gaussian noise
def gaussian(sigma=10, mu=0):
    return np.random.normal(mu, sigma)

# N samples from uniform distribution on [a, b]
# each sample is (x,f(x)) + noise(mu,sigma)
def samples(N, a, b, sigma=10, mu=0):
    S = []
    for _ in range(N):
        x = np.random.rand()*(b-a)+a
        noise = gaussian(sigma, mu)
        S+=[(x,f(x)+noise)]
    return S

S = samples(500, 16, 512)
print(S)

# hopefully same enumeration order...
x = [s[0] for s in S]
y = [s[1] for s in S]

plt.scatter(x,y)
plt.show()


