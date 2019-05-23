#! /usr/bin/python3
import sys

class Stack:
    def __init__(self, size):
        self.top = None
        self.capacity = size
        self.stack = [] * size
    def __init__(self):
        self.top = None
        self.capacity = sys.maxsize
        self.stack = []
    def push(self, value):
        if (self.size() == self.capacity):
            return False

        self.stack.append(value)
        if (self.size() == 0):
            self.top = 0
        else:
            self.top = self.top + 1
        return True
    def pop(self):
        if (self.size() == 1):
            self.top = None
        else:
            self.top = self.top - 1
        return self.stack.pop()

    def size(self):
        if (self.top == None):
            return 0
        return self.top + 1
    def isEmpty(self):
        return self.size() == 0

    def peek(self):
        if (self.size() == 0):
            return None
        return self.stack[self.top]
    def print_data(self):
        print(self.stack)
