"""
Module that generate data
"""

import numpy as np
import numpy.random as rand

def gen_func(n, a, b, c, d):
    """
    Generate random function from normal distribution
    """
    data = rand.rand(n, 2)
    data[0] *= (b - a)
    data[0] += a
    data[1] *= (d - c)
    data[1] += c
    return data
