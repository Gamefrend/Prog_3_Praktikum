import sys

if len(sys.argv) < 2:
    print("Keine Argumente angegeben")
    sys.exit(0)

with open(r'C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3' +"\u005C" + sys.argv[1]) as file:
    text = file.read()

text = text.splitlines()
print([x.split(";")[4] for x in text if x.split(";")[0] == "Herr"])
print(sum([int(x.split(";")[3]) for x in text if x.split(";")[0] == "Frau"]))
print(max([(x.split(";")[4], int(x.split(";")[3])) for x in text if x.split(";")[2][0] == "J"])[0])
print([x.split(";")[0] + " " + x.split(";")[1] +" bekommt mehr, als "+ ("er" if x.split(";")[0] == "Herr" else "sie") +" verdient hat!" for x in text if int(x.split(";")[3])>100000])
