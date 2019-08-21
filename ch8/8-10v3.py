#! /usr/bin/python3
import sys
from enum import Enum

class Color(Enum):
    Red = 1
    Black = 2
    White = 3
    Yellow = 4
    Green = 5

screen = []

def paintFillHelper(screen, r, c, ocolor, ncolor):
    if r <0 or c <0:
        return
    if r>=len(screen) or c >= len(screen[0]):
        return
    if screen[r][c] != ocolor:
        return
    screen[r][c] = ncolor
    paintFillHelper(screen, r-1, c, ocolor, ncolor)
    paintFillHelper(screen, r+1, c, ocolor, ncolor)
    paintFillHelper(screen, r, c-1, ocolor, ncolor)
    paintFillHelper(screen, r, c+1, ocolor, ncolor)
    return


def paintFill(screen, r, c, ncolor):
    if not screen:
        return
    if screen[r][c] == ncolor:
        return
    paintFillHelper(screen, r, c, screen[r][c], ncolor)

def main(argv):
    paintFill(screen, int(argv[1]), int(argv[2]), int(argv[3]))

if __name__ == "__main__":
    main(sys.argv)
