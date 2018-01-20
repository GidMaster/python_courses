"""
Min-max
"""

def my_min(*args, key=(lambda x: x )):
    if len(args) == 1:
        args = args[0]
    min_value = args[0]
    for argument in args:
        if key(argument) < key(min_value):
            min_value = argument
    return min_value

def my_max(*args, key=(lambda x: x )):
    if len(args) == 1:
        args = args[0]
    max_value = args[0]
    for argument in args:
        if key(argument) > key(max_value):
            max_value = argument
    return max_value

def main():
    my_args = [1,2,4,123,0,-12]
    print(my_min(my_args, key=abs))
    print(my_max(my_args, key=abs))

if __name__ == '__main__':
    main()