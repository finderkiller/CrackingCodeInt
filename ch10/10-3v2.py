#! /usr/bin/python3
import sys

def search(input, left, right, value):
    if (right < left):
        return -1
    mid = (left+right)//2
    if (input[mid] == value):
        return mid
    if (input[left] < input[mid]):
        if input[left] <= value and input[mid] > value:
            return search(input, left, mid-1, value)
        else:
            return search(input, mid+1, right, value)
    elif (input[left] > input[mid]):
        if (input[mid] < value and input[right] >= value):
            return search(input, mid+1, right, value)
        else:
            return search(input, left, mid-1, value)
    elif input[left] == input[mid]:
        if input[mid] != input[right]:                  #input[mid] without rotate
            return search(input, mid+1, right, value)
        else:
            ret = search(input, mid+1, right, value)
            if ret == -1:
                ret = search(input, left, mid-1, value)
            return ret
    return -1


def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(value)
    search(input, 0, len(input-1), int(argv[2]))

if __name__ == "__main__":
    main(sys.argv)
