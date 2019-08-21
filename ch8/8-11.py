#! /usr/local/bin/python3
import sys
import time

def sol_brute_helper(amount, denom, index):
    if (amount == 0):
        return 1
    if (index == len(denom)):
        return 0
    ways = 0
    denommount = denom[index]
    i = 0
    while(i * denommount <= amount):
        remain = amount - i * denommount
        ways += sol_brute_helper(remain, denom, index + 1)
        i += 1
    return ways

def sol_brute(n):
    denom = [5, 2, 1]
    return sol_brute_helper(n, denom, 0)

def sol_dp_helper(amount, denom, index, table):
    if ((amount, index) in table):
        return table[(amount, index)]
    if (amount == 0):
        return 1
    if (len(denom) - 1 == index):
        return 1
    ways = 0
    denommount = denom[index]
    i = 0
    while(i * denommount <= amount):
        remain = amount - i * denommount
        ways += sol_dp_helper(remain, denom, index + 1, table)
        i += 1
    table[(amount, index)] = ways
    return table[(amount, index)]


def sol_dp(n):
    table = {}
    denom = [5, 2, 1]
    return sol_dp_helper(n, denom, 0, table)

def main(argv):
    start = time.time()
    print(sol_brute(int(argv[1])))
    end = time.time()
    print(end-start)
    start = time.time()
    print(sol_dp(int(argv[1])))
    end = time.time()
    print(end-start)

if __name__ == "__main__":
    main(sys.argv)
