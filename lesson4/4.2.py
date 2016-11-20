#3.5 and 3.6 using functions


def measure(length):
    if length > 99999:
        print("length is to long")
        return None
    else:
        cm = "|...."
        ruler = ""
        for i in range(length):
            ruler+=cm
        ruler+="|"
        ruler+="\n"
        ruler += "0"
        for i in range(1, length+1):
            ruler += "{0:5d}".format(i)

        return ruler

print(measure(5))
print(measure(15))


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
