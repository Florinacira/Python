# Creati o clasa Student cu 2 atribute, un nume si o nota.
# Instantiati cele 2 fielduri prin intermediul constructorului.
# a) Scrieti 2 functii pentru nota: get_grade care sa returneze nota studentului si set_grade care sa ii modifice nota.
# Asigurativa ca e si logic, nu doar ca functioneaza:)!
# b) Scrieti o functie care sa descrie elevul: "The student`s name is .... and has the grade ..."
# c) Creati o lista de studenti primita ca input de la tastatura; dupa ce ati construit-o, afisati descrierea fiecarui student
# d) Filtrati lista de studenti (sau construiti una noua) astfel incat sa ramana doar acei studenti care au o nota de trecere:
# de preferat determinati daca studentul are nota de trecere sau nu folosindu`va de o alta functie a clasei Student

class Student:
#a
    def __init__(self, nume, nota):
        self.nume = nume
        self.nota = nota

    def get_grade(self):
        return self.nota
    
    def set_grade(self, noua_nota):
        self.nota = noua_nota
        print(f'Noua nota este: {self.nota}')
#b
    def descriere (self):
        print(f'The student`s name is {self.nume} and has the grade {self.nota}')

my_student = Student('Alex',9)
print(my_student.get_grade())
my_student.set_grade(7)
my_student.descriere()

#c
list_of_students = []
while True:
    student_name = input('Student name:')
    if student_name == 'stop':
       break
    student_nota = int(input('Student nota: '))
    student1 = Student(student_name, student_nota)
    list_of_students.append(student1)
for stud in list_of_students:
    stud.descriere()
#d
new_list = []
for stud in list_of_students:
    if stud.get_grade() >= 5:
        new_list.append(stud)
for stud in new_list:
    stud.descriere()


