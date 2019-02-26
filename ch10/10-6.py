#! /usr/bin/python3
import sys
import math


def sol1():
    numberof = 1 << 32
    array = [] * (numberof//8)
    print(numberof)
    print(math.log(sys.maxsize, 2))


def main(argv):
    print(sol1())

if __name__ == "__main__":
    main(sys.argv)
