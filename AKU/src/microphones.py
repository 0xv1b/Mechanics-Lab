import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat

# Data Retrieval and Formatting
sheet_id = "1wUUL4bo96UOyQWv32BtwYP6PANxHw7POJzXLyf0Nyus"
sheet_name = "Microphones"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dataframe = pd.read_csv(url)

distances_cm = dataframe["Distance (cm)"]
time_µs = dataframe["Time (µs)"]

distances_m = dataframe["Distance (m)"]
time_s = dataframe["Time (s)"]


# Uncertainties:
# Uncertainty in ruler: 1.4 mm + half step size = 1.9 mm
err_ruler_m = (1.9 * math.pow(10, -3))
err_ruler_cm = (1.9 * math.pow(10, -1))

# Uncertainty in Oscilloscope: Step Size (4 or 10 µs)
err_osc_s = (10 * math.pow(10, -6))
err_osc_µs = 10 * math.pow(10, -3)


# Curve Fitting
def line(x, m, c):
    return m*x + c

# Slope is 347.6678795109381 m/s
(m, c), cov = curve_fit(line, time_µs, distances_cm)
x_fit = np.linspace(780, 2350, 200)
y_fit = line(x_fit, m, c)

print(f"slope = {m}")
print(f"y-intercept = {c}")


# Worst possible line
worst_distances = [distances_cm[0] - err_ruler_cm, distances_cm[len(distances_cm) - 1] + err_ruler_cm]

worst_times = [time_µs[0] + err_osc_µs, time_µs[len(time_µs) - 1] - err_osc_µs]

# This Slope is worst (356.82414698162734 m/s)
(m_bad, c_bad), cov = curve_fit(line, worst_times, worst_distances)
print(f"Worst Slope 1: {m_bad}")
print(f"Error in Slope is: {m_bad - m}")
print(f"Error in y-intercept is: {c_bad - c}")

y_bad = line(x_fit, m_bad, c_bad)

# Plotting
fig, ax= plt.subplots()

plt.grid(True)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

ax.set_xlabel("Time [µs]", fontsize=24)
ax.set_ylabel("Distance [cm]", fontsize=24)

ax.errorbar(time_μs, distances_cm, xerr = err_osc_μs, yerr=err_ruler_cm,fmt = " ", capsize=2, capthick=1)
ax.plot(x_fit,y_fit, color="green")
#ax.plot(x_fit,y_bad, color="red")


plt.legend(["Best fit line"], fontsize=24)
plt.show()

# Speed of sound obtained from microphones (347.6678795109381 ± 9.156267470689215) m/s


speed_mps = ufloat(347.6678795109381, 9.156267470689215)
density_kgpm3 = ufloat(1.293, 0)
pressure_pa = ufloat(96258.8, 133.32)

k = speed_mps**2 * density_kgpm3 / pressure_pa
print(f"Adiabatic coefficient: {k}")