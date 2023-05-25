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

alpha = 0.5
kappa = 1.0
nu = 1/(2*16**2)
w = 1.0

def utility(tau):
    L = (-kappa+sqrt(kappa**2+4*(alpha/nu)*((1-tau)*w)**2))/(2*(1-tau)*w)
    C = kappa + (1-tau)*w*L
    G = tau*w*L
    return np.log(C**alpha*G**(1-alpha))-nu*L**2/2

def opt_t(x):

    def obj(x):
        tau = x
        return -utility(tau)
    
    solution = optimize.minimize(obj, 0.25, method='Nelder-Mead')

    opt_t = solution.x

    return opt_t

    



