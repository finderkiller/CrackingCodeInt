#!/usr/bin/python
import sys
min_stack = []

class Stack:
    def __init__(self):
        self.top = None
        self.min_top = None
        self.min_stack = []
        self.stack = []
    def push(self, value):
        self.stack.append(value)
        self.top = len(self.stack) - 1
        if self.min() >= value:
            self.min_stack.append(value)
            self.min_top = len(self.min_stack) - 1
            print self.min_stack
    def pop(self):
        if (len(self.stack) == 0):
            return None
        result = self.stack.pop()
        if (len(self.stack) == 0):
            self.top = None
        else:
            self.top = len(self.stack) - 1

        if result == self.min():
            self.min_stack.pop()
            if (len(self.min_stack) == 0):
                self.min_top = None
            else:
                self.min_top = len(self.min_stack) - 1
        return result

    def min(self):
        if len(self.min_stack) == 0:
            return sys.maxint
        else:
            return self.min_stack[self.min_top]

def main(argv):
    stack = Stack()
    for idx in range(len(argv[1])):
        stack.push(int(argv[1][idx]))

    for idx in range(int(argv[2])):
        print stack.pop()

    print "min is ", stack.min()


if __name__ == "__main__":
    main(sys.argv)
