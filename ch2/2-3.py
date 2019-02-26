#! /usr/bin/python2
import sys
from basic_node import LinkedList

# using cur.next pointing to deleted item
def sol_remove_middle(head, removed_item):
    cur = head
    while (cur.next != None):
        if (cur.next.data == removed_item):
            cur.next = cur.next.next
        else:
            cur = cur.next

# using cur pointing to deleted item
def sol2_remove_middle(head, removed_item):
    cur = head
    while (cur != None):
        if (cur.next == None) {
            return
        }
        if (cur.data == removed_item):
            cur.data = cur.next.data
            cur.next = cur.next.next
        else:
            cur = cur.next

def main(argv):
    linked_list = LinkedList()
    if (len(argv) < int(argv[len(argv) - 1])):
        return
    for idx in range(1, len(argv) - 1, 1):
        linked_list.add(argv[idx])
    linked_list.print_data()
    sol_remove_middle(linked_list.head, argv[len(argv) - 1])
    linked_list.print_data()

if __name__ == "__main__":
    main(sys.argv)
