class Queue:

    def __init__(self, size):
        self.items = []
        self.size = size

    def __str__(self):             # podglądanie kolejki
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):             # nigdy nie jest pusta
        if len(self.items) == self.size:
            return True
        else:
            return False

    def put(self, data):
        if self.is_full():
            raise ValueError("Kolejka jest pełna")
        else:
            self.items.append(data)

    def get(self):
        if self.is_empty():
            raise ValueError("Kolejka jest pusta")
        else:
            return self.items.pop(0)

'''q1 = Queue(3)
q1.put(23)
q1.put(2)
q1.put(112)
print(q1.get())
print(q1.get())
print(q1.get())
print(q1.get())'''
