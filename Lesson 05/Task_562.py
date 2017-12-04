"""
Estimation
"""

from random import randint

number = randint(1, 50)

print(f"Случайное число - {number}")

if number % 2 != 0:
    print('Плохо.')
elif 2 <= number <= 5:
    print('Неплохо.')
elif 6 <= number <= 20:
    print('Так себе.')
elif number > 20:
    print('Отлично.')