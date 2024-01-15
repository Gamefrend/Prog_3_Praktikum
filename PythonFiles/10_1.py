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
        return f"Diese Messung hat den Timestamp {self.timeStamp} und Temperatur von {self.temperatura}"

    def __eq__(self, other):
        print("??")
        return self.timeStamp == other.timeStamp and self.temperatura == other.temperatura


Messungen1 = Messungen("2019-01-11 17:45:01.356640", 19.5)
Messungen2 = Messungen('"2019-01-11 17:45:01.356640",19.5')

print(Messungen2)
eval(repr(Messungen1)) == Messungen1

