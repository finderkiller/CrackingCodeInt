#! /usr/bin/python3
import sys

#sol1 sort and compare,
#sol2 table

def getFreqency(string):
    table = {}
    for char in string:
        if char in table:
            table[char] += 1
        else:
            table[char] = 1
    return table

def sol2(str1, str2):
    tab1e1 = getFreqency(str1)
    table2 = getFreqency(str2)
    for key, value in tab1e1.items():
        if (key in table2) and value == table2[key]:
            continue
        else:
            return False
    return True


def main(argv):
    if len(argv[1]) != len(argv[2]):
        print("error")
        return
    if not sol2(argv[1], argv[2]):
        print("error")
    else:
        print("same")

if __name__ == "__main__":
    main(sys.argv)
