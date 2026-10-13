def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return i * i * r

V = int(input("Enter voltage value: "))
R = int(input("Enter resistance value: "))

I = ohms_current(V, R)
P = power_dissipated(I, R)

print("Current =", I, "A")
print("Power =", P, "W")
