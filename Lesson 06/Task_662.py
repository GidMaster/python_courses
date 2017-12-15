"""
Max - Min
"""

elements = [10.2, -2.2, 0, 1.1, 0.5]

if elements:
    maximum = max(elements)
    minimum = min(elements)
    result = maximum - minimum
else:
    result = 0
print(round(result, 2))
