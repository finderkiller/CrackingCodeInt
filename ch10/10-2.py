#! /usr/bin/python3
import sys

def sol(array):
    ret = []
    hashmap = {}
    for string in array:
        key = ''.join(sorted(string))
        if key in hashmap:
            hashmap[key].append(string)
        else:
            hashmap[key] = [string]

    for key in hashmap:
        ret.extend(hashmap[key])

    return ret

def main(argv):
    a = []
    for value in argv[1].split(','):
        a.append(value)
    print(sol(a))

if __name__ == "__main__":
    main(sys.argv)
