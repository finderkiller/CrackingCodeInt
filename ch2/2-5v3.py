#! /usr/bin/python2
from basic_node import LinkedList
from basic_node import Node
import sys


#Q1 is backward, as a result, the recursion is only for concate on head,
def sol_Q1_recursive(cur_a, cur_b, carry):
    if not cur_a and not cur_a:
        return None
    value = carry
    if cur_a:
        value += cur_a.data
    if cur_b:
        value += cur_b.data
    node = Node(value%10)
    node.next = sol_Q1_recursive(cur_a.next if cur_a else None, cur_b.next if cur_b else None, value//10)
    return node

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
def sol_Q2(head_a, head_b):
    if not head_a or not head_b:
        return None
    if not head_a:
        return head_b
    if not head_b:
        return head_a
    length_a = node_length(head_a)
    length_b = node_length(head_b)
    if length_a < length_b:
        self.sol_Q2(head_b, head_a)
    head_b = prepandZero(head_b, length_a - length_b)
    result = self.sol_recursive_Q2(head_a, head_b)
    if result.carry != 0:
        node = Node(result.carry)
        node.next = result.node
        return node
    return result.node


def node_length(head):
    length = 0
    while head != None:
        length += 1
        head = head.next
    return length

def prepandZero(head, length):
    if head == None:
        return
    while length > 0:
        node = Node(0)
        node.next = head
        head = node
        length -= 1
    return head


def sol_recursive_Q2(cur_a, cur_b):
    if not cur_a and not cur_b:
        return Ret(None, 0)
    prev = sol_recursive_Q2(cur_a.next, cur_a.next)
    value = prev.carry
    value += cur_a.data + cur_b.data
    node = Node(value % 10)
    node.next = prev.node
    return Ret(node, value // 10)
    
#common function
class Ret:
    def __init__(self, node, carry):
        self.node = node
        self.carry = carry

def main(argv):
    linked_list_a = LinkedList()
    linked_list_b = LinkedList()
#     linked_list_output = sol_Q1_recursive(linked_list_a.head, linked_list_b.head, 0)
    linked_list_output = sol_Q1_interation(linked_list_a.head, linked_list_b.head)
#     linked_list_output = sol_Q2(linked_list_a, linked_list_b)
    linked_list_output.print_data()

if __name__ == "__main__":
    main(sys.argv)
