#! /usr/bin/python3
import sys



#pseudocode
def movedisk(n, origin, buffer, destination):
    if (n <= 0):
        return
    #move n-1 from origin to buffer using destination as a buffer
    movedisk(n - 1, origin, buffer, destination)

    moveTop(origin, destination)

    #move n-1 from buffer to destination, using origin as a buffer
    modedisk(n - 1, buffer, destination, origin)
    return

class Tower:
    def __init__(self, n):
        self.index = n
        self.disks = []
    def add(self, value):
        self.disks.append(value)
    def popTop(self):
        return self.disks.pop()
    def size(self):
        return len(self.disks)


def movedisks(n, origin, destination, buffer):
    if (n <= 0):
        return
    movedisks(n - 1, origin, buffer, destination)
    destination.add(origin.popTop())
    movedisks(n - 1, buffer, destination, origin)

def main(argv):
    tower0 = Tower(0)
    tower1 = Tower(1)
    tower2 = Tower(2)

    for i in range(int(argv[1]), 0, -1):
        tower0.add(i)
    print(tower0.disks)
    movedisks(int(argv[1]), tower0, tower2, tower1)
    print(tower2.disks)



if __name__ == "__main__":
    main(sys.argv)
