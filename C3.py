def decimal_to_binary(n):
    whole = int(n)
    fraction = n - whole
    binary = ""

    if whole == 0:
        binary = "0"

    while whole > 0:
        binary = str(whole % 2) + binary
        whole = whole // 2

    if fraction > 0:
        binary = binary + "."

        for i in range(10):
            fraction = fraction * 2

            if fraction >= 1:
                binary = binary + "1"
                fraction = fraction - 1
            else:
                binary = binary + "0"

    return binary


n = float(input("Enter a decimal number: "))
print("Binary:", decimal_to_binary(n))
