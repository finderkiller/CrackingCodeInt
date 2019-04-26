#! /usr/bin/python3
import sys

class Tower:
    def __init__(self, index):
        self.index = index
        self.disks = []
    def add(self, value):
        self.disks.append(value)
    def pop(self):
        return self.disks.pop()

def moveDisks(n, ori, dest, buf):
    if (n == 0):
        return
    moveDisks(n-1, ori, buf, dest)
    dest.add(ori.pop())
    moveDisks(n-1, buff, dest, ori)

def main(argv):
    tower1 = Tower(1)
    tower2 = Tower(2)
    tower3 = Tower(3)

    for value in range(int(argv[1]), 0, -1)
        tower1.add(value)
    print(tower1.disks)
    moveDisks(int(argv[1]), tower1, tower2, tower3)
    print(tower3.disks)


if __name__ == "__main__":
    main(sys.argv)
