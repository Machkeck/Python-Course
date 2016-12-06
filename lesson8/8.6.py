# -*- coding: utf-8 -*-
"""
8.6
Za pomocą techniki programowania dynamicznego napisać program obliczający wartości funkcji P(i, j). Porównać z wersją rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową (np. słownik) do przechowywania wartości funkcji. Wartości w tablicy wypełniać kolejno wierszami.

P(0, 0) = 0.5,
P(i, 0) = 0.0 dla i > 0,
P(0, j) = 1.0 dla j > 0,
P(i, j) = 0.5 * (P(i-1, j) + P(i, j-1)) dla i > 0, j > 0.

"""
from time import clock

#Wersja dynamiczna
P = {(0, 0): 0.5, (0, 1): 1.0, (1, 0): 0.0}

def Pd(i, j):
    if i < 0 or j < 0:
        raise ValueError("Błąd: i<0 lub j<0")
    else:
        if i == 0:
            return 1.0
        elif j == 0:
            return 0.0
        else:
            p = P.get((i, j))
            if p != None:
                return p
            else:
                p = 0.5*(Pd(i-1, j)+Pd(i, j-1))
                P[(i, j)] = p
                return p

#Wersja rekurencyjna

def Pr(i, j):
    if i < 0 or j < 0:
        raise ValueError("Błąd: i<0 lub j<0")
    else:
        if i == 0 and j == 0:
            return 0.5
        elif i == 0:
            return 1.0
        elif j == 0:
            return 0.0
        else:
            return 0.5*(Pr(i-1, j)+Pr(i, j-1))



def compare(x, y):
    start = clock()
    valuePr = Pr(x, y)
    stopPr = clock() - start
    start = clock()
    valuePd = Pd(x, y)
    stopPd = clock() - start

    print("Rekurencyjnie: P("+str(x)+", "+str(y)+") = "+str(valuePr)+" Czas: %e" % stopPr)
    print("Dynamicznie: P("+str(x)+", "+str(y)+") = "+str(valuePd)+" Czas: %e" % stopPd )
    if stopPr > stopPd:
        print("Metoda dynamiczna była szybsza")
    elif stopPr < stopPd:
        print("Metoda rekurencyjna była szybsza")
    else:
        print("Obie metody zostały wykonane w takim samym czasie")
    print()

compare(5,6)
compare(8,5)
compare(3,3)
compare(1,1)
compare(88,33)

#Wniosek: wersja dynamiczna jest bardziej optymalna niz wersja rekurencyjna
