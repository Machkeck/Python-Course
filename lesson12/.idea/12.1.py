#wyszukiwanie liniowe

from random import randint

def linear_search(L, left, right, y):
    """Wyszukiwanie liniowe w ciągu."""
    i = left
    while i <= right:
        if y == L[i]:
            return i
        i = i + 1
    return None

def create_list(n, k):
    L=[]
    for i in range(n):
        L.append(randint(0,k-1))
    return L

def find_all(n, k):
    F=[]
    L=create_list(n, k)
    y = randint(0,k-1)
    #L=[0,0,0,0,0,0,0,0,0,0]
    #y=1
    print("y = "+str(y)+" L = "+str(L))
    i=0
    while i != len(L):
        item = linear_search(L,i,len(L)-1,y)
        if item != None:
            F.append(item)
            i=item+1
        else:
            i+=1
    if len(F)!=0:
        return "List of indexes: "+str(F)
    else:
        return "No occurences found"

print(find_all(10,2))



