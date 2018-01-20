"""
Ghost's age
"""

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)

def make_transperency_table(max_transperency, max_age):
    FIBONACCI = list(map(fib, range(0, 21)))
    previous_transperency = max_transperency
    transperency_table = {}
    for age in range(max_age):
        if age in FIBONACCI:
            transperency = previous_transperency - age
        else:
            transperency = previous_transperency + 1
        transperency_table[transperency] = age
        previous_transperency = transperency
    return transperency_table

max_age = 5000
max_transperency = 10000
current_transperency = 9998
transperency_table = make_transperency_table(max_transperency, max_age)

try:
    print(f'current age for {current_transperency} transperency is {transperency_table[current_transperency]}')
except KeyError as e:
    print('Such value does not exist for transperency.')
