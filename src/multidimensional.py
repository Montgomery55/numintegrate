import numpy as np

def rectangle_rule_nd(f, bounds, n):
    dim = len(bounds)
    if isinstance(n, int):
        n = (n,) * dim
    
    grids = [np.linspace(a, b, num) for (a, b), num in zip(bounds, n)]
    mesh = np.meshgrid(*grids, indexing='ij')
    points = np.stack([m.reshape(-1) for m in mesh], axis=-1)

    vals = np.apply_along_axis(f, 1, points)

    vols = [(b - a) / (num - 1) for (a, b), num in zip(bounds, n)]
    dV = np.prod(vols)

    return np.sum(vals) * dV

def monte_carlo_nd(f, bounds, n_samples):
    dim = len(bounds)
    a = np.array([b[0] for b in bounds])
    b = np.array([b[1] for b in bounds])
    vol = np.prod(b-a)

    random_points = np.random.uniform(low=a, high=b, size=(n_samples, dim))
    values = np.apply_along_axis(f, 1, random_points)

    return vol * np.mean(values)
