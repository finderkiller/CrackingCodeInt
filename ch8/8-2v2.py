#! /usr/local/bin/python3
import sys

def sol2(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    failedPoints = set()
    if sol_DP(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
        return path
    return None

def sol_DP(maze, r, c, path, failedPoints):
    if r < 0 or c < 0 or not maze[r][c]:
        return False

    if (r, c) in failedPoints:
        return False
    isOrigin = r==0 and c==0
    if isOrigin or sol_DP(maze, r-1, c, path, failedPoints) or sol_DP(maze, r, c-1, path, failedPoints):
        path.append((r, c))
        return True

    failedPoints.add((r,c))
    return False

def sol1(maze):
    if maze == None or len(maze) == 0:
        return None
    path = []
    if sol_brute_force(maze, len(maze)-1, len(maze[0])-1, path):
        return path
    return None

def sol_brute_force(maze, r, c, path):
    if r < 0 or c < 0 or not maze[r][c]:
        return False

    isOrigin = r==0 and c == 0
    if (isOrigin or sol_brute_force(maze, r-1, c, path) or sol_brute_force(maze, r, c-1, path)):
        path.append((r, c))
        return True

    return False


def main(argv):
    a = [[None]*3] * 2
    print(a)
    w = 8
    h = 3
    maze = [True] * w
    maze = [maze] * h
    print(maze)
    print(sol1(maze))
    print(sol2(maze))

if __name__ == "__main__":
    main(sys.argv)
