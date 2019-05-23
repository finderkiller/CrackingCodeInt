#! /usr/bin/python3
import sys

#bit vector

#sol2
def sol_table(input):
    table = set()
    for char in input:
        if char in table:
            return False
        else:
            table.add(char)
#sol3, w/o data structure, timeO(n^2)
#sol4, sort and compare with next char



def main(argv):
    sol1(argv[1])

if __name__ == "__main__":
    main(sys.argv)
