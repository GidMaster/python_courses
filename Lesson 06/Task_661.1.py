"""
 Sum all even index multiplay last index
"""

elements = [0, 1, 2, 3, 4, 5]
summary = sum(elements[::2]) * elements[-1]
print(summary)