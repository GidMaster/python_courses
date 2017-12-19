"""
Smart Sorting
"""

elements = (-20, -5, 10, -10, -12, 0, 0, 15)

new_list = sorted(elements, key=abs)
print(new_list)