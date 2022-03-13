import math
fc = 1.8
hb = 20
#d=distance of mobile from base station
z = (pow(20,2)+pow(30,2))
d = (pow(z, 0.5)/1000)
path_loss = 135.41+(12.49*(math.log10(fc)))-(4.99*(math.log10(hb)))+((46.84-2.34*(math.log10(hb)))*(math.log10(d)))
print(path_loss)