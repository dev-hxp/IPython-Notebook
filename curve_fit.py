import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def func(x, a, b, c):
    return a * np.exp(-b * x) + c


x_data = np.linspace(0, 4, 50)
y = func(x_data, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.random(size=x_data.size)
y_data = y + y_noise
plt.plot(x_data, y_data, 'b-', label='data')


popt, pcov = curve_fit(func, x_data, y_data)

plt.plot(x_data, func(x_data, *popt), 'r-', label='fit')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
