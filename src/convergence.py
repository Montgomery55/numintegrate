import numpy as np
from .integrator import integrate_1d

def test_convergence(f, a, b, method, ns, reference_value, tol=1e-6):
    results = []
    hs = []
    errors = []

    for n in ns:
        if method == 'adaptive':
            val = integrate_1d(f, a, b, method=method)
            err = abs(val - reference_value)
            results.append({'n': None, 'h': None, 'value': val, 'error': err})
            break
        else:
            val = integrate_1d(f, a, b, method=method, n=n)
            h = (b-a) / n
            err = abs(val - reference_value)
            hs.append(h)
            errors.append(err)
            results.append({'n': n, 'h': h, 'value': val, 'error': err})

    rate = None
    if len(hs) >= 2:
        log_hs = np.log(hs)
        log_errs = np.log(errors)
        slope, intercept = np.polyfit(log_hs, log_errs, 1)
        rate = -slope
    return results, rate
