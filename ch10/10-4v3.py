#! /usr/bin/python3
import sys

def elementAt(input, index):
    try:
        value = input[index]
    except:
        value = -1
    return value


def sol(input, target):
    if len(input) == 0:
        return -1
    index = 1
    while elementAt(input, index) != -1 and input[index] < target:
        index *= 2

    return impl(input, index//2, index, target)

def impl(input, start, end, target):
    while (start <= end):
        mid = (start+end)//2
        if elementAt(input, mid) == -1 or elementAt(input, mid) > target:
            end = mid - 1
        elif elementAt(input, mid) < target:
            start = mid + 1
        else:
            return mid
    return -1


def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))
    print(sol(input, int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
