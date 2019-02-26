#! /usr/bin/python2
from basic_stack import Stack
import sys

#sol1: time:O(n^2), space:O(n)
def sort_by_two_stack(stack, sorted_stack):
    while(not stack.isEmpty()):
        cur = stack.pop()
        if (sorted_stack.isEmpty()):
            sorted_stack.push(cur)
            continue
        while (not sorted_stack.isEmpty() and sorted_stack.peek() < cur):
            stack.push(sorted_stack.pop())
        sorted_stack.push(cur)

def main(argv):
    stack = Stack()
    sorted_stack = Stack()
    for idx in range(len(argv[1])):
        stack.push(int(argv[1][idx]))
    stack.print_data()
    sort_by_two_stack(stack, sorted_stack)
    sorted_stack.print_data()

if __name__ == "__main__":
    main(sys.argv)
