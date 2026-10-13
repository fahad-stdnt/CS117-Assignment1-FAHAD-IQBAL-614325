v = float(input("Enter voltage (V): "))
r = float(input("Enter resistance (ohm): "))

if r <= 0:
    print("Invalid resistance")
else:
    I = v / r
    print("Current =", I, "A")

    if I > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
