import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

# Data Retrieval & Formatting
sheet_id = "1sZzhWCqxi44YKxXbq1tyydLVGl66UPOIH3cLEblhoKQ"
sheets = ["25C", "27C", "30C", "32C", "35C", "37C", "40C", "42C", "45C"]
get_url = lambda sheet : f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet}"

dataframes = {}
x_data = []
y_data = []
for sheet in sheets:
    
    dataframes[sheet] = pd.read_csv(get_url(sheet))
    x_data.append(dataframes[sheet]["Molar Volume (dec) (cm^3 / mol)"].dropna())
    y_data.append(dataframes[sheet]["Pressure (dec) (Bar)"].dropna())
    # x_data.append(dataframes[sheet]["Molar Volume (inc)"].dropna())
    # y_data.append(dataframes[sheet]["Pressure (inc)"].dropna())
    # Unavailable due to dumbass team who forgot to measure increasing values


# Setup plot

fig, axes = plt.subplots()
plt.grid(True)
axes.set_ylabel('Pressure [Bar]', fontsize=24)
axes.set_xlabel('Molar Volume [cm^3 / mol]', fontsize=24)
axes.set_title('Isotherms', fontsize=24)

# Plotting Data
legend_data = []
for i in range(len(sheets)-1):
    legend_data.append(axes.scatter(x_data[i], y_data[i], s=8, label=re.sub("[C]", " ± 0.6 °C", sheets[i])))

# Plotting one set of points with error TODO: CHANGE THE MFIN COLOUR
legend_data.append(axes.errorbar(x_data[len(sheets)-1], y_data[len(sheets)-1],fmt='o--',ms=3,
              xerr= dataframes["45C"]["Error (Molar Volume) (dec) (cm^3 / mol)"].dropna(), 
              yerr= 0.85, capsize=3, capthick=1, elinewidth=1, label="45 ± 0.6 °C (with error)"))


# Plotting Coexistence Boundary Points
x_coexistence = [397, 322, 568.2, 473.5, 151.5, 643.9, 132.6, 606.1, 833.3, 132.6, 662.9]
y_coexistence = [34.5, 36, 28.5, 30.0, 31.0, 25.0, 27.0, 25.5, 21.5, 35.0, 23.0]
legend_data.append(axes.scatter(x_coexistence, y_coexistence, s=20, marker="X", c="red", label="Coexistence area boundary points"))

# Setup legend 
legend_names = []
for sheet in sheets:
    legend_names.append(re.sub("[C]", " ± 0.6 °C", sheet))

plt.legend(handles = legend_data, fontsize=18, frameon=True)

plt.show()