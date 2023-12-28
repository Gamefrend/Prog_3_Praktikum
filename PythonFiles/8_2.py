def ggT(x,y):
    if x==y:
        return x
    else:
        if x<y:
            x,y=y,x
        return ggT(x-y,y)

def testListggT(lst):
    for i in lst:
        print(i)

with open(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\ggT_Beispiele.txt","r+") as temp:
    tempContent = temp.read()
    tempArray = tempContent.split("\n")

for e in tempArray:
    e = e.split(" ")
    print("Der ggT von "+e[0]+" und "+e[1]+" soll "+e[2]+" sein. Der Algorythmus kam auf die Zahl "+str(ggT(int(e[0]),int(e[1]))))
    #print(True if(str(ggT(int(e[0]),int(e[1]))) == e[2])else False)
#print(ggT(504,4784))
