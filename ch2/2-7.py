#! /usr/bin/python2
from basic_node import LinkedList
import sys

#sol1: time:O(A+B), space:O(1), iteration first to find the length and determined whether has intersection or not
def sol_find_intersection(linked_list_a, linked_list_b):
    length_a = 0
    length_b = 0
    cur_a = linked_list_a.head
    cur_b = linked_list_b.head
    while(cur_a != None):
        length_a += 1
        cur_a = cur_a.next

    while(cur_b != None):
        length_b += 1
        cur_b = cur_b.next
    if (cur_a is cur_b):
        print "Has Intersection"
    else:
        return

    cur_a = linked_list_a.head
    cur_b = linked_list_b.head
    diff = abs(length_a - length_b)
    if(length_a > length_b):
        for idx in range(diff):
            cur_a = cur_a.next
    else:
        for idx in range(diff):
            cur_b = cur_b.next
    while(cur_a != None and cur_b != None):
        if (cur_a is cur_b):
            print "Intersection Point, value is", cur_a.data
            return cur_a
        cur_a = cur_a.next
        cur_b = cur_b.next

def main(argv):
    linked_list_a = LinkedList()
    linked_list_b = LinkedList()
    for idx in range(2):
        linked_list_b.add(idx)
    tail_b = linked_list_b.head

    while (tail_b.next != None):
        tail_b = tail_b.next

    for idx in range(1, len(argv) - 1, 1):
        new_node = linked_list_a.add(int(argv[idx]))
        if (idx == int(argv[len(argv) - 1])):
            tail_b.next = new_node
    linked_list_a.print_data()
    linked_list_b.print_data()

    sol_find_intersection(linked_list_a, linked_list_b)

if __name__ == "__main__":
    main(sys.argv)
