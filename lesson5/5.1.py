#1
import rekurencja

print(rekurencja.factorial(6))
print(rekurencja.fibonacci(5))

#2
import importlib #for reloading in python 3.x
importlib.reload(rekurencja)

import rekurencja as rek

print(rek.factorial(6))
print(rek.fibonacci(5))

#3
from rekurencja import *

print(factorial(6))
print(fibonacci(5))

#4
from rekurencja import factorial
from rekurencja import fibonacci

print(factorial(6))
print(fibonacci(5))