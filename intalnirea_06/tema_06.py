#ex1
'''Clasa Cerc
Atribute: raza, culoare
Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria
diametru()
circumferinta()'''

class circle:
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descriere_cerc(self):
         print(f'Culoarea cercului este: {self.culoare} ')
         print(f'Raza cercului este: {self.raza}')

    def aria(self):
        return (f'Aria cercului este:{3.14 * (self.raza **2)}')

    def diametru(self):
        return (f'Diametrul este:{self.raza * 2}')

    def circumferinta(self):
        return (f'Circumferinta cercului este:{3.14* (self.raza * 2)}')

my_circle = circle(8,'verde')
new_circle = circle(4,'rosu')
print(my_circle.descriere_cerc())
print(new_circle.descriere_cerc())
print(my_circle.aria())
print(new_circle.aria())
print(my_circle.diametru())
print(new_circle.diametru())
print(my_circle.circumferinta())
print(new_circle.circumferinta())

#ex2
'''Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie() va PRINTA lungime, latime, culoare
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va 
suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().'''

class Dreptunghi:
    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f'Dreptunghiul are lungimea de {self.lungime}, latimea de {self.latime} si culoarea {self.culoare}')
    def aria(self):
         return (f'Aria dreptunghiului este: {self.lungime * self.latime}')
    def perimetru(self):
        return(f'Perimetrul este:{2*(self.latime + self.lungime)}')
    def scimba_culoarea(self,noua_culoare):
        self.culoare = noua_culoare


dreptunghiul_meu= Dreptunghi(10,6,'alb')
dreptunghi_nou = Dreptunghi(20,15,'negru')
print(dreptunghiul_meu.descriere())
print(dreptunghiul_meu.aria())
print(dreptunghiul_meu.perimetru())
print(dreptunghiul_meu.scimba_culoarea('galben'))
dreptunghi_nou = Dreptunghi(20,15,'negru')
print(dreptunghi_nou.descriere())
print(dreptunghi_nou.aria())
print(dreptunghi_nou.perimetru())
print(dreptunghi_nou.scimba_culoarea('Verde'))
print(dreptunghi_nou.descriere())

#ex3
'''Clasa Angajat
Atribute: nume, prenume, salariu
Constructor() pt toate atributele // constructor reprezinta __init__
Metode:
descrie() print nume, prenume, salariu
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)'''

class Angajat:
    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
       print (f'Numele angajatului este:{self.nume} {self.prenume} si are salariul de : {self.salariu} lei')
    def nume_complet(self):
        return (f'Numele complet al angajatului este {self.nume} {self.prenume}')
    def salariu_lunar(self):
        return(f'Salariul lunar al angajatului este: {self.salariu} lei')
    def salariu_anual(self):
        return (f'Salariul anual al angajatului este:{self.salariu *12} ')
    def marire_salariu (self,procent):
        self.salariu = self.salariu + (self.salariu * procent /100)
        return (f'Salariul angajatului in urma maririi este:{self.salariu}')

angajatul  = Angajat('Popescu','Bogdan', 5000)
angajatul.descriere()
print(angajatul.nume_complet())
print(angajatul.salariu_lunar())
print(angajatul.salariu_anual())
print(angajatul.marire_salariu(15))

#ex4
'''Clasa Factura
Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
schimba_cantitatea(cantitate)
schimba_pretul(pret)
schimba_nume_produs(nume)
genereaza_factura() - va printa tabelar daca reusiti

Factura seria x numar y
Data: generati automat data de azi
Produs | cantitate | pret bucata | Total “
Telefon |      7       |       700       | 49000     '''

