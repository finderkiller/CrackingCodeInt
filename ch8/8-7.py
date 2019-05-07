#! /usr/local/bin/python3
import sys

def sol3(string):
    result = []
    sol3_helper("", string, result)
    return result

def sol3_helper(prefix, remainder, result):
    if (len(remainder) == 0):
        result.append(prefix)
        return
    for idx in range(len(remainder)):
        start = remainder[:idx]
        end = remainder[idx + 1:]
        sol3_helper(prefix + remainder[idx], str(start) + str(end), result)

def sol2(remainder):
    permutations = []
    if (len(remainder) == 0):
        permutations.append("")
        return permutations

    for idx in range(len(remainder)):
        start = remainder[:idx]
        end = remainder[idx + 1:]
        partial = sol2(str(start) + str(end))

        for s in partial:
            permutations.append(remainder[idx] + s);

    return permutations

def sol1(string):
    permutations = []
    if (string == None):
        return permutations
    if (len(string) == 0):
        permutations.append("")
        return permutations
    first = string[0]
    remainder = sol1(string[1:])
    for per in remainder:
        permutations.extend(insertchar(per, first))

    return permutations


def insertchar(string, char):
    ret = []
    for idx in range(len(string) + 1):
        ret.append(str(string[:idx]) + char + str(string[idx:]))
    return ret

def main(argv):
    print(sol1(argv[1]))
    print(sol2(argv[1]))
    print(sol3(argv[1]))

if __name__ == "__main__":
    main(sys.argv)
