"""
 Sum all even index multiplay last index
"""

elements = [0, 1, 2, 3, 4, 5]
summary = 0
result = 0

for index in range(len(elements)):
    if index % 2 == 0:
        summary += elements[index]
result = summary * elements[len(elements) - 1]

print(result)