class Factura:
    seria = 'ITF'
    def __init__(self,numar,nume_produs,cantitate,pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return(f'Cantitate produs:{self.cantitate}')
    def schimba_pretul(self,pret):
        self.pret_buc = pret
        return(f'Noul pret al produsului este:{self.pret_buc}')
    def schimba_nume_produs(self,nume):
        self.nume_produs = nume
        return(f'Noul produs este:{self.nume_produs}')
    def genereaza_factura(self):
        from datetime import date
        data = date.today()
        self.total = self.cantitate * self.pret_buc
        return f""""
        Factura seria {self.seria} numar {self.numar}
        Data : {data}         
        Produs | cantitate  | pret bucata | Total 
        {self.nume_produs}|     {self.cantitate}    |      {self.pret_buc}      |  {self.total}"""


noua_factura = Factura(500,'LAPTOP',1,4300)
print(noua_factura.schimba_cantitatea(3))
print(noua_factura.schimba_pretul(5100))
print((noua_factura.schimba_nume_produs('tableta')))
print(noua_factura.genereaza_factura())

#ex5
'''Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate
Metode:
afisare_sold() - Titularul x are in contul y suma de n lei
debitare_cont(suma)
creditare_cont(suma)'''

class Cont:
    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold
    def afisare_sold(self):
        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei')
    def debitare_cont(self,suma):
         self.sold = self.sold + suma
         return self.sold
    def creditare_sold(self,suma):
         self.sold = self.sold - suma
         return self.sold

contul1 = Cont('RO47BBBB','Ionescu',2000)
contul1.afisare_sold()
print(contul1.debitare_cont(300))
print(contul1.creditare_sold(150))
contul2 = Cont('RO47AAAA','Popescu',3500)
contul2.afisare_sold()
print(contul2.debitare_cont(1400))
print(contul2.creditare_sold(365))

#ex6
'''Clasa Masina
Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
Culoare = gri - toate masinile cand ies din fabrica sunt gri
Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
Culori disponibile = alegeti voi 5-7 culori
Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
Inmatriculata = False
Constructor: model, viteza_maxima
Metode:
descrie() (se vor printa toate atributele, inafara de culori_disponibile)
inmatriculare() - va schimba atributul inmatriculata in True
vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
franeaza() - masina se va opri si va avea viteza 0
'''
class Masina:
    Culoare = 'gri'
    Viteza_actuala = 0
    culori_disponibile ={'alb','negru','rosu','verde','albastru'}
    marca = 'Volvo'
    inmatriculata = False

    def __init__(self,model,viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima
    def descriere(self,marca,viteza_actuala,culoare,inmatriculata):
        print(f'Masina {marca},model: {self.model},viteza_maxima: {self.viteza_maxima},viteza_actuala: {viteza_actuala},culoare: {culoare},inmatriculata: {inmatriculata}')
    def inmatriculare(self):
        self.inmatriculata = True
        return (f'Masina este inmatriculata: {self.inmatriculata}')
    def vopseste(self,culoare):
        culori_disponibile = {'alb', 'negru', 'rosu', 'verde', 'albastru'}
        if culoare in culori_disponibile:
            culoare = culoare
        else:
              return 'error'
        return(f'Noua culoare a masinii:{culoare}')
    def accelereaza(self,viteza):
        if viteza < 0:
            return'error'
        elif viteza > self.viteza_maxima:
            viteza = self.viteza_maxima
        else:
            viteza = viteza
        return viteza
    def franeaza(self):
        viteza_actuala = 0
        return f'Masina se v-a opri si v-a avea viteza {viteza_actuala}.'

masina_mea = Masina('XC90',180)
masina_mea.descriere('Volvo',0,'gri',False)
print(masina_mea.inmatriculare())
print(masina_mea.vopseste('alb'))
print(masina_mea.accelereaza(190))
print(masina_mea.franeaza())
noua_masina = Masina('tdv6',200)
noua_masina.descriere('RangeRover',0,'gri',False)
print(noua_masina.inmatriculare())
print(noua_masina.vopseste('negru'))
print(noua_masina.accelereaza(220))
print(noua_masina.franeaza())

#ex7
'''Clasa TodoList
 
Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

Metode:
adauga_task(nume, descriere) - se va adauga in dict
finalizeaza_task(nume) - se va sterge din dict
afiseaza_todo_list() - doar cheile
afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, printam detalii suplimentare daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
Daca acesta raspunde nu - la revedere
daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
'''
class TodoList:
    todo = {}
    def adauga_task(self,nume,descriere):
        if nume not in self.todo:
         self.todo[nume] = descriere
        print(self.todo)
    def finalizeaza_task(self,nume):
        del self.todo[nume]
        print(self.todo)
    def afiseaza_todo_list(self):
        todo_list= self.todo.keys()
        print(todo_list)
    def afiseaza_detalii_suplimentare(self,nume_task):
        if nume_task not in self.todo:
            r = input('Doriti sa adaugati task-ul in lista?')
            if r == 'Da':
                detalii_task = input('Introduceti detalii task: ')
                self.adauga_task(nume_task, detalii_task)
            else:
                print('La revedere!')
        else:
            print('Detaliile taskului', nume_task, 'sunt: ', self.todo[nume_task])

todo1 = TodoList()
todo1.adauga_task('task_1','invata Python')
todo1.adauga_task('task_2','citeste')
todo1.adauga_task('task_3','scrie cod')
todo1.finalizeaza_task('task_2')
todo1.afiseaza_todo_list()
todo1.afiseaza_detalii_suplimentare('task_5')