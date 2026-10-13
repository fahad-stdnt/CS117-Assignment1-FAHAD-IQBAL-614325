def parallel_resistance(resistors):
    total = 0

    for R in resistors:
        total = total + 1 / R

    return 1 / total

n = int(input("How many resistors? "))
resistors = []

for i in range(n):
    R = float(input("Enter resistance: "))
    resistors.append(R)

answer = parallel_resistance(resistors)

print("Parallel resistance =", round(answer, 2), "ohm")
