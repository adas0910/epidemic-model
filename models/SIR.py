"""
SIR disease model

N = 100
"""

import numpy as np
from ODE_Solver import ForwardEuler
from matplotlib import pyplot as plt

class SIR:
    def __init__(self, recov, trans, S_0, I_0, R_0):
        """
        recov, trans: parameters in the ODE system
        S_0, I_0, R_0: initial values
        N = S_0 + I_0 + R_0
        """

        if isinstance(recov, (float, int)):
            # Is number?
            self.recov = lambda t: recov 
        elif callable(recov):
            self.recov = recov

        if isinstance(trans, (float, int)):
            self.trans = lambda t: trans 
        elif callable(trans):
            self.trans = trans

        self.initial_conditions = [S_0, I_0, R_0]

    def __call__(self, u, t):

        S, I, R = u 

        return np.asarray([
            (-self.trans(t)*S*I)/N, # Susceptibles
            (self.trans(t)*S*I)/N - self.recov(t)*I, # Infected
            self.recov(t)*I # Recovered
        ])

if __name__ == "__main__":

    sir = SIR(0.1, 0.17, S_0, I_0, R_0)
    solver = ForwardEuler(sir)
    solver.set_initial_conditions(sir.initial_conditions)

    time_steps = np.linspace(0, 365, 1000)
    u, t = solver.solve(time_steps)

    plt.plot(t, u[:, 0], color='yellow', label="Susceptible")
    plt.plot(t, u[:, 1], color='red', label="Infected")
    plt.plot(t, u[:, 2], color='green', label="Recovered")
    #plt.axhline(0.054, 0, 365, color='black', label="no. of Beds")
    plt.axvline(2, 0, 100, color='pink') # Day no.
    plt.legend()
    plt.show()