def star_to_delta(ra, rb, rc):
    S = ra * rb + rb * rc + rc * ra

    rab = S / rc
    rbc = S / ra
    rca = S / rb

    return rab, rbc, rca


ra = float(input("Enter Ra: "))
rb = float(input("Enter Rb: "))
rc = float(input("Enter Rc: "))

a, b, c = star_to_delta(ra, rb, rc)

print("RAB:", round(a, 2), "ohm")
print("RBC:", round(b, 2), "ohm")
print("RCA:", round(c, 2), "ohm")
