x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;    
#ok, znak ';' mozna stosowac aby w jednej linijce podac wiele instrukcji ale ';' na koncu wiersza jest zbedny.

for i in "qwerty": if ord(i) < 100: print i
#nie mozna podac tak rozbudowanego polecenia w jednej linijce(2 wciecia)

for i in "axby": print ord(i) if ord(i) < 100 else i
#ok, wyrazenie sklada sie z petli for oraz wyrazenia trojargumentowego(1 wziecie)
