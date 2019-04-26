#! /usr/bin/python3
import sys

def sol1_iteration(input):
    for idx, value in enumerate(input):
        if (idx == value):
            return idx
    return -1

def sol2_recursive(input, start, end):
    if (end < start):
        return -1
    mid = (start + end)//2
    if (mid == input[mid]):
        return mid
    elif mid < input[mid]:
        return sol2_recursive(input, start, mid - 1)
    else:
        return sol2_recursive(input, mid+1, end)

def sol3_recursive_duplicated(input, start, end):
    if (end < start):
        return -1
    mid = (start + end)//2
    if (mid == input[mid]):
        return mid

    leftmost = min(mid-1, input[mid])
    left = sol3_recursive_duplicated(input, start, leftmost)
    if left >=0:
        return left

    rightmost = max(mid+1, input[mid])
    right = sol3_recursive_duplicated(input, rightmost, end)
    return right

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))

    print(sol1_iteration(input))
    print(sol2_recursive(input, 0, len(input)-1))           #for distincted value
    print(sol3_recursive_duplicated(input, 0, len(input)-1))           #for non-distincted value

if __name__ == "__main__":
    main(sys.argv)
