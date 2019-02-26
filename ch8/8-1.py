#! /usr/bin/python3
import sys

def sol_brute_force(value):
    if (value < 0):
        return 0
    elif (value == 0):
        return 1
    else:
        return sol_brute_force(value - 1) + sol_brute_force(value - 2) + sol_brute_force(value - 3)

def sol_memorization(value):
    memo = [-1] * (value + 1)
    return countway(value, memo)

def countway(value, memo):
    if (value < 0):
        return 0
    elif (value == 0):
        return 1

    if memo[value] == -1:
        memo[value] = countway(value - 1, memo) + countway(value - 2, memo) + countway(value - 3, memo)

    return memo[value]


def main(argv):
    print(sol_memorization(int(argv[1])))
    print(sol_brute_force(int(argv[1])))

if __name__ == "__main__":
    main(sys.argv)
