#! /usr/bin/env python2
import sys

# sol1, sol2: time:O(n), space: O(1), using odd_checker while first iteration, not more second interation
def sol_hash_table(test):
    counter = [0] * 128
    odd_checker = 0
    for char in test:
        counter[ord(char)] += 1
        if counter[ord(char)] % 2 == 0:
            odd_checker -= 1
        elif counter[ord(char)] % 2 == 1:
            odd_checker += 1
    return odd_checker <= 1

#sol3: time:O(n), space: O(1), it doesn't need to consider the size of "checker" since python would handle the large int
def sol_bit_vector(test):
    checker = 0
    for char in test:
        idx = ord(char)
        print idx
        if idx < 0:
            return False
        checker ^= (1<<idx)
        #if checker & (1 << idx) == 0:
            #checker |= (1<<idx)
        #else:
            #checker &= ~(1<<idx)
        print bin(checker)

    return checker == 0 or (checker & (checker - 1)) == 0


def main(argv):
#    if sol_hash_table(str(argv[1])):
    if sol_bit_vector(str(argv[1])):
        print "True"
    else:
        print "False"

if __name__ == "__main__":
    main(sys.argv)
