"""
list from numbers
"""
def reverse(number):
    char_list = list(reversed(str(number)))
    return char_list

def main():
    number = 35421748554
    print(reverse(number))

if __name__ == '__main__':
    main()