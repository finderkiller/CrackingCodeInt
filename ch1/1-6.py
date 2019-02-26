#! /usr/bin/env python2
import sys

#1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
#or example, the string aabcccccaaa would become a2b1c5a3.
#If the "compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def sol_basic(test):
    if len(test) == 0:
        return ""
    output = ""

    count = 0
    for idx, cur in enumerate(test):
        count += 1
        if idx + 1 >= len(test) or test[idx + 1] != cur:
            output += cur + str(count)      #this is not efficient, using stringBuilder in Java can reduce the time complexity
            count = 0
    if (len(output) > len(test)):
        return test
    else:
        return output

def main(argv):
    print sol_basic(str(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
