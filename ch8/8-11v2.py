#! /usr/bin/python3
import sys

def sol_brute(amount):
    denoms = [25, 10, 5, 1]
    return sol_brute_helper(amount, denoms, 0)

def sol_brute_helper(amount, denoms, index):
    if amount == 0:
        return 1
    if index == len(denoms) - 1:
        return 1
    ways = 0
    denomAmount = denoms[index]
    i = 0
    while(i*denomAmount <= amount):
        remain = amount - i * denomAmount
        ways += sol_brute_helper(remain, denoms, index + 1)
        i += 1
    return ways

def sol_dp(amount):
    table = {}
    denoms = [25, 10, 5, 1]
    return sol_dp_helper(amount, denoms, 0, table)

def sol_dp_helper(amount, denoms, index, table):
    if amount == 0:
        return 1
    if index == len(denoms) - 1:
        return 1
    if (amount, index) in table:
        return table[(amount, index)]
    ways = 0
    denomAmount = denoms[index]
    i = 0
    while amount >= i * denomAmount:
        remain = amount - i *denomAmount
        ways += sol_dp_helper(remain, denoms, index+1, table)
        i+=1
    table[(amount, index)] = ways
    return table[(amount, index)]

def main(argv):
    print(sol_brute(int(argv[1])))
    print(sol_dp(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
