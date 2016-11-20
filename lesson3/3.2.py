L = L.sort() #odnoszenie sie do nie przypisanej zmiennej
x, y = 1, 2, 3 #zbyt wiele wartosci do przypisania
X = 1, 2, 3 ; X[1] = 4 #Nie mozna zmieniac wartosc dla danej krotki
X = [1, 2, 3] ; X[3] = 4 #Pozycje w liscie indeksowane sa od zera wiec X[3] odwoluje sie do pola poza rozmiarem listy
X = "abc" ; X.append("d") #Wartosci string'a w Python nie mozna zmiennac stad tez nie istnieje funkcja .append() dla takiego obiektu
map(pow, range(8))#funkcja pow() przyjmuje 2 argumenty a tu podany jest tylko jeden.
