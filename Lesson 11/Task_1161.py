"""
accidents are no coincidence
"""
from random import uniform

def new_random(number):
    for i in range(number):
        yield uniform(0, number)

def main():
    n = 3
    print(list(new_random(n)))

if __name__ == '__main__':
    main()
