"""
Smart multiplies
"""

from random import randint

number = randint(1, 100000000)

print(f'Число: {number}')
result = 1
number_to_string = str(number)

for digit_to_string in number_to_string:
    digit = int(digit_to_string)
    if digit != 0:
        result = result * digit
print(f'Дано число {number}. Результат "умного умножения" будет: {result}.')