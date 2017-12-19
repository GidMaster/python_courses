"""
Median
"""

elements = [1, 300, 2, 300, 1]

elements.sort()

list_len = len(elements)

if (list_len % 2) == 0:
    median = (elements[list_len // 2] + elements[(list_len // 2) - 1]) / 2
else:
    median = elements[list_len // 2]
print(median)
