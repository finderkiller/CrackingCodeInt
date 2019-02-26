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
    if (maze == None or len(maze) == 0):
        return None
    path = []
    if (sol_brute_force(maze, len(maze) - 1, len(maze[0]) - 1, path)):
        return path
    return None

def sol_brute_force(maze, r, c, path):
    if (r < 0 or c < 0 or not maze[r][c]):
        return False

    if (r == 0 and c == 0):
        path.append((0, 0))
        return True

    if (sol_brute_force(maze, r - 1, c, path) or sol_brute_force(maze, r, c - 1, path)):
        path.append((r, c))
        return True

    return False

def sol2(maze):
    if (maze == None or len(maze) == 0):
        return None
    path = []
    failedPoints = set()

    if (getPath(maze, len(maze) - 1, len(maze[0]) - 1, path, failedPoints)):
        return path
    return None

def getPath(maze, r, c, path, failedPoints):
    if (r < 0 or c < 0 or not maze[r][c]):
        return False

    if ((r, c) in failedPoints):
        return False

    if (r == 0 and c == 0):
        path.append((r, c))
        return True

    if (getPath(maze, r - 1, c , path, failedPoints) or getPath(maze, r, c - 1, path, failedPoints)):
        path.append((r, c))
        return True

    failedPoints.add((r, c))
    return False


if __name__ == "__main__":
    main(maze)
