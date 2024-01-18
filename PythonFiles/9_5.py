import glob
import os.path

print(os.path.getsize(r"C:\Users\eniav\Desktop\Uni Aufgaben\Prog 3\bonz.txt"))
listOfFilenames = glob.glob("**/*.py", recursive=True)
print(list(map(lambda x: x[0], sorted([(n, os.path.getsize(n)) for n in listOfFilenames], key=lambda x: x[1])[:-4:-1])))

