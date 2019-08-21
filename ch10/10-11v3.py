#! /usr/bin/python3
import sys

def sol2(array):
    if not array or len(array) == 2:
        return array
    for idx in range(1, len(array), 2):
        pos = findMax(array, idx-1, idx, idx+1)
        swap(array, idx, pos)
    return array
    

def findMax(array, a, b, c):
    leftvalue = array[a] if a < len(array) else -sys.maxsize-1
    midvalue = array[b] if b < len(array) else -sys.maxsize-1
    rightvalue = array[c] if c < len(array) else -sys.maxsize-1

    max_value = max(leftvalue, midvalue, rightvalue)
    if max_value == leftvalue:
        return a
    if max_value == midvalue:
        return b
    if max_value == rightvalue:
        return c

def sol1(array):
    if not array:
        return array
    array = sorted(array)
    for idx in range(1, len(array), 2):
        swap(array, idx-1 idx)
    return array

def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = array[a]

def main(argv):
    a = []
    for value in argv[1].split(','):
        a.append(int(value))
    print(sol1(a))
    print(sol2(a))

if __name__ == "__main__":
    main(sys.argv)
