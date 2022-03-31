#ex1
''' Functie care sa calculeze si sa returneze suma a 2 numere'''
def sum(nr1,nr2):
    s = nr1 +nr2
    return s

s1 = sum(7,9)
s2 = sum(88,13)
print(s1)
print(s2)

#ex2
'''Functie care sa returneze TRUE daca un numar este par, FALSE pt impar'''

def par_impar(nr):
    if nr % 2 ==0:
        return True
    else:
        return False

r = par_impar(7)
r1 = par_impar(88)
print(r1)
print(r)

#ex3
'''Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) '''

def number_of_character(nume,prenume,nume_mijlociu):
    for i in nume:
        n = len(nume+prenume+nume_mijlociu)
        return (f'Numele complet are {n} caractere')

r = number_of_character('Cira', 'Florina', 'Ancuta')
print(r)


#ex4
''' Functie care returneaza aria dreptunghiulu'''

def aria(L,l):
    a = L * l
    return (f'Aria dreptunghiului este: {a}')
a1 = aria(9,4)
a2 = aria(15,9)
print(a1)
print(a2)

#ex5
'''Functie care returneaza aria cercului'''

def aria_cerc (r):
    a = 3.14 *(r**2)
    return (f'Aria cercului este : {a}')
aria1 = aria_cerc(11)
aria2 = aria_cerc(4)
print(aria1)
print(aria2)

#ex6
'''Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu'''

def string(str):
    caracter = input('Introduceti un caracter:')
    if caracter and caracter.upper() in str:
        return True
    else:
        return False
answer = string('Florina')
print(answer)

#ex7
'''Functie fara return, primeste un string si printeaza pe ecran:
Nr de caractere lower case este x
Nr de caractere upper case exte y 
'''
def lower_upper(str):
    str_lower = 0
    str_upper = 0
    for i in str:
        if i.islower():
            str_lower += 1
        if i.isupper():
            str_upper += 1
    print(f'Nr de caractere lower case este {str_lower}')
    print(f'Nr de caractere upper case este {str_upper}')
lower_upper('Numele meu este Cira Florina ')

#ex8
'''Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive'''

def pozitive_list(list):
    lst = []
    for i in list:
        if i >= 0 :
            lst.append(i)
    return lst

r = pozitive_list([9,3,6,-8,-1,2,-4])
print(r)

#ex9
''' Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
Primul numar x este mai mare decat al doilea nr y
Al doilea nr y este mai mare decat primul nr x
Numerele sunt egale. '''

def number(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif x < y:
        print (f'Al doilea nr {y} este mai mare decat primul nr {x} ')
    else:
        print('Numerele sunt egale')
number(5,8)
number(0,0)

#ex10
'''Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False'''

def set_of_numbers(nr,set):
    for i in set:
        if nr not in set :
            set.add(nr)
            print('am adaugat numarul nou in set')
            return True
        else:
            print('nu am adaugat numarul in set. Acesta exista deja')
            return False
set_of_numbers(8,{8,4,2,1})

#ex11
'''Functie care primeste o luna din an si returneaza cate zile are acea luna'''
def month_days(month):
    if month in ('Ianuarie','martie','Mai','iulie', 'august', 'octombrie', 'decembrie'):
        return 'Luna are 31 de zile'
    elif month in ('aprilie', 'iunie', 'septembrie', 'noiembrie'):
        return 'Luna are 30 de zile'
    else:
        return 'Luna are 28 de zile'

l  = month_days('februarie')
l1 = month_days('martie')
l2 = month_days('iunie')
print(l)
print(l1)
print(l2)

#ex12
''' Functie calculator care sa returneze 4 valori 
Suma, diferenta, inmultirea, impartirea a 2 numere

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)'''

def calculator(nr1,nr2):
    a = nr1 + nr2
    b = nr1 - nr2
    c = nr1 * nr2
    d = nr1 / nr2
    return a,b,c,d
a,b,c,d,= calculator(10,2)
print(f'Suma:{a}')
print(f'Diferenta:{b}')
print(f'Inmultirea:{c}')
print(f'Impartirea:{d}')

#ex13
'''Functie care primeste o lista de cifre (adica doar 0-9)
Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare litera
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
'''

def list_nr(lst):
    dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in range(len(lst)):
        dict[lst[i]] = lst.count(lst[i])
        return dict
l = list_nr([1, 3, 1, 5, 9, 7, 7, 5, 5])
print(l)

#ex14
'''Functie care primeste 3 numere
Returneaza valoarea maxima dintre ele'''

def max_value(nr1,nr2,nr3):
    return (f'Valoarea maxima este:{max(nr1,nr2,nr3)}')
m = max_value(8,4,9)
print(m)

#ex15
'''Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
Ex: daca dam nr 3
Suma va fi 6 (0+1+2+3)
'''
def sum_nr(nr):
    sum = 0
    for i in range(nr+1):
        sum += i
    return sum

s = sum_nr(7)
print(s)

#ex16
'''Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
‘Numele este de baiat’ sau ‘Numele este de fata’'''

def name(nume):
    if nume[-1] == 'a':
        print('Numele este de fata')
    else:
        print('Numele este de baiat')
name('Florina')
name('Bogdan')
#ex17
'''Functie care primesete 2 liste de numere (numerele pot fi dublate)
Returnati numerele comune 

Ex:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}'''

def list_of_nr(lst1,lst2):
    lst3 = set(lst1) & set(lst2)
    return lst3
lst = list_of_nr([1, 1, 2, 3],[2, 2, 3, 4] )
print(lst)

#ex18
''' Functie care sa aplice o reducere de pret
Daca produsul costa 100 lei si aplicam reducere de 10%
Pretul va fi 90
Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida'''

def price_discount(price,discount):
    dis = discount * price/100
    p = price - dis
    if discount > price:
        return ('Reducerea e invalida')
    else:
        return(f'Pretul redus este:{p}')

p1 = price_discount(100,10)
p2 = price_discount(340,25)
print(p1)
print(p2)

#ex19
''' Functie care sa afiseze data si ora curenta'''

def date_time():
    import datetime
    now = datetime.datetime.now()
    print(now)
date_time()

#ex20
'''Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
'''
def birth_days():
    import datetime
    now = datetime.datetime.now()
    birth = datetime.datetime(1994,5,5)
    next_birthday = datetime.datetime(2022,5,5)
    days_until_birthday = next_birthday - now
    print(days_until_birthday.days+1)

birth_days()

#ex21
'''Scrieti o functie care verifica daca un numar natural dat ca argument este sau nu prim.
!Un numar e prim daca se imparte exact NUMAI la 1 si la el insusi (nu are niciun alt divizor)!
Ex: is_prime(17) => True
      is_prime(8) => False'''

def prime_nr(nr):
    for i in range(2, nr):
        if nr % i == 0:
            return False
        else:
            return True
r  = prime_nr(7)
r1 = prime_nr(22)
print(r)
print(r1)

#ex22
'''Creati o functie care are ca parametrii 2 numere naturale  a,b cu a<b si returneaza lista formata din numerele prime din intervalul [a,b]
Ex: list_of_primes_in_interval(3, 31) =>  [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]'''
def prime_list(a,b):
    lst = []
    for i in range(a, b+1):
        for j in range(2,i):
           if i % j == 0:
              break
        else:
           lst.append(i)
    return lst
raspuns = prime_list(2,89)
print(raspuns)
