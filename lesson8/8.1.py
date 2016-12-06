# -*- coding: utf-8 -*-
'''
8.1:
Zbadać problem szukania rozwiązań równania liniowego postaci a * x + b * y + c = 0. Podać specyfikację problemu. Podać algorytm rozwiązania w postaci listy kroków, schematu blokowego, drzewa. Podać implementację algorytmu w Pythonie w postaci funkcji solve1(), która rozwiązania wypisuje w formie komunikatów.

Specyfikacja problemu:
Gdy szukamy rozwiązań równania liniowego postaci a*x+b*y+c=0 możemy natrafić na 5 przypadków:
1)  Wszystkie współczynniki wynoszą zero
    Równanie jest nieokreślone. Rozwiązanie xeR i yeR.
2)  a=0 i b=0 i c!=0
    Równanie sprzeczne. Rozwiązanie xe(zbiór pusty), ye(zbiór pusty)
3)  a = 0 i b!=0
    Równanie prowadzi do postaci b*y=-c.
    Rozwiązaniem jest xeR i y=-c/b
4)  b=0 i a!=0
    Równanie prowadzi do postaci a*x=-c.
    Rozwiązaniem jest x=-c/a i yeR
5)  a!=0 i b!=0
    Przekształcając otrzymujemy y=(-c-a*x)/b
    Rozwiązaniem jest prosta y=(-c-a*x)/b, czyli zbiór punktów o wzorze (y, (-c-a*x)/b)

Lista Kroków:
1)  wczytaj a,b,c
2)  jeśli a = 0 i b = 0:
    2.1 jeśli c = 0
        2.1.a   Wypisz:"Równanie jest nieokreślone. Rozwiązanie xeR i yeR"
        2.1.b   Przejdz do pkt. 6
    2.2 else
        2.2.a   Wypisz:"Równanie jest sprzeczne. Rozwiązanie xe(zbiór pusty),ye(zbiór pusty)"
        2.2.b   Przejdz do pkt. 6
3)  jeśli a = 0
    3.1 Wypisz: "Rozwiązaniem jest prosta: xeR i y=-c/b"
    3.2 Przejdz do pkt. 6
4)  jeśli b = 0
    4.1 Wypisz: "Rozwiązaniem jest prosta: x = -c/a i yeR"
    4.2 Przejdz do pkt. 6
5)  wypisz: "Rozwiązaniem jest prosta y=(-c-a*x)/b, zbiór punktów o wzorze (y, (-c-a*x)/b)"
6)  koniec
'''


def solve1(a, b, c):

    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0 and b == 0:
        if c == 0:
            print("Równanie jest nieokreślone. Rozwiązanie xeR i yeR")
            return
        else:
            print("Równanie jest sprzeczne. Rozwiązanie xe(zbiór pusty),ye(zbiór pusty)")
            return
    if a == 0:
        print("Rozwiązaniem jest prosta: xeR i y = "+str(-float(c)/float(b)))
        return
    if b == 0:
        print("Rozwiązaniem jest prosta: x = "+str(-float(c)/float(a))+" i yeR")
    solution = str(float(-c)/float(b))+"+("+str(float(-a)/float(b))+")x"
    print("Rozwiązaniem jest prosta y = "+solution+", zbiór punktów o wzorze (y, "+solution+")")

print("Rozwiązywanie równania liniowego postaci a x + b y + c = 0.")
try:
    print("Podaj a: ")
    a = float(input())
    print("Podaj b: ")
    b = float(input())
    print("Podaj c: ")
    c = float(input())
    solve1(a ,b ,c)
except ValueError:
    print("Zły typ wartości")