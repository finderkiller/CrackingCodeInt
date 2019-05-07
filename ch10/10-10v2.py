#! /usr/bin/python3
import sys

class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.size = 0
        self.data = data

    def Insert(self, data):
        if (data <= self.data):
            if self.left == None:
                self.left = TreeNode(data)
            else:
                self.left.Insert(data)
        else:
            if self.right == None:
                self.right = TreeNode(data)
            else:
                self.right.Insert(data)
        self.size += 1

def GetRank(node, data):
    if node == None:
        return -1
    left_size = self.left.size if self.left != None else 0
    if node.data == data:
        return left_size
    elif data < node.data:
        return GetRank(node.left, data)
    else:
        right_rank = GetRank(node.right, data)
        return left_size + 1 + right_rank if right_rank != -1 else -1


def main(argv):
    root = None
    for value in argv[1].split(','):
        if root == None:
            root = TreeNode(value)
        else:
            root.Insert(value)

    rank = GetRank(root, int(argv[2]))
    if rank == -1:
        print("not found")
    else:
        print(rank)



if __name__ == "__main__":
    main(sys.argv)
