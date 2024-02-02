import re
class RoemerZahl:
    def __init__(self, input=""):
        if re.compile("^([C]*[L]*[X]*[V]*[I]*)$|^([0-9]+)$").fullmatch(input) is None and not input == "":
            raise ValueError("")
        if re.compile("^([0-9]+)$").fullmatch(input) is not None:
            self.modern = input
            self.roemerZahl = self.umwandelnRoemisch(input)
        else:
            self.roemisch = input
            self.modern = self.umwandeln(input)

    def umwandeln(self, input):
        output = 0
        lookup = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100}
        for char in input:
            output += lookup[char]
        return output

    def umwandelnRoemisch(self, input):
        lookup = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C"}
        output = ""
        for e in [100, 50, 10, 5, 1]:
            while int(input)//e > 0:
                output += lookup[e]
                input = str(int(input) - e)
        return output

    def __len__(self):
        return len(self.modern)

    def __add__(self, other):
        output = ""
        lookup = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100}
        for e in lookup:
            if re.compile(re.escape(e)).findall(self.roemisch+other.roemisch) is not None:
                for i in range(len(re.compile(re.escape(e)).findall(self.roemisch+other.roemisch))):
                    output += e
        return RoemerZahl(output[::-1])

    def __gt__(self, other):
        if self.modern == other.modern:
            return self.roemisch > other.roemisch
        return self.modern > other.modern

    def __repr__(self):
        return "RoemerZahl('"+self.roemisch+"')"

    def __str__(self):
        return self.roemisch

zahl1 = RoemerZahl("")
zahl2 = RoemerZahl("XIII")
zahl3 = RoemerZahl("C")
try:
    zahl4 = RoemerZahl("IXIIV")
except ValueError as e:
    print (e)
zahl5 = RoemerZahl("101")
print(zahl2.modern)
print(str(eval(repr(zahl2))))
print(str(zahl1) == "")
print(zahl2+zahl3)
print(zahl5.roemerZahl, zahl5.modern)
print(list(map(str, sorted([zahl1, zahl2, zahl3, RoemerZahl("IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"), RoemerZahl("CLLV")]))))
print(list(map(str, sorted([RoemerZahl("XVII"), RoemerZahl("VVVII")]))))
