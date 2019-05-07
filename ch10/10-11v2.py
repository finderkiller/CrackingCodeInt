#! /usr/bin/python3
import sys

def sol2(input):
    for idx in range(1, len(input), 2):
        maxidx = FindMaxIdx(input, idx-1, idx, idx+1)
        if (idx != maxidx):
            swap(input, idx, maxidx)
    return input

def FindMaxIdx(array, left, mid, right):
    leftValue = array[left] if 0 <= left < len(array) - 1 else -sys.maxint-1
    midValue = array[mid] if 0 <= mid <= len(array) - 1 else -sys.maxint-1
    rightValue = array[right] if 0 <= right <= len(array) - 1 else -sys.maxint-1

    maxValue = max(leftValue, midValue, rightValue)

    if maxValue == leftValue:
        return left
    elif maxValue == midValue:
        return mid
    else:
        return right


def sol1(input):
    sorted_array = sorted(input)
    for idx in range(1, len(sorted_array), 2):
        swap(sorted_array, idx-1, idx)
    return sorted_array

def swap(sorted_array, a, b):
    tmp = sorted_array[a]
    sorted_array[a] = sorted_array[b]
    sorted_array[b] = tmp


def main(argv):
    input = []
    for data in argv[1].split(','):
        input.append(data)
    print(sol1(input))
    print(sol2(input))

if __name__ == "__main__":
    main(sys.argv)
