

def sum_seq(sequence):
    suma = 0
    for element in sequence:
        if isinstance(element, (list, tuple)):
            suma += sum_seq(element)
        else:
            suma += element
    return suma

seq = [1, 2, 3, [2, 4], (1, 4, 5, [1, 1, 1])]
print(sum_seq(seq))