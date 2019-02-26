#! /usr/bin/python3
import sys
import time

def sol_modified_recursive(a, b):
    smaller = a if a < b else b
    bigger = a if a >= b else b

    return modified_recursive_helper(smaller, bigger)

def modified_recursive_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1
    halfpro = modified_recursive_helper(s, bigger)
    if (smaller % 2 != 0):
        return halfpro + halfpro + bigger
    else:
        return halfpro + halfpro

def sol_dp(a, b):
    smaller = a if a < b else b
    bigger = a if a >= b else b

    memo = [None] * (smaller + 1)
    return dp_helper(smaller, bigger, memo)

def dp_helper(smaller, bigger, memo):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    if memo[smaller] != None:
        return memo[smaller]

    s = smaller >> 1
    side1 = dp_helper(s, bigger, memo)
    if (smaller % 2 != 0):
        side2 = dp_helper(smaller - s, bigger, memo)
    else:
        side2 = side1
    memo[smaller] = side1 + side2
    return memo[smaller]

def sol_recursive(a, b):
    smaller = a if a < b else b
    bigger = a if a >= b else b

    return recursive_helper(smaller, bigger)

def recursive_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    s = smaller >> 1
    side1 = recursive_helper(s, bigger)
    if (smaller % 2 != 0):
        side2 = recursive_helper(smaller - s, bigger)
    else:
        side2 = side1
    return side2 + side1

def main(argv):
    start = time.time()
    print(sol_dp(int(argv[1]), int(argv[2])))
    end = time.time() - start
    print(end)
    start = time.time()
    print(sol_recursive(int(argv[1]), int(argv[2])))
    end = time.time() - start
    print(end)
    start = time.time()
    print(sol_modified_recursive(int(argv[1]), int(argv[2])))
    end = time.time() - start
    print(end)


if __name__ == "__main__":
    main(sys.argv)
