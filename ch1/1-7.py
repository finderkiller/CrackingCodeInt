#! /usr/bin/python3

#1-7: matrix rotate, hint: layer by layer
MATRIX = [[1,2,3], [4,5,6], [7,8,9]]

def rotate(matrix):
    if (len(matrix) == 0 or len(matrix[1]) != len(matrix)):
        return False
    for layer in range(len(matrix)//2):     #// is the same as / in c language
        first = layer
        last = len(matrix) - 1 - layer
        for idx in range(first, last, 1):   #last doesn't need to traverse since last one is the first one of anthor array
            offset = idx - first
            top = matrix[first][idx]
            matrix[first][idx] = matrix[last-offset][first]
            matrix[last-offset][first] = matrix[last][last-offset]
            matrix[last][last-offset] = matrix[idx][last]
            matrix[idx][last] = top
    print (matrix)
    return True
def main():
    rotate(MATRIX)

if __name__ == "__main__":
    main()


#!偏向這個寫法，比較直觀，設好每一次的上下左右
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []
        rowup = 0
        rowdown = len(matrix)-1
        colleft = 0
        colright = len(matrix[0])-1
        
        while rowup < rowdown:
            for col in range(colleft, colright):
                offset = col - colleft
                tmp = matrix[rowup][col]
                matrix[rowup][col] = matrix[rowdown-offset][colleft]
                matrix[rowdown-offset][colleft] = matrix[rowdown][colright-offset]
                matrix[rowdown][colright-offset] = matrix[rowup+offset][colright]
                matrix[col][colright] = tmp
            rowup +=1
            rowdown -=1
            colright -=1
            colleft +=1
        