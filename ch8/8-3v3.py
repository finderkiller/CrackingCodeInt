#! /usr/bin/python3
import sys

#if it is not distincted element array
def magicFast(array, start, end):
    if start > end:
        return -1
    mid = start + (end-start)//2

    value = array[mid]
    if  value == mid:
        return mid
    left = magicFast(array, start, min(mid-1, value))
    if left >=0:
        return left
    return magicFast(array, max(mid+1, value), end)

#if it is distincted element array
def magicFast0(array, start, end):
    if start > end:
        return -1
    mid = start + (end-start)//2

    if array[mid] == mid:
        return mid
    elif  array[mid] > mid:
        return magicFast0(start, mid-1)
    else:
        return magicFast0(mid+1, end)


def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(int(argv[idx]))
    print(magicFast(input, 0, len(input) - 1))

if __name__ == "__main__":
    main(sys.argv)
