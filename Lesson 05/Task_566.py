"""
Lefthands 
Didn't undestand where loops?
"""

words = ["bright aright", "ok"]

delimiter = ','

main_string = delimiter.join(words)

main_string = main_string.lower()
main_string =  main_string.replace('right', 'left')

print(main_string)
