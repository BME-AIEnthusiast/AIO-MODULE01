# Examples 4
class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None

    def enqueue(self, value):
        if not self.is_full():
            self.queue.append(value)

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        return None


queue1 = Queue(capacity=5)
queue1.enqueue(1)
queue1.enqueue(2)
# Output example 1
print(queue1.is_full())
# Output example 2
print(queue1.front())
# Output example 3
print(queue1.dequeue())
# Output example 4
print(queue1.front())
# Output example 5
print(queue1.dequeue())
# Output example 6
print(queue1.is_empty())
