'''jucatori = ['A', 'B', 'C', 'D', 'E']
Schimbari_max = 3
Schimbari_efectuate =input('Selectati jucatorul care paraseste terenul: ')

if Schimbari_efectuate in jucatori:
       jucator_nou = input('Selectati jucatorul care intra pe teren:')
       jucatori.append(jucator_nou)
       jucatori.pop(jucatori.index(Schimbari_efectuate))
       Schimbari_max= Schimbari_max-1
       print(f'A intrat jucatorul {jucator_nou} si a iesit jucatorul {Schimbari_efectuate}. Mai aveti:{Schimbari_max} schimbari')
       print(jucatori)
else:
       print(f' Nu se poate efectua schimbarea deoarece jucatorul {Schimbari_efectuate} nu se afla pe teren')
       print(f'Mai aveti :{Schimbari_max} schimbari')

jucatori = ['A', 'B', 'C', 'D', 'E']
Schimbari_max = 3
Schimbari_efectuate =int(input('Schimbari efectuate: '))
Schimabari_ramase= Schimbari_max - Schimbari_efectuate
try:
     if 'B' in jucatori and Schimbari_efectuate < 3:
       jucatori.remove('B')
       jucatori.insert(2,'x')
       print(f'A intrat jucatorul x si a iesit jucatorul B. Mai aveti:{Schimabari_ramase} schimbari')
       print(jucatori)
except Schimbari_efectuate >= 3:
       print('Nu mai aveti schimbari ramase')
else:
     if 'B' not in jucatori:
       print(' Nu se poate efectua schimbarea deoarece jucatorul B nu e in teren')
       print(f'Mai aveti :{Schimabari_ramase} schimbari')

#Printati cei 3 elevi si notele lor Ex: ‘Ana a luat nota {x}’ Doar nota o veti lua folosindu-va de cheie

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
#practic vreau sa afisezi '{var_pt_cheie} a luat nota {var_pt_valoare}' folosindu`te de for si construindu`ti tu variabilele astea 2)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
for keys in dict1:
    print(f'{keys} a luat nota {dict1[keys]}')




zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica', 'altceva'}
if weekend & zile_sapt== weekend:
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')



#ex16
# Given the string "fox, cat, cow, horse". Display the following message "You found your dog" if 'dog' is in the string,
# otherwise print the last animal from the string

str = 'fox, cat, cow, horse'
if 'dog' in str:
    print('You found your dog')
else:
    str2 = str.split(', ')
    print(str2[-1])

#ex17

L = float(input('lungime='))
l = float(input('latime='))
i = float(input('inaltine='))
volum = l*L*i
print(volum)
print(f'Volumul cubului este {volum}')

#ex.20
str = 'Coral is either the stupidest animal or the smartest rock'
x = int(input('x='))
print(str[:-x])

# varianta 1
x = int(input('x='))
y = int(input('y='))
z = int(input('z='))

if x % 2 == 0 and y % 2==0 and z % 2 == 0:
    print('3 numare sunt pare')
elif  x % 2 == 0 and y % 2==0 or x%2==0 and z%2==0 or y%2==0 and z%2==0:
    print('2 numere sunt pare')
elif z % 2 == 0 or x % 2 == 0 or y % 2 == 0:
    print('1 numer este par')
else:
    print('Nu sunt numere pare')

'''
# TEMA 3

#ex1
'''
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si,', 'do']
print(note_muzicale)
note_muzicate_inverse = note_muzicale[::-1]
print(note_muzicate_inverse)
note_muzicate_inverse.reverse()
print(note_muzicate_inverse)
#ex2
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si,', 'do']
print(note_muzicale.count('do'))
print(f'Do apare de {note_muzicale.count("do")}')

#ex3
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
noua_lista = lista1 + lista2
print(noua_lista)
lista1.extend(lista2)
print(lista1)

#ex4
lista1.sort()
print(lista1)
lista1.remove(0)
print(lista1)

#ex5
if len(lista1) <= 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

 #ex6

lista1.clear()
print(lista1)

#ex7
if len(lista1) <= 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')
#ex8
dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
print(dict1.keys())
#ex9
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
#varianta2

for keys in dict1:
    print(f"{keys} a luat nota {dict1[keys]}")

#ex10

dict1['Dorel'] = 6
print(dict1)

#ex11
del dict1['Gigel']
print(dict1)
dict1['Ionica'] = 9
print(dict1)

#ex12
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)
#ex13
if weekend.issubset(zile_sapt):
     print('Weekend este un subset')
else:
    print('Weekend  nu este un subset')

#ex14
print(zile_sapt - weekend)
#ex15
print(zile_sapt & weekend)

#ex16

jucatori = ['a', 'b', 'c', 'd', 'e']
schimbari_max = 3
schimbari_efectuate = input('jucatorul care iese este:')

if schimbari_efectuate in jucatori:
    jucator_nou = input('jucatorul care intra este:')
    jucatori.append(jucator_nou)
    jucatori.pop(jucatori.index(schimbari_efectuate))
    print(jucatori)
    schimbari_max = schimbari_max -1
    print(f"A iesit jucatorul {schimbari_efectuate} si a intrat jucatorul {jucator_nou}")
    print(f"mai aveti {schimbari_max} schimbari")
else:
    print(f"Nu se poate efectua schimbarea deoarece jucatorul {schimbari_efectuate} nu e in teren")
'''
#ex17

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_e = []
for fruit in fruits:
    if 'e' in fruit:
        fruits_with_e.append(fruit)
        print(fruits_with_e)

#ex18

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fructe = []
for fruit in fruits:
    if len(fruit) == 6:
        fructe.append(fruit)
        print(fructe)
        print(f'Fructele cu 6 caractere sunt{fructe}')
