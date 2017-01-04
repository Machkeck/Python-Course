#mediana

from random import randint

def create_list(n, k):
    L=[]
    for i in range(n):
        L.append(randint(0,k-1))
    return L

def mediana_sort(L, left=0, right=0):
    M = sorted(L)
    length = len(L)
    if length %2 == 0:
        return (M[int((length-1)/2)],M[int((length-1)/2+1)])
    else:
        return M[int((length)/2)]

L = create_list(10,100)
print("L = "+str(L))
print("Mediana = "+str(mediana_sort(L)))
L = create_list(9,100)
print("L = "+str(L))
print("Mediana = "+str(mediana_sort(L)))

#L = [3,25,4,2]
#M = sorted(L)
#print(L)
#print(M)
#print(mediana_sort(L,0,len(L)-1))