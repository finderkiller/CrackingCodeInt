#! /usr/bin/python2
from basic_tree_node import *
import sys

#time:time:O(n+km), which k is the number of occurrences of T2's root in T1, space:O(logn + logm)
def sol_inplace_compare(node1, node2):
    if node2 == None:
        return True
    return go_through_T1(node1, node2)

def go_through_T1(node1, node2):
    if node1 == None:
        return False
    if node1.value == node2.value and matchTree(node1, node2):
        return True
    return go_through_T1(node1.left, node2) or go_through_T1(node1.right, node2)
def matchTree(node1, node2):
    if (node1 == None and node2 == None):
        return True
    if (node1 == None or node2 == None):
        return False
    if (node1.value != node2.value):
        return False
    return matchTree(node1.left, node2.left) and matchTree(node1.right, node2.right)

#time:O(n+m), space:O(n+m), which n is the number of nodes of Tree1, m is the number of nodes of Tree2
def sol_using_extra_space(node1, node2):
    string1 = getPreOrderStr(node1)
    string2 = getPreOrderStr(node2)

    print "string1 is " + string1
    print "string2 is " + string2
    return string1.find(string2) != -1

def getPreOrderStr(node):
    if (node == None):
        return "x";
    string = ""
    string += str(node.value)
    string += getPreOrderStr(node.left)
    string += getPreOrderStr(node.right)
    return string

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(value)
    node1 = build_tree_node(input)
    node1.print_data()
    node1.print_by_level()

    input = []
    for value in argv[2].split(','):
        input.append(value)
    node2 = build_tree_node(input)
    node2.print_data()
    node2.print_by_level()

#    if sol_using_extra_space(node1, node2):
#        print("Tree2 is subtree of Tree1")

    if sol_inplace_compare(node1, node2):
        print("Tree2 is subtree of Tree1")
if __name__ == "__main__":
    main(sys.argv)
