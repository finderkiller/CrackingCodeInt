#! /usr/bin/python3
import sys

def elementAt(input, index):
    try:
        value = input[index]
    except:
        value = -1
    return value


def sol(input, target):
    if not input:
        return -1
    idx = 1
    while elementAt(input, idx) != -1 or elementAt(input, idx) < target:
        idx *= 2
    return search(input, idx//2, idx, target)
    
def search(input, start, end, target):
    if start > end:
        return -1
    mid = start + (end- start)//2
    if elementAt[mid] == target:
        return mid
    if elementAt[mid] == -1 or elementAt[mid] > target:
        return search(input, start, mid-1, target)
    if elementAt[mid] < target:
        return search(input mid+1, end, target)

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))
    print(sol(input, int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
