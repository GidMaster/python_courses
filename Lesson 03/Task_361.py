"""
Input: name, surname
Result: Print string "Hello NAME SURNAME! You just delved into Python. Great start!"
"""
import re

name = ''
surname = ''

name_pattern = re.compile(r'[a-zA-Z\-\']+')


while (re.match(name_pattern, name) is None) or (re.match(name_pattern, surname) is None):
    if not re.match(name_pattern, name):
        name = input('Type name (from the capital letter): ')
    if not re.match(name_pattern, surname):
        surname = input('Type surname (from the capital letter): ')
output = 'Hello {name} {surname}! You just delved into Python. Great start!'.format(name=name.capitalize(), surname=surname.capitalize())
print(output)
