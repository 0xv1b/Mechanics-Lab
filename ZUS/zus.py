import math
import error
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties import unumpy

# Data Retrieval
sheet_id = "1sZzhWCqxi44YKxXbq1tyydLVGl66UPOIH3cLEblhoKQ"
sheet_name = "50C"
dataframe = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}")



# Data Formatting
#x_data = dataframe["1/Volume"][0:21]
#x_error = dataframe["Error (1/Volume)"][0:21]
#y_data = dataframe["Pressure * Volume"][0:21]
#y_error = dataframe["Error (Pressure * Volume)"][0:21]

x_data = dataframe["1/Volume (cm^-3)"][0:21]
x_error = dataframe["Error (1/Volume) (cm^-3)"][0:21]
y_data = dataframe["Pressure * Volume (Bar * cm^3)"][0:21]
y_error = dataframe["Error (Pressure * Volume) (Bar * cm^3)"][0:21]



def line(x, m, c):
    return m*x + c

(m, c), paramcov = curve_fit(line, x_data, y_data)
print(m, c)

x_line = np.linspace(0, 0.5)
y_line = line(x_line, m, c)

worst_x = [x_data[0] + x_error[0], x_data[len(x_data) - 1] - x_error[len(x_error) - 1]]
worst_y = [y_data[0] - y_error[0], y_data[len(y_data) - 1] + y_error[len(y_error) - 1]]

(m_bad, c_bad), paramcov = curve_fit(line, worst_x, worst_y)
#print(m_bad, c_bad)

x_w_line = np.linspace(0, 0.5)
y_w_line = line(x_line, m_bad, c_bad)


fig, ax =  plt.subplots()
points= []
ax.errorbar(x_data, y_data, xerr= x_error, yerr = y_error, fmt="o--", capsize=2, capthick=1, ms=3) 

ax.plot(x_line, y_line, c="green")
ax.plot(x_w_line, y_w_line, c="red")

plt.xlabel("1/Volume [cm^-3]", fontsize=24)
plt.ylabel("Pressure * Volume [Bar * cm^3]", fontsize=24)
plt.title("Determining no. of moles", fontsize=32)
plt.grid(True)
plt.legend(["Best fit line", "Worst fit line", "Data points"], fontsize=24)

plt.show()