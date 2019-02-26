#! /usr/bin/env python2
import sys

#1.2 Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.

#sol1: two string sort and compare, time:O(nlogn), space:O(1)

#sol2: hash table, time:O(n), space:O(1)~=128 char_a
#it should not using str_b_counter, just decrease the element of str_a_counter when traverse str_b
def sol_boolean_vector(str_a, str_b):
    str_a_counter = [0] * 128
    str_b_counter = [0] * 128
    for char_a in str_a:
        str_a_counter[ord(char_a)] += 1

    for char_b in str_b:
        str_b_counter[ord(char_b)] += 1

    for idx in range(len(str_a_counter)):
        if str_a_counter[idx] != str_b_counter[idx]:
            return False
    return True

def main(argv):
    str_a = str(argv[1])
    str_b = str(argv[2])
    if len(str_a) != len(str_b):
        return -1

    if sol_boolean_vector(str_a, str_b):
        print "is permutation"

if __name__ == "__main__":
    main(sys.argv)
