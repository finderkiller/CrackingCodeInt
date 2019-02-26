#! /usr/bin/python2

#1.8 Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0,
#its entire row and column are set to 0.

MATRIX = [[0, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 0]]
#sol1: time:O(n^2), space:O(1), using first col and first row for recording
def sol_using_existing_space(matrix):
    h = len(matrix)
    if h == 0:
        return False
    w = len(matrix[0])
    firstRowHasZero = False
    firstColHasZero = False

    for value in matrix[0]:
        if value == 0:
            firstRowHasZero = True
            break
    for row in range(h):
        if matrix[row][0] == 0:
            firstColHasZero = True
            break

    for row in range(1, h, 1):
        for col in range(1, w, 1):
            if (matrix[row][col] == 0):
                matrix[0][col] = 0
                matrix[row][0] = 0

#nullify column
    for idx in range(1, w, 1):
        if (matrix[0][idx] == 0):
            for row in range(1, h, 1):
                matrix[row][idx] = 0
#nullify row
    for idx in range(1, h, 1):
        if (matrix[idx][0] == 0):
            matrix[idx] = [0] * w

    if firstRowHasZero:
        matrix[0] = [0] * w
    if firstColHasZero:
        for row in range(h):
            matrix[row][0] = 0
    print matrix

#sol2: time:O(n^2), space:O(n), recording the location of zero value in extra list
def sol_using_extra_space(matrix):
    h = len(matrix)
    if h == 0:
        return False
    w = len(matrix[0])
    row_zero_record = []
    col_zero_record = []

    for row in range(h):
        for col in range(w):
            if (matrix[row][col] == 0):
                row_zero_record.append(row)
                col_zero_record.append(col)
    for value in row_zero_record:
        matrix[value] = [0] * w
    for value in col_zero_record:
        for row in range(h):
            matrix[row][value] = 0

    print matrix

def main():
#    sol_using_extra_space(MATRIX)
    sol_using_existing_space(MATRIX)

if __name__ == "__main__":
    main()
