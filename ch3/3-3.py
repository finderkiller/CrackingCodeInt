#! /usr/bin/python2
from basic_stack import Stack
import sys

#sol1: without implement rolling over if someone want to popAt specific stack of the set of stacks
class SetOfStacks:
    def __init__(self):
        self.cur_stack_idx = None
        self.stack_plates = []

    def push(self, value):
        if (len(self.stack_plates) == 0):
            stack = Stack(5)
            stack.push(value)
            self.stack_plates.append(stack)
            self.cur_stack_idx = 0
            return True
        elif not (self.stack_plates[self.cur_stack_idx].push(value)):
            stack = Stack(5)
            stack.push(value)
            self.stack_plates.append(stack)
            self.cur_stack_idx += 1
        return True
    def pop(self):
        ret = self.stack_plates[self.cur_stack_idx].pop()
        if (self.stack_plates[self.cur_stack_idx].size() == 0):
            self.stack_plates.pop()
            if (self.cur_stack_idx == 0):
                self.cur_stack_idx = None
            else:
                self.cur_stack_idx -= 1
        return ret

    def peek(self):
        if self.cur_stack_idx == None:
            return None
        else:
            print self.stack_plates[self.cur_stack_idx].stack
            return self.stack_plates[self.cur_stack_idx].peek()

def main(argv):
    stack = SetOfStacks()
    for idx in range(len(argv[1])):
        stack.push(int(argv[1][idx]))

    for idx in range(int(argv[2])):
        print stack.pop()
    print stack.peek()

if __name__ in "__main__":
    main(sys.argv)
