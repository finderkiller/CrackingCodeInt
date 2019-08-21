#! /usr/bin/local/python3
import sys

def sol(head, k):
    p1 = head
    p2 = head
    for i in range(k):
        if (p2 == None):
            return None
        p2 = p2.next
    
    while(p2 == None):
        p1 = p1.next
        p2 = p2.next
    return p1

def main(argv):
    head = []
    sol(head, 3)

if __name__ == "__main__":
    main(sys.argv)