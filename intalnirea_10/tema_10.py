#ex.1 Avand o lista de clienti, folosindu`va de dict comprehension implementati un giveaway unde fiecare client primeste un discount aleatoriu (intre 1 - 100%)
#customers = ["Alex","Bob","Carol","Dave","Eugen"]
#examplu output: {'Alex': 15, 'Bob': 23, 'Carol': 90, 'Dave': 78, 'Eugen': 51}
print('Ex1')
#varianta clasica:
'''
customers = ["Alex", "Bob", "Carol", "Dave", "Eugen"]
import random
discount_dict = {}
for customer in customers:
    discount_dict[customer] = random.randint(1, 100)

print(discount_dict)
'''
#dict comprehension:

import random
customers = ["Alex", "Bob", "Carol", "Dave", "Eugen"]
discount_dict = {customer: random.randint(1, 100) for customer in customers}
print(discount_dict)

#ex2 Calculati produsul numerelor prime de 2 cifre cu ajutorul filter si reduce
print('Ex2')

def is_prime(i):
         for j in range(2, i):
           if i % j == 0:
               return False
         else:
               return True

list_of_prime_nr=list(filter(is_prime, range(10,100)))
print(list_of_prime_nr)

from functools import reduce
def add(a,b):
    return a*b
the_product = reduce(add,list_of_prime_nr)
print(the_product)

#3 Folosindu`va de lambda impreuna cu map/filter/reduce calulati suma numerelor divizibile cu 7 dintre primele 100 numere naturale
print('Ex3')
'''
def is_divisible(nr):
    return nr % 7 == 0
divisible_list = list(filter(is_divisible, range(1,101)))
print(divisible_list)

def sum(a,b):
    return a+b
the_sum = reduce(sum,divisible_list)
print(the_sum)
'''

divisible_list = list(filter(lambda nr: nr % 7 == 0, range(1, 100)))
print(divisible_list)
print(reduce(lambda nr1, nr2: nr1 + nr2, divisible_list))
