#! /usr/bin/python2
from basic_node import LinkedList
from basic_node import Node
import sys


#Q1 is backward, as a result, the recursion is only for concate on head,
def sol_Q1_recursive(cur_a, cur_b, carry):
    if (cur_a == None and cur_b == None and carry == 0):
        return None
    value = carry
    if (cur_a != None):
        value += cur_a.data
    if (cur_b != None):
        value += cur_b.data

    return add_to_head(sol_Q1_recursive(
        cur_a.next if cur_a != None else None,
        cur_b.next if cur_b != None else None,
        value/10), value%10)

def sol_Q1_interation(cur_a, cur_b):
    if (cur_a == None and cur_b == None):
        return
    result = LinkedList();
    itr_a = cur_a
    itr_b = cur_b
    carry = 0
    while (itr_a != None or itr_b != None):
        value = carry
        if (itr_a != None):
            value += itr_a.data
        if (itr_b != None):
            value += itr_b.data
        result.add(value%10)
        carry = value/10
        itr_a = itr_a.next
        itr_b = itr_b.next
    if (carry != 0):
        result.add(carry)

    return result

#Follow up: Q2 is backward, as a result, the recursion is only for concate on head,
def sol_Q2(len_a, len_b, linked_list_a, linked_list_b, carry):
    if (len_a > len_b):
        padingZero(linked_list_b, len_a - len_b)
    else:
        padingZero(linked_list_a, len_b - len_a)

    result = sol_recursive_Q2(linked_list_a.head, linked_list_b.head)
    if (result.carry > 0):
        add_to_head(result.linked_list, result.carry)
    return result.linked_list

def padingZero(linked_list, length):
    for idx in range(length):
        new_node = Node(0)
        new_node.next = linked_list.head
        linked_list.head = new_node

def sol_recursive_Q2(cur_a, cur_b):
    if(cur_a == None and cur_b == None):
        return Ret(None, 0)
    result = sol_recursive_Q2(cur_a.next, cur_b.next)
    value = cur_a.data + cur_b.data + result.carry
    linked_list = add_to_head(result.linked_list, value%10)
    return Ret(linked_list, value/10)

#common function
def add_to_head(linked_list, value):
    new_node = Node(value)
    if (linked_list == None):
        linked_list = LinkedList()
    else:
        new_node.next = linked_list.head
    linked_list.head = new_node
    return linked_list

class Ret:
    def __init__(self, linked_list, carry):
        self.linked_list = linked_list
        self.carry = carry

def main(argv):
    linked_list_a = LinkedList()
    linked_list_b = LinkedList()
    for idx in range(1, len(argv[1]) - 1, 1):
        linked_list_a.add(int(argv[1][idx]))
    for idx in range(1, len(argv[2]) - 1, 1):
        linked_list_b.add(int(argv[2][idx]))
    linked_list_a.print_data()
    linked_list_b.print_data()
#     linked_list_output = sol_Q1_recursive(linked_list_a.head, linked_list_b.head, 0)
    linked_list_output = sol_Q1_interation(linked_list_a.head, linked_list_b.head)
#     linked_list_output = sol_Q2(len(argv[1]), len(argv[2]), linked_list_a, linked_list_b, 0)
    linked_list_output.print_data()

if __name__ == "__main__":
    main(sys.argv)
