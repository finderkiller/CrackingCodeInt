#! /usr/bin/python3
import sys

def buildFreqTable(string):
    table = {}
    for value in string:
        if value not in table:
            table[value] = 1
        else:
            table[value] += 1
    return table

def getPer(hashmap, prefix, remainder, result):
    if (remainder == 0):
        result.append(prefix)
        return

    for key in hashmap.keys():
        count = hashmap.get(key)
        if (count > 0):
            hashmap[key] -= 1
            getPer(hashmap, prefix + key, remainder - 1, result)
            hashmap[key] += 1

def main(argv):
    hashmap = buildFreqTable(argv[1])
    result = []
    getPer(hashmap, "", len(argv[1]), result)
    print(result)


if __name__ == "__main__":
    main(sys.argv)
