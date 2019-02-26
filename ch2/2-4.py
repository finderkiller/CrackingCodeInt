#! /usr/bin/python2
from basic_node import LinkedList
import sys

#sol1: travese and insert to two new less than pivot list and greater-equal to pivot list, and merge them
#sol2: travese and insert less in head and insert greater one in tail
def sol_no_extra_space(linked_list, pivot):
    tail = linked_list.head
    cur = linked_list.head.next
    tail.next = None

    while (cur != None):
        next_cur = cur.next
        if (cur.data < pivot):
            cur.next = linked_list.head
            linked_list.head = cur
            print linked_list.head.data
            linked_list.print_data()
        else:
            tail.next = cur
            tail = cur
            tail.next = None
        cur = next_cur

def main(argv):
    linked_list = LinkedList()
    for idx in range(1, len(argv) - 1, 1):
        linked_list.add(int(argv[idx]))
    linked_list.print_data()
    sol_no_extra_space(linked_list, int(argv[len(argv) - 1]))

if __name__ == "__main__":
    main(sys.argv)
