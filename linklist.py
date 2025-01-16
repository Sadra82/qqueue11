class Node:
    def __init__(self, data):
        self.data = data  # مقدار داده‌ای که در گره ذخیره شده
        self.next = None  # اشاره‌گر به گره بعدی (در ابتدا None است)
        self.prev = None  # اشاره‌گر به گره قبلی


# تعریف کلاس برای لیست پیوندی
class LinkedList:
    def __init__(self):
        self.head = None  # اشاره‌گر به اولین گره (در ابتدا خالی است)

    # افزودن یک گره در انتهای لیست
    def append(self, data):
        new_node = Node(data)
        if self.head is None:  # اگر لیست خالی است
            self.head = new_node
            return
        # حرکت به انتهای لیست
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # نمایش مقادیر لیست
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # حذف گره بر اساس مقدار
    def delete(self, data):
        current = self.head
        # اگر گره اول حاوی مقدار باشد
        if current and current.data == data:
            self.head = current.next
            current = None
            return
        # جستجو برای گره حاوی مقدار
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        # اگر گره پیدا نشود
        if current is None:
            print(f"Value {data} not found in the list.")
            return
        # حذف گره
        prev.next = current.next
        current = None

    # جستجوی مقدار در لیست
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

      
# تعریف کلاس برای لیست پیوندی حلقوی
class CircularLinkedList:
    def __init__(self):
        self.head = None  # اشاره‌گر به اولین گره

    # افزودن گره به انتهای لیست
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # اگر لیست خالی است
            self.head = new_node
            new_node.next = self.head  # اشاره به خودش برای ایجاد حلقه
        else:
            current = self.head
            while current.next != self.head:  # حرکت به انتهای لیست
                current = current.next
            current.next = new_node
            new_node.next = self.head  # ایجاد حلقه به گره اول

    # نمایش مقادیر لیست
    def display(self):
        if not self.head:  # اگر لیست خالی است
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # وقتی دوباره به گره اول رسیدیم
                break
        print("(head)")

    # حذف گره بر اساس مقدار
    def delete(self, data):
        if not self.head:  # اگر لیست خالی است
            print("List is empty")
            return
        
        current = self.head
        prev = None

        # اگر گره‌ای که باید حذف شود، گره اول است
        if current.data == data:
            while current.next != self.head:  # حرکت به انتهای لیست
                current = current.next
            if self.head.next == self.head:  # اگر فقط یک گره در لیست باشد
                self.head = None
            else:
                current.next = self.head.next
                self.head = self.head.next
            return

        # جستجوی گره‌ای که باید حذف شود
        while current.next != self.head and current.data != data:
            prev = current
            current = current.next

        # اگر گره پیدا شود
        if current.data == data:
            prev.next = current.next
        else:
            print(f"Value {data} not found in the list")

    # جستجوی مقدار در لیست
    def search(self, data):
        if not self.head:  # اگر لیست خالی است
            return False
        current = self.head
        while True:
            if current.data == data:
                return True
            current = current.next
            if current == self.head:  # وقتی به گره اول برگردیم
                break
        return False



