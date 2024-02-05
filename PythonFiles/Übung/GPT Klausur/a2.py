import re
class Buch:
    anzahlBuecher = 0
    def __init__(self, titel, autor, ISBN):
        self.titel = titel
        self.autor = autor
        self.ISBN = int(ISBN)
        Buch.anzahlBuecher += 1

    def __str__(self):
        return "Name: " + self.titel + "\nAutor: " + self.autor + "\nISBN: " + str(self.ISBN)

    def __repr__(self):
        return 'Buch("' + self.titel + '", "' + self.autor + '", "' + str(self.ISBN) + '")'

    def __eq__(self, other):
        return self.titel == other.titel and self.autor == other.autor and self.ISBN == other.ISBN

    def validISBN(self):
        return re.compile(r"^[\d]{13}$").match(str(self.ISBN)) is not None


buch1 = Buch("a", "z", 123)
buch2 = Buch("a", "z", "123")
buch3 = eval(repr(buch1))
buch4 = buch1
print(buch1 == buch3)
print(buch1 == buch4)
print(buch1)
print(buch1.validISBN())
print(Buch.anzahlBuecher)
