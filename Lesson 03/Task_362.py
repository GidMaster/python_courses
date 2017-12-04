"""
Input: Chapter, wide
result: Psedo graphic letter H with arrows
"""
chapter = input("chapter: ")
wide = input("wide: ")
wide = int(wide)

for i in range(wide):
    print((chapter*i).rjust(wide-1) + chapter + (chapter*i).ljust(wide-1))
for i in range(wide+1):
    print((chapter*wide).center(wide*2) + (chapter*wide).center(wide*6))
for i in range((wide+1)//2):
    print((chapter*wide*5).center(wide*6))    
for i in range(wide+1):
    print((chapter*wide).center(wide*2) + (chapter*wide).center(wide*6))    
for i in range(wide):
    print(((chapter*(wide-i-1)).rjust(wide) + chapter + (chapter*(wide-i-1)).ljust(wide)).rjust(wide*6))
