import math
from euclidean_algorithm import extended_euclidean_algorithm
INPUT_NUMBER = 101287292
field = 6319
m1 = 128 % field
m2 = 7292 % field

p = 71
q = 89 
e = 3

n =p*q

t = math.lcm(p-1, q-1)
r, x, y = extended_euclidean_algorithm(e, t)
d = x % t  
s1 = (m1**d)%n
s2 = (m2**d)%n 
assert (s1**e)%n == m1
assert (s2**e)%n == m2

s3 = (s1 * s2) % n
m3 = (m1 * m2) % n

assert pow(s3, e, n) == m3