# import
import numpy as np
from scipy import optimize
from scipy.optimize import minimize_scalar
import sympy as sm
from sympy import simplify
from sympy.solvers import solve
from sympy import *
sm.init_printing()
import matplotlib.pyplot as plt
from IPython.display import display, Math, Markdown

def profits(kappa, l, eta, w):
    return kappa*l**(1-eta)-w*l

def max_profits(kappa, eta, w):
    obj = lambda l: -profits(kappa, l, eta, w)
    x0 = 0.5
    sol = optimize.minimize(obj, x0, method='Nelder-Mead')
    optimal_l = sol.x

    return optimal_l

