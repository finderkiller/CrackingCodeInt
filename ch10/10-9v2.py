#! /usr/bin/python3
import sys

M = []

class Coordinate:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def IsInbound(self, matrix):
        if matrix == None:
            return False
        if matrix[0] == None:
            return False
        if self.row < 0 or self.col < 0:
            return False
        if self.row > len(matrix)-1 or self.col > len(matrix[0])-1:
            return False
        return True

    def IsBefore(self, coordinate):
        return self.row <= coordinate.row and sel.col <= coordinate.col
    def SetAverage(self, first, end):
        self.row = (first.row + end.row)//2
        self.col = (first.col + end.col)//2

def search(matrix, value):
    row = 0
    col = len(matrix[0]) - 1
    while (row < len(matrix) and col >= 0):
        if matrix[row][col] == value:
            return True
        elif matrix[row][col] > value:
            col -= 1
        else:
            row += 1
    return False

def bsearch(matrix, value, start, end):
    if not start.IsInbound(matrix) or not end.IsInbound(matrix):
        return None
    if not start.IsBefore(end):
        return None
    if matrix[start.row][start.col] == value:
        return start

    leftup = Coordinate(start.row, start.col)
    dist = min(end.row-start.row, end.col-start.col)
    rightdown = Coordinate(leftup.row+dist, leftup.col+dist)
    mid = Coordinate(0, 0)

    while(leftup.IsBefore(rightdown)):
        mid.setAverage(leftup, rightdown)
        if (matrix[mid.row][mid.col] == value):
            return mid
        elif matrix[mid.row][mid.col] < value:
            leftup.row = mid.row+1
            leftup.col = mid.col+1
        else:
            rightdown.row = mid.row-1
            rightdown.col = mid.col-1
    return partition(matrix, value, start, end, leftup)

def partition(matrix, value, start, end, leftup):
    lowerleftstart = Coordinate(leftup.row, start.col)
    lowerleftend = Coordinate(end.row, leftup.col-1)
    upperrightstart = Coordinate(start.row, leftup.col)
    upperrightend = Coordinate(leftup.row-1, end.col)

    result = bsearch(matrix, value, lowerleftstart, lowerleftend)
    if (result != None):
        return result
    return bsearch(matrix, value, upperrightstart, upperrightend)


def main(sys):
    search(M, value)
    bsearch(M, value, Coordinate(0, 0), Coordinate(len(M)-1, len(M[0])-1))

if __name__ == "__main__":
    main(sys.argv)
