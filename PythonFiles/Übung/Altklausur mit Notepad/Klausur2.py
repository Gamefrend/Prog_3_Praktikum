class Obstsalat:

    def __init__(self, name=None, zutaten=None):
        self.gewicht = 0
        if name is None:
            self.name = ""
            self.zutaten = {}
        elif isinstance(zutaten, dict):
            if len(name.split("-")) > 1:
                self.name = name
            else:
                self.name = name.capitalize()
            self.zutaten = zutaten
            for e in zutaten:
                self.gewicht += zutaten[e]
        else:
            self.name = name.capitalize()
            self.zutaten = {name.capitalize(): int(zutaten)}
            self.gewicht = zutaten
        if self.gewicht > 17:
            raise ValueError

    def __repr__(self):
        return f"Obstsalat('{self.name}')"

    def __add__(self, other):
        listofNames = []
        zutaten = {}
        name = ""
        if len(self.name.split("-")) > 1:
            listofNames.extend(self.name.split("-"))
        elif self.name != "":
            listofNames.append(self.name)
        if len(other.name.split("-")) > 1:
            listofNames.extend(other.name.split("-"))
        elif other.name != "":
            listofNames.append(other.name)

        listofNames = set(listofNames)

        for s in sorted(listofNames):
            name += s + "-"
        for e in self.zutaten:
            if e in zutaten:
                zutaten[e] = zutaten[e] + self.zutaten[e]
            else:
                zutaten.update({e: self.zutaten[e]})
        for e in other.zutaten:
            if e in zutaten:
                zutaten[e] = zutaten[e] + other.zutaten[e]
            else:
                zutaten.update({e: other.zutaten[e]})
        return Obstsalat(name[:-1], zutaten)

    def __gt__(self, other):
        if self.name == other.name:
            return self.gewicht > other.gewicht
        return self.name > other.name


lst = sorted([Obstsalat("M", 5), Obstsalat("T", 4), Obstsalat("C", 2), Obstsalat("T", 1)])

print([f"{o.name}, {o.gewicht}" for o in lst])


