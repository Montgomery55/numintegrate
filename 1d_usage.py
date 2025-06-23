import numpy as np
import scipy
from src.integrator import *

f = lambda x: np.exp(-x**2)
a, b = 0, 1
exact = 0.5*(np.pi)**(0.5)*scipy.special.erf(1)
trap = np.round(integrate_1d(f, a, b, method="trapezoidal", n=100), 6)
sim = np.round(integrate_1d(f, a, b, method="simpson", n=100), 6)
gauss = np.round(integrate_1d(f, a, b, method="gauss", n=100), 6)
adapt = np.round(integrate_1d(f, a, b, method="adaptive", n=100), 6)

print("Method, value, error" )
print(f"Trapezoidal: {trap}, {np.round(exact - trap, 6)}")
print(f"Simpson: {sim}, {np.round(exact - sim, 6)}")
print(f"Adaptive Simpson: {adapt}, {np.round(exact - adapt, 6)}")
print(f"Gauss-Legendre: {gauss}, {np.round(exact - gauss, 6)}")

