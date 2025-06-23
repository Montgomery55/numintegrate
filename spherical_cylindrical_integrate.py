import numpy as np
import scipy
from src.integrator import *
from src.multidimensional import *

def f(X):
    r = np.linalg.norm(X, axis=1)
    return np.exp(-r**2)

val = integrate_spherical(
    f,
    r_bounds=(0, 5),
    theta_bounds=(0, np.pi),
    phi_bounds=(0, 2*np.pi),
    n=100
)
print("Spherical integral ≈", val)

f = lambda X: np.ones(X.shape[0])  # Volume of shell

val = integrate_cylindrical(
    f,
    r_bounds=(1, 2),
    theta_bounds=(0, 2*np.pi),
    z_bounds=(0, 3),
    n=100
)
print("Cylindrical volume =", val)
