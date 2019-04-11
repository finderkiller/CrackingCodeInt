#! /usr/bin/python2
from basic_tree_node import *
import sys
minint = -sys.maxint -1

#sol2: using check_height compute height and diff on the same time
#time: O(n), touch every node
def sol2_is_balanced(root):
    return check_height(root) != minint

def check_height(node):
    if (node == None):
        return -1
    left_height = check_height(node.left)
    if left_height == minint:
        return minint
    right_height = check_height(node.right)
    if right_height == minint:
        return minint

    height_diff = abs(left_height - right_height)

    if (height_diff > 1):
        return minint
    return max(left_height, right_height) + 1

#sol1: this solution is not efficient, since while travering the tree for getHeight, it can also get the diff of the node
#time: O(nlogn)? since (n-1) + (n-3) + ... ,total logn items;
def sol1_is_balanced(root):
    if (root == None):
        return True
    height_diff = abs(getHeight(root.left) - getHeight(root.right))
    if (height_diff > 1):
        return False
    return sol1_is_balanced(root.left) and sol1_is_balanced(root.right)
# the height of the leafs of binary tree is 0
def getHeight(node):
    if (node == None):
        return -1
    return max(getHeight(node.left), getHeight(node.right)) + 1

def main(argv):
    input = []
    for value in range(1, len(argv), 1):
        input.append(value)
        node = build_tree_node(input)

    node.print_data()
    # print sol1_is_balanced(node)
    print sol2_is_balanced(node)
if __name__ == "__main__":
    main(sys.argv)
