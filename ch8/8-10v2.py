#! /usr/bin/python3
import sys

def paintFillHelper(screen, row, col, ocolor, ncolor):
    if (row < 0 or row >= len(screen) or col < 0 or col >= len(screen[0])):
        return False
    if (screen[row][col] == ocolor):
        screen[row][col] = ncolor
        paintFillHelper(screen, row-1, col, ocolor, ncolor)
        paintFillHelper(screen, row+1, col, ocolor, ncolor)
        paintFillHelper(screen, row, col-1, ocolor, ncolor)
        paintFillHelper(screen, row, col+1, ocolor, ncolor)
    return True

def paintFill(screen, row, col, ncolor):
    if screen[row][col] == ncolor:
        return False
    return paintFillHelper(screen, row, col, screen[row][col], ncolor)


def main(argv):
    screen = []
    paintFill(screen, r, c ncolor)

if __name__ == "__main__":
    main(sys.argv)
