"""
Not unic elements.
"""

elements = [1, 2, 3, 1, 3]

not_unic_elements = [element for element in elements if elements.count(element) > 1]
print(not_unic_elements)

