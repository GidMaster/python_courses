"""
Rounding
"""

from random import uniform

a = uniform(0, 1000)
print(str(a))
print(str(round(a, 2)))
print('{0:=011}'.format(round(a, 2)))
