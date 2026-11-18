d = -20
p = 17
while d < 0:
    d += p


valid_points = []

for x in range(p):
    for y in range(p):
        if ((x**2) + (y**2)) %p == (1 + d*(x**2)*(y**2)) %p:
            valid_points.append((x, y)) 


def point_addition(p1, p2):

    x1, y1 = p1
    x2, y2 = p2
    term = d * x1 * x2 * y1 * y2

    x = ((x1 * y2 + y1 * x2) * pow(1 + term, -1, p)) % p
    y = ((y1 * y2 - x1 * x2) * pow(1 - term, -1, p)) % p
    return (x, y)


def print_addition_table():
    for i in valid_points:
        line = ""
        for j in valid_points:
            line += str(point_addition(i, j)) + " "
        print(line)


print_addition_table()




def find_generators():
    generators = []
    identity = (0, 1)
    for point in valid_points:
        current = identity
        for j in range(1, len(valid_points) + 1):
            current = point_addition(current, point)

            if current == identity:
                if j == len(valid_points):
                    generators.append(point)
                break

    return generators

print("")
print("Generators: ", find_generators())

g = find_generators()[0]
x = 2 * (9 % 7) + 3
y = 2 * (2 % 7) + 3

def generator_addition(g, coeff):
    point = (0, 1)
    for _ in range(coeff):
        point = point_addition(point, g)
    return point

alice_public_point = generator_addition(g, x)
bob_public_point = generator_addition(g, y)

alice_shared_point = generator_addition(alice_public_point, y)
bob_shared_point = generator_addition(bob_public_point, x)
assert alice_shared_point == bob_shared_point


alice_public_point_2 =generator_addition(g, 8)
print(alice_public_point_2)

shared_point = generator_addition(alice_public_point_2, 5)
print(shared_point)