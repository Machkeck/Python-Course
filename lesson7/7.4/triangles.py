from points import Point

class Triangle:
    """Klasa reprezentujaca trojkaty na plaszczyznie."""

    def __init__(self, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
        # Nalezy zabezpieczyc przed sytuacja, gdy punkty sa wspolliniowe.

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        if self.pt1 == self.pt2 or self.pt1 == self.pt3 or self.pt2 == self.pt3:
            raise ValueError("Two points identical-cannot create triangle")
        if x1*y2*1+x2*y3*1+x3*y1*1-1*y2*x3-1*y3*x1-1*y1*x2 == 0:
            raise ValueError("Points are on the same line")

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        return "[({},{}), ({},{}), ({},{})]".format(self.pt1.x, self.pt1.y,self.pt2.x, self.pt2.y,self.pt3.x, self.pt3.y)

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return "Triangle({}, {}, {}, {}, {}, {})".format(self.pt1.x, self.pt1.y,self.pt2.x, self.pt2.y,self.pt3.x, self.pt3.y)

    def __eq__(self, other):   # obsluga tr1 == tr2
        if self.pt1 == other.pt1 and self.pt2 == other.pt2 and self.pt3 == other.pt3:
            return True
        else:
            return False

    def __ne__(self, other):        # obsluga tr1 != tr2
        return not self == other

    def center(self):          # zwraca srodek trojkata
        return Point((self.pt1.x+self.pt2.x+self.pt3.x)/3,(self.pt1.y+self.pt2.y+self.pt3.y)/3)

    def area(self):            # pole powierzchni
        return (abs((self.pt2.x-self.pt1.x)*(self.pt3.y-self.pt1.y)-(self.pt2.y-self.pt1.y)*(self.pt3.x-self.pt1.x))/2.0)

    def move(self, x, y):       # przesuniecie o (x, y)
        self.pt1.x += x
        self.pt2.x += x
        self.pt3.x += x
        self.pt1.y += y
        self.pt2.y += y
        self.pt3.y += y
        return self

    def make4(self):            # zwraca liste czterech mniejszych
        p12 = Point((self.pt1.x+self.pt2.x)/2.0, (self.pt1.y+self.pt2.y)/2.0)
        p13 = Point((self.pt1.x+self.pt3.x)/2.0, (self.pt1.y+self.pt3.y)/2.0)
        p23 = Point((self.pt2.x+self.pt3.x)/2.0, (self.pt2.y+self.pt3.y)/2.0)

        t1 = Triangle(self.pt1.x, self.pt1.y, p12.x, p12.y, p13.x, p13.y)
        t2 = Triangle(p12.x, p12.y, self.pt2.x, self.pt2.y, p23.x, p23.y)
        t3 = Triangle(p12.x, p12.y, p13.x, p13.y, p23.x, p23.y)
        t4 = Triangle(p13.x, p13.y, p23.x, p23.y, self.pt3.x, self.pt3.y)
        return [t1, t2, t3, t4]


'''t1 = Triangle(1,2,1,3,2,2)
print(t1)
print(t1.center())
print(t1.area())
print(t1.make4())
print(t1.move(99,99))
print(t1)'''