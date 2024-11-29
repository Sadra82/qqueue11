class Queue:
    def __init__(self):
        # ایجاد آرایه خالی برای صف
        self.queue = []

    def is_empty(self):
        # بررسی خالی بودن صف
        return len(self.queue) == 0

    def enqueue(self, item):
        # اضافه کردن عنصر به انتهای صف
        self.queue.append(item)

    def dequeue(self):
        # حذف عنصر از ابتدای صف
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.queue.pop(0)

    def peek(self):
        # مشاهده عنصر اول صف بدون حذف
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.queue[0]

    def size(self):
        # بازگرداندن تعداد عناصر موجود در صف
        return len(self.queue)



class CircularQueue:
    def __init__(self, capacity):
        # مقداردهی اولیه آرایه و متغیرها
        self.capacity = capacity 
        self.queue = [None] * capacity  
        self.front = -1 
        self.rear = -1

    def is_empty(self):
        # بررسی خالی بودن صف
        return self.front == -1

    def is_full(self):
        # بررسی پر بودن صف
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        # اضافه کردن عنصر به صف
        if self.is_full():
            raise OverflowError("Queue is full")
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        # حذف عنصر از ابتدای صف
        if self.is_empty():
            raise IndexError("Queue is empty")
        removed_item = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return removed_item

    def peek(self):
        # مشاهده اولین عنصر بدون حذف
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.queue[self.front]

    def size(self):
        # محاسبه تعداد عناصر در صف
        if self.is_empty():
            return 0
        if self.rear >= self.front:
            return self.rear - self.front + 1
        return self.capacity - self.front + self.rear + 1

    def reverse(self):
        if self.is_empty():
            return
        temp = []
        while not self.is_empty():
            temp.append(self.dequeue())
        for item in reversed(temp):
            self.enqueue(item)
