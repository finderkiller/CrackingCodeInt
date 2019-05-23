#! /usr/bin/python3
import sys

def sol1_recursive_helper(small, big):
    if small == 0:
        return 0
    if small == 1:
        return big
    s = small >> 1
    side1 = sol1_recursive(s, big)
    side2 = side1
    if small % 2 == 1:
        side2 += big
    return side1 + side2

def sol1_recursive(a, b):
    if a == 0 or b == 0:
        return 0
    if a > b:
        small = b
        big = a
    else:
        big = b
        small = a
    return sol1_recursive_helper(small, big)

def sol2_dp_helper(small, big, table):
    if small == 0:
        return 0
    if small == 1:
        return big
    if table[small] != None:
        return table[small]
    s = small >> 1
    side1 = sol2_dp_helper(s, big, table)
    side2 = side1
    if small % 2 == 1:
        side2 += big
    table[small] = side1 + side2
    return table[small]

def sol2_dp(a, b):
    if a == 0 or b == 0:
        return 0
    if a > b:
        small = b
        big = a
    else:
        big = b
        small = a
    table = [None] * (small+1)
    return sol2_dp_helper(small, big, table)

def main(argv):
    print(sol1_recursive(int(argv[1]), int(argv[2])))
    print(sol2_dp(int(argv[1]), int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
