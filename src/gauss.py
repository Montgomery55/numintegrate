import numpy as np

def gauss_legendre(f, a, b, n=10):
    [x, w] = np.polynomial.legendre.leggauss(n)
    xp = 0.5 * (b-a) * x + 0.5 * (b+a)
    wp = 0.5 * (b-a) * w
    return np.sum(wp * f(xp))
