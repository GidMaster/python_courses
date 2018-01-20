"""
Palindrom
"""

def palindrom(line):
    length = len(line)
    for i in range(int(length/2)):
        if line[i] != line[length -1 - i]:
            return False
    return True

def main():
    line = 'ollo'
    print(palindrom(line))


if __name__ == '__main__':
    main()    