import fractions

class Frac:
    """Klasa reprezentujaca ulamek."""

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Time({},{})".format(self.x, self.y)

    def __add__(self, other):   # frac1 + frac2
        M = self.y * other.y
        L = self.x * other.y + other.x * self.y
        gcd = fractions.gcd(L, M)
        frac3 = Frac(L / gcd, M / gcd)
        return frac3
    def __sub__(self, other):  # frac1 - frac2
        return self+(-other)

    def __mul__(self, other):  # frac1 * frac2
        a = self.x * other.x
        b = self.y * other.y
        gcd = fractions.gcd(a, b)
        a /= gcd
        b /= gcd
        return Frac(a,b)

    def __div__(self, other):  # frac1 / frac2
        return self*(~other)

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotnosc: ~frac
        return Frac(self.y, self.x)

    def __cmp__(self, other):  # cmp(frac1, frac2)
        cmp = self-other
        if cmp.x == 0:
            return 0
        if cmp.x > 0:
            return 1
        else:
            return -1

    def __float__(self):      # float(frac)
        return float(self.x)/float(self.y)

