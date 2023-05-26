import numpy as np
from scipy.optimize import minimize, root

# define parameters
sigma = 1.5
rho = 1.5
epsilon = 1.0
alpha = 0.5
kappa = 1.0
nu = 1/(2*16**2)
w = 1.0
tau = 0.5145 # optimal_tau

# define utility function
def utility(L, w, tau, G):
    C = kappa + (1 - tau) * w * L
    utility = ((alpha * C**((sigma - 1) / sigma) + (1 - alpha) * G**((sigma - 1) / sigma))**(sigma / (sigma - 1)))**(1 - rho) - 1 / (1 - rho)
    disutility = nu * L**(1 + epsilon) / (1 + epsilon)
    res = utility - disutility
    return res

# define labor supply function
def labor_supply(w, tau, G):
    print("labor_supply")
    obj = lambda L: utility(L, w, tau, G)
    res = minimize(obj, 5, bounds=[(0, 24)])
    return res.x[0]

# define function to find G
def find_G(G, w, tau):
    L = labor_supply(w, tau, G)
    result = G - tau * w * L
    return result

# find the value of G
initial_guess = 0.5
G_solution = root(find_G, initial_guess, args=(w, tau))

optimal_G = G_solution.x[0]
optimal_G
