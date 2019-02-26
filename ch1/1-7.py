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
