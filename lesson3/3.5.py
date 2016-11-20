
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
