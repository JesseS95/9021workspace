

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self, step):
        start = self.head
        for i in range (step - 2):
            start = start.next_node

        move = self.head
        while move.next_node:
            move = move.next_node
        end = move
        end.next_node = self.head

        self.head = start.next_node
        tom = self.head
        start.next_node = self.head.next_node
        start = self.head

        while (step > 1):
            for _ in range ( step - 1 ):
                tom = tom.next_node
                if  tom == end:
                    step -= 1
            start.next_node = tom.next_node
            tom.next_node = tom.next_node.next_node
            tom = start.next_node
            start = tom
        end.next_node = None







    
    
    
