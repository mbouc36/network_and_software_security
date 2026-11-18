
irreducible_polynomial = 0x11B

def gf_multiply(a,b):
    result = 0
    while b > 0:
        if b & 1:
            result ^= a
        a <<=1
        if a & 0x100:
            a ^=irreducible_polynomial
        b>>=1

    return result

print(hex(gf_multiply(0x57, 0x83)))
print(hex(gf_multiply(0x53, 0xCA)))

B = (292 % 255) + 1

print("B is: ", hex(B))
print("B * 0x1C: ", hex(gf_multiply(B, 0x1C)))





for i in range(1, 0x100):
    if gf_multiply(B, i) == 0x01:
        print(f"Inverse: 0x{i:02X}")
        break
else:
        print("No multiplicative inverse")

assert gf_multiply(0x26, 0xA8) == 0x01