#! /usr/bin/python3
import sys

def getSubsetsUsingBits(input):
    allsubsets = []
    total = 1 << len(input)
    for value in range(total):
        subset = converToSubset(value, input)
        allsubsets.append(subset)
    return allsubsets

def converToSubset(value, input):
    subset = []
    index = 0
    while(value > 0):
        if (value & 1 == 1):
            subset.append(input[index])
        value >>= 1
        index += 1
    return subset


def getSubsets(input, index):
    allsubsets = []
    if index == -1:
        allsubsets.append([])
        return allsubsets

    allsubsets = getSubsets(input, index - 1)
    item = input[index]
    moresubsets = []
    for subsets in allsubsets:
        newsubsets = list(subsets)  #//copy from subsets
        newsubsets.append(item)
        moresubsets.append(newsubsets)
    allsubsets.extend(moresubsets)

    return allsubsets


def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))
    print(getSubsets(input, len(input) - 1))
    print(getSubsetsUsingBits(input))


if __name__ == "__main__":
    main(sys.argv)
