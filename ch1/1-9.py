#! /usr/bin/python3
import sys

#1.9 String Rotation: Assume you have a method isSubst ring which checks if one word is a substring
#of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one

def sol_concate(str_a, str_rotated):
    if (len(str_a) != len(str_rotated) or len(str_a) == 0):
        return False

    str_rotated = str_rotated + str_rotated
    return (str_a in str_rotated)

def main(argv):
    print (sol_concate(str(argv[1]), str(argv[2])))

if __name__ == "__main__":
    main(sys.argv)
