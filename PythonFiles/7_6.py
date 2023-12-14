outputListe = []

def drehliste(inputList):
    outputListe.append(inputList.pop())
    if (len(inputList) == 0):
        return outputListe
    return drehliste(inputList)

print(drehliste([1, 2, 3]))