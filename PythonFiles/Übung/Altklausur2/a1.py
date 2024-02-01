class Obstsalat:

    def __init__(self, name=None, gewicht=None):
        if name is not None:
            self.name = name[0].upper() + name[1:].lower()
            self.zutaten = {name : gewicht}
        else:
            self.name = ""
            self.zutaten = {}

    def __repr__(self):
        return "Obstsalat("+ self.name +")"

obstsalat = Obstsalat()
obstsalat2 = Obstsalat("ApFel", 5)
print(obstsalat)
print(obstsalat2)