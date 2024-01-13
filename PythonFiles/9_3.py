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

countedCharsDict = {"a":0}
def countChars(x):
    x = x.lower()
    if x not in countedCharsDict:
        if not x.isalpha():
            return
        countedCharsDict.update({x: 1})
    else:
        countedCharsDict.update({x: countedCharsDict.get(x)+1})

def mapChartoList(x):
    if x in sortedList:
        return haefigkeitListe[sortedList.index(x)]
    else:
        return x

haefigkeitListe = ['e', 'n', 'i', 'a', 's', 't', 'r', 'u', 'h', 'd', 'l', 'c', 'm', 'o', 'g', 'k', 'w', 'b', 'z', 'f', 'v', 'p', 'j', 'x', 'y', 'q']

list(map(countChars,text))
sortedList = sorted(countedCharsDict, key=countedCharsDict.get, reverse=True)
print(listToString(list(map(mapChartoList, text))))
