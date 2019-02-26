#! /usr/bin/python2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            return new_node
        cur = self.head
        while(cur.next != None):
            cur = cur.next
        cur.next = new_node
        return new_node
    def pop_head(self):
        if (self.isEmpty()):
            return None
        cur = self.head
        self.head = self.head.next
        return cur.data

    def add_head(self, data):
        new_node = Node(data)
        if (self.head == None):
            self.head = new_node
            return new_node
        new_node.next = self.head
        self.head = new_node
        return new_node
    def isEmpty(self):
        return self.head == None

    def print_data(self):
        cur = self.head
        output = []
        while(cur != None):
            output.append(cur.data)
            cur = cur.next
        print output
