import re

patternPLZ = re.compile(r'\d{5}')
patternDatum = re.compile(r"\d{2}.\d{2}.\d{4}")
patternEuro = re.compile(r"\d{1,3}((\.\d{3})|(\d{1,3}))*(,\d\d)?(\sEuro)?")
patternTel = re.compile(r"((\+(\d{2})\s\d{2})|\d{5}/)(([-\s]\d{2})|\d)*")
patternEmail = re.compile(r"\w+([.-]\w+)*@[a-z][\w-]+(\.[a-z]\w+)+")
parterns = [patternPLZ, patternDatum, patternEuro, patternTel]

with open(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\Regex.txt") as file:
    inhalt = file.readlines()

for line in inhalt:
    aktuellesPattern = None
    match line.split("\t")[0]:
        case "PLZ":
            aktuellesPattern = patternPLZ
            typ = "PLZ"
        case "Datum":
            aktuellesPattern = patternDatum
            typ = "Datum"
        case "EUR":
            aktuellesPattern = patternEuro
            typ = "Euro"
        case "Tel":
            aktuellesPattern = patternTel
            typ = "Telefonnummer"
        case "Email":
            aktuellesPattern = patternEmail
            typ = "Email"
    print(line.split("\t")[1] + " ist " +
        ("EINE" if aktuellesPattern.fullmatch(line.split("\t")[1]) is not None else "KEINE") + " " + typ)
