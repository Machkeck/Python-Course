

#iteracyjnie
def odwracanie(L,left, right):
    if left >= right:
        return None
    else:
        L[left:right+1] = L[left:right+1][::-1]

print("iteracyjnie")
L = [1, 34, 5, 6, 78, 9, 76, 45, 4, 123, 21]
print(L)
odwracanie(L,2,4)
print(L)

#rekurencyjnie
def odwracanie(L, left, right):
    if left >= right:
        return None
    else:
        L[left], L[right] = L[right], L[left]
        if left+1 != right-1:
            odwracanie(L, left+1, right-1)

print("rekurencyjnie")
L = [1, 34, 5, 6, 78, 9, 76, 45, 4, 123, 21]
print(L)
odwracanie(L, 2, 4)
print(L)

