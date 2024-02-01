class Obstsalat:

    def __init__(self, name=None, zutaten=None):

        if isinstance(zutaten, dict):
            self.name = name
            self.zutaten = zutaten
            self.gewicht = sum(zutaten.values())
            #if self.gewicht > 17:
            #    raise ValueError("")
        elif name is not None:
            self.name = name[0].upper() + name[1:].lower()
            self.zutaten = {self.name : zutaten}
            self.gewicht = zutaten
        else:
            self.name = ""
            self.zutaten = {}
            self.gewicht = 0

    def __gt__(self, other):
        return self.name > other.name

    def __repr__(self):
        return "Obstsalat("+ self.name +")"

    def __add__(self,other):
        namenliste = set()
        namenliste.update(self.name.split("-") + other.name.split("-"))
        namenliste = list(namenliste)
        sorted(namenliste)
        neuezutaten = self.zutaten.copy()
        for e in other.zutaten:
            if e in neuezutaten:
                neuezutaten[e] = neuezutaten[e] + other.zutaten[e]
            else:
                neuezutaten[e] = other.zutaten[e]
        neuername = ""
        for namen in namenliste:
            neuername += namen + "-"
        return Obstsalat(neuername[:-1], neuezutaten)


obstsalat = Obstsalat()
obstsalat2 = Obstsalat("ApFel", 5)
obstsalat4 = Obstsalat("kaRotte", 20)
print(obstsalat)
print(obstsalat2)
obstsalatmischung = obstsalat2 + obstsalat4
print(obstsalat2, obstsalat2.name, obstsalat2.zutaten, obstsalat2.gewicht)
print(obstsalat4, obstsalat4.name, obstsalat4.zutaten)
print(obstsalatmischung, obstsalatmischung.name, obstsalatmischung.zutaten, obstsalatmischung.gewicht)
obstsalatmischung += obstsalat2
print(obstsalatmischung, obstsalatmischung.name, obstsalatmischung.zutaten, obstsalatmischung.gewicht)
obstsalatmischung = Obstsalat("Papaya", 5) + Obstsalat("Kiwi", 8) + Obstsalat("TrAUbe", 4)
print(obstsalatmischung, obstsalatmischung.name, obstsalatmischung.zutaten, obstsalatmischung.gewicht)
obstArray = [obstsalat, obstsalatmischung, obstsalat2]
print(obstArray)
print(sorted(obstArray))

