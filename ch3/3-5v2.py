#! /usr/bin/python3
import sys
from basic_stack import Stack


def sort(stack, sorted_stack):
    while not stack.isEmpty():
        top = stack.pop()
        while (not sorted_stack.isEmpty())and top > sorted_stack.peek():
            stack.push(sorted_stack.pop())
        sorted_stack.push(top)
    return sorted_stack

def main(argv):
    stack = Stack()
    sorted_stack = Stack()
    for data in argv[1].split(','):
        stack.push(int(data))
    sort(stack, sorted_stack)
    sorted_stack.print_data()



if __name__ == "__main__":
    main(sys.argv)
