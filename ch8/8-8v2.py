#! /usr/local/bin/python3
import sys

def getFreq(string):
    map = {}
    for value in string:
        if value not in map:
            map[value] = 1
        else:
            map[value] += 1
    return map

def getPermutation(charMap, prefix, remaining, results):
    if remaining == 0:
        results.append(prefix)
    for key in charMap.keys():
        count = charMap[key]
        if count > 0:
            charMap[key] -= 1
            getPermutation(charMap, prefix+key, remaining-1, results)
            charMap[key] += 1

def main(argv):
    charMap = getFreq(argv[1])
    results = []
    getPermutation(charMap, "", len(argv[1]), results)
    print(results)


if __name__ == "__main__":
    main(sys.argv)