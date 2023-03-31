import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, fmin

# Data Retrieval and Formatting
sheet_id = "1wUUL4bo96UOyQWv32BtwYP6PANxHw7POJzXLyf0Nyus"
sheet_name = "Resonance"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
dataframe = pd.read_csv(url)

length_500_cm = dataframe["Length (cm) (500 Hz)"]
length_1000_cm = dataframe["Length (cm) (1kHz)"]
length_2000_cm = dataframe["Length (cm) (2 kHz)"]

length_500_m = dataframe["Length (m) (500 Hz)"]
length_1000_m = dataframe["Length (m) (1kHz)"]
length_2000_m = dataframe["Length (m) (2 kHz)"]


# Uncertainties:
# Uncertainty in ruler: 1.4 mm + half step size = 1.9 mm
err_ruler_m = (1.9 * math.pow(10, -3))
err_ruler_cm = (1.9 * math.pow(10, -1))


# Plotting

fig, (ax1, ax2) = plt.subplots(2)

ax1.set_xlabel("# of Maximum")
ax1.set_ylabel("Length [cm]")

ax1.errorbar(np.arange(1, 12, 1), length_500_cm, yerr=err_ruler_cm, capsize=2, capthick=1)
ax1.errorbar(np.arange(1, 12, 1), length_1000_cm, yerr=err_ruler_cm, capsize=2, capthick=1)
ax1.errorbar(np.arange(1, 12, 1), length_2000_cm, yerr=err_ruler_cm, capsize=2, capthick=1)


plt.show()