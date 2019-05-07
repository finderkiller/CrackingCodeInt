#! /usr/bin/python3
import sys

class Array:
    def __init__(self, size):
        self.array = [-1]*size
        self.curidx = 0
    def push(self, data):
        self.array[self.curidx] = data
        self.curidx += 1
    def get(self, index):
        return self.array[index]

def Search(a, value):
    index = 1
    while(a.get(index) != -1 and a.get(index) < value):
        index *= 2
    return BinearySearch(a, value, index//2, index)

def BinearySearch(a, value, low, high):
    while(low<=high):
        mid = (low + high)//2
        middle = a.get(mid)
        if (middle == -1 or middle > value):
            high = mid - 1
        elif (middle < value):
            low = mid + 1
        else:
            return mid
    return -1

def main(argv):
    a=Array(255)
    for value in argv[1].split(','):
        a.push(int(value))
    print(Search(a, int(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
