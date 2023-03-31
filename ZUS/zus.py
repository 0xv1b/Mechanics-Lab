import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data Retrieval
sheet_id = "1sZzhWCqxi44YKxXbq1tyydLVGl66UPOIH3cLEblhoKQ"
sheet_1, sheet_2, sheet_3, sheet_4 = ("50C", "30C", "37C", "45C")
get_url = lambda sheet : f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet}"

# Google sheets data stored in pandas dataframes
dataframe_50C = pd.read_csv(get_url(sheet_1))
dataframe_30C = pd.read_csv(get_url(sheet_2))
dataframe_37C = pd.read_csv(get_url(sheet_3))
dataframe_45C = pd.read_csv(get_url(sheet_4))

# Test
# print(dataframe_50C["Volume"][4])

# Plotting 50°C curve
x_data = dataframe_50C["1/Volume"][0:21]
x_error = dataframe_50C["Error (1/Volume)"][0:21]
y_data = dataframe_50C["Pressure * Volume"][0:21]
y_error = dataframe_50C["Error (Pressure * Volume)"][0:21]

def line(x, m, c):
    return m*x + c

(m, c), paramcov = curve_fit(line, x_data, y_data)
print(m, c)

x_line = np.linspace(0, 0.5)
y_line = line(x_line, m, c)


fig, ax =  plt.subplots()
ax.errorbar(x_data, y_data, xerr= x_error, yerr = y_error, fmt="o")

ax.plot(x_line, y_line)

plt.xlabel("Pressure * Volume")
plt.ylabel("1/Volume")
plt.title("ZUS")

plt.show()