# -*- coding: utf-8 -*-
import queue

class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

    def insert(self, data):
        if self.data < data:      # na prawo
            if self.right:
                self.right.insert(data)
            else:
                self.right = Node(data)
        elif self.data > data:    # na lewo
            if self.left:
                self.left.insert(data)
            else:
                self.left = Node(data)
        else:
            pass    # ignoruję duplikaty

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return True
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return False

def count_leafs(top):
    if top == None:
        return 0
    elif top.left == None and top.right == None:
        return 1
    else:
        return count_leafs(top.left) + count_leafs(top.right)
        

def count_total(top):
    if top is None:
        return 0
    sum = 0
    aqueue = queue.Queue()
    aqueue.put(top)
    while not aqueue.empty():
        node = aqueue.get()
        sum += node.data
        if node.left:
            aqueue.put(node.left)
        if node.right:
            aqueue.put(node.right)
    return sum

root = Node(30)
root.insert(15)
root.insert(20)
root.insert(50)
root.insert(31)
root.insert(23)
root.insert(10)
"""
        30
       /   \
     15     50
    /  \   /
   10  20  31
        \
         23
"""

print(count_leafs(root))
print(count_total(root))
