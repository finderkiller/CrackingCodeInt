#! /usr/bin/python2
import sys
from basic_node import LinkedList

#2.1 Remove Dups: Write code to remove duplicates from an unsorted linked list.
#FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?
#sol1: time:O(n), space:O(n)

def sol_using_buffer(linked_list):
    hash_set = set()
    prev = None
    cur = linked_list.head
    while(cur != None):
        if (cur.data in hash_set):
            prev.next = cur.next
        else:
            hash_set.add(cur.data)
            prev = cur
        cur = cur.next

#sol2: time:O(n^2), no extra space, removing node could using only one pointer but need to consider the value of first node
def sol_two_pointer(linked_list):
    cur = linked_list.head
    while (cur != None):
        prev = cur                  #先用prev，但其實可以不用，只要先把第一個node的情況想好即可，因為while迴圈裡面都是處理itr.next理的事情
        itr = cur.next
        while (itr != None):
            if (itr.data == cur.data):
                prev.next = itr.next
            else:
                prev = itr
        cur = cur.next

#sol2: without prev pointer, using itr.next as iterator
def sol_two_pointer_wo_prev(linked_list):
    cur = linked_list.head
    while (cur.next != None):
        itr = cur
        while (itr.next != None):
            if (itr.next.data == cur.data):
                itr.next = itr.next.next
            else:
                itr = itr.next
        cur = cur.next


def main(argv):
    linked_list = LinkedList()
    for idx in range(1, len(argv), 1):
        linked_list.add(argv[idx])
    linked_list.print_data()

    if linked_list.head == None:
        return
    sol_using_buffer(linked_list)
#    sol_two_pointer(linked_list)
    linked_list.print_data()

if __name__ == "__main__":
    main(sys.argv)
