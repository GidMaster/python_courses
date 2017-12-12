"""
Fizz Buzz
"""

while True:
    number = input('Input number: ')
    if not number.isdecimal():
        print('It\'s not a number.')
        break
    number = int(number)
    if (number % 3 == 0) and (number % 5 == 0):
        print('Fizz Buzz')
        break
    elif number % 3 == 0:
        print('Fizz')
        break
    elif number % 5 == 0:
        print('Buzz')
        break
    else:
        print(number)
        
