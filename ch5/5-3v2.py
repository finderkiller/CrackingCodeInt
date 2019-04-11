#! /usr/local/bin/python3
import sys

def find_longest(value):
    print(bin(value))
    print(~value)
    print(bin(~value))
    if value == -1:
        return 32

    currentPath = 0
    maxlength = -1
    previousPath = 0
    while (value != 0):
        if (value & 1 == 1):
            currentPath += 1
        else if (value & 1 == 0):
            previousPath = currentPath if (value&2)==1 else 0
            currentPath = 0
        maxlength = max(previousPath + currentPath + 1, maxlength)
        value = value >> 1

def main(argv):
    print(find_longest(int(argv[1])))


if __name__ == "__main__":
    main(sys.argv)