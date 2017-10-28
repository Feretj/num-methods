"""
    Some utils for other modules
"""


import numpy as np

def gen_p(a, b, x1, x2):
    """
    Generate p as aw(b - w)
    """
    x = np.arange(x1, x2, 0.1)
    p = a*x*(b - x)
    return np.stack((x, p))
