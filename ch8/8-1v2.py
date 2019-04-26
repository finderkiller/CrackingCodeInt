#! /usr/bin/python3
import sys

def sol_brute_force(value):
    if (value < 0):
        return 0
    if (value == 0):
        return 1
    return sol_brute_force(value-1) + sol_brute_force(value-2) + sol_brute_force(value-3)

def sol_mem(value):
    mem = [-1] * (value+1)    #1~value, ignore idx0
    return countway(value, mem)

def countway(value, mem):
    if (value < 0):
        return 0
    if value == 0:
        return 1
    if mem[value] > -1:
        return mem[value]

    mem[value] = countway(value-1, mem) + countway(value-2, mem) + countway(value-3, mem)
    return mem[value]

def main(argv):
    print(sol_brute_force(int(argv[1])))
    print(sol_mem(int(argv[1])))


if __name__ "__main__":
    main(sys.argv)
