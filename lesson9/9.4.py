# -*- coding: utf-8 -*-

class Node:
    """Klasa reprezentująca węzeł listy jednokierunkowej."""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)   # bardzo ogólnie


class SingleList:
    """Klasa reprezentująca całą listę jednokierunkową."""

    def __init__(self, *arguments):
        self.length = 0         # nie trzeba obliczać za każdym razem
        self.head = None
        self.tail = None
        for item in arguments:
            self.insert_head(item)

    def is_empty(self):
        return self.length == 0

    def count(self):      # tworzymy interfejs do odczytu
        return self.length

    def insert_head(self, data):    # algorytm klasy O(1)
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            node.next = self.head
            self.head = node
        self.length = self.length + 1

    def insert_tail(self, data):    # algorytm klasy O(1)
        node = Node(data)
        if self.length == 0:
            self.head = self.tail = node
        else:                   # dajemy na koniec listy
            self.tail.next = node
            self.tail = node
        self.length = self.length + 1

    def remove_head(self):          # algorytm klasy O(1)
        if self.length == 0:
            raise Exception("pusta lista")
        node = self.head
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:   # zabezpieczenie
            self.tail = None
        return node.data
    
    def reverse(self):
        if self.length == 0:
            raise Exception("pusta lista")
        prev = None
        current = self.head
        self.tail = current
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    	    
	    	


# Zastosowanie.
alist = SingleList()
alist.insert_head(11)         # [11]
alist.insert_head(22)         # [22, 11]
alist.insert_tail(33)         # [22, 11, 33]
#alist.reverse()
print "tail ",alist.tail.data
print "head ",alist.head.data
print "reverse:"
alist.reverse()
print "tail ",alist.tail.data
print "head ",alist.head.data


print "length", alist.length  # odczyt atrybutu
print "length", alist.count() # wykorzystujemy interfejs, lepsze
while not alist.is_empty():   # kolejność 22, 11, 33
    print "remove head", alist.remove_head()
