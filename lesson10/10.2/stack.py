# -*- coding: utf-8 -*-

class Stack:

    def __init__(self, size):
        #self.items = size * [None]  # utworzenie tablicy
        self.items = []
        self.size = size

    def __str__(self):                  # podglądamy stos
        return str(self.items)

    def is_empty(self):
        return not self.items

    def is_full(self):                  #
        if len(self.items) == self.size:
            return True
        else:
            return False


    def push(self, item):
        if self.is_full():
            raise ValueError("Stos jest pełny")
        else:
            self.items.append(item)         # dodajemy na koniec

    def pop(self):                      # zwraca element
        if self.is_empty():
            raise ValueError("Stos jest pusty")
        else:
            return self.items.pop()         # zabieram od końca

'''s1 = Stack(2)
s1.push(5)
s1.push(45)
print(s1.pop())
print(s1.pop())'''
