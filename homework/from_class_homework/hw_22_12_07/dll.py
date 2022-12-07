class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __str__(self):
        return str(self.value)


class OrderedLinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            current = self.current
            self.current = self.current.next
            return current
        raise StopIteration

    def print(self):
        for node in self:
            print(node, end='  ')
        print()

    def add_node(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        elif self.head.value > node.value:
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                if current.next.value > node.value:
                    node.next = current.next
                    current.next = node
                    break
                elif current.next.value < node.value:
                    current = current.next
                else:
                    break
            if current.next is None:
                current.next = node

