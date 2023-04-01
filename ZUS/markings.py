import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin

# Setup Data
x_coexistence = [778.4, 155.7, 978.5, 711.7, 155.7, 800.6, 556.0, 177.9, 667.2, 378.1, 467.0]
y_coexistence = [23.0, 35.0, 21.5, 25.5, 27.0, 24.5, 30.0, 31.0, 28.5, 36.0, 34.5]

x_co_m = np.array([0.000662878787, 0.0001325757576, 0.0008333333333, 0.0006060606061, 0.0001325757576, 0.0004734848485, 0.0001515151511, 0.0005681818182, 0.000321969697,0.0003977272727])
y_co_m = np.array([2300000, 3500000, 2150000, 2550000, 2700000, 3000000, 3100000, 2850000, 3600000, 3450000])


x_co_m_err = np.array([0.0000885512296, 0.00001771024592, 0.0001113215458, 0.0000809611242, 0.00001771024592, 0.00006325087828, 0.00002024028105, 0.00007590105394, 0.00004301059723, 0.00005313073776])
x_worst = x_co_m + x_co_m_err
y_worst = np.array(y_co_m) - 85000


x_co_m = x_co_m * math.pow(10, 6)
y_co_m = y_co_m * math.pow(10, -5)

x_worst = x_worst * math.pow(10, 6)
y_worst = y_worst * math.pow(10, -5)

# Setup Curve
def curve(x, a, b, c):
    return a*x + b/x + c

(a, b, c), cov = curve_fit(curve, x_co_m, y_co_m)

# print((a, b, c))

x_data = np.linspace(60, 800, 400)
y_data = curve(x_data, a, b, c)

# Find critical point

# x_max = fmin(lambda x: -curve(x, a, b, c), 0)
# y_max = curve(x_max, a, b, c)
# print(x_max, y_max)

(x_max, y_max) = (254.130125, 34.99096081)
x_continuition = np.linspace(60, x_max, 400)
y_continuition = -(0.02*(x_continuition - x_max))**3 + y_max


# Setup worst curve


# Find worst critical point


# Setup plot

fig, axes = plt.subplots()
axes.set_ylabel('Pressure [Bar]', fontsize=24)
axes.set_xlabel('Molar Volume [cm^3/mol]', fontsize=24)
axes.set_title('Areas', fontsize=24)

# Plotting Data
legend_data = []
axes.plot(x_data, y_data, color="black")
axes.plot(x_continuition, y_continuition, '--', color="black")


# axes.fill([0,1000, 1000, 0], [0, 0, 200, 200], "red")
# axes.fill(np.append(x_continuition, [ 60]), np.append(y_continuition, [12]), "blue")
# axes.fill(np.append(x_data, [ 800]), np.append(y_data, [-20]), "green")

# Plotting Coexistence Boundary Points
legend_data.append(axes.scatter(x_co_m, y_co_m, s=20, marker="X", c="purple", label="Coexistence area boundary points"))
legend_data.append(axes.errorbar(x_max, y_max, xerr= 33.94, yerr= 0.85,color="orange",ms=50, capsize=2, capthick=1, label="Critical Point"))




# Setup legend 
plt.legend(handles = legend_data, frameon=True, facecolor="white", edgecolor="black", fontsize=24)

plt.show()