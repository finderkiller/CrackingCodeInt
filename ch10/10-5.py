#! /usr/bin/python3
import sys

def search(array, low, high, x):
    if (low > high):
        return -1
    mid = (low + high)//2
    if (array[mid] == ""):
        left = mid - 1
        right = mid + 1
        while(True):
            if (left < low and right > high):
                return -1
            elif left >= low and array[left] != "":
                mid = left
                break
            elif right <= high and array[right] != "":
                mid = right
                break
            left -= 1
            right += 1

    if (array[mid] == x):
        return mid
    elif (array[mid] > x):
        return search(array, low, mid - 1, x)
    else:
        return search(array, mid + 1, high, x)

def searchmain(array, x):
    if (array == None or x == None or x == ""):
        return -1
    return search(array, 0, len(array), x)

def main(argv):
    a= []
    for string in argv[1].split(','):
        a.append(string)
    print(a)
    index = searchmain(a, argv[2])
    print(index)

if __name__ == "__main__":
    main(sys.argv)
