#! /usr/bin/python3
import sys


def sol3_modified_recursive(a, b):
    smaller = a if a < b else b
    bigger = a if a>= b else b
    sol3_helper(smaller, bigger)

def sol3_helper(smaller, bigger):
    if (smaller == 0):
        return 0
    if (smaller == 1):
        return bigger
    s = smaller >> 1
    side1 = sol3_helper(s, bigger)
    side2 = side1
    if (smaller % 2 !=0):
        side2 += bigger
    return side1+side2

def sol2_dp(a, b):
    smaller = 0
    bigger = 0
    if a >= b:
        smaller = b
        bigger = a
    else:
        smaller = a
        bigger = b
    mem = [None] * smaller+1
    sol1_dp_helper(smaller, bigger, mem)

def sol2_dp_helper(smaller, bigger, mem):
    if (smaller == 0):
        return 0
    if (smaller == 1):
        return bigger
    if (mem[smaller] != None):
        return mem[smaller]

    s = smaller >> 1
    side1 = sol2_dp_helper(s, bigger, mem)
    side2 = 0
    if (smaller % 2 != 0):
        side2 = sol2_dp_helper(smaller - s, bigger, mem)
    else:
        side2 = side1

    mem[smaller] = side1 + side2
    return mem[smaller]

def sol1_recursive(a, b):
    smaller = 0
    bigger = 0
    if a >= b:
        smaller = b
        bigger = a
    else:
        smaller = a
        bigger = b
    sol1_recursive_helper(smaller, bigger)

def sol1_recursive_helper(smaller, bigger):
    if (smaller == 0):
        return 0
    if (smaller == 1):
        return bigger
    s = smaller >> 1
    side1 = sol1_recursive_helper(s, bigger)
    side2 = 0
    if (smaller % 2 != 0):
        side2 = sol1_recursive_helper(smaller - s, bigger)
    else:
        side2 = side1
    return side2 + side1

def main(argv):
    print(sol1_recursive(int(argv[1]), int(argv[2])))
    print(sol2_dp(int(argv[1]), int(argv[2])))
    print(sol3_modified_recursive(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
