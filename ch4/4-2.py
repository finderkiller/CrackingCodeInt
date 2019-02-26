#! /usr/bin/python2
from basic_tree_node import TreeNode
import sys

def build_tree_node(array):
    if len(array) == 0:
        return None
    mid = len(array) / 2
    node = TreeNode(array[mid])
    node.left = build_tree_node(array[:mid])
    node.right = build_tree_node(array[mid+1:])
    return node

def main(argv):
    input = []
    for value in range(1, len(argv), 1):
        input.append(value)
        node = build_tree_node(input)
    node.print_data()

if __name__ == "__main__":
    main(sys.argv)
