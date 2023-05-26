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
from types import SimpleNamespace


# define profit
def profits(kappa, l, eta, w):
    return kappa*l**(1-eta)-w*l

# maximize profits
def max_profits(kappa, eta, w):
    # define objective function
    obj = lambda l: -profits(kappa, l, eta, w)
    # initial guess
    x0 = 0.5
    sol = optimize.minimize(obj, x0, method='Nelder-Mead') # Nelder-Mead is a good solver for simple problems
    # save solution as the optimal l
    optimal_l = sol.x

    return optimal_l

        

