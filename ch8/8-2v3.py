#! /usr/bin/python3
import sys

w, h = 8, 5;
maze = [[True for x in range(w)] for y in range(h)]
class Point:
    def __init__(self, r, c):
        self.r = r
        self.c = c

def main(maze):
    point1 = Point(2, 3)
    point2 = point1
    print(hash(point1))
    print(hash(point2))
    test = set()
    test.add(point1)
    print(point2 in test)
#     print((2, 3) in test)
    print(sol1(maze))
    print(sol2(maze))

def sol1(maze):
    if not maze:
        return
    result = []
    if not helper(maze, len(maze)-1, len(maze[0]-1, result):
        return
    return result

def helper(maze, r, c, result):
    if r < 0 or c <0 or not maze[r][c]:
        return False
    if r==0 and c==0:
        result.append((r, c))
        return True
    if self.helper(maze, r-1, c, result) or self.helper(maze, r, c-1, result):
        result.append(r,c)
        return True
    return False
   
def sol2(maze):
    if not maze:
        return
    failedpoints = set()
    result = []
    if helper(maze, len(maze)-1, len(maze[0])-1, result, failedpoints):
        return result
    return

def helper(maze, r, c, result, failedPoints):
    if r < 0 or c < 0 or not maze[r][c]:
        return False
    if r == 0 and c == 0:
        result.append((r, c))
        return True
    if (r, c) in failedPoints:
        return False
    
    if helper(maze, r-1, c, result, failedPoints) or helper(maze, r, c-1, result, failedPoints):
        result.append((r, c))
        return True
    failedPoints.add((r, c))
    return False
    


if __name__ == "__main__":
    main(maze)
