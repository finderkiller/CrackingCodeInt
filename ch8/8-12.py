#! /usr/bin/python3
import sys

GridSize = 8
def getways(row, cols, results):
    if (row == GridSize):
        results.append(list(cols))
        return
    for col in range(GridSize):
        if (CheckValidColumn(row, col, cols)):
            cols[row] = col
            getways(row+1, cols, results)
    return

def CheckValidColumn(row, col, cols):
    for row_index in range(row):
        if (cols[row_index] == col):
            return False
        column_diff = abs(cols[row_index] - col)
        row_diff = abs(row_index - row)

        if (row_diff == column_diff):
            return False
    return True

def main():
    results = []
    cols = [None] * GridSize
    getways(0, cols, results)
    print(results)

if __name__ == "__main__":
    main()
