#! /usr/bin/python3
import sys

def swap_odd_even_bit(value):
    print(bin(value))
    print(bin((int('aaaaaaaa', 16) & value) >> 1))
    print(bin((int('55555555', 16) & value) << 1))
    return ((int('aaaaaaaa', 16) & value) >> 1) | ((int('55555555', 16) & value) << 1)
def main(argv):
    print(bin(swap_odd_even_bit(int(argv[1], 2))))

if __name__ == "__main__":
    main(sys.argv)