# تعریف کلاس برای لیست پیوندی دوطرفه
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # اشاره‌گر به اولین گره

    # افزودن گره به انتهای لیست
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # اگر لیست خالی است
            self.head = new_node
            return
        current = self.head
        while current.next:  # حرکت به انتهای لیست
            current = current.next
        current.next = new_node
        new_node.prev = current

    # نمایش مقادیر لیست از ابتدا به انتها
    def display_forward(self):
        if not self.head:  # اگر لیست خالی است
            print("List is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # نمایش مقادیر لیست از انتها به ابتدا
    def display_backward(self):
        if not self.head:  # اگر لیست خالی است
            print("List is empty")
            return
        current = self.head
        while current.next:  # حرکت به انتهای لیست
            current = current.next
        while current:  # حرکت از انتها به ابتدا
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    # حذف گره بر اساس مقدار
    def delete(self, data):
        if not self.head:  # اگر لیست خالی است
            print("List is empty")
            return
        
        current = self.head

        # اگر گره‌ای که باید حذف شود، گره اول باشد
        if current.data == data:
            if current.next:  # اگر بیش از یک گره وجود دارد
                self.head = current.next
                self.head.prev = None
            else:  # اگر تنها یک گره در لیست وجود دارد
                self.head = None
            return

        # جستجوی گره مورد نظر
        while current and current.data != data:
            current = current.next

        # اگر گره پیدا نشود
        if not current:
            print(f"Value {data} not found in the list")
            return

        # حذف گره
        if current.next:  # اگر گره مورد نظر آخرین گره نباشد
            current.next.prev = current.prev
        if current.prev:  # اگر گره مورد نظر اولین گره نباشد
            current.prev.next = current.next

    # جستجوی مقدار در لیست
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False


class DoublyLinkedList:
    """کلاس لیست پیوندی دوطرفه"""
    def __init__(self):
        self.head = None  # اشاره‌گر به اولین گره
        self.size = 0     # اندازه لیست

    def insert_at_begin(self, data):
        """افزودن گره به ابتدای لیست"""
        new_node = Node(data)
        if self.head:  # اگر لیست خالی نیست
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """افزودن گره به انتهای لیست"""
        new_node = Node(data)
        if not self.head:  # اگر لیست خالی است
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.size += 1

    def insert_at_index(self, data, index):
        """افزودن گره در یک موقعیت مشخص"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.insert_at_begin(data)
        elif index == self.size:
            self.insert_at_end(data)
        else:
            new_node = Node(data)
            current = self.head
            for _ in range(index - 1):  # حرکت به موقعیت مورد نظر
                current = current.next
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node
            self.size += 1

    def update_node(self, data, index):
        """به‌روزرسانی مقدار یک گره در یک موقعیت مشخص"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        current.data = data

    def remove_node_at_begin(self):
        """حذف گره از ابتدای لیست و بازگرداندن مقدار آن"""
        if not self.head:
            raise Exception("List is empty")
        data = self.head.data
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size -= 1
        return data

    def remove_node_at_end(self):
        """حذف گره از انتهای لیست و بازگرداندن مقدار آن"""
        if not self.head:
            raise Exception("List is empty")
        current = self.head
        while current.next:
            current = current.next
        data = current.data
        if current.prev:
            current.prev.next = None
        else:
            self.head = None
        self.size -= 1
        return data

    def remove_node_at_index(self, index):
        """حذف گره از یک موقعیت مشخص و بازگرداندن مقدار آن"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            return self.remove_node_at_begin()
        elif index == self.size - 1:
            return self.remove_node_at_end()
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            data = current.data
            current.prev.next = current.next
            current.next.prev = current.prev
            self.size -= 1
            return data

    def size_of_list(self):
        """بازگرداندن اندازه لیست"""
        return self.size

    def invert(self):
        """معکوس کردن لیست"""
        if not self.head:
            return
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def concatenate(self, other_list):
        """الحاق یک لیست پیوندی دیگر به انتهای این لیست"""
        if not isinstance(other_list, DoublyLinkedList):
            raise TypeError("Can only concatenate with another DoublyLinkedList")
        if not other_list.head:
            return
        if not self.head:
            self.head = other_list.head
            self.size = other_list.size
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = other_list.head
        other_list.head.prev = current
        self.size += other_list.size

    def display(self):
        """نمایش لیست به صورت متوالی"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")



