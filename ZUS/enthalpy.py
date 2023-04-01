import math
import error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin

vapor_pressure = [23.88, 23.75, 25.80, 27.90, 28.70, 29.90, 33.40, 33.70]
temperature = [298.15, 300.15, 303.15, 305.15, 308.15, 310.15, 313.15, 315.15]
enthalpy = [11.4179171, 11.57641902, 10.35627206, 8.95652936, 8.445517057, 7.545676656, 4.08768343, 3.691951746]
enthalpy_err = [2.1, 2.2, 2, 1.9, 1.8, 1.7, 1.5, 1.5]



def line(x, m, c):
    return m*x + c

(m, c), paramcov = curve_fit(line, temperature, vapor_pressure)
print(m, c)

(mw, cw), paramcovw = curve_fit(line, [298.75, 314.55], [24.18, 33.4])
print(mw, cw)

print(f"error in slope: {m - mw}")


(m, c), paramcov = curve_fit(line, temperature, enthalpy)

x_data = np.linspace(298, 316, 100)
y_data = line(x_data, m, c)

# Plotting Data

fig, axes = plt.subplots()
axes.set_ylabel('Enthalpy [kJ/mol]', fontsize=24)
axes.set_xlabel('Temperature [K]', fontsize=24)
axes.set_title('Enthalpy vs Temperature', fontsize=24)

axes.errorbar(temperature, enthalpy, xerr=0.6, yerr= enthalpy_err, fmt=" ", capsize=2, capthick=1)
axes.plot(x_data, y_data, color="green")

axes.legend(["Best fit line", "Data points"], fontsize=24)


plt.show()