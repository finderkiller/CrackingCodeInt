#! /usr/bin/python2
from basic_node import LinkedList
from basic_node import Node
import sys

def sol3_Q1_iteration(a, b):
    result_list = LinkedList()
    cur_a = a
    cur_b = b
    carry = 0
    while (cur_a != None or cur_b != None or carry != 0):
        value = carry
        if a != None:
            value += cur_a.data
        if b != None:
            value += cur_b.data
        result_list.add(value % 10)
        carry = value //10
        cur_a = cur_a.next
        cur_b = cur_b.next
    return result_list

def sol2_Q1_recursive(a, b):
    result_list = LinkedList()
    helper(a, b, 0, result_list)
    return result_list

def helper(a, b, carry, result_list):
    if a == None and b == None and carry == 0:
        return
    value = carry
    if a != None:
        value += a.data
    if b != None:
        value += b.data
    result_list.add(value % 10)
    return helper(
            a.next if a != None else None,
            b.next if b != None else None,
            value//10,
            result_list
            )

def sol1_Q1_recursive(a, b, carry):
    if a == None and b == None and carry == 0:
        return None
    value = carry
    if a != None:
        value += a.data
    if b != None:
        value += b.data
    return add_to_head(
            sol1_Q1_recursive(
                a.next if a!= None else None,
                b.next if b!= None else None,
                value//10),
            value%10)


def add_to_head(linked_list, value):
    new_node = Node(value)
    if linked_list == None:
        linked_list = LinkedList()
    else:
        new_node.next = linked_list.head
    linked_list.head = new_node
    return linked_list

def sol_Q2(a, b):
    lena = length(a.head)
    lenb = length(b.head)
    if lena > lenb:
        prependZero(b, lena - lenb)
    elif lenb > lena:
        prependZero(a, lenb - lena)
    result = Q2_helper(a.head, b.head)
    if result.head.data == 0:
        result.pop_head()
    return result

def Q2_helper(a, b):
    if a == None and b == None:
        linked_list = LinkedList()
        linked_list.add(0)
        return linked_list
    result = Q2_helper(a.next, b.next)
    value = a.data + b.data + result.head.data
    result.head.data = value % 10
    result.add_head(value // 10)

    return result


def prependZero(linked_list, count):
    while count > 0:
        new_node = Node(0)
        new_node.next = linked_list.head
        linked_list.head = new_node
        count -= 1
    return

def length(node):
    if node == None:
        return 0
    return length(node.next) + 1

def main(argv):
    linked_list_a = LinkedList()
    linked_list_b = LinkedList()
    for data in argv[1].split(','):
        linked_list_a.add(int(data))
    for data in argv[2].split(','):
        linked_list_b.add(int(data))
    linked_list_a.print_data()
    linked_list_b.print_data()

#     linked_list_output = sol1_Q1_recursive(linked_list_a.head, linked_list_b.head, 0)
#     linked_list_output.print_data()
#     linked_list_output = sol2_Q1_recursive(linked_list_a.head, linked_list_b.head)
#     linked_list_output.print_data()
#     linked_list_output = sol3_Q1_iteration(linked_list_a.head, linked_list_b.head)
#     linked_list_output.print_data()
    linked_list_output = sol_Q2(linked_list_a, linked_list_b)
    linked_list_output.print_data()
if __name__ == "__main__":
    main(sys.argv)
