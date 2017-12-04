"""
arithmetic mean
"""

from random import randint

a = randint(0, 100)
b = randint(0, 100)
c = randint(0, 100)

mean = (a + b + c) / 3

print("First number: {}".format(str(a)))
print("Second number: {}".format(str(b)))
print("Third number: {}".format(str(c)))
print("arithmetic mean: {}".format(str(mean)))
print("({0}+{1}+{2})/3={3:3}".format(str(a), str(b), str(c), str(mean)))