class LinkedListArray:
    """کلاس ساختمان داده آرایه با استفاده از لیست پیوندی"""
    def __init__(self):
        self.head = None  # اشاره‌گر به اولین گره
        self.size = 0     # اندازه آرایه

    def insert_at_end(self, data):
        """افزودن یک عنصر به انتهای آرایه"""
        new_node = Node(data)
        if not self.head:  # اگر آرایه خالی است
            self.head = new_node
        else:
            current = self.head
            while current.next:  # حرکت به انتهای لیست
                current = current.next
            current.next = new_node
        self.size += 1

    def insert_at_index(self, data, index):
        """افزودن یک عنصر در یک موقعیت مشخص"""
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_node = Node(data)
        if index == 0:  # افزودن در ابتدای آرایه
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):  # حرکت به موقعیت قبل از موقعیت مورد نظر
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def remove_at_index(self, index):
        """حذف یک عنصر از یک موقعیت مشخص"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:  # حذف از ابتدای آرایه
            data = self.head.data
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):  # حرکت به موقعیت قبل از موقعیت مورد نظر
                current = current.next
            data = current.next.data
            current.next = current.next.next
        self.size -= 1
        return data

    def get_at_index(self, index):
        """دسترسی به مقدار یک عنصر در موقعیت مشخص"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):  # حرکت به موقعیت مورد نظر
            current = current.next
        return current.data

    def update_at_index(self, data, index):
        """به‌روزرسانی مقدار یک عنصر در موقعیت مشخص"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):  # حرکت به موقعیت مورد نظر
            current = current.next
        current.data = data

    def size_of_array(self):
        """بازگرداندن اندازه آرایه"""
        return self.size

    def display(self):
        """نمایش مقادیر آرایه"""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class LinkedListQueue:
    """کلاس صف با استفاده از لیست پیوندی"""
    def __init__(self):
        self.front = None  # اشاره‌گر به ابتدای صف
        self.rear = None   # اشاره‌گر به انتهای صف
        self.size = 0      # اندازه صف

    def enqueue(self, data):
        """افزودن عنصر به انتهای صف"""
        new_node = Node(data)
        if not self.rear:  # اگر صف خالی است
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node  # اتصال گره جدید به انتهای صف
            self.rear = new_node       # به‌روزرسانی اشاره‌گر انتها
        self.size += 1

    def dequeue(self):
        """حذف عنصر از ابتدای صف و بازگرداندن مقدار آن"""
        if not self.front:  # اگر صف خالی است
            raise Exception("Queue is empty")
        data = self.front.data
        self.front = self.front.next  # به‌روزرسانی اشاره‌گر ابتدای صف
        if not self.front:  # اگر صف خالی شد
            self.rear = None
        self.size -= 1
        return data

    def peek(self):
        """مشاهده مقدار ابتدای صف بدون حذف آن"""
        if not self.front:  # اگر صف خالی است
            raise Exception("Queue is empty")
        return self.front.data

    def is_empty(self):
        """بررسی خالی بودن صف"""
        return self.size == 0

    def size_of_queue(self):
        """بازگرداندن اندازه صف"""
        return self.size

    def display(self):
        """نمایش مقادیر صف"""
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


class LinkedListStack:
    """کلاس پشته با استفاده از لیست پیوندی"""
    def __init__(self):
        self.top = None  # اشاره‌گر به بالای پشته
        self.size = 0    # اندازه پشته

    def push(self, data):
        """افزودن عنصر به بالای پشته"""
        new_node = Node(data)
        new_node.next = self.top  # گره جدید به گره بالای فعلی اشاره می‌کند
        self.top = new_node       # گره جدید بالای پشته می‌شود
        self.size += 1

    def pop(self):
        """حذف عنصر از بالای پشته و بازگرداندن مقدار آن"""
        if self.is_empty():  # بررسی خالی بودن پشته
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next  # به‌روزرسانی اشاره‌گر به گره بعدی
        self.size -= 1
        return data

    def peek(self):
        """مشاهده مقدار بالای پشته بدون حذف آن"""
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data

    def is_empty(self):
        """بررسی خالی بودن پشته"""
        return self.top is None

    def size_of_stack(self):
        """بازگرداندن اندازه پشته"""
        return self.size

    def display(self):
        """نمایش مقادیر پشته"""
        current = self.top
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
