class QueueUsingStacks:
    def __init__(self):
        self.stack1, self.stack2 = [], []

    def enqueue(self, value):
        self.stack1.append(value)
        print(f"{value} has been added to the queue.")

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        
        if not self.stack2:
            print("The queue is empty, no elements to dequeue.")
            return None
        
        dequeued_value = self.stack2.pop()
        print(f"{dequeued_value} has been removed from the queue.")
        return dequeued_value

    def is_empty(self):
        return not (self.stack1 or self.stack2)

    def size(self):
        return len(self.stack1) + len(self.stack2)
