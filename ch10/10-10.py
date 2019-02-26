#! /usr/bin/python3
import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.size = 1
    def insertNode(self, value):
        if (value == None):
            return
        if (value <= self.value):
            if (self.left == None):
                self.left = TreeNode(value)
            else:
                self.left.insertNode(value)
        else:
            if (self.right == None):
                self.right = TreeNode(value)
            else:
                self.right.insertNode(value)
        self.size += 1
    def print_data(self):
        print (self.value)
        if (self.left != None):
            print ("/")
            self.left.print_data()
        if (self.right != None):
            print ("\\")
            self.right.print_data()
    def print_by_level(self):
        lists = []
        sol_bfs(self, lists)
        print_lists(lists)

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
        print (output)

def getRank(node, value):
    if (node == None):
        return -1
    leftSize = node.left.size if node.left != None else 0
    if (value == node.value):
        return leftSize
    elif (value < node.value):
        return getRank(node.left, value)
    else:
        rank = getRank(node.right, value)
        return leftSize + 1 + rank if rank != -1 else -1


def main(argv):
    root = None
    for value in argv[1].split(','):
        if (root == None):
            root = TreeNode(int(value))
        else:
            root.insertNode(int(value))
    root.print_by_level()
    rank = getRank(root, int(argv[2]))
    if rank == -1:
        print("Not found")
    else:
        print(rank)

if __name__ == "__main__":
    main(sys.argv)
