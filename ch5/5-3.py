#! /usr/bin/python3
import sys

def sol(value):
    print(bin(value))
    print(bin(~value))
    print(~value)
    if (~value == 0):
        return bytes(value)*8
    current_length = 0
    previous_length = 0
    max_length = 1
    while(value != 0):
        if (value & 1 == 1):
            current_length += 1
        else:
            previous_length = current_length if value & 2 == 1 else 0
            current_length = 0

        max_length = max(previous_length + 1 + current_length, max_length)
        value = value >> 1

    return max_length

def main(argv):
    print(sol(int(argv[1], 2)))

if __name__ == "__main__":
    main(sys.argv)
