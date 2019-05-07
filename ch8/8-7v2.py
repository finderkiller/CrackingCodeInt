#! /usr/local/bin/python3
import sys

def sol3(string):
    results = []
    sol3_helper("", string, results)
    return results
    
def sol3_helper(prefix, reminder, results):
    if len(reminder)== 0:
        results.append(prefix)
        return
    for idx in range(len(reminder)):
        before = reminder[:idx]
        after = reminder[idx+1:]
        cur = reminder[idx]
        sol3_helper(prefix + cur, before+after, results)


def sol2(string):
    if (len(string) == 0):
        return [""]
    permutations = []
    for idx in range(len(string)):
        before = string[:idx]
        after = string[idx+1:]
        subpermutations = sol2(before + after)
        for subpermutation in subpermutations:
            permutations.append(string[idx] + subpermutation)
    return permutations

def sol1(string):
    if (len(string) == 0):
        return [""]
    permutations = []
    remainders = sol1(string[1:])
    cur = string[0]
    for remainder in remainders:
        permutations.extend(insertChar(cur, remainder))

    return permutations

def insertChar(char, remainder):
    permutations = []
    for idx in range(0, len(remainder)+1, 1):
        permutations.append(remainder[:idx] + char + remainder[idx:])
    return permutations

def main(argv):
    print(sol1(argv[1]))
    print(sol2(argv[1]))
    print(sol3(argv[1]))

if __name__ == "__main__":
    main(sys.argv)