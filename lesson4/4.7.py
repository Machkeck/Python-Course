
def flatten(seq):
    L = []
    for element in seq:
        if isinstance(element,(list,tuple)):
            L.extend(flatten(element))
        else:
            L.append(element)
    return L

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
