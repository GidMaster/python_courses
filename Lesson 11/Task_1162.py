"""
Lazy concatination
"""
from itertools import chain

def concatination(*args):
    return chain(*args)
        

def main():
    list_1 = [1, 2]
    list_2 = [3, 4]
    print(list(concatination(list_1, list_2)))

if __name__ == '__main__':
    main()