import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin

# Setup Data
x_coexistence = [778.4,
155.7,
978.5,
711.7,
155.7,
800.6,
556.0,
177.9,
667.2,
378.1,
467.0]
y_coexistence = [23.0,
35.0,
21.5,
25.5,
27.0,
24.5,
30.0,
31.0,
28.5,
36.0,
34.5]

# Setup Curve
def curve(x, a, b, c):
    return a*x + b/x + c

(a, b, c), cov = curve_fit(curve, x_coexistence, y_coexistence)

print((a, b, c))#

x_data = np.linspace(100, 700, 400)
y_data = curve(x_data, a, b, c)



# Find critical point
x_max = fmin(lambda x: -curve(x, a, b, c), 0)
y_max = curve(x_max, a, b, c)

print(x_max)


# Setup plot
plt.style.use("dark_background")

fig, axes = plt.subplots()
axes.set_ylabel('Pressure (bar)')
axes.set_xlabel('Molar Volume')
axes.set_title('Areas')

# Plotting Data
legend_data = []
axes.plot(x_data, y_data)
axes.fill(x_data, y_data, "white")

# Plotting Coexistence Boundary Points
legend_data.append(axes.scatter(x_coexistence, y_coexistence, s=20, marker="X", c="red", label="Coexistence area boundary points"))




# Setup legend 
plt.legend(handles = legend_data, fontsize=10, frameon=True)

plt.show()