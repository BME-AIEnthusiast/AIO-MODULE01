# Examples 3

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def is_full(self):
        return len(self.stack) == self.capacity

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def push(self, value):
        if not self.is_full():
            self.stack.append(value)

    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        return None


stack1 = Stack(capacity=5)
stack1.push(1)
stack1.push(2)
# Output example 1
print(stack1.is_full())
# Output example 2
print(stack1.top())
# Output example 3
print(stack1.pop())
# Output example 4
print(stack1.top())
# Output example 5
print(stack1.pop())
# Output example 6
print(stack1.is_empty())
