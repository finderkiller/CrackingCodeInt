#! /usr/bin/python3

class TreeNode:
    def __init__(self, value):
        self.value = int(value)
        self.left = None
        self.right = None
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
def build_tree_node(array):
    if len(array) == 0:
        return None
    mid = len(array) // 2
    node = TreeNode(array[mid])
    node.left = build_tree_node(array[:mid])
    node.right = build_tree_node(array[mid+1:])
    return node
