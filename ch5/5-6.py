#! /usr/bin/python3
import sys

def sol1(a, b):
    print(a)
    print(b)
    c = a ^ b
    ret = 0
    while(c != 0):
        ret += c & 1
        c = c >> 1
    return ret

def sol2(a, b):
    c = a ^ b
    ret = 0
    while(c != 0):
        ret += 1
        c &= c-1
    return ret

def main(argv):
    print(sol1(int(argv[1], 2), int(argv[2], 2)))
    print(sol2(int(argv[1], 2), int(argv[2], 2)))
if __name__ == "__main__":
    main(sys.argv)
