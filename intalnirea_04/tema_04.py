#ex1

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(f'Masina mea preferata este {masina}')

masini = range(9)
for masina in range(9):
       print(f'Masina mea preferata este {masina}')

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
m = len(masini)
i = 0
while i < m:
    print(f'Masina mea preferata este {masini[i]}')
    i += 1

#ex2

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in range(1, len(masini) - 1):
    masini[masina] = masini[masina].upper()
else:
    print(masini)

#ex3

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print("Am gasit masina dorita de dumneavoastra.")
        break
    else:
        print(f'Am gasit masina {masina}. Mai cautam')

#ex4

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue
    print(f'S-ar putea sa va placa masina {masina}')

#ex5

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masini_vechi = []
for masina in masini:
    if masina == 'Lastun' or masina == 'Trabant':
        masini_vechi.append(masina)
print(f'Modele vechi: {masini_vechi}')
masini[5] = 'Tesla'
masini[7] = 'Tesla'
print(f'Modele noi: {masini}')

#ex6

pret_masini = {'Dacia': 6800, 'Lastun': 500, 'Opel': 1100, 'Audi': 19000, 'BMW': 23000}
for masina, pret in pret_masini.items():
    if pret <= 15000:
        print(masina, pret)
        print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina}')

#ex7

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
n = 0
for nr in numere:
    if nr == 3:
       n = n+1
       print(nr)
print(f'3 apare de {n} ori')

#ex8

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
suma = 0
for nr in numere:
    suma = suma+nr
print(f'Suma numerelor este {suma}')

#ex9

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere.sort()
print(numere[:-1])
#ex10

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
new_list = []
for n in numere:
    if n > 0:
        n = -n
        new_list.append(n)
print(new_list)

#ex11

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for nr in alte_numere:
    if nr % 2 == 0:
        numere_pare.append(nr)
    if nr % 2 != 0:
        numere_impare.append(nr)
    if nr >0:
        numere_pozitive.append(nr)
    else:
        numere_negative.append(nr)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')

#ex12
#Aceeasi lista. Ordonati crescator lista fara sa folositi sort
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
for nr in range(0, len(alte_numere)):
    for n in range(nr+1, len(alte_numere)):
        if (alte_numere[nr] > alte_numere[n]):
            alte_numere[nr], alte_numere[n] = alte_numere[n],  alte_numere[nr]
print(alte_numere)
#ex13

import random
numar_secret = random.randrange(1,30)
nr_inceput = 1
nr_final = 30
while True:
    numar_ghicit = int(input(f'Ghiceste un numar intre {nr_inceput} si {nr_final}:'))
    if numar_ghicit == numar_secret:
        print('Felicitari! Ati ghicit!')
        break
    elif numar_ghicit < numar_secret:
        print('Nr secret e mai mare')
        nr_inceput = numar_ghicit
    else:
        print('Nr secret e mai mic')
        nr_final = numar_ghicit

#ex14

numar = int(input('Introduceti un numar:'))
for i in range(numar+1):
    print (i *str(i))

#ex15

tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
for nr in range(len(tastatura_telefon)):
    lst = tastatura_telefon[nr].copy()
    for n in range(len(tastatura_telefon[nr])):
        print(f'Cifra curenta este {lst[n]}')














