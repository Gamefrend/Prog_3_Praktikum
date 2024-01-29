import re

patternPLZ = re.compile(r'\d{5}')
patternDatum = re.compile(r"\d+.\d+.\d{4}")
patternEuro = re.compile(r"\d{1,3}(\.\d{3}|\d{1,3})*(,\d\d)?(\sEuro)?")
patternTel = re.compile(r"(\+(\d{2})\s)?(\d\d|\s(\d)+\s)*\d{2}")
parterns = [patternPLZ, patternDatum, patternEuro, patternTel]

with open(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\Regex.txt") as file:
    inhalt = file.readlines()

for line in inhalt:
    line = line.split("\t")[1]
    for pattern in parterns:
        if pattern.match(line) != None:
            if len(pattern.match(line).group()) == len(line):
                if pattern == patternPLZ:
                    print(line +" ist eine PLZ")
                elif pattern == patternDatum:
                    print(line +" ist ein Datum")
                elif pattern == patternEuro:
                    print(line +" ist ein Geldberag")
                elif pattern == patternTel:
                    print(line +" ist ein Telefonnummer")
