#! /usr/local/bin/python3
import sys
from basic_tree_node import *

def allSequence(node):
    results = []
    if (node == None):
        results.append([])
        return results
    
    prefix = []
    prefix.append(node.value)

    leftseq = allSequence(node.left)
    rightseq = allSequence(node.right)
    for left in leftseq:
        for right in rightseq:
            weaved = []
            weavedList(left, right, weaved, prefix)
            results += weaved
    return results

def weavedList(left, right, results, prefix):
    if (len(right) == 0 or len(left) == 0):
        result = prefix.copy()
        result += left
        result += right
        results.append(result)
        return

    lefthead = left.pop(0)
    prefix.append(lefthead)
    weavedList(left, right, results, prefix)
    prefix.pop()
    left.insert(0, lefthead)


    righthead = right.pop(0)
    prefix.append(righthead)
    weavedList(left, right, results, prefix)
    prefix.pop()
    right.insert(0, righthead)

    return 


def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))
    root = build_tree_node(input)
    root.print_by_level()
    root.print_data()

    output = allSequence(root)
    for value in output:
        print(value)

if __name__ == "__main__":
    main(sys.argv)