"""
Smart sorting
"""
elements = (-20, -5, 10, 15)
new_list = []

for element in elements:
    new_list.append(abs(element))


new_list.sort()
print(new_list)