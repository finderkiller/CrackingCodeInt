#! /usr/bin/python3
import sys

def search(array, start, end, x):
    if start >end:
        return -1
    mid = start + (end-start)//2
    left = right = mid
    while True:
        if left < start or right > end:
            return -1
        if array[left] != "":
            mid = left
            break
        if array[right] != "":
            mid = right
            break
        left -=1
        right +=1
    if array[mid] == x:
        return mid
    elif array[mid] > x:
        return search(array, start, mid-1, x)
    else:
        return search(array, mid+1, end, x)


def searchmain(array, x):
    if not array:
        return -1
    if not x:
        return -1
    return search(array, 0, len(array)-1, x)

def main(argv):
    a= []
    for string in argv[1].split(','):
        a.append(string)
    print(a)
    index = searchmain(a, argv[2])
    print(index)

if __name__ == "__main__":
    main(sys.argv)
