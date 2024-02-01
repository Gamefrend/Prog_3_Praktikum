class RoemerZahl:
    def __init__(self, input=""):
        self.roemisch = input
        self.modern = self.umwandeln(input)

    def umwandeln(self, input):
        output = 0
        lookup = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100}
        counter = 0
        while counter < len(input):
            if counter+1 <len(input):
                if input[counter] < input[counter+1]:
                    output += lookup[input[counter+1]] - lookup[input[counter]]
                    counter += 1
                else:
                    output += lookup[input[counter]]
            else:
                output += lookup[input[counter]]
            counter += 1
        return output

zahl1 = RoemerZahl("")
zahl2 = RoemerZahl("XIII")
zahl3 = RoemerZahl("C")
zahl4 = RoemerZahl("IXIIV")
print(zahl2.modern)
print(zahl4.modern)