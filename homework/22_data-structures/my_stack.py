class Stack:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list == []

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def peek(self):
        return self.list[-1]

    def size(self):
        return len(self.list)

    def get_from_stack(self, position):
        return self.list[position]
