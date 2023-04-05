import&nbsp;math

def&nbsp;refraction(k,&nbsp;t_delta,&nbsp;r_last,&nbsp;R_natural,&nbsp;d_n,&nbsp;rx_last):
&nbsp;&nbsp;return&nbsp;r_last&nbsp;+&nbsp;(R_natural&nbsp;+&nbsp;d_n&nbsp;+&nbsp;rx_last&nbsp;-&nbsp;r_last)*(1&nbsp;-&nbsp;math.exp((-1)*(t_delta/k)))

time_constant&nbsp;=&nbsp;float(input("Time&nbsp;constant&nbsp;(months)&nbsp;=&nbsp;"))
time_gap&nbsp;=&nbsp;float(input("Time&nbsp;difference&nbsp;in&nbsp;refractions&nbsp;(months)&nbsp;=&nbsp;"))
last_refraction&nbsp;=&nbsp;float(input("Last&nbsp;value&nbsp;of&nbsp;refraction&nbsp;(Diopters)&nbsp;=&nbsp;"))
natural_refraction&nbsp;=float(input("Natural&nbsp;refraction&nbsp;point&nbsp;(Diopters)&nbsp;=&nbsp;"))
near_demand&nbsp;=&nbsp;float(input("Effective&nbsp;near&nbsp;use&nbsp;power&nbsp;(Diopters)&nbsp;=&nbsp;"))
last_rx&nbsp;=&nbsp;float(input("Last&nbsp;correction&nbsp;prescription&nbsp;=&nbsp;"))

next_refraction&nbsp;=&nbsp;refraction(time_constant,&nbsp;time_gap,&nbsp;last_refraction,&nbsp;natural_refraction,&nbsp;near_demand,&nbsp;last_rx)

print(f"Next&nbsp;refraction&nbsp;is&nbsp;{next_refraction}")
