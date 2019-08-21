#! /usr/local/bin/python3
import sys

def getways(row, gridsize, collect, result):
    if row == gridsize:
        result.append(list(collect))
        return
    for col in range(gridsize):
        if (CheckValidColumn(row, col, collect)):
            collect.append(col)
            getways(row+1, gridsize, collect, result)
            collect.pop()

def CheckValidColumn(row, col, collect):
    for row_index in range(len(collect)):
        if collect[row_index] == col:
            return False
        col_diff = abs(collect[row_index] - col)
        row_diff = abs(row_index - row)

        if col_diff == row_diff:
            return False
    return True
    

def main():
    result = []
    collect = []
    getways(0, 8, collect, result)
    print(result)

if __name__ == "__main__":
    main()
