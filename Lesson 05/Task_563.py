"""
sequence
"""

from random import randint

number = randint(1, 9)
sequence = ''

for i in range(1, number):
    sequence += str(i)
print(f"N = {number}, результат = {sequence}")