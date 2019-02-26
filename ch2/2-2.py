#! /usr/bin/python2
import sys
from basic_node import LinkedList

#sol1: time:O(n), too trival, not recommend in the interview
def sol_using_length(linked_list, k):
    cur = linked_list.head
    length = 0
    x = 0
    while (cur != None):
        length += 1
        cur = cur.next
    x = length - k
    cur = linked_list.head

    for idx in range(x):
        cur = cur.next
    print_linked_list(cur)

#sol2: time:O(n), space: each iteration has O(n)
def sol_recursive(cur, k):
    if cur == None:
        return 0
    idx = sol_recursive(cur.next, k) + 1
    if idx == k:
        print_linked_list(cur)
    return idx

#sol3: time:O(n), space: O(1), p2先走3步，p1,p2一起走，p2到底了那p1還差3步到底，也就是p1所在的位置是最後第3個
def sol_iteration(cur, k):
    p1 = cur
    p2 = cur
    for idx in range(k):
        p2 = p2.next

    while(p2 != None):
        p2 = p2.next
        p1 = p1.next
    print_linked_list(p1)

def print_linked_list(cur):
    output = []
    while (cur != None):
        output.append(cur.data)
        cur = cur.next
    print output

def main(argv):
    linked_list = LinkedList()
    if (len(argv) < int(argv[len(argv) - 1])):
        return
    for idx in range(1, len(argv) - 1, 1):
        linked_list.add(argv[idx])
    linked_list.print_data()
#    sol_using_length(linked_list, int(argv[len(argv) - 1]))
#    sol_recursive(linked_list.head, int(argv[len(argv) - 1]))
    sol_iteration(linked_list.head, int(argv[len(argv) - 1]))
if __name__ == "__main__":
    main(sys.argv)
