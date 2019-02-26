#! /usr/bin/python3
import sys

#if it is not distincted element array
def magicFast(array, start, end):
    if (start > end):
        return -1
    mid = (end + start) // 2
    mid_value = array[mid]
    if (mid_value == mid):
        return mid

    # search left
    left = magicFast(array, start, min(mid_value, mid - 1))
    if (left >= 0):
        return left

    #search right
    right = magicFast(array, max(mid_value, mid + 1), end)
    return right

#if it is distincted element array
def magicFast0(array, start, end):
    if (start > end):
        return -1
    mid = (end + start)//2
    if (array[mid] < mid):
        return magicFast0(array, mid + 1, end)
    elif (array[mid] > mid):
        return magicFast0(array, start, mid - 1)
    else:
        return mid


def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(int(argv[idx]))
    print(magicFast(input, 0, len(input) - 1))

if __name__ == "__main__":
    main(sys.argv)
