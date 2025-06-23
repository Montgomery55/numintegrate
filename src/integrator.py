from .trapozoidal import trapozoidal
from .simpson import simpson
from .gauss import gauss_legendre
from .adaptive import adaptive_simpson
from .multidimensional import *


def integrate_nd(f, bounds, method='rectangle', n=10000):
    if method == 'rectangle':
        return rectangle_rule_nd(f, bounds, n)
    elif method == 'mc':
        return monte_carlo_nd(f, bounds, n)
    else:
        raise ValueError(f"Uknown method: {method}")

def integrate_1d(f, a, b, method="trapezoidal", n=100):
    if method == "trapezoidal":
        return trapozoidal(f, a, b, n)
    elif method == "simpson":
        return simpson(f, a, b, n)
    elif method == "gauss":
        return gauss_legendre(f, a, b, n)
    elif method == "adaptive":
        return adaptive_simpson(f, a, b)
    else:
        raise ValueError(f"Unknown method: {method}")
