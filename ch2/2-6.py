#! /usr/bin/python2
from basic_node import LinkedList
from basic_node import Node
import sys


#sol1: time:O(n), space:O(n)
def sol_reverse_and_compare(linked_list):
    reversed_link_list = LinkedList()
    cur = linked_list.head

    # create reversed_link_list
    while(cur != None):
        new_node = Node(cur.data)
        new_node.next = reversed_link_list.head
        reversed_link_list.head = new_node
        cur = cur.next

    cur = linked_list.head
    reversed_cur = reversed_link_list.head
    while(cur != None and reversed_cur != None):
        if (cur.data != reversed_cur.data):
            return False
        cur = cur.next
        reversed_cur = reversed_cur.next

    return True

#sol2: time:O(n), space:O(n)
def sol_stack_iteration(linked_list):
    slow = linked_list.head
    fast = linked_list.head

    stack = []

    while (fast != None and fast.next != None):
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast != None:           #pointing last one means containing odd number
        slow = slow.next       #move slow from middle node to the next node

    while (slow != None):
        if (slow.data != stack.pop()):
            return False
        slow = slow.next
    return True

#sol3: time:O(n), space:O(n)
class Ret:
    def __init__(self, result, node):
        self.result = result
        self.node = node

def sol_using_recursive(linked_list, length):
    return sol_recursive(linked_list.head, length).result

def sol_recursive(cur, length):
    if (length == 1):                       #odd number
        return Ret(True, cur.next)
    if (length == 0):                       #even number
        return Ret(True, cur)

    result = sol_recursive(cur.next, length-2)
    if not result.result:
        return result

    if cur.data != result.node.data:
        return Ret(False, result.node)
    else:
        return Ret(True, result.node.next)

def main(argv):
    linked_list = LinkedList()
    for idx in range(1, len(argv), 1):
        linked_list.add(int(argv[idx]))
    linked_list.print_data()
#    result = sol_reverse_and_compare(linked_list)
#    result = sol_stack_iteration(linked_list)
    result = sol_using_recursive(linked_list, len(argv) - 1)
    print ("Is Palindrome" if result else "Not Palindrome")

if __name__ == "__main__":
    main(sys.argv)
