#! /usr/bin/python3
import sys


def getSubsetsUsingBits(input):
    max_size = 1 << len(input)

    allsubsets = []
    for value in range(max_size):
        subset = converToSubset(value, input)
        allsubsets.append(subset)
    return allsubsets

def converToSubset(value, input):
    subset = []
    idx = 0
    while(value > 0):
        if value & 1 == 1:
            subset.append(input[idx])
        value >>= 1
        idx += 1
    return subset

def getSubsets(input, index):
    if index == -1:
        allsubsets = []
        allsubsets.append([])
        return allsubsets

    allsubsets = getSubsets(input, index - 1)
    cur_item = input[index]
    moresubsets = []
    for subsets in allsubsets:
        newsubsets = list(subsets)
        newsubsets.append(cur_item)
        moresubsets.append(newsubsets)
    allsubsets.extend(moresubsets)
    return allsubsets

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))
    print(getSubsets(input, len(input)-1))
    print(getSubsetsUsingBits(input))

if __name__ == "__main__":
    main(sys.argv)
