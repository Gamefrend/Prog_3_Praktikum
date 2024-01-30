import re

with open(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\access.log") as file:
    inhalt = file.read()

getBilder = re.compile(r"GET.*\.(png|jpg|gif)")
nullUhr = re.compile(r"\[//:00:\d{2}:\d{2}")
einUhr = re.compile(r"\[//:01:\d{2}:\d{2}")
alleEintraege = re.compile(r"\n")
print(len(getBilder.findall(inhalt)))
print(len(alleEintraege.findall(inhalt)))
print(len(einUhr.findall(inhalt))/len(alleEintraege.findall(inhalt))*100)
print(len(einUhr.findall(inhalt)))
