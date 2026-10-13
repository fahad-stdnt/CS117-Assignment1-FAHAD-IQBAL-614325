n = int(input("How many resistors? "))
total = 0

for i in range(1, n + 1):
    R = float(input("Enter R" + str(i) + ": "))
    total = total + R

print("Total resistance =", total, "ohm")
