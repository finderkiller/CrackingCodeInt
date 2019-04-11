#! /usr/local/bin/python3
import sys
from basic_tree_node import *

def sol3_is_BST(node):
    return sol3_impl(node, None, None)

def sol3_impl(node, min, max):
    if (node == None):
        return True
    if (max != None and node.value > max):
        return False
    if (min != None and node.value <= min):
        return False
    if (not sol3_impl(node.left, min, node.value) or not sol3_impl(node.right, node.value, max)):
        return False
    return True

last_print = -sys.maxsize-1
def sol2_is_BST(node):
    global last_print
    if (node == None):
        return True
    if (not sol2_is_BST(node.left)):
        return False
    if (node.value < last_print):
        return False
    last_print = node.value
    if (not sol2_is_BST(node.right)):
        return False
    return True

def sol1_is_BST(root):
    check_array = []
    add_to_array(root, check_array)
    for idx in range(1, len(check_array), 1):
        if(check_array[idx] < check_array[idx - 1]):
            return False
    return True

def add_to_array(node, check_array):
    if (node == None):
        return
    add_to_array(node.left, check_array)
    check_array.append(node.value)
    add_to_array(node.right, check_array)


def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(int(argv[idx]))
    root = build_tree_node(input)
    # if (sol1_is_BST(root)):
    # if (sol2_is_BST(root)):
    if (sol3_is_BST(root)):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main(sys.argv)