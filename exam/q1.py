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
from math import sqrt, log
from scipy.optimize import minimize_scalar
from scipy.optimize import minimize

# define baseline parameters
alpha = 0.5
kappa = 1.0
nu = 1/(2*16**2)
w = 1.0
tau = 0.3

# define utility function as a function of L*, C and G
def utility(tau, kappa, alpha, nu, w):
    L = (-kappa+sqrt(kappa**2+4*(alpha/nu)*((1-tau)*w)**2))/(2*(1-tau)*w)
    C = kappa+(1-tau)*w*L
    G = tau*w*L
    return log(C**alpha*G**(1-alpha))-nu*L**2/2

# solve for optimal tau
def optimal_tau():

    # define objective function as a function of tau
    obj = lambda tau: -utility(tau, kappa, alpha, nu, w) # negative sign -> we wish to maximize

    # minimize the negative utility function to find tau that max utility
    res = minimize_scalar(obj, bounds=(0, 1), method='bounded') # 0 < tau < 1

    optimal_tau = res.x
    max_utility = -res.fun

    return optimal_tau, max_utility

sigma = 1.001
rho = 1.001
epsilon = 1.0

def CES_utility(tau, kappa, alpha, nu, w, sigma, rho, epsilon, L):
    C = kappa+(1-tau)*w*L
    G = tau*w*L
    num = ((alpha*C**((sigma-1)/sigma)+(1-alpha)*G**((sigma-1)/sigma))**(sigma/(sigma-1)))**(1-rho)-1
    den = 1-rho
    return num/den-(nu*L**(1+epsilon)/(1+epsilon))

def labor_supply(tau, w):
    # Define the objective function for labor supply
    obj = lambda L: -CES_utility(tau, kappa, alpha, nu, w, sigma, rho, epsilon, L)
 
    L_min = 0
    L_max = 24
    
    x0 = 15.0

    res = optimize.minimize(obj, x0, bounds=[(L_min, L_max)], method='Nelder-Mead')
    # Find the optimal labor supply that maximizes utility
    optimal_L = res.x[0]
    G = tau*w*optimal_L
    return optimal_L

def find_G(tau, w, L):
    return tau*w*L

# solve for optimal tau
def CES_optimal_tau():

    # define objective function as a function of tau
    obj = lambda CES_tau: -CES_utility(CES_tau, kappa, alpha, nu, w, sigma, rho, epsilon, labor_supply(CES_tau,w)) # negative sign -> we wish to maximize

    # minimize the negative utility function to find tau that max utility
    CESres = minimize_scalar(obj, bounds=(0, 1), method='bounded') # 0 < tau < 1

    CES_optimal_tau = CESres.x
    CES_max_utility = -CESres.fun

    return CES_optimal_tau, CES_max_utility