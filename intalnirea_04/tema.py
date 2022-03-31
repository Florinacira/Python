#ex1
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(f'Masina mea preferata este :{masina}')

for masina in range(len(masini)):
    print(f'Masina mea preferata este {masina} ')
'''
m = len(masini)
n = 0
while n < m:
    n = n + 1
    print(f'Masina mea preferata este: {masini[n]} ')
'''
#ex2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in range(1,len(masini)-1):
    masini[masina] = masini[masina].upper()
print(masini)
#ex3
'''Aceeasi lista, 
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel (else apartine de if, nu de for)
   Printam Am gasit masina X. Mai cautam

'''
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print('am gasit masina dorita de dumneavoastra')
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

#ex4
'''Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun. 
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
(nu trebuie else)
Printati S-ar putea sa va placa masina x
'''
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

#ex5
'''Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == "Trabant" or masina == "Lastun":
        masini_vechi.append(masina)
        masini[masini.index(masina)] = "Tesla"
print(f' Modele vechi: {masini_vechi}')
print(f' Modele noi: {masini}')

#ex6
'''Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
Iterati prin lista


'''
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(f' Pentru un buget de sub 15000 euro puteti alege masina {masina}')

#ex7
'''Avand lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)

'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
n=0
for nr in numere:
    if nr==3:
        n = n+1
print(f'3 apare de {n}')

#ex8

'''Aceeasi lista
Iterati prin ea
Calculati si afisati suma numerelor
(nu aveti voie sa folositi sum)
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma=0
for  nr in numere:
        suma= suma+nr
print(suma)

#ex9
'''Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
for nr in numere:
    numere.sort()
print(numere[-1])

#ex10
''''''
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
new_list = []
for nr in numere:
    if nr > 0:
       nr = - nr
       new_list.append(nr)
print(new_list)


