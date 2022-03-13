from cmath import sqrt
import math


#For n = 4
print("(a)")
n1 = 4
N = 7
#let, Q = frequency_reuse_factor

Q = pow(3*N,0.5)
signal_to_noise_interference_ratio =int(10*(math.log10(pow(Q,n1)/6)))
#signal_to_noise_interference_ratio= 10*log10((Q^n1)/6)

if signal_to_noise_interference_ratio >= 15:
    print("N=7 can be used.")
else:
    print("N=7 can not be used.")


#For n = 3
print("(b)")
n2 = 3
signal_to_noise_interference_ratio =  int(10*(math.log10(pow(Q,n2)/6)))
if signal_to_noise_interference_ratio >= 15:
    print("N=7 can be used.")
else:
    print("N=7 can not be used.")



#For n = 12

N = 12
Q2 = pow(3*N, 0.5)
signal_to_noise_interference_ratio = int(10*(math.log10(pow(Q2,n2)/6)))
print(signal_to_noise_interference_ratio)
if signal_to_noise_interference_ratio >= 15:
    print("N=12 can be used.")
else:
    print("N=12 can not be used.")

