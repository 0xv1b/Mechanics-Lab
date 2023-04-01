import error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat
from uncertainties import unumpy


vapor_pressure = [23.88, 23.75, 25.80, 27.90, 28.70, 29.90, 33.40, 33.70]
inv_temp = np.array([0.003354, 0.003332, 0.003299, 0.003277, 0.003245, 0.003224, 0.003193, 0.003173])
temp = 1/inv_temp
temperature = unumpy.uarray([temp], [0.6, 0.6, 0.6, 0.6,0.6, 0.6, 0.6, 0.6,])
inv_temperature = 1/temperature
print(inv_temperature)


def exponential(x, a, b):
    return a*np.exp(-b*x)

(a, b), cov = curve_fit(exponential, inv_temp, vapor_pressure)

print((a, b))
print(cov)

x_data = np.linspace(0.0031, 0.0034, 100)
y_data = exponential(x_data, a, b)


# Plotting
plt.grid(True)

fig, axes = plt.subplots()
axes.set_ylabel('Vapor Pressure [Bar]', fontsize=24)
axes.set_xlabel('1/Temperature [1/K]', fontsize=24)
axes.set_title('Arrhenius Graph', fontsize=24)
plt.yscale("log")



axes.errorbar(inv_temp, vapor_pressure,fmt=" ", xerr=0.0000065, yerr=error.err_vapour_pressure_bar, capsize=2, capthick=1)


axes.plot(x_data, y_data, color="green")

axes.legend(["Best fit curve", "Data points"], fontsize=24)

plt.show()