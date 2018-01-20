"""
schufle
"""
from itertools import product

x = {0, 1}
n = 3
z = 2

result = []

for i in product(x, repeat=n):
    #print(i)
    #print(sum(i))
    if sum(i) != z:
        result.append(i)

print(result)