"""
Fizz Buzz
"""

while True:
    number = input('Input number: ')
    if not number.isdecimal():
        print('It\'s not a number.')
        break
    number = int(number)
    response = ('Fizz Buzz' if (number % 3 == 0) and (number % 5 == 0) else
                'Fizz' if number % 3 == 0 else 
                'Buzz' if number % 5 == 0 else
                str(number))
    print(response)
        