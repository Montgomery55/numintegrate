import numpy as np
from .integrator import integrate_1d

def test_convergence(f, a, b, method, ns, reference_value, tol=1e-6):
    results = []
    for n in ns:
        if method == 'adaptive':
            val = integrate_1d(f, a, b, method=method)
            err = abs(val - reference_value)
            results.append({'n': None, 'value': val, 'error': err})
            break
        else:
            val = integrate_1d(f, a, b, method=method, n=n)
            err = abs(val - reference_value)
            results.append({'n': n, 'value': val, 'error': err})
    return results
