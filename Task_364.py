"""
Input: some digints in format xxxxxxxxx.xxx
Output: formated output xxx,xxx,xxx.xx
"""

amount = '12.12'

integer = amount.split('.')[0]
after_float = amount.split('.')[1]

formated_integer = ''

for i in range(len(integer)):
    if (i % 3 == 0) and (i != 0) :
        formated_integer = ',' + formated_integer
    formated_integer = integer[len(integer)- i - 1] + formated_integer
print("{0}.{1}".format(formated_integer, after_float))
