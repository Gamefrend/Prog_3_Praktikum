
class Student:
    studierende = 0
    def __init__(self, vorname, nachname, Matrklnr):
        self.vorname = vorname
        self.nachname = nachname
        self.Matrklnr = int(Matrklnr)
        Student.studierende += 1
    def __repr__(self):
        return "Student('"+self.vorname+"', '"+self.nachname+"', '"+str(self.Matrklnr)+"')"

    def get_full_name(self):
        return self.vorname+" "+self.nachname

    def get_student_info(self):
        return ("Der Stundent heißt: " + self.vorname + " " + self.nachname + " und hat die Matrikelnummer: "+ str(self.Matrklnr))
    def __eq__(self, other):
        return self.vorname == other.vorname and self.nachname == other.nachname and self.Matrklnr == other.Matrklnr


ich = Student("Enis", "Avdovic", 12374783)
print(ich.get_full_name())
print(repr(ich))
print(ich.get_student_info())
print(eval(repr(ich)).get_student_info())
print(eval(repr(ich))==ich)
jemandanderes = Student("nise", "vdovica", 1237483)
print(Student.studierende)

