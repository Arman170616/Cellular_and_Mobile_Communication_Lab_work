import math 

hm = 2
fc = 900
hb = 100
d = 4
a_hm = (3.2*(math.log10(11.75*hm))*(math.log10(11.75*hm)))-4.97
path_loss = 69.55+26.16*(math.log10(fc))-13.82*(math.log10(hb))-a_hm+(44.9-6.55*(math.log10(hb)))*(math.log10(d))
print(path_loss)

 