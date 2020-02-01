from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

l = 0.1
k = 0.02


def model(z, t):
    r = z[0]
    i = z[1]
    s = z[2]
    drdt = l*i
    didt = k*s*t - drdt
    dsdt = - didt - drdt
    dzdt = [drdt, didt, dsdt]
    return dzdt


z0 = [0, 1, 10000]
t = np.linspace(0, 120, 1200)
z = odeint(model, z0, t)

plt.plot(t, z[:, 0], 'b-', label="death and cure")
plt.plot(t, z[:, 1], 'r-', label="infected")
plt.plot(t, z[:, 2], 'g-', label="suspectible")
plt.legend(loc="best")
plt.show()
