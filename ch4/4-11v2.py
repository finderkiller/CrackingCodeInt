#! /usr/bin/python3
import sys
import random
from basic_tree_node import sol_bfs, print_lists
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.size = 1
    def insertInorder(self, value):
        if value <= self.value:
            if not self.left:
                self.left = TreeNode(value)
            else:
                self.left.insertInorder(value)
        else:
            if not self.right:
                self.right = TreeNode(value)
            else:
                self.right.insertInorder(value)
        self.size += 1
    def getRandomNodeByIndex(self):
        idx = random.randint(0, self.size-1)
        return self.getIthNode(idx)
    def getIthNode(self, index):
        leftsize = self.left.size if self.left else 0
        if index == leftsize:
            return self
        elif index < leftsize:
            return self.left.getIthNode(index)
        return self.right.getIthNode(index-(leftsize+1))
    def print_by_level(self):
        lists = []
        sol_bfs(self, lists)
        print_lists(lists)

def main(argv):
    for idx, value in enumerate(argv[1].split(',')):
        if idx == 0:
            root = TreeNode(value)
            continue
        root.insertInorder(value)
    root.print_by_level()
    #sol1: dump or data into array, and random the index to choice the node, extra space, time:O(n), space:O(n)
    #sol2: maintain an array reflecting the structure of the tree, and random index of array
    #sol3: label index to all node in-order, and random the label, then find the label inorderly, time:O(n), no extra space
    #      However, while deleting and inserting, you must reset the label again.
    #sol3: using random function each traverse, time:O(logn) or precisely O(D), which D is the depth of the tree
    #sol4: fast but not working, randoming depth, but the possiblity is not the same
    #sol5: 1/3, not working
    #sol6: using leftsize and rightsize for randoming, so we need to record size while deleting and inserting
    #sol7: randint cost a lot, so just random once and using this index to find the index-th place node in in-order traverse, time:O(logn) or precisely O(D), which D is the depth of the tree
    rd_node = root.getRandomNodeByIndex()
    print (rd_node.value)

if __name__ == "__main__":
    main(sys.argv)
