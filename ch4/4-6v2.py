#! /usr/local/bin/python3
import sys
from basic_tree_node import *

def find_next_node(node):
    if (node == None):
        return None
    if (node.right != None):
        return find_left_most(node.right)
    cur = node
    parent = cur.parent
    while(parent != None and parent.right == cur):
        cur = parent
        parent = cur.parent
    return parent

def find_left_most(node):
    if (node == None):
        return None
    if (node.left == None):
        return node
    return find_left_most(node.left)

def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(argv[idx])
    root = build_tree_node(input)
    root.print_by_level()
    root.print_data()

    node = find_next_node(root)
    print(node.value)

if __name__ == "__main__":
    main(sys.argv)