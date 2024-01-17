class Messungen:
    timeStamp = ""
    temperatura = 0.0

    def __init__(self, *elements):
        if len(elements) > 1:
            self.timeStamp = str(elements[0])
            self.temperatura = float(elements[1])
        else:
            self.timeStamp = str(elements[0].split(",")[0][1:-1])
            self.temperatura = float(elements[0].split(",")[1])

    def __repr__(self):
        return f"Messungen('{self.timeStamp}', {self.temperatura})"

    def __eq__(self, other):
        return str(self.timeStamp) == str(other.timeStamp) and self.temperatura == other.temperatura

    def __gt__(self, other):
        return self.temperatura > other.temperatura

    def __lt__(self, other):
        return self.temperatura <= other.temperatura

    def __str__(self):
        return f'Der Timstamp liegt bei {self.timeStamp} und die Temparatur bei {self.temperatura}'

messungen1 = Messungen("2019-01-11 17:45:01.356640", 21.5)
messungen2 = Messungen('"2019-01-11 17:45:01.356640",20.5')
messungen3 = Messungen("2019-01-11 17:45:01.356640", -20)
messungen4 = messungen3
alleMessungen = [messungen1, messungen2, messungen3]
print(messungen1)
print(messungen1 == messungen2)
print(sorted(alleMessungen))
print(messungen1 is messungen2)
print(messungen3 is messungen4)
