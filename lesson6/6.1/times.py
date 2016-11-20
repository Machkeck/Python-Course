class Time:
    """Klasa reprezentujaca odcinek czasu."""

    def __init__(self, s=0):
        """Zwraca instancje klasy Time."""
        self.s = int(s)

    def __str__(self):
        """Zwraca string 'hh:mm:ss'."""
        h = int(self.s / 3600)
        sec = int(self.s - h * 3600)
        m = int(sec / 60)
        sec = sec - m * 60
        return "{0:02d}:{1:02d}:{2:02d}".format(h, m, sec)

    def __repr__(self):
        """Zwraca string 'Time(s)'."""
        return "Time({0})".format(self.s)

    def __add__(self, other):
        """Dodawanie odcinkow czasu."""
        return Time(self.s + other.s)

    def __cmp__(self, other):           # porownywanie, -1|0|+1
        """Porownywanie odcinkow czasu."""
        return cmp(self.s, other.s)

    def __int__(self):                  # int(time1)
        """Konwersja odcinka czasu do int."""
        return self.s

