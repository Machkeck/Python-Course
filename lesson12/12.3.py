#mediana

from random import randint

def create_list(n, k):
    L=[]
    for i in range(n):
        L.append(randint(0,k-1))
    return L

def mediana_sort(L, left=0, right=0):
    M = sorted(L)
    #print("M="+str(M))
    length = len(L)
    if left < 0:
        left = 0
    if right > length:
        right = length-1
    if right < left:
        raise ValueError("left index greater than right index")

    if ((right-left)+1) %2 == 0:
        return (M[int(((right-left)-1)/2)+left],M[int(((right-left)-1)/2+1)+left])
    else:
        return M[int((right-left)/2)+left]

L = create_list(10,100)
print("L = "+str(L))
print("L sorted = "+str(sorted(L)))
print("Mediana[0,9] = "+str(mediana_sort(L,0,len(L)-1)))
print("Mediana[0,2] = "+str(mediana_sort(L,0,2)))
print("Mediana[2,3] = "+str(mediana_sort(L,2,3)))
print("Mediana[2,4] = "+str(mediana_sort(L,2,4)))
print("Mediana[2,29] = "+str(mediana_sort(L,2,29)))
print("Mediana[-1,19] = "+str(mediana_sort(L,-1,19)))
try:
    print("Mediana[-1,19] = " + str(mediana_sort(L, 3, 2)))
except ValueError:
    print("left index greater than right index")

print("")

L = create_list(9,100)
print("L = "+str(L))
print("L sorted = "+str(sorted(L)))
print("Mediana[0,9] = "+str(mediana_sort(L,0,len(L)-1)))

#L = [3,25,4,2]
#M = sorted(L)
#print(L)
#print(M)
#print(mediana_sort(L,0,len(L)-1))