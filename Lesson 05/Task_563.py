"""
sequence
"""

from random import randint

number = randint(1, 9)
sequence = ''

for i in range(number):
    sequence += str(i + 1)
print(f"N = {number}, результат = {sequence}")