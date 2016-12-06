# -*- coding: utf-8 -*-

"""
8.4
Zaimplementować algorytm obliczający pole powierzchni trójkąta, jeżeli dane są trzy liczby będące długościami jego boków. Jeżeli podane liczby nie spełniają warunku trójkąta, to program ma generować wyjątek ValueError.

"""

from math import sqrt

def checkTriangle(a, b ,c):
    if a + b <= c or a + c <= b or b + c <= a:
        return False
    else:
        return True

def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if checkTriangle(a, b, c):
        p = 0.5*(a + b + c)
        return sqrt(p*(p-a)*(p-b)*(p-c))
    else:
        raise ValueError("Niespełniona nierówność trójkąta")

print("Obliczanie pola powierzchni trojkata na podstawie jego bokow")
print("Podaj bok a: ")
a = float(input())
print("Podaj bok b: ")
b = float(input())
print("Podaj bok c: ")
c = float(input())

try:
    print("Pole wynosi: "+str(heron(a,b,c)))
except ValueError as e:
    print(e)
