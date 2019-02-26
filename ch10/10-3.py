#! /usr/bin/python3
import sys

def search(array, left, right, x):
    if (left > right):
        return -1
    mid = (left + right)//2
    if array[mid] == x:
        return mid
    if (array[left] < array[mid]): #left is ordered
        if (x>=array[left] and x <array[mid]):     #x in left
            return search(array, left, mid - 1, x)
        else:
            return search(array, mid + 1, right, x)
    elif (array[left] > array[mid]): # right is ordered
        if (x>array[mid] and x <= array[right]): #x in right
            return search(array, mid + 1, right, x)
        else:
            return search(array, left, mid - 1, x)
    elif (array[left] == array[mid]):
        if (array[mid] != array[right]):
            return search(array, mid + 1, right, x)
        else:
            result = search(array, mid + 1, right, x)
            if (result == -1):
                result = search(array, left, mid - 1, x)
            return result
    return -1

def main(argv):
    a = []
    for value in argv[1].split(','):
        a.append(int(value))

    index = search(a, 0, len(a) - 1, int(argv[2]))
    print(index)

if __name__ == "__main__":
    main(sys.argv)
