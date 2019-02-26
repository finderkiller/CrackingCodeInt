#! /usr/bin/env python2
import sys

#1.5 One Away: There are three types of edits that can be performed on strings: insert a character,
#remove a character, or replace a character. Given two strings, write a function to check if they are
#one edit (or zero edits) away.
#EXAMPLE
#pale, ple -> true
#pales. pale -> true
#pale. bale -> true
#pale. bake -> false

#sol1: one by one check, time:O(n^2), space:O(1)
#sol2: seperate replece and insert|| remove condition, time:O(n)
def check_insert(str_a, str_b):
    idx_a = 0
    idx_b = 0
    haveFoundDiff = False
    while(idx_a < len(str_a) and idx_b < len(str_b)):
        if str_a[idx_a] == str_b[idx_b]:
            idx_a += 1
            idx_b += 1
            continue
        else:
            if haveFoundDiff:
                return False
            idx_b += 1
            haveFoundDiff = True
    return True

def check_replacement(str_a, str_b):
    haveFoundDiff = False
    for idx in range(len(str_a)):
        if str_a[idx] != str_b[idx]:
            if haveFoundDiff:
                return False
            haveFoundDiff = True
    return True

def sol_traverse(first, second):
    if len(first) == len(second):
        return check_replacement(first, second)
    elif len(first) == len(second) + 1:
        return check_insert(second, first)
    elif len(first) == len(second) - 1:
        return check_insert(first, second)
    else:
        return False

def main(argv):
    if sol_traverse(str(argv[1]), str(argv[2])):
        print "True"
    else:
        print "False"

if __name__ == "__main__":
    main(sys.argv)
