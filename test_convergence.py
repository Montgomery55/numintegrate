import numpy as np
from src.convergence import test_convergence

f = lambda x: x**5 + 3*x**2 - 6
a, b = 0, 10
exact = 502820/3

ns = [2**i for i in range(0,10)]

for method in ['trapezoidal', 'simpson', 'gauss']:
    results = test_convergence(f, a, b, method, ns, exact)
    print(f"\nMethod: {method}")
    for r in results:
        print(f"n = {r['n']:>4}, value = {r['value']:.10f}, error = {r['error']:.2e}")


