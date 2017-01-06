import requests
import sys
from queue import *

import tkinter
import webbrowser
import time


def hello():
    tkinter.messagebox.showinfo("Say Hello", "Hello World")

class Node():
    def __init__(self, name="", color="white",dist=sys.maxsize, parent=None):
        self.name = name
        self.color = color
        self.dist = dist
        self.parent = parent
        self.adjacent = []
        self.pageid = None

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


def callback(event):
    webbrowser.open_new(r"https://pl.wikipedia.org/?curid="+event.widget.cget("text"))

def Gui_Print_Path(endNode,frame,end_time, request_time):
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


def BFS(start, end, frame=None):
    request_time = 0.0
    start_time = time.time()
    if frame!= None:
        for label in frame.grid_slaves():
            if int(label.grid_info()["row"]) > 1:
                label.grid_forget()
    ListOfNames=[]
    Q = Queue()
    s = Node(start,'grey',0,None)
    ListOfNames.append(start)
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        t1 = time.time()
        for result in query({'titles': u.name, 'prop': 'links', 'pllimit': '500'}):
            request_time += time.time()-t1
            L = deep_search('links',result)
            #print(L)

            try:
                u.pageid = deep_search("pageid", result)['pageid']
                u.addAdjacentList(L['links'])
            except KeyError:
                print(L, u.name)
            t1 = time.time()
        for item in u.adjacent:
            nname = deep_search('title',item)['title']
            #print(nname)
            if nname not in ListOfNames:
                ListOfNames.append(nname)
                v = Node(nname,'grey',u.dist+1,u)
                Q.put(v)
                if nname==end:
                    print("way found")
                    print(nname)
                    t1=time.time()
                    for result in query({'titles': nname}):
                        request_time+=time.time()-t1
                        v.pageid = deep_search("pageid", result)['pageid']
                    end_time = time.time() - start_time
                    if(frame==None):
                        Print_Path(v)
                        print(end_time,request_time)
                    else:
                        Gui_Print_Path(v,frame, end_time, request_time)
                    return True

        u.color = 'black'

def Run_Gui():
    top = tkinter.Tk()

    L1 = tkinter.Label(top, text="Start")
    L1.grid(row=0,column=0)
    E1 = tkinter.Entry(top, bd =5)
    E1.grid(row=0,column=1)

    L2 = tkinter.Label(top, text="Destination")
    L2.grid(row=0,column=2)
    E2 = tkinter.Entry(top, bd =5)
    E2.grid(row=0,column=3)

    B1 = tkinter.Button(top, text = "Search for Paths", command=lambda: BFS(start=E1.get(),end=E2.get(),frame=top))
    B1.grid(row=0,column=4)
    L3 = tkinter.Label(top, text="")
    L3.grid(row=1,column=0)

    top.mainloop()

#Run_Gui()
#BFS('Harry Potter','Cho Chang')
BFS('Kubuś Puchatek','Adolf Hitler')
