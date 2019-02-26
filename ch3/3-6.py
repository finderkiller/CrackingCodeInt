#! /usr/bin/python2
import sys
sys.path.append('../ch2')
from basic_node import LinkedList

#sol2: we can use two queue for two types animal, when dequeueing compare the order of the top of these queue
#sol1: dequeueSpecific time:O(n), since we search the list and remove
class AnimalQueue:
    def __init__(self):
        self.linked_list = LinkedList()
        self.size = 0
    def enqueue(self, animal_type):
        self.linked_list.add(animal_type)
    def dequeueAny(self):
        if (self.linked_list.isEmpty()):
            return None
        return self.linked_list.pop_head()
    def dequeueDog(self):
        return self.dequeueImp("Dog")
    def dequeueCat(self):
        return self.dequeueImp("Cat")

    def dequeueImp(self, animal_type):
        if (self.linked_list.isEmpty()):
            return None
        if (self.linked_list.head.data == animal_type):
            return self.linked_list.pop_head()

        cur = self.linked_list.head
        while(cur.next != None):
            if (cur.next.data == animal_type):
                ret = cur.next.data
                cur.next = cur.next.next
                return ret
            cur = cur.next
        return None
    def print_data(self):
        self.linked_list.print_data()

def main(argv):
    animal_queue = AnimalQueue()
    for idx in range(len(argv[1])):
        if (argv[1][idx] == "c"):
            value = "Cat"
        else:
            value = "Dog"
        animal_queue.enqueue(value)
    animal_queue.print_data()

    for idx in range(len(argv[2])):
        if (argv[2][idx] == "c"):
            print animal_queue.dequeueCat()
        elif argv[2][idx] == "d":
            print animal_queue.dequeueDog()
        elif argv[2][idx] == "a":
            print animal_queue.dequeueAny()
    animal_queue.print_data()
if __name__ == "__main__":
    main(sys.argv)
