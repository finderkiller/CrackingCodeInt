#! /usr/local/bin/python3
import sys
from basic_tree_node import *
minint = -sys.maxsize-1

def sol2_is_balanced(node):
    return checkHeight(node) != minint

def checkHeight(node):
    if (node == None):
        return -1
    rightHeight = checkHeight(node.right)
    if (rightHeight == minint):
        return minint
    leftHeight = checkHeight(node.left)
    if (leftHeight == minint):
        return minint
    diff = abs(rightHeight - leftHeight)
    if diff > 1:
        return minint
    return max(rightHeight, leftHeight) + 1

def sol1_is_balanced(node):
    if (node == None):
        return True
    diff = abs(getHeight(node.left) - getHeight(node.right))
    if (diff > 1):
        return False
    return sol1_is_balanced(node.left) and sol1_is_balanced(node.right)

def getHeight(node):
    if (node == None):
        return -1
    return max(getHeight(node.left), getHeight(node.right)) + 1

def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(argv[idx])
    root = build_tree_node(input)
    root.print_data()
    root.print_by_level()

    if (sol1_is_balanced(root)):
        print("is_balanced")


if __name__ == "__main__":
    main(sys.argv)