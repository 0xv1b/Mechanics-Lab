import math
from uncertainties import ufloat
from uncertainties import unumpy







temp = [298.15,
300.15,
303.15,
305.15,
308.15,
310.15,
313.15,
315.15]

vdiff=[610.8595,
615.2125,
544.923,
468.183,
437.173,
388.075,
208.216,
186.865]

vdiff_err = [106.1551351,
106.6027813,
99.54377076,
92.31250127,
89.55769376,
85.4256161,
73.37336668,
72.34034727]

dpdt = ufloat(0.626918,0.04337)

for i in range(8):
    enthalpy = ufloat(vdiff[i], vdiff_err[i]) * ufloat(temp[i], 0.6) * dpdt
    print(f"No.{i}:   {enthalpy}")





# Value for b is (0.085 ± 0.011) L/mol
# Value for a is (6.8 ± 1.8) Bar * L^2 / mol^2
# n = (0.00263 ± 0.00035) mol   OR   (2.63 ± 0.35) mmol


# Defining error constants for use across files
err_vol_cm3 = 0.025
err_vol_m3 = err_vol_cm3 * math.pow(10, -6)
err_pressure_bar = 0.85
err_pressure_pascal = err_pressure_bar * math.pow(10, 5)

err_thermo_c = 0.6
err_n_mol = 0.00035

err_vapour_pressure_bar = 0.3

critical_vol_m3 = 254.13 * math.pow(10, -6)
critical_pressure_pascal = 34.99 * math.pow(10, 5)

critical_vol_err_m3 = 33.94 * math.pow(10, -6)
critical_pressure_err_pascal = 0.85 * math.pow(10, 5)


crit_vol = ufloat(critical_vol_m3, critical_vol_err_m3)
crit_psi = ufloat(critical_pressure_pascal, critical_pressure_err_pascal)
n = ufloat(0.00263, err_n_mol)



