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


extended_euclidean_algorithm(INPUT_NUMBER, 117035)

print(f"The gcd of {INPUT_NUMBER} and {117035} is: {euclidean_algorithm(INPUT_NUMBER, 117035)}")


r, q1, q2 = extended_euclidean_algorithm(INPUT_NUMBER, 117035)
print(f"The gcd of {INPUT_NUMBER} and {117035} is: {r} where q1:{q1} q2:{q2}")


# check

if euclidean_algorithm(INPUT_NUMBER, 117035) != math.gcd(INPUT_NUMBER, 117035):
    print("Euclidean Algorithm Failed")

if r != math.gcd(INPUT_NUMBER, 117035) or q1*INPUT_NUMBER + q2*117035 != r :
     print("Extended Euclidean Algorithm Failed")