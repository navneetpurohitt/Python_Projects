class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    def enqueue(self, item):
        self.queue.append(item)
        print(self.queue)
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    def size(self):
        return len(self.queue)
    def __str__(self):
        return "Queue(" + ", ".join(str(item) for item in self.queue) + ")"    
    
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue)

queue.dequeue()
print(queue)
queue.enqueue(4)
print(queue)

queue.dequeue()
print(queue)

print(queue.is_empty())

print(queue.peek())
print(queue.size())