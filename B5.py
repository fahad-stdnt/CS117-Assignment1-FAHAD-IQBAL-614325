one = 0
five = 0
reject = 0

while True:
    R = float(input("Enter resistance (0 to stop): "))

    if R == 0:
        break
    elif R >= 99 and R <= 101:
        one = one + 1
    elif R >= 95 and R <= 105:
        five = five + 1
    else:
        reject = reject + 1

print("1% tolerance:", one)
print("5% tolerance:", five)
print("Reject:", reject)
