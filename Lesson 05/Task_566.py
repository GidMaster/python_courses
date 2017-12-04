"""
Lefthands 
Didn't undestand where loops?
"""

words = ["bright aright", "ok"]

delemiter = ','

main_string = delemiter.join(words)

main_string.lower()
main_string =  main_string.replace('right', 'left')

print(main_string)
