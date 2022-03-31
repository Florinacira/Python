#ex1
#Functie care sa calculeze si sa returneze suma a 2 numere

def sum (nr1, nr2):
   return (f'Suma este {nr1 + nr2}')
raspuns = sum (8,9)
print(raspuns)

#ex2
#Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def functie(numar):
    if numar % 2 == 0:
        return True
    else:
        return False

raspuns=functie(9)
print(raspuns)

#ex3   Functie care returneaza numarul total de caractere din numele tau complet.

def  name(nume, prenume, nume_mijlociu):
    return f"Numele complet are {len(nume+prenume+nume_mijlociu)}"
answer = name('Cira','Florina', 'Ancuta')
print(answer)

#ex4
# Functie care returneaza aria dreptunghiului
def aria_dreptunghiului(L,l):
    aria = int(L) * int(l)
    return f'Aria dreprunghiului este {aria}'
raspuns = aria_dreptunghiului(75,32)
print(raspuns)
#ex5

#Functie care returneaza aria cercului
def aria_cercului(raza):
    import math
    aria = math.pi*(raza**2)
    return f'Aria cercului este {aria}'
raspuns = aria_cercului(2)
print(raspuns)

#ex6

#Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

def string(str):
    caracter = input('Introduceti un caracter:')
    if caracter  and caracter.upper() in str:
        return True
    else:
        return False
answer = string('Florina')
print(answer)


#ex7

def upper_lower(string):
    str_lower = 0
    str_upper = 0
    for character in string:
        if character.islower():
           str_lower += 1
        if character.isupper():
            str_upper += 1
    print(f"Nr de caractere lower case este:{str_lower}")
    print(f"Nr de caractere upper case este:{str_upper}")
upper_lower('Eu Invat Python')

#ex8
# Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
def list_of_numbers(*args):
    positive_numbers = []
    for nr in args:
        if nr >= 0:
            positive_numbers.append(nr)
    return positive_numbers

answer = list_of_numbers(3,6,-7,9,-5,4,3,-1,0)
print(answer)

#ex9

def numbers(x,y):
    if x > y:
        print(f'Primul numar {x} este mai mare decat al doilea nr {y}')
    elif y > x:
        print(f'Al doilea numar {y} este mai mare decat primul nr {x}')
    else:
        print('Numerele sunt egale')

numbers(6,9)
numbers(0,0)
numbers(7,3)

#10

def numbers_and_set(nr,*args):
    for elem in args:
        if nr not in args:
            print('Am adaugat numarul nou in set.')
            return True
        else:
            print('Nu am adaugat numarul in set.Acesta exista deja.' )
            return False

numbers_and_set(7,8,7,6)

#ex11
#Functie care primeste o luna din an si returneaza cate zile are acea luna

def days_of_months(months):
    for month in months:
        if month=='1' or month=='3' or month=='5' or month=='7' or month=='9' or month== '11':
            return 'Luna are 31 de zile'
        elif month=='2':
            return 'Luna are 28 de zile'
        else:
            return 'Luna are 30 de zile'

a=days_of_months('7')
b=days_of_months('9')
print(a)
print(b)
 #varianta 2

def days_of_months(month):
    import calendar
    a = calendar.monthrange(2021, month)
    return (f'Luna are {a[1]} zile')


ras = days_of_months(9)
print(ras)

#ex12

def calculator(nr1,nr2):
    a = nr1 + nr2
    b = nr1 - nr2
    c = nr1 * nr2
    d = nr1 / nr2
    return a, b, c, d
a,b,c,d = calculator(10, 2)
a,b,c,d = calculator(7, 3)
print(f'Suma:{a}')
print(f'Diferenta:{b}')
print(f'Inmultirea:{c}')
print(f'Impartirea:{d}')

#ex13

def list(lst):
    my_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
    for i in range(len(lst)):
     my_dict[lst[i]] = lst.count(lst[i])
    return my_dict

r = list([9, 7, 4, 3, 0, 2, 5 ,5,1])
print(r)

#ex14

def max_value (*args):
    for arg in args:
       return max(args)

a = max_value(6,9,3)
b = max_value(76,9,33)
print(a)
print(b)

#ex15

def sum_of_number(nr):
    sum = 0
    for i in range(0, nr+1):
      sum = sum +i
    return sum
s = sum_of_number(7)
s1 = sum_of_number(3)

print(s)
print(s1)

#ex16

def romanian_name(name):
   if name[-1] != 'a':
       print('Numele este de baiat')
   else:
       print('Numele este de fata')

romanian_name('Anca')
romanian_name('Alex')
romanian_name('Florina')
romanian_name('Bogdan')

#ex17

def my_lists(list1, list2):
   return (set(list1) & set(list2))

l = my_lists([1, 1, 2, 3],[2, 2, 3, 4])
l1 = my_lists([3,6,8,9],[3,8,4,1,0,5])
print(l)
print(l1)

#ex18

def discount_price(price, discount):
    dis = discount * price / 100
    sale_price = price - dis
    if discount > price:
      return 'Reducerea e invalida'
    else:
     return (f'Pretul redus este:{sale_price}')

product1 = discount_price(130,15)
product2 = discount_price(100,105)
print(product1)
print(product2)

#ex19

def date_time():
    import datetime
    now = datetime.datetime.now()
    print(now)

date_time()


#ex20

'''
def birthday_days():
    import datetime
    now = datetime.datetime.now()
    birth = datetime.date(1994, 5, 5)
    next_birthday_year = now.year
    next_birthday = datetime.date(next_birthday_year, birth.month, birth.day)
    print(next_birthday)
    days_until_birthday = next_birthday - now
    print(days_until_birthday)

birthday_days()'''
# aici nu reusesc sa rezolv

#ex21

def prime_number(nr):
    prim = True
    for i in range(2, nr):
         if nr % i == 0:
             prim = False
    return prim

nr1 = prime_number(17)
nr2 = prime_number(8)
print(nr1)
print(nr2)

#ex22

def list_of_prime_nr(a,b):
    lst = []
    for i in range(a, b+1):
         for j in range(2,i):
              if i % j == 0:
                    break
         else:
              lst.append(i)
    return lst
l = list_of_prime_nr(2,88)
print(l)

