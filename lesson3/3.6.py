
def drawBox(width, length):
    H=["+"]*(width+1)
    L=["|"]*(width+1)
    H="---".join(H)+"\n"
    L="   ".join(L)+"\n"
    box=""
    for i in range(length):
        box+=H
        box+=L

    box+=H
    return box

print(drawBox(2, 4))
