#! /usr/bin/python2
from basic_tree_node import *
import sys
#sol3, min-max range
def sol3_min_max_range(node, min_value, max_value):
    if (node == None):
        return True
    if (min_value != None and node.value <= min_value) or (max_value != None and node.value > max_value):
        return False
    if not sol3_min_max_range(node.left, min_value, node.value) or not sol3_min_max_range(node.right, node.value, max_value):
        return False
    return True

#sol2: in-order traverse, without array, just record the last element, it is max element right now
last_node = None
def sol2_record_max(node):
    global last_node
    if (node == None):
        return True
    if not sol2_record_max(node.left):
        return False
    if (last_node != None and (node.value <= last_node.value)):
        return False
    last_node = node
    if not sol2_record_max(node.right):
       return False
    return True

#sol1: in-order traverse and copy into an array, check the order of element in array
#time:O(n), space: O(n)
def sol1_copy_array(root):
    check_array = []
    traverse_and_push(root, check_array)
    #then compare array element

def traverse_and_push(node, check_array):
    if (node == None):
        return
    traverse_and_push(node.left, check_array)
    check_array.append(node.value)
    traverse_and_push(node.right, check_array)

def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(argv[idx])
        node = build_tree_node(input)

    node.print_data()
    node.print_by_level()
#    sol1_copy_array(node)
#    print "Is BST" if sol2_record_max(node) else "Not BST"
    print "Is BST" if sol3_min_max_range(node, None, None) else "Not BST"


if __name__ == "__main__":
    main(sys.argv)
