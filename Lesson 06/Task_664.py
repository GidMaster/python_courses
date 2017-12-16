"""
Median
"""

elements = [1, 300, 2, 300, 1]

elements.sort()

if (len(elements) % 2) == 0:
    median = (elements[len(elements) // 2] + elements[(len(elements) // 2) - 1]) / 2
else:
    median = elements[len(elements) // 2]
print(median)

print(elements)