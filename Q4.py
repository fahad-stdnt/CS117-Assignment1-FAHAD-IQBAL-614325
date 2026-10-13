A = int(input("Enter A: "))
B = int(input("Enter B: "))

if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("Bits must be 0 or 1")
else:
    print("AND =", A * B)
    
    if A == 1 or B == 1:
        print("OR = 1")
    else:
        print("OR = 0")

    if A != B:
        print("XOR = 1")
    else:
        print("XOR = 0")
