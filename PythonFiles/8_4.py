with open(r'C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\fahrplan.txt') as fahrplan_file:
    fahrplan = fahrplan_file.read()

def wegBerechnung(start, ziel, zwischenZeit = 0, haltestellen= None):
    if haltestellen is None:
        haltestellen = list()
        haltestellen.append(start)
    if start == ziel:
        return (0,haltestellen)
    for line in fahrplan.splitlines():
        lineElements = line.split(";")
        if lineElements[1] == start:
            haltestellen.append(lineElements[2])
            zwischenZeit += int(lineElements[3])
            if haltestellen[-1] == ziel:
                return (zwischenZeit, haltestellen)
            else:
                return(wegBerechnung(lineElements[2], ziel, zwischenZeit, haltestellen))


lineElements = ["","Kelsterbach","Niederrad"]
print("Um von "+lineElements[1] +" nach " + lineElements[2]+ " zu fahren braucht man:")
print(str(wegBerechnung(lineElements[1],lineElements[2])[0]) + " Minuten und faehrt diese Haltesetellen an :" + str(wegBerechnung(lineElements[1],lineElements[2])[1]))
