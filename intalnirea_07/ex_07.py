# Creati o clasa Student cu 2 atribute, un nume si o nota.
# Instantiati cele 2 fielduri prin intermediul constructorului.
# a) Scrieti 2 functii pentru nota: get_grade care sa returneze nota studentului si set_grade care sa ii modifice nota.
# Asigurativa ca e si logic, nu doar ca functioneaza:)!
# b) Scrieti o functie care sa descrie elevul: "The student`s name is .... and has the grade ..."
# c) Creati o lista de studenti primita ca input de la tastatura; dupa ce ati construit-o, afisati descrierea fiecarui student
# d) Filtrati lista de studenti (sau construiti una noua) astfel incat sa ramana doar acei studenti care au o nota de trecere:
# de preferat determinati daca studentul are nota de trecere sau nu folosindu`va de o alta functie a clasei Student

class Student:
    def __init__(self, nume, nota):
        self.nume = nume
        self.nota = nota

    def get_grade(self):
        return self.nota
    
    def set_grade(self, noua_nota):
        self.nota = noua_nota

    def descriere (self):
        print(f'The student`s name is {self.nume} and has the grade {self.nota}')

    def students_list(self):
        lst = input('Introduceti studentii:')
