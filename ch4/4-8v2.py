#! /usr/local/bin/python3
import sys
from basic_tree_node import *

class Result:
    def __init__(self, node, isAncestor):
        self.node = node
        self.isAncestor = isAncestor
    def IsAncestor(self):
        return self.isAncestor
    def Node(self):
        return self.node
def sol4_common_ancestor(root, p, q):
    result = sol4_helper(root, p, q)
    if (result.IsAncestor()):
        return result.Node()
    return None

def sol4_helper(node, p, q):
    if (node == None):
        return Result(None, False)
    if (node == p and node == q):
        return Result(node, True)

    leftResult = sol4_helper(node.left, p, q)
    if (leftResult.IsAncestor()):
        return leftResult
    rightResult = sol4_helper(node.right, p, q)
    if (rightResult.IsAncestor()):
        return rightResult
    
    if (leftResult.Node() != None and rightResult.Node() != None):
        return Result(node, True)
    elif (node == p or node == q):
        node_is_ans = leftResult.Node() != None or rightResult.Node() != None
        return Result(node, node_is_ans)
    else:
        return Result(leftResult.node if leftResult.Node() !=  None else rightResult.node, False)


def sol3_common_ancestor(root, p, q):
    if not cover(root, p) or not cover(root, q):
        return None
    return helper(root, p, q)
    
def helper(node, p, q):
    if (node == None or node == p or node == q):
        return node
    ponleft = cover(node.left, p)
    qonleft = cover(node.left, q)
    if (ponleft != qonleft):
        return node
    if ponleft and qonleft:
        return helper(node.left, p, q)
    else:
        return helper(node.right, p, q)

def cover(root, node):
    if (root == None):
        return False
    if root == node:
        return True
    return cover(root.left, node) or cover(root.right, node)

def main(argv):
    input = []
    for value in argv[1].split(','):
        input.append(int(value))
    root = build_tree_node(input)
    p = root.left
    q = root.left.left

    cm = sol3_common_ancestor(root, p, q)
    cm = sol4_common_ancestor(root, p, q)
    print(cm.value)

if __name__ == "__main__":
    main(sys.argv)