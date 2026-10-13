def loaded_divider(vs, r1, r2, rl):
    unloaded = vs * r2 / (r1 + r2)
    parallel = r2 * rl / (r2 + rl)
    loaded = vs * parallel / (r1 + parallel)

    return unloaded, loaded


vs = float(input("Enter source voltage: "))
r1 = float(input("Enter R1: "))
r2 = float(input("Enter R2: "))
rl = float(input("Enter load resistance: "))

a, b = loaded_divider(vs, r1, r2, rl)

print("Unloaded voltage:", round(a, 2), "V")
print("Loaded voltage:", round(b, 2), "V")
