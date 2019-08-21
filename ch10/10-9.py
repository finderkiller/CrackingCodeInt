#! /usr/bin/python3
import sys
import math

M = [[],[]]

class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col
    def inbound(self, matrix):
        if (matrix == None):
            return False
        if (matrix[0] == None):
            return False
        if (0 <= self.row and self.row < len(matrix)) and (0 <= self.col and self.col < len(matrix[0])):
            return True
        return False
    def isbefore(self, coordinate):
        return self.row <= coordinate.row and self.col <= coordinate.col
    def setAverage(self, a, b):
        self.row = (a.row + b.row)//2
        self.col = (a.col + b.col)//2

def bsearch(matrix, origin, dest, x):
    if (not origin.inbound(matrix) or not dest.inbound(matrix)):
        return None
    if (not origin.isbefore(dest)):
        return None

    start = Coordinate(origin.row, origin.col)
    dist = math.min(dest.row - origin.row, dest.col - origin.col)
    end = Coordinate(origin.row + dist, origin.col + dist)
    p = Coordinate(0, 0)
    while (start.isbefore(end)):
        p.setAverage(start, end)
        if (matrix[p.row][p.col] == x):
            return p
        elif(matrix[p.row][p.col] < x):
            start.row = p.row + 1
            start.col = p.col + 1
        else:
            end.row = p.row - 1
            end.row = p.row - 1
    return partition(matrix, origin, dest, start, x)

def partition(matrix, origin, dest, start, x):
    lowerleftorigin = Coordinate(start.row, origin.col)
    lowerleftdest = Coordinate(dest.row, start.col - 1)
    upperrightorigin = Coordinate(origin.row, start.col)
    upperrightdest = Coordinate(start.row - 1, dest.col)

    p = bsearch(matrix, lowerleftorigin, lowerleftdest, x)
    if p == None:
        p = bsearch(matrix, upperrightorigin, upperrightdest, x)
    return p

def search(M, x):
    row = 0
    col = len(M[0]) - 1
    while(row < len(M) and col >= 0):
        if M[row][col] == x:
            return True
        elif M[row][col] > x:
            col -= 1
        else:
            row += 1
    return False

def main(argv):
    x = int(argv[1])
    print(search(M, x))
    print(bsearch(M, Coordinate(0, 0), Coordinate(len(M)-1, len(M[0])-1), x))

if __name__ == "__main__":
    main(sys.argv)
