# -*- coding: utf-8 -*-
"""
8.3
Obliczyć liczbę pi za pomocą algorytmu Monte Carlo. Wykorzystać losowanie punktów z kwadratu z wpisanym kołem. Sprawdzić zależność dokładności wyniku od liczby losowań. Wskazówka: Skorzystać z modułu random.

"""

import random

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""

    w_kole = 0

    for i in range(n):
        x = float(random.random()) / 1.0 * 2 - 1
        y = float(random.random()) / 1.0 * 2 - 1
        if x*x + y*y <= 1: #sprawdzam czy wylosowany punkt znajduje wewnatrz okręgu o promeniu równym 1
            w_kole += 1

    return 4.0 * w_kole / n

print(str(calc_pi(100)).ljust(9,' ')," dla n = ", 100)
print(str(calc_pi(1000)).ljust(9,' ')," dla n = ", 1000)
print(str(calc_pi(10000)).ljust(9,' ')," dla n = ", 10000)
print(str(calc_pi(100000)).ljust(9,' ')," dla n = ", 100000)
print(str(calc_pi(1000000)).ljust(9,' ')," dla n = ", 1000000)
print(str(calc_pi(10000000)).ljust(9,' ')," dla n = ", 10000000)
