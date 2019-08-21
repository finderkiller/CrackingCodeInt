#! /usr/bin/python2
from basic_tree_node import *
import sys

def find_next_node(node):
    if not node:
        return
    if node.right:
        return find_left_most(node.right)
    while node.parent != None and node.parent.right == node:
        node = node.parent
    return node.parent

def find_left_most(node):
    while node != None and node.left!= None:
        node = node.left
    return node
    

def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(argv[idx])
        node = build_tree_node(input)

    node.print_data()
    node.print_by_level()
    next_node = find_next_node(node.left.right)
    print next_node.value
    next_node = find_next_node(node)
    next_node = find_next_node(node.right.right)

if __main__== "__main__":
    main(sys.argv)
