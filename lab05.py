import math

pt=50
fc=900
gt=1 
gr=1
d=100;
print('(a)')
Transmitter_power_in_dBm= math.ceil(10*(math.log10(50*1000)))
print("Transmitter power in dBm", Transmitter_power_in_dBm)
print('(b)')

Transmitter_power_in_dBW= math.ceil(10*(math.log10(50*1)))
print("Transmitter power in dBW", Transmitter_power_in_dBW)
pr_mW=(pt*gt*gr*(3/9)*(3/9))/(16*3.1416*3.1416*10)
received_power_in_dBm=10*(math.log10(pr_mW))
print("received_power_in_dBm",received_power_in_dBm)
pr_10km= received_power_in_dBm+(20*(math.log10(100/10000)))
print("pr_10km", pr_10km)
