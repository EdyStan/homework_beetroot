class Node:

    def __init__(self, value, next_node=None, prev_node=None):
        self.prev = prev_node
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self):
        self._head = None
        self._tail = None
        self._index_count = 0
        self._number_of_elements = 0
        self._iter_elem = None  # current element for iteration

    def __iter__(self):
        self._index_count = 0
        self._iter_elem = None
        return self

    def __next__(self):
        while self._index_count < self._number_of_elements:
            self._index_count += 1
            if self._iter_elem is None:
                self._iter_elem = self._head
            else:
                self._iter_elem = self._iter_elem.next

            return self._iter_elem

        raise StopIteration

    def add__tail_node(self, value):
        self._number_of_elements += 1
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

    def add__head_node(self, value):
        self._number_of_elements += 1
        node = Node(value)
        if self._head is None:
            self._head = node
            self._tail = node
        else:
            self._head.prev = node
            node.next = self._head
            self._head = node
