#! /usr/bin/python3
import sys

def merge(a, b, counta, countb):
    indexa = counta - 1
    indexb = countb - 1
    indexMerge = counta + countb - 1

    while(indexb >= 0):
        if indexa >=0 and a[indexa] >= b[indexb]:
            a[indexMerge] = a[indexa]
            indexa -= 1
        else:
            a[indexMerge] = b[indexb]
            indexb -= 1
        indexMerge -= 1
    return


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
        a[idx] = value
    for idx, value in enumerate(argv[2].split(',')):
        b[idx] = value

    merge(a, b, counta, countb)
    print(a)



if __name__ == "__main__":
    main(sys.argv)
