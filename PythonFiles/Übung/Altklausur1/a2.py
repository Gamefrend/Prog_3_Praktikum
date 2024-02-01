import re

def wordpos(it):
    nurBuchstaben = re.compile(r"[^a-zA-Z]+")
    couterzeile = 0
    for e in it:
        counterwort = 0
        couterzeile += 1
        for i in nurBuchstaben.split(e):
            if i.isalpha():
                counterwort += 1
                yield (i, couterzeile, counterwort)

def sieheoben(it):
    verweis = {}
    for i in wordpos(it):
        if i[0].isalpha():
            if i[0] not in verweis:
                verweis[i[0]] = (i[1], i[2])
                yield (i[0])
            else:
                yield (i[0] + " (siehe Zeile " + str(i[2]) + ", Wort " + str(i[1]) + ")")

def shortify(it, n=5):
    for i in wordpos(it):
        if len(i[0]) > n:
            yield i[0][:n-2] + "..." + i[0][-1]
        else:
            yield i[0]



for e in shortify(["hallooooooo du","kleine Mauuuuuus 69 123aha123", "hallo du","klein"],3):
    print(e)