import numpy as np

def adaptive_simpson(f, a, b, tol=1e-6, max_recursion=20):
    def simpson_rule(f, a, b):
        fa = f(a)
        fb = f(b)
        fmid = f((a+b)/2)
        return ((1/6)*(b-a)) * (fa + 4*fmid + fb)

    def recursive(f, a, b, tol, depth):
        c = (a+b) / 2
        S = simpson_rule(f, a, b)
        S_left = simpson_rule(f, a, c)
        S_right = simpson_rule(f, c, b)
        error = (S_left + S_right - S)

        if depth <= 0 or error < 15 * tol:
            return S_left + S_right + (S_left + S_right - S) / 15
        else:
            return recursive(f, a, c, tol / 2, depth - 1) + recursive(f, c, b, tol / 2, depth - 1)

    return recursive(f, a, b, tol, max_recursion)
