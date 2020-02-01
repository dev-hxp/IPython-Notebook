from scipy.integrate import solve_ivp
from scipy import constants
import numpy as np
import matplotlib.pyplot as plt
y0 = [constants.pi/3, 0]
t_span = [0, 10]
t = np.linspace(0, 10, 100)


def pend(t, y):
    return [y[1], -constants.g/2*np.sin(y[0])]


sol = solve_ivp(pend, t_span, y0, t_eval=t)
plt.plot(sol.t, sol.y[0])
plt.ylabel(r'angle($\theta$)')
plt.xlabel('time(s)')
plt.show()
