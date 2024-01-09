import sys

if len(sys.argv) < 2:
    print("Keine Argumente angegeben")
    sys.exit(0)

with open(r'C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3' +"\u005C" + sys.argv[1]) as file:
    text = file.read()

def listToString(list):
    out = ""
    for e in list:
        out+=e
    return out

countedChars = {"a":0}
def countChars(x):
    if x not in countedChars:
        countedChars.update({x: 1})
    else:
        countedChars.update({x: countedChars.get(x)+1})

print(list(map(countChars,text)))