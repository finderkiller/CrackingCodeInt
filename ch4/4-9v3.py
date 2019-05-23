#! /usr/bin/python3
import sys

def allSequence(node):
    results = []
    if node == None:
        results.append([])
        return results
    prefix = []
    prefix.append(node.value)
    leftSeq = allSequence(node.left)
    rightSeq = allSequence(node.right)
    for left in leftSeq:
        for right in rightSeq:
            weaved = []
            weavedList(left, right, prefix, weaved)
            results += weaved
    return results


def weavedList(first, second, prefix, results):
    if len(first) == 0 or len(second) == 0:
        result = list(prefix)
        result += first
        result += second
        results.append(result)
        return
    firstHead = first.pop(0)
    prefix.append(firstHead)
    weavedList(first, second, prefix, results)
    prefix.pop()
    first.insert(0, firstHead)

    secondHead = second.pop(0)
    prefix.append(secondHead)
    weavedList(first, second, prefix, results)
    prefix.pop()
    second.insert(0, secondHead)


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
