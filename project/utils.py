"""
This module contains utility functions for the wiki_path_finder.py program. To generate HTML documentation for this module issue the
command:

    pydoc -w utils

"""


import requests
import sys
from queue import *

import tkinter
import webbrowser
import time

class Node():
    """
    Node wraps the title of the wikipedia page adding parameters and functions for creating and searching graphs
    """
    def __init__(self, name="", color="white",dist=sys.maxsize, parent=None):
        """
        Constructs a new object of type Node.

        :param name: The name of Node
        :param color: The color of Node
        :param dist: The distance from root
        :param parent: The parent of the Node
        :return: returns nothing
        """
        self.name = name
        self.color = color
        self.dist = dist
        self.parent = parent
        self.adjacent = []
        self.pageid = None

    def addAdjacentList(self, list):
        """
        Adds new elements two the objects adjacent list

        :param list: list object with Node neighbours
        :return: returns nothing
        """
        self.adjacent += list


def query(request):
    """
    creates a query and sends it to the Wikipedia API using the requests module. Yields the results from the Wikipedia API

    :param request: A string request to the Wikipedia API
    :return: the result from the Wikipedia API
    """
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
    """
    searches json/dictionary for a key

    :param needles: the key
    :param haystack: the json or dictionary
    :return: the value for the given key
    """
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

def callback(event):
    """
    creates a link to the wikipedia page with the passed pageid

    :param event:
    :return: creates a link to the url
    """
    webbrowser.open_new(r"https://pl.wikipedia.org/?curid="+event.widget.cget("text"))

def Gui_Print_Path(endNode,frame,end_time, request_time):
    """
    creates gui elements based on the path to the endNode

    :param endNode: the searched node
    :param frame: the parent gui element
    :param end_time: the time taken to search for a path
    :param request_time: the time taken for the Wikipedia API to return results
    :return: returns nothing
    """
    print("printing gui")
    Parent = endNode.parent
    L = []
    while (Parent != None):
        L.append(Parent)
        Parent = Parent.parent
    L.reverse()
    i = 0
    for item in range(len(L)):
        node = tkinter.LabelFrame(frame, bg="green" if L[item].dist==0 else "yellow", width=30)
        #node.grid_columnconfigure(0, weight=1, uniform="fred")
        node.grid(row=2, column=i)

        label1 = tkinter.Label(node, text=L[item].name, bg="green" if L[item].dist==0 else "yellow")
        label1.pack()

        label2 = tkinter.Label(node, text=str(L[item].pageid), cursor="hand2", bg="green" if L[item].dist==0 else "yellow")
        label2.pack()
        label2.bind("<Button-1>", callback)

        label3 = tkinter.Label(frame, text="--▶")
        label3.grid(row=2, column=i+1)

        i += 2

    node = tkinter.LabelFrame(frame,bg="red", width=30)
    #node.grid_columnconfigure(0, weight=1, uniform="fred")
    node.grid(row=2, column=i)

    label1 = tkinter.Label(node, text=endNode.name, bg="red")
    label1.pack()

    label2 = tkinter.Label(node, text=str(endNode.pageid), cursor="hand2", bg="red")
    label2.bind("<Button-1>", callback)
    label2.pack()

    L3 = tkinter.Label(frame, text="")
    L3.grid(row=3, column=0)

    node1 = tkinter.LabelFrame(frame, width=30)
    #node1.grid_columnconfigure(0, weight=1, uniform="fred")
    node1.grid(row=4, column=0)
    label = tkinter.Label(node1, text="Distance from start: " + str(endNode.dist))
    label.pack()

    node1 = tkinter.LabelFrame(frame, width=30)
    #node1.grid_columnconfigure(0, weight=1, uniform="fred")
    node1.grid(row=4, column=1)
    label = tkinter.Label(node1, text="Total time: " + str(round(end_time,5))+"s")
    label.pack()

    node1 = tkinter.LabelFrame(frame, width=30)
    #node1.grid_columnconfigure(0, weight=1, uniform="fred")
    node1.grid(row=4, column=2)
    label = tkinter.Label(node1, text="Wiki request time: " + str(round(request_time,5))+"s")
    label.pack()



def Print_Path(endNode):
    """
    prints the path in the console

    :param endNode: the searched node
    :return: returns nothing
    """
    Parent=endNode.parent
    L = []
    while(Parent != None):
        L.append(Parent.name)
        Parent = Parent.parent
    L.reverse()
    for item in range(len(L)):
        print(L[item],"-> ",end="")
    print(endNode.name,endNode.pageid)
    print("Distance from start: "+str(endNode.dist))