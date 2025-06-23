import numpy as np

def spherical_grid(r_bounds, theta_bounds, phi_bounds, n):
    r = np.linspace(*r_bounds, n)
    theta = np.linspace(*theta_bounds, n)
    phi = np.linspace(*phi_bounds, n)

    R, T, P = np.meshgrid(r, theta, phi, indexing='ij')
    x = R * np.sin(T) * np.cos(P)
    y = R * np.sin(T) * np.sin(P)
    z = R * np.cos(T)

    X = np.stack([x.ravel(), y.ravel(), z.ravel()], axis=1)
    J = (R**2 * np.sin(T)).ravel()
    return X, J

def cylindrical_grid(r_bounds, theta_bounds, z_bounds, n):
    r = np.linspace(*r_bounds, n)
    theta = np.linspace(*theta_bounds, n)
    z = np.linspace(*z_bounds, n)

    R, T, Z = np.meshgrid(r, theta, z, indexing='ij')
    x = R * np.cos(T)
    y = R * np.sin(T)

    X = np.stack([x.ravel(), y.ravel(), Z.ravel()], axis=1)
    J = R.ravel()

    return X, J

