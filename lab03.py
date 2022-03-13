from math import ceil, floor


Au = 0.1
GOS = 0.005
#U = total number of user

print("(a)")
c = 1
A = 0.005
U = ceil(A/Au)
print("total number of user",U)

print("(b)")
c = 5
A = 1.13
U = floor(A/Au)
print("total number of user =",U)

print("(c)")
c = 10
A = 3.96
U = floor(A/Au)
print("total number of user",U)

print("(d)")
c = 20
A = 11.10
U = floor(A/Au)
print("total number of user",U)

print("(e)")
c = 100
A = 80.9
U = floor(A/Au)
print("total number of user",U)
