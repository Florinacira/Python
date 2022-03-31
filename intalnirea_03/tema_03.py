
#ex1
my_list = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
print(my_list)
my_list1 = my_list[::-1]
print(my_list1)
my_list1.reverse()
print(my_list1)

#ex2
my_list = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si', 'do']
my_list.count('do')
print(f'Do apare de: {my_list.count("do")} ori.')

#ex3
list1 = [3, 1, 0, 2]
list2 = [6, 5, 4]
my_new_list = list1 + list2
print(my_new_list)
list1.extend(list2)
print(list1)

#ex4
my_new_list.sort()
print(my_new_list)
my_new_list.remove(0)
print(my_new_list)

#ex5
'''Folosind un if verificati lista generata la ex3 si afisati:Lista este goala,Lista nu este goala'''

if len(my_new_list) <= 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala')

#ex6

my_new_list.clear()
print(my_new_list)

#ex7

if len(my_new_list) <= 0:
    print('Lista este goala.')
else:
    print('Lista nu este goala')

#ex8
'''Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}.Folositi o functie ca sa afisati Elevii (cheile)'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())

#ex9
'''Printati cei 3 elevi si notele lor Ex: ‘Ana a luat nota {x}’ Doar nota o veti lua folosindu-va de cheie'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(f"Ana a luat nota {dict1['Ana']}")
print(f"Gigel a luat nota {dict1['Gigel']}")
print(f"Dorel a luat nota {dict1['Dorel']}")
#varianta2

for keys in dict1:
    print(f"{keys} a luat nota {dict1[keys]}")

#ex10
'''Dorel a facut contestatie si a primit 6.Modificati nota lui Dorel in 6.Printati nota dupa modificare'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
dict1['Dorel'] = 6
print(dict1)

#ex11
'''Gigel se transfera din clasa. Cautati o functie care sa il stearga. Vine un coleg nou. Adaugati Ionica, cu nota 9
Printati dictionarul schimbat.'''

dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
del dict1['Gigel']
print(dict1)
dict1['Ionica'] = 9

print(dict1)

#ex12
'''Adaugati in zilele_sapt ‘luni’.Afisati zile_sapt'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
zile_sapt.add('luni')
print(zile_sapt)

#ex13
'''Folositi un if si verificati daca  Weekend este un subset al zilelor din sapt, Weekend nu este un subset al zilelor din sapt
'''
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if weekend & zile_sapt:
    print('Weekend este un subset al zilelor din sapt')
else:
    print('Weekend nu este un subset al zilelor din sapt')
print(weekend.issubset(zile_sapt))

#ex14
'''Afisati diferentele dintre aceste 2 seturi'''

print(zile_sapt - weekend)

#ex15
'''Afisati intersectia elementelor din aceste 2 seturi'''

print(zile_sapt & weekend)

#ex16

jucatori = ['A', 'B', 'C', 'D', 'E']
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

#ex17

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list_fruits = []
for elem in fruits:
    if 'e' in elem:
        list_fruits.append(elem)
        print(list_fruits)

#ex18

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new_fruits = []
for x in fruits:
    if len(x) == 6:
        new_fruits.append(x)
        print(new_fruits)




