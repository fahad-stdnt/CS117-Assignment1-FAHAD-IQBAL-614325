readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)

count = 0
highest = readings[0]
lowest = readings[0]
total = 0

for value in readings:
    if value > 3.2:
        count = count + 1

    if value > highest:
        highest = value

    if value < lowest:
        lowest = value

    total = total + value

average = total / len(readings)

print("Readings above 3.2V : ", count)
print("Highest:", highest, "V")
print("Lowest:", lowest, "V")
print("Average:", average, "V")
