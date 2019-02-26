#! /usr/bin/python2
import sys
from basic_node import LinkedList

# fast_ptr 2k, slow_ptr is k, show when the slow pty is entering in the loop, fast_ptr has already k steps in loop, that means fast_ptr is
# loop_size - k away from the slow_ptr, then after loop_size - k steps, they will meet together. Since slow_ptr move loop_size - k steps from the start of loop, we could say that the meeting point is k steps away from the start of loop. Finaly, use two ptrs separately from the beginning of the linked list and the meeting point, when these two steps meet, we will find the start of the loop.

def sol_find_loop_start(head):
    fast_ptr = head
    slow_ptr = head
    has_loop = False
    loop_start_idx = 0

    while(fast_ptr != None and fast_ptr.next != None):
        fast_ptr = fast_ptr.next.next
        slow_ptr = slow_ptr.next
        if (fast_ptr is slow_ptr):
            has_loop = True
            break

    if not has_loop:
        return False
    slow_ptr = head
    while(not (fast_ptr is slow_ptr)):
        loop_start_idx += 1
        fast_ptr = fast_ptr.next
        slow_ptr = slow_ptr.next
    print "Find loop start, idx is ", loop_start_idx
    return True

def main(argv):
    linked_list = LinkedList()
    for idx in range(1, len(argv)-1, 1):
        linked_list.add(argv[idx])
    tail = linked_list.head
    loop_start = linked_list.head

    linked_list.print_data()
    while(tail.next != None):
        tail = tail.next
    for idx in range(int(argv[len(argv)-1])):
        loop_start = loop_start.next
    tail.next = loop_start

    sol_find_loop_start(linked_list.head)

if __name__ == "__main__":
    main(sys.argv)
