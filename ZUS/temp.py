import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from scipy.optimize import curve_fit, fmin

# Data Retrieval & Formatting
sheet_id = "1sZzhWCqxi44YKxXbq1tyydLVGl66UPOIH3cLEblhoKQ"
sheets = ["25C", "27C", "30C", "32C", "35C", "37C", "40C", "42C", "45C"]
get_url = lambda sheet : f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet}"

dataframes = {}
x_data = []
y_data = []
for sheet in sheets:
    dataframes[sheet] = pd.read_csv(get_url(sheet))
    x_data.append(dataframes[sheet]["Molar Volume (dec)"].dropna())
    y_data.append(dataframes[sheet]["Pressure (dec)"].dropna())
    # x_data.append(dataframes[sheet]["Molar Volume (inc)"].dropna())
    # y_data.append(dataframes[sheet]["Pressure (inc)"].dropna())
    # Unavailable due to dumbass team who forgot to measure increasing values


# Setup plot
plt.style.use("dark_background")

fig, axes = plt.subplots()
axes.set_ylabel('Pressure (bar)')
axes.set_xlabel('Molar Volume')
axes.set_title('Isotherms')

# Plotting Data
legend_data = []
#for i in range(len(sheets)):
#    legend_data.append(axes.scatter(x_data[i], y_data[i], s=8, label=re.sub("[C]", " ± 0.6 °C", sheets[i])))
i = 6
legend_data.append(axes.scatter(x_data[i], y_data[i], s=8,c="red", label=re.sub("[C]", " ± 0.6 °C", sheets[i])))


# Plotting Coexistence Boundary Points
x_coexistence = [397, 322, 568.2, 473.5, 151.5, 643.9, 132.6, 606.1, 833.3, 132.6, 662.9]
y_coexistence = [34.5, 36, 28.5, 30.0, 31.0, 25.0, 27.0, 25.5, 21.5, 35.0, 23.0]

def curve(x, a, b, c):
    return a*x + b/x + c

(a, b, c), cov = curve_fit(curve, x_coexistence, y_coexistence)

x_data = np.linspace(50, 800, 500)
y_data = curve(x_data, a, b, c)


axes.plot(x_data, y_data)


# Setup legend 

plt.legend(handles = legend_data, fontsize=10, frameon=True)

plt.show()