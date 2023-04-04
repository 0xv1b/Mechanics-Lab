import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat

# Data Retrieval and Formatting
sheet_id = "1wUUL4bo96UOyQWv32BtwYP6PANxHw7POJzXLyf0Nyus"
sheet_name = "Resonance"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dataframe = pd.read_csv(url)

length_500_cm = dataframe["Length (cm) (500 Hz)"][0:3]
length_1000_cm = dataframe["Length (cm) (1kHz)"][0:6]
length_2000_cm = dataframe["Length (cm) (2 kHz)"][1: 11]

length_500_m = dataframe["Length (m) (500 Hz)"][0:3]
print(length_500_m)
length_1000_m = dataframe["Length (m) (1kHz)"][0:6]
print(length_1000_m)
length_2000_m = dataframe["Length (m) (2 kHz)"][1: 11]

print(length_2000_m)


# Uncertainties:
# Uncertainty in ruler: 1.4 mm + half step size = 1.9 mm
err_ruler_m = (1.9 * math.pow(10, -3))
err_ruler_cm = (1.9 * math.pow(10, -1))
err_osc = 1


# Curve Fitting
def line(x, m, c):
    return m*x + c

# 2kHz
(m, c), cov = curve_fit(line, np.arange(2, 12, 1), [0.114, 0.198, 0.286, 0.369, 0.456, 0.545, 0.632, 0.715, 0.803, 0.887])
print(f"2 kHz: {m, c}")


(m_bad, c_bad), cov = curve_fit(line, [2, 11], [(0.114 - err_ruler_m), (0.887 + err_ruler_m)])
print(f"2 kHz (Worst): {m_bad, c_bad}")
print(f"2 kHz (Error): {m - m_bad, c - c_bad}")


osc = ufloat(2000, 1)
slope = ufloat(m, (m_bad - m))
intercept = ufloat(c, (c - c_bad))
length = 10*slope + intercept
speed = (4 * length * osc / 19)
print(speed)


#1 kHz
(m, c), cov = curve_fit(line, [1, 2, 3, 4, 5,6], length_1000_m)
print(f"1 kHz: {m, c}")


(m_bad, c_bad), cov = curve_fit(line, [1, 6], [(0.063 - err_ruler_m), (0.919 + err_ruler_m)])
print(f"1 kHz (Worst): {m_bad, c_bad}")
print(f"1 kHz (Error): {m - m_bad, c - c_bad}")

osc = ufloat(1000, 1)
slope = ufloat(m, (m_bad - m))
intercept = ufloat(c, (c - c_bad))
length = 10*slope + intercept
speed = (4 * length * osc / 19)
print(speed)

# 500 Hz

(m, c), cov = curve_fit(line, [1, 2, 3], length_500_m)
print(f"500 Hz: {m, c}")

(m_bad, c_bad), cov = curve_fit(line, [1, 3], [(0.153 - err_ruler_m), (0.844 + err_ruler_m)])
print(f"500 Hz (Worst): {m_bad, c_bad}")
print(f"500 Hz (Error): {m - m_bad, c - c_bad}")

osc = ufloat(500, 1)
slope = ufloat(m, (m_bad - m))
intercept = ufloat(c, (c - c_bad))
length = 10*slope + intercept
speed = (4 * length * osc / 19)
print(speed)


# Plotting

fig, ax = plt.subplots()
plt.grid(True)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

ax.set_xlabel("# of Maximum", fontsize=24)
ax.set_ylabel("Length [cm]", fontsize=24)


(m, c), cov = curve_fit(line, np.arange(1, 4, 1), length_500_cm)
x_data = np.linspace(0, 3.1, 100)
y_data = line(x_data, m , c)
ax.plot(x_data, y_data, lw=1)
ax.errorbar(np.arange(1, 4, 1), length_500_cm, yerr=err_ruler_cm, capsize=2, capthick=1, fmt=" ")


(m, c), cov = curve_fit(line, np.arange(1, 7, 1), length_1000_cm)
x_data = np.linspace(0, 6.1, 100)
y_data = line(x_data, m , c)
ax.plot(x_data, y_data, lw=1)
ax.errorbar(np.arange(1, 7, 1), length_1000_cm, yerr=err_ruler_cm, capsize=2, capthick=1, fmt=" ")


(m, c), cov = curve_fit(line, np.arange(2, 12, 1), length_2000_cm)
x_data = np.linspace(0, 11.1, 100)
y_data = line(x_data, m , c)
ax.plot(x_data, y_data, lw=1)
ax.errorbar(np.arange(2, 12, 1), length_2000_cm, yerr=err_ruler_cm, capsize=2, capthick=1, fmt=" ")

plt.legend(["Best fit line (500 Hz)", "Best fit line (1000 Hz)", "Best fit line (2000 Hz)"], fontsize=24)
plt.show()