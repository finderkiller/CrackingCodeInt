#! /usr/bin/python2
import sys
from basic_tree_node import *

#sol1 and sol2 assume that each node has a pointer to its parent
#sol1: like Q2-7, using two pointers to find first intersection if nodes have the pointer to point its parent
#sol2: find two node whether cover each other or not, then find sibling, nothing found then go to parent's parent and find parent's sibling

#sol3: no pointer point to parent, time: O(n), since in a balanced tree, there are n nodes in right and left side
def find_common_ancestor(root, p, q):
    if not cover(root, p) or not cover(root, q):
        return None
    return find_common_ancestor_helper(root, p, q)

def find_common_ancestor_helper(node, p, q):
    if (node == None or node is p or node is q):        #include p cover q, or q cover p
        return node
    isPOnLeft = cover(node.left, p)
    isQOnLeft = cover(node.left, q)
    if isPOnLeft != isQOnLeft:
        return node             #first common ancestor
    if isPOnLeft and isQOnLeft:
        return find_common_ancestor_helper(node.left, p, q)
    else:
        return find_common_ancestor_helper(node.right, p, q)

def cover(root, node):
    if root == None:
        return False
    if node is root:
        return True
    return cover(root.left, node) or cover(root.right, node)
#sol4: optimize for sol3, return p if find p, return q if find q, return null if not found, return common ancestor if foundit


def main(argv):
    input = []
    for idx in range(1, len(argv), 1):
        input.append(argv[idx])
        node = build_tree_node(input)

    node.print_data()
    node.print_by_level()

    p = node.left
    q = node.left.left
    common_ancestor = find_common_ancestor(node, p, q)
    print common_ancestor.value

if __name__ == "__main__":
    main(sys.argv)
