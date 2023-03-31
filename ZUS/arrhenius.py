import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin

vapor_pressure = [23.88, 23.75, 25.80, 27.90, 28.70, 29.90, 33.40, 33.70]
inv_temp = [0.003354, 0.003332, 0.003299, 0.003277, 0.003245, 0.003224, 0.003193, 0.003173]


# Plotting
plt.style.use("dark_background")

fig, axes = plt.subplots()
axes.set_ylabel('Vapor Pressure')
axes.set_xlabel('1/Temperature')
axes.set_title('Arrhenius Graph')
plt.yscale("log")

def exponential(x, a, b):
    return a*np.exp(-b*x)

(a, b), cov = curve_fit(exponential, inv_temp, vapor_pressure)

print((a, b))
print(cov)

x_data = np.linspace(0.0031, 0.0034, 100)
y_data = exponential(x_data, a, b)

axes.plot(x_data, y_data)


axes.scatter(inv_temp, vapor_pressure)

plt.show()