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

# set seed
np.random.seed(2023)

def global_optimizer(bounds, tau, _K, K, objective):

   # create vector for plotting later
   x_k0_values = []
   
   # for k in 0, 1, ..., K - 1
   for k in range(0,K):

      # 3A draw random x uniformly within bounds
      x1_k = np.random.uniform(low=bounds[0], high=bounds[1])
      x2_k = np.random.uniform(low=bounds[0], high=bounds[1])
      x_k = np.array([x1_k, x2_k])

      # 3B if k > K don't jump to 3E - if k <= K do jump to 3E
      if k > _K:

         # 3C compute chi_k
         chi_k = 0.5 * (2 / (1 + np.exp((k - _K) / 100)))

         # 3D set x_k0
         x_k0 = chi_k * x_k + (1 - chi_k) * x_star

      else:
         # else set the x_k0 to the randomly found x_k vector
         x_k0 = x_k
      
      # append the x_k0 value for plotting later
      x_k0_values.append(x_k0)

      # 3E run optimizer
      res = optimize.minimize(objective, x_k0, method='BFGS')
      x_k_star = res.x

      # 3F update best solution
      if k == 0 or objective(x_k_star) < objective(x_star):
         x_star = x_k_star
      
      # 3E check if break
      if objective(x_star) < tau:
         return x_star, x_k0_values