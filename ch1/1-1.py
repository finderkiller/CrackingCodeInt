#! /usr/bin/env python2
import sys

#1.1 Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

#sol1: using int as a bit vector, set bit when it encounter char: 1<<int(char)-int(a)

#sol2: time:O(n), space:O(1) spacefor ASCII, if unicode, need more space
def sol_boolean_vector(test):
    char_checker = [False] * 128
    for cur in test:
        if char_checker[ord(cur)]:
            print "duplicated is " + cur
            return True
        else:
            char_checker[ord(cur)] = True


#sol3: time:O(n^2), space:O(1)
def sol_ori_structure (test):
    for idx in range(len(test)):
        for check_idx in range(idx + 1, len(test)):
            if test[idx] == test[check_idx]:
                print "duplicated is " + test[idx]
                return True

#sol4: time:O(nlogn), space:O(1)sort and compare with next char

def main(argv):
#    sol_ori_structure(str(argv[1]))
    sol_boolean_vector(str(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
