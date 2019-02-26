#! /usr/bin/python3
import sys

def elementAt(array, index):
    if index >= len(array):
        return -1
    return array[index]

def search_wo_size(array, x):
    index = 1
    while(elementAt(array, index) != -1 and array[index] < x):
        index *= 2
    return binary_search(array, index//2, index, x)

def binary_search(array, low, high, x):
    while (low <= high):
        mid = (low + high)//2
        if (elementAt(array, mid) == -1 or elementAt(array, mid) > x):
            high = mid - 1
        elif (elementAt(array, mid) < x):
            low = mid + 1
        else:
            return mid
    return -1

def main(argv):
    a = []
    for value in argv[1].split(','):
        a.append(int(value))
    index = search_wo_size(a, int(argv[2]))
    print(index)

if __name__ == "__main__":
    main(sys.argv)
