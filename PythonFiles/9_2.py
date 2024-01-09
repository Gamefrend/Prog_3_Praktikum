import sys

from six import unichr

def listToString(list):
    out = ""
    for e in list:
        out+=e
    return out

def encrypt(x):
    if x - 97 > 0 and x - 97 < 24:
        return key[x - 97]
    else: return x
def decrypt(x):
    index = 0
    for e in key:
        if unichr(x) == e:
            return val[index]
        index = index + 1
    return unichr(x)

if len(sys.argv) < 2:
    print("Keine Argumente angegeben")
    sys.exit(0)

key = ["w", "g", "s", "n", "q", "c", "d", "v", "m", "e", "y", "l", "u", "z", "o", "a", "b", "h", "r", "j", "f", "k", "x", "i", "p", "t"]
val = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
with open(r'C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3' +"\u005C" + sys.argv[1]) as file:
    inhalt = file.read()

print(inhalt)
print(listToString(list(map(decrypt, (map(ord, inhalt))))))

