import numpy as np

def simpson(f, a, b, n=100):
    if n % 2 == 1:
        n += 1
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a)/n
    return h / 3 * (y[0] + 2*np.sum(y[2:n:2]) + 4*np.sum(y[1:n:2]) + y[n])
