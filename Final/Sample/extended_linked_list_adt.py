from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def remove_duplicates(self):
        if not self.head:
            return
        if not self.head.next_node:
            return
        exist_value = set()
        node = self.head
        exist_value.add(node.value)
        while node.next_node.next_node:
            if node.next_node.value in exist_value:
                node.next_node = node.next_node.next_node
            else:
                node = node.next_node
                exist_value.add(node.value)
        if node.next_node.value in exist_value:
            node.next_node = None
            