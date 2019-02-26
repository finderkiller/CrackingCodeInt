#! /usr/bin/env python2
import sys

#1.3 URLify: Write a method to replace all spaces in a string with '%20:
#you may assume that the string has sufficient space at the end to hold the additional characters,
#and that you are given the "true" length of the string. (Note: If implementing in Java,
#please use a character array so that you can perform this operation in place.)

#sol1:A simple solution is to create an auxiliary string and copy characters one by one. Whenever a space is encountered, place %20 in place of it.
#     time:O(n), space:O(n)
#sol2: time:O(n), space:O(1)

def sol_in_place(str_a, true_length):
    space_count = 0
    for idx in range(true_length):
        if (str_a[idx] == " "):
            space_count += 1
    idx_final = true_length + space_count*2 - 1

    for idx_a in range(true_length-1, -1, -1):
        if str_a[idx_a] == " ":
            str_a = str_a[:idx_final] + "0" + str_a[idx_final+1:]
            str_a = str_a[:idx_final-1] + "2" + str_a[idx_final:]
            str_a = str_a[:idx_final-2] + "%" + str_a[idx_final-1:]
            idx_final -= 3
        else:
            str_a = str_a[:idx_final] + str_a[idx_a] + str_a[idx_final+1:]
            idx_final -= 1

    print str_a



def main(argv):
    sol_in_place(str(argv[1]), int(argv[2]))

if __name__ == "__main__":
    main(sys.argv)
