"""
cipher cage
"""

import numpy

cipher = ( 'X...',
            '..X.',
            'X..X',
            '....')
for row in cipher:
    print(row)

cipher_90 = tuple(zip(*cipher[::-1]))
print ('+90')
for row in cipher_90:
    print(row)
cipher_180= (cipher[::-1])
print ('+180')
for row in cipher_180:
    print(row)

crypted_message = ( 'itdf',
                    'gdce',
                    'aton',
                    'qrdi')
# результат: 'icantforgetiddqd'

