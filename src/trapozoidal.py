import numpy as np

def trapozoidal(f, a, b, n=100):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b-a) / n # dX
    return h * (0.5 * y[0] + np.sum(y[1:-1] + 0.5 * y[-1]))
