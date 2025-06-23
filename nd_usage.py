import numpy as np
import scipy
from src.integrator import *

f2d = lambda x: np.exp(-x[0]**2 - x[1]**2)
bounds = [(-5, 5), (-5, 5)]
mc_2d = integrate_nd(f2d, bounds, method='mc', n=100)
rec_2d = integrate_nd(f2d, bounds, method='rectangle', n=100)
exact_2d = np.pi*scipy.special.erf(5)**2

print("Method, value, error" )
print(f"2D MC: {np.round(mc_2d, 6)}, {np.round(exact_2d - mc_2d, 6)}")
print(f"2D Rec: {np.round(rec_2d, 6)}, {np.round(exact_2d - rec_2d, 6)}")

f3d = lambda x: np.exp(-x[0]**2 - x[1]**2 - x[2]**2)
bounds = [(-5, 5), (-5, 5), (-5, 5)]
mc_3d = integrate_nd(f3d, bounds, method="mc", n=1000)
exact_3d = np.pi**(3/2)*scipy.special.erf(5)**3

print(f"3D MC: {np.round(mc_3d, 6)}, {np.round(exact_3d - mc_3d, 6)}")

