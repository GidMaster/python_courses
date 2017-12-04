"""
carpet
"""

print("Carpet.")
height = input("height of carpet: ")

if height.isdigit():
    height = int(height)
    if height > 7:
        width = height * 3
        for puzzle in range(1, height, 2):
            print(('.|.' * puzzle).center(width, '-'))
        print('WELCOME'.center(width, '-'))
        for puzzle in range(height-2, 0, -2):
            print(('.|.' * puzzle).center(width, '-'))
    else:
        print("Too small.")
else:
    print("wrong input.")