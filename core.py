import math

def refraction(k, t_delta, r_last, R_natural, d_n, rx_last):
  return r_last + (R_natural + d_n + rx_last - r_last)*(1 - math.exp((-1)*(t_delta/k)))

time_constant = float(input("Time constant (months) = "))
time_gap = float(input("Time difference in refractions (months) = "))
last_refraction = float(input("Last value of refraction (Diopters) = "))
natural_refraction =float(input("Natural refraction point (Diopters) = "))
near_demand = float(input("Effective near use power (Diopters) = "))
last_rx = float(input("Last correction prescription = "))

next_refraction = refraction(time_constant, time_gap, last_refraction, natural_refraction, near_demand, last_rx)

print(f"Next refraction is {next_refraction}")
