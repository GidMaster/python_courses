"""
Modulo operation
"""

from random import randint

a = randint(0, 100)
b = randint(0, 100)


if a >= b:
    modulus = a % b
    integer = a // b
else:
    modulus = b % a
    integer = b // a



print("First number: {}".format(str(a)))
print("Second number: {}".format(str(b)))
print("modulus: {}".format(str(modulus)))
print("integer: {}".format(str(integer)))
