class ArrayOperations:
    def __init__(self):
        self.array = []


    def insert(self, index, value):
        if 0 <= index <= len(self.array):
            self.array.insert(index, value)
            print(f"Inserted {value} at index {index}")
        else:
            print("Invalid index")


    def delete_by_value(self, value):
        if value in self.array:
            index = self.array.index(value)
            self.array.remove(value)
            print(f"Deleted value {value} at index {index}")
            return index
        else:
            print(f"Value {value} not found")
            return -1


    def delete_by_index(self, index):
        if 0 <= index < len(self.array):
            value = self.array.pop(index)
            print(f"Deleted value {value} at index {index}")
        else:
            print("Invalid index")


    def display(self):
        print("Array:", self.array)

    def append(self, value):
        self.array.append(value)
        print(f"Appended {value} to the array")


    def reverse(self):
        self.array = self.array[::-1]
        print("Array reversed")


    def search_by_value(self, value):
        if value in self.array:
            index = self.array.index(value)
            print(f"Value {value} found at index {index}")
            return index
        else:
            print(f"Value {value} not found")
            return -1