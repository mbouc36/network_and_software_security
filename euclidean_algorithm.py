import math

INPUT_NUMBER = 101287292
def gcd(a, b):
    """
    Finds the greatest common divisor of two integers
    """
    if a == 0:
        return b

    return gcd(b % a, a)


def euclidean_algorithm(a, b):
    """Simply finds the GCD of 2 ints """
    return gcd(a, b)

def extended_euclidean_algorithm(a, b):
    """Finds the GCD but also calculates x and y such that:
        ax + by = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1

    gcd, x1, y1 =  extended_euclidean_algorithm(b % a, a)
    x = y1 - (b//a) * x1
    y = x1

    return gcd, x, y


if __name__ == "__main__":

    extended_euclidean_algorithm(INPUT_NUMBER, 117035)

    print(f"The gcd of {INPUT_NUMBER} and {117035} is: {euclidean_algorithm(INPUT_NUMBER, 117035)}")


    r, q1, q2 = extended_euclidean_algorithm(INPUT_NUMBER, 117035)
    print(f"The gcd of {INPUT_NUMBER} and {117035} is: {r} where q1:{q1} q2:{q2}")


    # check

    if euclidean_algorithm(INPUT_NUMBER, 117035) != math.gcd(INPUT_NUMBER, 117035):
        print("Euclidean Algorithm Failed")

    if r != math.gcd(INPUT_NUMBER, 117035) or q1*INPUT_NUMBER + q2*117035 != r :
        print("Extended Euclidean Algorithm Failed")

    c = (292 % 270) + 1

    r, x, y = extended_euclidean_algorithm(c, 271)
    print("The multiplicative inverse of c is : ", x % 271)
    if x % 271 != pow(c, -1, 271):
        print("failed to calc multiplicative inverse")


    def compute_repeated_exponential_mod(base, exponent, mod):
        result = 1

        for _ in range(exponent):
            result = (result * base) % mod

        return result

    u = 92 + 2

    print("U^250 mod 569 =",compute_repeated_exponential_mod(u, 350, 569))
    print("Using pow: ", pow(u, 350, 569))
    print("u^350 = ", pow(u, 350))
    print("Number of digits in u^350 :", len(str( pow(u, 350))))


    full = pow(u, 350)
    reduced = pow(u, 350, 569)

    print("Digits in u^350:", len(str(full)))
    print("Digits in u^350 mod 569:", len(str(reduced)))