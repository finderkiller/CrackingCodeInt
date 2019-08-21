#! /usr/local/bin/python3
from basic_tree_node import *
import sys

def allSequence(node):
    if (node == None):
        return [[]]
    result = []
    leftseq = allSequence(node.left)
    rightseq = allSequence(node.right)
    for left in leftseq:
        for right in rightseq:
            tmp = []
            collect = []
            weavedList(left, right, collect, tmp)
            for seq in tmp:
                seq.insert(0, node.value)
                result.append(seq)
    return result

#weaved is difficult, need to review
def weavedList(left, right, collect, result):
    if not left:
        result.append(collect+right)
        return
    if not right:
        result.append(collect+left)
        return
    collect.append(left[0])
    weavedList(left[1:], right, collect, result)
    collect.pop()

    collect.append(right[0])
    weavedList(left, right[1:], collect, result)
    collect.pop()

def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(argv[idx])
        node = build_tree_node(input)

    node.print_data()
    node.print_by_level()
    output = allSequence(node)
    for value in output:
        print (value)
if __name__ == "__main__":
    main(sys.argv)
