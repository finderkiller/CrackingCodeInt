#! /usr/bin/python2
from basic_tree_node import *
import sys

#using level as an index of list of list
def sol_dfs(root, lists, level):
    if (root == None):
        return
    current = []
    if (len(lists) == level):           #first time travsers in this level
        lists.append(current)
    else:
        current = lists[level]
    current.append(root)
    sol_dfs(root.left, lists, level + 1)
    sol_dfs(root.right, lists, level + 1)

def sol_bfs(root, lists):
    if (root == None):
        return
    current = [root]

    while (len(current) != 0):
        lists.append(current)
        parents = current
        current = []
        for parent in parents:
            if (parent.left != None):
                current.append(parent.left)
            if (parent.right != None):
                current.append(parent.right)

def print_lists(lists):
    for cur in lists:
        output = []
        for node in cur:
            output.append(node.value)
        print output

def main(argv):
    input = []
    for value in range(1, len(argv), 1):
        input.append(value)
        node = build_tree_node(input)
    lists = []
#    sol_dfs(node, lists, 0)
    sol_bfs(node, lists)
    node.print_data()
    print_lists(lists)

if __name__ == "__main__":
    main(sys.argv)
