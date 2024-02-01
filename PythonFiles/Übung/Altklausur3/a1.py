import re
class RoemerZahl:
    def __init__(self, input=""):
        if re.compile("^([C]*[L]*[X]*[V]*[I]*)$|([1-9]+)").fullmatch(input) is None and not input == "":
            raise ValueError("")
        print(re.compile("^([C]*[L]*[X]*[V]*[I]*)*$|([1-9]+)").fullmatch(input))
        self.roemisch = input
        self.modern = self.umwandeln(input)

    def umwandeln(self, input):
        output = 0
        lookup = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100}
        for char in input:
            output += lookup[char]
        return output
    def __repr__(self):
        return "RoemerZahl('"+self.roemisch+"')"

    def __str__(self):
        return self.roemisch

zahl1 = RoemerZahl("")
zahl2 = RoemerZahl("XIII")
zahl3 = RoemerZahl("C")
zahl4 = RoemerZahl("IXIIV")
print(zahl2.modern)
print(zahl4.modern)
print(str(eval(repr(zahl2))))
print(str(zahl1) == "")
