#! /usr/bin/env python2
import sys

#1.6 String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
#or example, the string aabcccccaaa would become a2b1c5a3.
#If the "compressed" string would not become smaller than the original string, your method should return
#the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def sol_basic(test):
    if not test:
        return 0
    count = 0
    result = ""
    for idx in range(len(test)):
        count += 1
        if idx == len(test)-1 or test[idx] != test[idx+1]:
            result += test[idx] + str(count)
            count = 0
    return result if len(result) < test else test
        

    

def main(argv):
    print sol_basic(str(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
