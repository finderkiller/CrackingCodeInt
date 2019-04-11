#! /usr/local/bin/python3
import sys
from basic_tree_node import *

def sol2_is_subtree(root1, root2):
    if (root2 == None):
        return True
    return go_through_t1(root1, root2)

def go_through_t1(node1, node2):
    if (node1 == None):
        return False
    if (node1.value == node2.value and matchTree(node1, node2)):
        return True
    return go_through_t1(node1.left, node2) or go_through_t1(node1.right, node2)

def matchTree(node1, node2):
    if (node1 == None and node2 == None):
        return True
    if (node1 == None or node2 == None):
        return False
    if (node1.value != node2.value):
        return False
    return matchTree(node1.left, node2.left) and matchTree(node1.right, node2.right)

def sol1_is_subtree(root1, root2):
    preorder_string1 = build_preoder_string(root1)
    preorder_string2 = build_preoder_string(root2)

    print(preorder_string1)
    print(preorder_string2)

    if len(preorder_string1) > len(preorder_string2):
        return preorder_string1.find(preorder_string2) != -1
    else:
        return preorder_string2.find(preorder_string1) != -1

def build_preoder_string(node):
    if (node == None):
        return 'x'
    string = str(node.value)
    string += build_preoder_string(node.left)
    string += build_preoder_string(node.right)
    return string

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(value)
    root1 = build_tree_node(input)
    root1.print_data()

    input = []
    for value in argv[2].split(','):
        input.append(value)
    root2 = build_tree_node(input)
    root2.print_data()

    if (sol1_is_subtree(root1, root2)):
    # if (sol2_is_subtree(root1, root2)):
        print("found")
    else:
        print("not found")

if __name__ == "__main__":
    main(sys.argv)