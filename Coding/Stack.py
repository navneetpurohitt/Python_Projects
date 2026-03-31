class Stack:
    def __init__(self):
        self.stack = []
    def is_empty(self):
        return len(self.stack) == 0
    def push(self, item):
        self.stack.append(item)
        print(self.stack)
    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    def size(self):
        return len(self.stack)
    def clear(self):
        self.stack.clear()
    
    def __str__(self):
        return str(self.stack)


stack = Stack()
stack.is_empty()  # True
stack.push(1)
stack.push(2)
stack.push(3)
s = stack.size()  # 3
print(s)
s = stack.peek()  # 3
print(s)

s = stack.pop()  # 3
print(s)
s = stack.size()  # 2
print(s)
s = stack.peek()  # 2
print(s)
s = stack.pop()  # 2
print(s)
