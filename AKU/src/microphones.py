import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin

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
(m, c), cov = curve_fit(line, time_s, distances_m)
x_fit = np.linspace(0, 1.0, 100)
y_fit = line(x_fit, m, c)

print(f"slope = {m}")
print(f"y-intercept = {c}")
print(cov)


# Worst possible line
worst_distances_1 = [distances_m[0] - err_ruler_m, distances_m[len(distances_m) - 1] + err_ruler_m]
worst_distances_2 = [distances_m[0] + err_ruler_m, distances_m[len(distances_m) - 1] - err_ruler_m]

worst_times_1 = [time_s[0] + err_osc_s, time_s[len(time_s) - 1] - err_osc_s]
worst_times_2 = [time_s[0] - err_osc_s, time_s[len(time_s) - 1] + err_osc_s]

# 1st Slope is worse (356.82414698162734 m/s)
(m_bad_1, c_bad_1), cov = curve_fit(line, worst_times_1, worst_distances_1)
print(f"Worst Slope 1: {m_bad_1}")
print(f"Error in Slope is: {m_bad_1 - m}")
print(f"Error in y-intercept is: {c_bad_1 - c}")


(m_bad_2, c_bad_2), cov = curve_fit(line, worst_times_2, worst_distances_2)
print(f"Worst Slope 2: {m_bad_2}")


# Plotting
fig, (ax1, ax2) = plt.subplots(2)

ax1.set_xlabel("Time [µs]")
ax1.set_ylabel("Distance [cm]")

ax1.errorbar(time_μs, distances_cm, xerr = err_osc_μs, yerr=err_ruler_cm, capsize=2, capthick=1)



ax2.set_xlabel("Time [s]")
ax2.set_ylabel("Distance [m]")

ax2.scatter(time_s, distances_m)
ax2.plot(x_fit, y_fit)

plt.show()

# Speed of sound obtained is (347.6678795109381 ± 9.156267470689215) m/s