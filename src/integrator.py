from .trapozoidal import trapozoidal
from .simpson import simpson
from .gauss import gauss_legendre
from .adaptive import adaptive_simpson

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
