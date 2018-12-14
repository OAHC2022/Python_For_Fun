"""
Let a,b,q,r belong to Z with a = b*q + r
Using Euclidean algorithm: gcd(a,b) = gcd(b,r) to make a GCD calculator
"""
a = int(input("Give me an integer: "))
b = int(input("Give me an integer: "))
temp_a = a
temp_b = b
r = 0
q = 0
u = 0
v = 0
gcd = 0
while True:
    if temp_a % temp_b == 0:
        gcd = temp_b
        break
    r = temp_a % temp_b
    temp_a = temp_b
    temp_b = r

print("The greatest common divisor of {} and {} is {}".format(a,b,gcd))
