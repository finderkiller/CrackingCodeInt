#! /usr/bin/python3
import sys

def merge(a, b, indexa, indexb):
    indexmerge = len(a) - 1
    while(indexb >= 0):
        if (indexa >= 0 and a[indexa] > b[indexb]):
            a[indexmerge] = a[indexa]
            indexa -= 1
        else:
            a[indexmerge] = b[indexb]
            indexb -= 1
        indexmerge -= 1


def main(argv):
    counta = 0
    countb = 0
    for value in argv[1].split(','):
        counta += 1
    for value in argv[2].split(','):
        countb += 1
    a = [None] * (counta + countb)
    b = [None] * countb
    for idx, value in enumerate(argv[1].split(',')):
        a[idx] = int(value)
    for idx, value in enumerate(argv[2].split(',')):
        b[idx] = int(value)
    print(a)
    print(b)
    merge(a, b, counta - 1, countb - 1)
    print(a)


if __name__ == "__main__":
    main(sys.argv)
