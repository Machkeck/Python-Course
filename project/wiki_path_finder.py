"""
This module contains the program for searching path from one Wikipedia page to another. Pages are connected via links. To generate HTML documentation for this module issue the
command:

    pydoc -w wiki_path_finder
"""
from utils import *



def BFS(start, end, frame=None):
    """
    Graph search algorithm similar to Broad-First-Search.
    The main difference is that the graph isn't created beforehand but dynamically with each Wikipedia API query.
    For safety the Wikipedia API restricts the number of queries per second as well as their size.
    Because of this the algorithm is greatly slowed down. Additionally the API might deny access entirely when to many queries are sent.


    :param start: the starting wikipedia page title
    :param end: the destination wikipedia page title
    :param frame: the parent gui element
    :return: returns True when the destination title is found
    """


    if frame != None:  # clear the previous path
        for label in frame.grid_slaves():
            if int(label.grid_info()["row"]) > 1:
                label.grid_forget()

    for result in query({'titles': start}):
        c1=len(deep_search("pageid", result))
    for result in query({'titles': end}):
        c2=len(deep_search("pageid", result))
    if (c1+c2) == 2:

        request_time = 0.0
        start_time = time.time()

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
                except KeyError:#in case of redlinks
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
    else:
        node1 = tkinter.LabelFrame(frame, width=30)
        # node1.grid_columnconfigure(0, weight=1, uniform="fred")
        node1.grid(row=4, column=0)
        label = tkinter.Label(node1, text="Incorrect page title: "+("start " if c1==0 else "")+("destination" if c2==0 else ""))
        label.pack()

def Run_Gui():
    """
    Runs the GUI application
    :return: nothing
    """
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

#program start
Run_Gui()

#command line queries without gui
#BFS('Harry Potter','Cho Chang')
#BFS('Kubuś Puchatek','Adolf Hitler')