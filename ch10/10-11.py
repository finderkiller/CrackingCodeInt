#! /usr/bin/python3
import sys

def sol2(array):
    ret = list(array)
    for idx in range(1, len(ret), 2):
        maxidx = findMax(ret, idx - 1, idx, idx + 1)
        swap(ret, idx, maxidx)
    return ret

def findMax(array, a, b, c):
    valuea = array[a] if 0 < a < len(array) else (-sys.maxsize-1)
    valueb = array[b] if 0 < b < len(array) else (-sys.maxsize-1)
    valuec = array[c] if 0 < c < len(array) else (-sys.maxsize-1)

    maxValue = max(valuea, valueb, valuec)
    if (maxValue == valuea):
        return a
    elif maxValue == valueb:
        return b
    else:
        return c

def sol1(array):
    ret = []
    ret = sorted(array)
    for idx in range(1, len(ret), 2):
        swap(ret, idx - 1, idx)
    return ret

def swap(array, a, b):
    tmp = array[a]
    array[a] = array[b]
    array[b] = tmp

def main(argv):
    a = []
    for value in argv[1].split(','):
        a.append(int(value))
    print(sol1(a))
    print(sol2(a))

if __name__ == "__main__":
    main(sys.argv)
