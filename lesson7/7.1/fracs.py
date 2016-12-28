import fractions

class Frac:
    """Klasa reprezentujaca ulamek."""

    def __init__(self, x=0, y=1):
        if (isinstance(x,int) or isinstance(x,float) or isinstance(x,long)) and (isinstance(y,int)or isinstance(y,float)or isinstance(y,long)):
            if x%1 == 0 and y%1 == 0:
                if y == 0:
                    raise ValueError("zero denominator")
                self.x = int(x)
                self.y = int(y)
            elif x%1 != 0 and y%1==0:

                parts = x.as_integer_ratio()
                self.x = int(parts[0])
                self.y = int(int(parts[1])*y)

            elif x%1 == 0 and y%1 != 0:
                parts = y.as_integer_ratio()
                self.x = int(int(parts[1])*x)
                self.y = int(parts[0])

            elif x%1 != 0 and y%1 != 0:
                partsl = x.as_integer_ratio()
                a = int(partsl[0])
                b = int(partsl[1])
                partsm = y.as_integer_ratio()
                c = int(partsm[0])
                d = int(partsm[1])
                self.x = a * d
                self.y = b * c

            elif isinstance(x, int):
                self.x = x
                self.y = 1

            gcd = fractions.gcd(self.x, self.y)
            self.x /= gcd
            self.y /= gcd

        else:
            raise ValueError("Cannot recognize arguments")


    def __str__(self):         # zwraca "x/y" lub "x" dla y=1
        if self.y == 1:
            return str(self.x)
        else:
            return "{}/{}".format(self.x, self.y)

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Time({},{})".format(self.x, self.y)

    def __add__(self, other):   # frac1 + frac2, frac+int
        other = self.toFrac(other)
        M = self.y * other.y
        L = self.x * other.y + other.x * self.y
        frac3 = Frac(L, M)
        return frac3

    __radd__ = __add__  # int+frac

    def __sub__(self, other):  # frac1 - frac2, frac-int
        other = self.toFrac(other)
        return self+(-other)

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        other = self.toFrac(other)
        return other-self

    def __mul__(self, other):  # frac1 * frac2
        other = self.toFrac(other)
        a = self.x * other.x
        b = self.y * other.y
        return Frac(a,b)

    __rmul__ = __mul__  # int*frac

    def __div__(self, other):  # frac1 / frac2
        other = self.toFrac(other)
        return self*(~other)

    def __rdiv__(self, other):  # int/frac
        other = self.toFrac(other)
        return other/self

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

    def toFrac(self, s):
        if isinstance(s,Frac):
            return s
        elif isinstance(s, int) or isinstance(s, float):
            return Frac(s)
        else:
            raise ValueError("Invalid argument")
'''n = 2.4
parts = n.as_integer_ratio()
x = int(parts[0])
y = int(parts[1])
print(x,y)

f1 = Frac(2.0,4.4)
f2 = Frac(3,2)
print(f1)
print(f1*f2)'''