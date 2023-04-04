import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin
from uncertainties import ufloat

# Data Retrieval and Formatting

purple_length = (29.7 * math.pow(10, -3))
purple_diameter = (0.3703 * math.pow(10, -3))
white_length = (31.65 * math.pow(10, -3))
white_diameter = (0.2645 * math.pow(10, -3))

sheet_id = "1P4OrWc5vJkqiV26ToXuKYyCGziOuLwaWtaeXhGgXHx4"
sheet_name = "Capillary"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dataframe = pd.read_csv(url)

height_cm_purple = dataframe["Height (cm) (Purple)"]
time_s_purple = dataframe["Time (s) (Purple)"]
mass_g_purple = dataframe["Mass (g) (Purple)"]

height_cm_white = dataframe["Height (cm) (White)"]
time_s_white = dataframe["Time (s) (White)"]
mass_g_white = dataframe["Mass (g) (White)"]


# Uncertainties:


# Plotting
fig, ax = plt.subplots()

ax.set_xlabel("Stuff")
ax.set_ylabel("Other Stuff")

plt.show()