import math


t_r_distance= 5
E_field=pow(10,-3) 
d0=1000
d=5000
ht=50
hr=1.5
frequency=900
lemda= 300/900
print("(a)")
length_of_antenna=lemda/4
print("length_of_antenna",length_of_antenna)
a = (2.555/10)
gain= pow(10, a)
print("gain",gain)

print('(b)')
Er_d= (2*E_field*d0*2*3.1416*ht*hr)/(lemda*d*d)
Ae=(gain*pow(lemda,2))/(4*3.1416)
Pr_d= (pow(Er_d,2)/(120*3.1416))*Ae
received_power_at_5_km_distance= 10*(math.log10(Pr_d))
print(received_power_at_5_km_distance)