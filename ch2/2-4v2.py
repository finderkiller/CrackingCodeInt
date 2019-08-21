#! /usr/bin/python2
from basic_node import LinkedList
import sys

#sol1: travese and insert to two new less than pivot list and greater-equal to pivot list, and merge them
#sol2: travese and insert less in head and insert greater one in tail
def sol_no_extra_space(head, pivot):
    if not head:
        return
    tail = head
    cur = head.next
    head.next = None
    while cur != None:
        nextStart = cur.next
        cur.next = None
        if cur.data >= pivot:
            tail.next = cur
            tail = cur
        else:
            cur.next = head
            head = cur
        cur = nextStart
    return head

def main(argv):
    linked_list = LinkedList()
    for idx in range(1, len(argv) - 1, 1):
        linked_list.add(int(argv[idx]))
    linked_list.print_data()
    sol_no_extra_space(linked_list, int(argv[len(argv) - 1]))

if __name__ == "__main__":
    main(sys.argv)
