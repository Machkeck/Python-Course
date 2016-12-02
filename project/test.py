import requests
import json
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


def query(request):
    request['action'] = 'query'
    request['format'] = 'json'
    lastContinue = {'continue': ''}
    while True:
        # Clone original request
        req = request.copy()
        # Modify it with the values returned in the 'continue' section of the last result.
        req.update(lastContinue)
        # Call API
        result = requests.get('http://pl.wikipedia.org/w/api.php', params=req).json()

        if 'error' in result:
            raise Error(result['error'])
        if 'warnings' in result:
            print(result['warnings'])
        if 'query' in result:
            yield result['query']
        if 'continue' not in result:
            break
        lastContinue = result['continue']

def deep_search(needles, haystack):
    found = {}
    if type(needles) != type([]):
        needles = [needles]

    if type(haystack) == type(dict()):
        for needle in needles:
            if needle in haystack.keys():
                found[needle] = haystack[needle]
            elif len(haystack.keys()) > 0:
                for key in haystack.keys():
                    result = deep_search(needle, haystack[key])
                    if result:
                        for k, v in result.items():
                            found[k] = v
    elif type(haystack) == type([]):
        for node in haystack:
            result = deep_search(needles, node)
            if result:
                for k, v in result.items():
                    found[k] = v
    return found

'''for result in query({'titles': 'Sebastian_Fabijański', 'prop': 'links', 'pllimit': '500'}):
    #print(result)
    L = deep_search('links', result)
    for item in L['links']:
        LI = deep_search('title',item)
        #print()
        for link in LI.values():
            #print(link)
            for next in query({'titles': link, 'prop': 'links', 'pllimit': '500'}):
                pass
                #print(next)
    print("--------------------------")
    #print(deep_search('links',result))'''

def Print_Path(endNode):
    Parent=endNode.parent
    L = []
    while(Parent != None):
        L.append(Parent.name)
        Parent = Parent.parent
    L.reverse()
    for item in range(len(L)):
        print(L[item],"-> ",end="")
    print(endNode.name)


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
            try:
                u.addAdjacentList(L['links'])
            except KeyError:
                print(L, u.name)
        for item in u.adjacent:
            nname = deep_search('title',item)['title']
            if nname not in ListOfNames:
                ListOfNames.append(nname)
                v = Node(nname,'grey',u.dist+1,u)
                Q.put(v)
                if nname==end:
                    print("way found")
                    print(nname)
                    Print_Path(v)
                    return True
                    break

        u.color = 'black'

def BFS1(start):
    ListOfNodes=[]
    Q = Queue()
    s = Node(start,'grey',0,None)
    ListOfNodes.append(s)

    for result in query({'titles': s.name, 'prop': 'links', 'pllimit': '500'}):
        L = deep_search('links',result)
        for item in L['links']:
            LI = deep_search('title',item)
            if LI['title'] == 'Warszawa':
                print("Way found")
                print(LI['title'])
                break

BFS('Harry Potter','Cho Chang')
#for result in query({'generator': 'allpages', 'prop': 'links', 'pllimit':'500'}):
    #print(_finditem(result,'title'))
    #print(result)
    #for key,value in result.items():

