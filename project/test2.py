import sys
from queue import *


class Node():
    def __init__(self, name="", color="white",dist=sys.maxsize, parent=None):
        self.name = name
        self.color = color
        self.dist = dist
        self.parent = parent
        self.adjacent = []
    def addAdjacentList(self, list):
        self.adjacent += list

def BFS(start, end):
    ListOfNames=[]
    Q = Queue()
    s = Node(start,'grey',0,None)
    ListOfNames.append(start)
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for result in query({'titles': u.name, 'prop': 'links', 'pllimit': '500'}):
            L = deep_search('links',result)
            u.addAdjacentList(L['links'])
        for item in u.adjacent:
            nname = deep_search('title',item)
            if nname not in ListOfNames:
                v = Node(nname,'grey',u.dist+1,u)
                Q.put(v)
                if nname==end:
                    print("way found")
                    break

        u.color = 'black'