from _10_1 import Messungen
from _10_4 import MessreiheEigenIter


class Messreihe:
    def __init__(self, messungen):
        self.alleMessungen = set()
        try:
            for messung in messungen:
                if isinstance(messung, Messungen):
                    self.alleMessungen.add(messung)
                if isinstance(messung, str):
                    self.alleMessungen.add(Messungen(messung))
        except TypeError as e:
            if messungen is not None:
                if isinstance(messungen, Messungen):
                    self.alleMessungen.add(messungen)
                if isinstance(messungen, str):
                    self.alleMessungen.add(Messungen(messungen))
    def __str__(self):
        out = ""
        i = 1
        for messung in self.alleMessungen:
            out += "Die "+ str(i) +". Messung ist: " +str(messung)+"\n"
            i = i+1
        return out

    def __len__(self):
        return len(self.alleMessungen)

    def __add__(self, *other):
        if isinstance(other[0], tuple):
            if isinstance(other[0][0], Messungen):
                for i in range(len(other[0])):
                    self.alleMessungen.add(other[0][i])
        if isinstance(other[0], Messreihe):
            for e in other[0]:
                self.alleMessungen.add(e)
        else:
            self.alleMessungen.add(other[0])
        return self

    def __iter__(self):
        #normaler iter as einer Liste generieren
        #return iter(self.alleMessungen)

        #custom Iter
        #funktioniert ist aber sehr langsam
        #return MessreiheEigenIter(self.alleMessungen)

        #generator selbst schreiben
        for e in self.alleMessungen:
            yield e

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            if isinstance(index, int):
                return list(self.alleMessungen)[index]
            return Messreihe(list(self.alleMessungen)[index])
        if isinstance(index, str):
            return Messreihe(list(filter(lambda x: x.timeStamp[:len(index)] == index, [x for x in self.alleMessungen])))


with open(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\messwerte.csv") as file:
    data = file.readlines()

def enum(messreihe):
    return zip(list(range(len(messreihe))), messreihe)
def testsFuer10_2():
    messreihe = Messreihe(data)
    print(len(messreihe))
    messreihe += Messungen('"a",10'), Messungen('"q",10'), Messungen('"a",10')
    print(len(messreihe))
    print(messreihe[0])
    print(messreihe[1])
    messreihe2 = messreihe["2015-04-20"]
    messreihe3 = Messreihe(('"fefe",20', '"fufu",30'))
    print(messreihe2)
    print(messreihe3)
    print(messreihe2[90:80:-1])

def testsFuer10_3():
    messreihe = Messreihe(data)
    print(len(messreihe))
    messreihe += Messungen('"a",10')
    messreihe += Messungen('"a",999999999999999')
    print(len(messreihe))
    print(min(messreihe, key=lambda x: x.temperatura))
    print(max(messreihe, key=lambda x: x.temperatura))
    print([x.timeStamp for x in messreihe if x.temperatura > 33])
    print(len([x for x in messreihe if x.timeStamp[0:4] == "2017" and x.temperatura > 26]))
    print(max([x.timeStamp for x in messreihe if int(x.temperatura) == 17]))
    print(sum([x.temperatura for x in messreihe["2017-10"]+messreihe["2017-11"]+messreihe["2017-12"]])
          / len(messreihe["2017-10"]+messreihe["2017-11"]+messreihe["2017-12"]))

def testsFuer10_4():
    messreihe = Messreihe(data)
    print(messreihe[5].timeStamp[0:9])
    print([x for x in messreihe if x.timeStamp[0:10] == "2016-04-21" and 20 < x.temperatura < 20.2])
    it1, it2 = iter(messreihe), iter(messreihe)
    for i in range(10):
        m1, m2 = next(it1), next(it2)
    print(m1, m2, "Problem" if m1 != m2 else "OK")
    for i, e in enum(messreihe[0:10]):
        print(str(i)+"."+str(e))

testsFuer10_4()

