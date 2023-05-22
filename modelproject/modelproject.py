import numpy as np
from scipy import optimize
import sympy as sm
from sympy.solvers import solve
# for later use, in order to write tilde-variables, we need the following package
from sympy import *
sm.init_printing()
import matplotlib.pyplot as plt
from IPython.display import display, Math, Markdown

# global variables for data collection
evals = 0
fks = [] # function values for k's
fhs = [] # function values for h's

# using this collect function as the callback function for the Newton-Krylov root solver
# where x is the current solution and f the corresponding residual
# however, we do not care for the x's, only the function values
def krylov_collect(x, fs):
    global evals
    global fks
    global fhs
    fks.append(abs(fs[0])) # we take the absolute value of the function value because the difference matter, not the sign
    fhs.append(abs(fs[1]))
    evals += 1

# x0 is our initial values
def reset(x0, objective):
    global evals
    global fks
    global fhs
    evals = 0
    
    # the callback method doesn't return the functional values for our inital values
    # we initialize them in our data collection arrays here
    init_fs = objective(x0)
    fks = [abs(init_fs[0])]
    fhs = [abs(init_fs[1])]

def plot_convergence():
    global evals
    global fks
    global fhs

    fig = plt.figure(figsize=(10,4))

    # plot the function values for the k's
    ax = fig.add_subplot(1,2,1)
    ax.plot(np.arange(evals+1),fks,'-o',ms=4,color='black')
    ax.set_title("k convergence")
    ax.set_xlabel('iteration')
    ax.set_ylabel('function value')

    # pot the function values for the h's
    ax = fig.add_subplot(1,2,2)
    ax.plot(np.arange(evals+1),fhs,'-o',ms=4,color='black')
    ax.set_title("h convergence")
    ax.set_xlabel('iteration')
    ax.set_ylabel('function value')