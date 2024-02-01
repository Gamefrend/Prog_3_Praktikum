class Spendensammler:
    def __init__(self):
        self.betrag = 0
        self.spender = {}

    def __len__(self):
        return len(self.spender)
    def meldung(self, s):
        personen = self.namensfinder(s.split(" mit ")[0])
        betrag = int(s.split(" mit ")[1].split(" ")[0])
        for e in personen:
            if e in self.spender:
                self.spender[e] = self.spender[e] + betrag
            else:
                self.spender.update({e: betrag})

    def namensfinder(self, s):
        output = []
        for e in s.split(" "):
            if e == "und":
                pass
            elif e[len(e)-1] == ",":
                output.append(e[:-1])
            else:
                output.append(e)
        return output

    def topspender(self):
        output = []
        for e in list(self.spender):
            output.append((e, self.spender[e]))
        return sorted(output, key=lambda x: x[1], reverse=True)

sammler = Spendensammler()
print(sammler.namensfinder("Kunigu, aba und berta"))
sammler.meldung("Harry, Berta und Jo mit 69 Euro")
sammler.meldung("Jo mit 1 Euro")
print(sammler.spender)
print(len(sammler))
print(sammler.topspender())
