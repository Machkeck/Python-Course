# -*- coding: utf-8 -*-

import random
"""
Kolejka losowa zaimplementowana w postaci tablicy dwukierunkowej.
Dodatkowo kazdy wezel Kolejki jest zapamietywany w slowniku pos_map.
Pole current gwarantuje to ze przy wstawianiu wezla do kolejki funkcją put(),
wezel otrzyma unikalny klucz do slownika.
W funkcji remove() losujemy klucz ze slownika i usuwamy ten klucz ze slownika. Nastepnie w zaleznosci od tego czy
wylosowany wezel jest poczatkiem, koncem, jedynym elementem kolejki czy elementem posrodku,
odpowiednio przestawiane sa referencje w sasiednich wezlach. Ostatecznie zwracana jest wartosc wylosowanego węzła
Rozwiazanie to wymaga wiecej pamieci bo wykorzystywany jest dodatkowy slownik, jednak w żadnej funkcji nie pojawia się
potrzeba iteracji po wszystkich węzłach kolejki.
Miejscem, które może spowolnić działanie programu, gdy operujemy na wiekszej ilosci danych, jest linijka:
-----node_key = random.choice(self.pos_map.keys())-----,gdzie losujemy klucz ze slownika. Gdyby zastapic zwykły
słownik słownikiem z biblioteki 'randomdict' (https://github.com/robtandy/randomdict) można by wylosować klucz w stałym czasie.

"""
class Node:

    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.data)

class RandomQueue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.pos_map = {}
        self.size = 0
        self.current = 1

    def is_empty(self):
        return not self.head

    def put(self, data):
        node = Node(data)
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self.size += 1
        self.pos_map[self.current] = node
        self.current += 1


    def remove(self):                  # zwraca losowy element
        if any(self.pos_map):
            node_key = random.choice(self.pos_map.keys())
            node = self.pos_map[node_key]
            del self.pos_map[node_key]
            if node.next == None and node.prev == None:#single
                self.size -= 1
                self.head = None
                self.tail = None
                return node.data
            if node.next == None and node.prev != None:#tail
                p = node.prev
                p.next = None
                self.tail = p
                self.size -= 1
                return node.data
            if node.next != None and node.prev == None:#head
                n = node.next
                n.prev = None
                self.head = n
                self.size -= 1
                return node.data
            if node.next != None and node.prev != None:
                p = node.prev
                n = node.next
                p.next = n
                n.prev = p
                self.size -= 1
                return node.data
        else:
            return None

    def is_full(self):
        return False

q1 = RandomQueue()
for i in range(10):
    q1.put(i)
for i in range(9):
    print(q1.remove())
    print("Head",q1.head.data,"Tail",q1.tail.data)
    print("")

'''print("H",q1.head.data)
q1.put(352)
print("T",q1.tail.data)
q1.put(89)
print("T",q1.tail.data)
q1.put(3)
print("T",q1.tail.data)
q1.put(845)
print("H",q1.head.data)

print (q1.remove())
print (q1.remove())
print (q1.remove())
print (q1.remove())'''

