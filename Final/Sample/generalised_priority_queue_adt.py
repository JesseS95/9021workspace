
'''
A max priority queue abstract data type to insert pairs of the form (datum, priority).
If a pair is inserted with a datum that already occurs in the priority queue, then
the priority is (possibly) changed to the (possibly) new value.
'''


class EmptyPriorityQueueError(Exception):
    def __init__(self, message):
        self.message = message


class PriorityQueue():
    min_capacity = 1

    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self._data = [None] * capacity
        self._length = 0
        
    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def bubble_up(self, element):
        index_of_element = self._data.index(element)
        father_node = self._data[index_of_element // 2]
        if index_of_element == 1:
            return
        if father_node[1] >= element[1]:
            return
        else:
            self._data[index_of_element // 2] = element
            self._data[index_of_element] = father_node
            self.bubble_up(self._data[index_of_element // 2])

    def bubble_down(self, element):
        index_of_element = self._data.index(element)
        if index_of_element * 2 >= len(self._data):
            return
        else:
            left_child = self._data[index_of_element * 2]
            right_child = self._data[index_of_element * 2 + 1]
            if left_child == None:
                return
            elif left_child != None and right_child == None:
                if left_child[1] <= element[1]:
                    return
                else:
                    self._data[index_of_element] = left_child
                    self._data[index_of_element * 2] = element
                    return
            else:
                if left_child[1] >= right_child[1]:
                    if element[1] >= left_child[1]:
                        return
                    else:
                        self._data[index_of_element] = left_child
                        self._data[index_of_element * 2] = element
                        self.bubble_down(self._data[index_of_element * 2])
                else:
                    if element[1] >= right_child[1]:
                        return
                    else:
                        self._data[index_of_element] = right_child
                        self._data[index_of_element * 2 + 1] = element
                        self.bubble_down(self._data[index_of_element * 2 + 1])
                        

    def insert(self, element):
        for i in range(1, len(self._data)):
            if self._data[i] == None:
                self._data[i] = [element[0], element[1]]
                self._length += 1
                self.bubble_up(self._data[i])
                return

            if self._data[i][0] == element[0]:
                self._data[i] = [element[0], element[1]]
                if i == 1:
                    self.bubble_down(self._data[i])
                    return
                elif element[1] > self._data[i//2][1]:
                    self.bubble_up(self._data[i])
                    return
                else:
                    self.bubble_down(self._data[i])
                    return
        # if no space
        self._data += [[element[0], element[1]]]
        self._data += [None] * (self._data.index([element[0], element[1]]) - 1)
        self._length += 1
        self.bubble_up([element[0], element[1]])
        return
        
        
            

    def delete(self):
        if self._data[1] == None:
            raise EmptyPriorityQueueError('Error')
        else:
            self._data[1], self._data[self._length] = self._data[self._length], self._data[1]
            deleted_item = self._data[self._length]
            self._data[self._length] = None
            self._length -= 1
            self.bubble_down(self._data[1])
            if self._length < len(self._data) // 2:
                self._data = self._data[: -(self._length + 1)]
            return deleted_item[0]
            

pq = PriorityQueue()
           
L = [('A', 13), ('B', 13), ('C', 4), ('D', 15), ('E', 9), ('F', 4), ('G', 5),('H', 14), ('A', 4), ('B', 11), ('C', 15), ('D', 2), ('E', 17), ('A', 8),('B', 14), ('C',12), ('D', 9), ('E', 5), ('A', 6), ('B', 16)]
for e in L:
    pq.insert(e)
    print(f'{pq._data}')

for _ in range(len(pq)):
    print(f'{pq.delete()} {pq._data}')
