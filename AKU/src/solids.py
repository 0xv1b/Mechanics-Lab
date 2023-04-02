import math
from uncertainties import ufloat

err_ruler_cm = 0.19
pvc_density_g_cm3 = ufloat(1.4, 0.2)
aluminium_density_g_cm3 = ufloat(2.7, 0.1)
copper_density_g_cm3 = ufloat(8.95, 0.05)


# Copper
copper_time_ms = ((ufloat(3.920, 0.020)/5) + (ufloat(3.920, 0.020)/5) + (ufloat(3.920, 0.020)/5))/3
copper_time_s = copper_time_ms/1000

length_copper_cm = ufloat(150.0, err_ruler_cm)
length_copper_m = length_copper_cm / 100

speed_copper_mps = 2 * length_copper_m / copper_time_s
copper_modulus = speed_copper_mps**2 * copper_density_g_cm3 * 1000

print(f"Speed of sound in Copper: {speed_copper_mps}")
print(f"Modulus of Elasticity: {copper_modulus}")



# Aluminium
aluminium_time_ms = ((ufloat(4.240, 0.020)/7) + (ufloat(4.240, 0.020)/7) + (ufloat(4.240, 0.020)/7))/3
aluminium_time_s = aluminium_time_ms/1000

length_aluminium_cm = ufloat(149.6, err_ruler_cm)
length_aluminium_m = length_aluminium_cm / 100

speed_aluminium_mps = 2 * length_aluminium_m / aluminium_time_s
aluminim_modulus = speed_aluminium_mps**2 * aluminium_density_g_cm3 * 1000

print(f"Speed of sound in Aluminium: {speed_aluminium_mps}")
print(f"Modulus of Elasticity: {aluminim_modulus}")



# PVC
pvc_time_ms = ((ufloat(4.640, 0.020)/4) + (ufloat(3.560, 0.020)/3) + (ufloat(4.520, 0.020)/4))/3
pvc_time_s = pvc_time_ms/1000

length_pvc_cm = ufloat(126.3, err_ruler_cm)
length_pvc_m = length_pvc_cm / 100

speed_pvc_mps = 2 * length_pvc_m / pvc_time_s
pvc_modulus = speed_pvc_mps**2 * pvc_density_g_cm3 * 1000

print(f"Speed of sound in PVC: {speed_pvc_mps}")
print(f"Modulus of Elasticity: {pvc_modulus}")

