"""
Not uniq elements.
"""

elements = [1, 2, 3, 3, 5]

not_uniq_elements = [element for element in elements if elements.count(element) > 1]
print(not_uniq_elements)

