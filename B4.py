voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9,
            12.0, 11.8, 11.6, 11.5, 11.5, 11.2]

count = 1
longest = 1
start = voltages[0]
end = voltages[0]
temp = voltages[0]

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        count = count + 1
    else:
        count = 1
        temp = voltages[i]

    if count > longest:
        longest = count
        start = temp
        end = voltages[i]

print("Longest continuous drop:", longest, "readings")
print("Started at:", start, "V")
print("Ended at:", end, "V")
