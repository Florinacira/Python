#ex1
# Write a function that takes as argument a natural number and prints all numbers between 0 and itself
def nat_number(nr):
    for elem in range(1,nr):
        print(elem)
nat_number(7)

# Modify the previous function to return the numbers inside a list instead

def nat_number(nr):
    number_list = []
    for elem in range(1, nr):
        number_list.append(elem)
    return number_list
r = nat_number(7)
print(r)

#ex2
# Write a function that takes as argument a natural number x and an optional argument natural number y
#(that if not passed, takes as default value 2). The function which will print the result of x to the power y
# as a verbose f-string: "The result of x={} to the power of y={} is:{} "
def nat_number(x,y=2):

    n = x ** y
    print(f'The result of x={x} to the power of y={y} is:{n}')

nat_number(2,4)

#ex3
# Write a function that has one string argument and creates a substring made of the first, middle and last character of the string
# e.g.:  substring('Michael') => 'Mhl'
#        substring('Adrian')  => 'Arn' / 'Ain' (either one works)

def string(str):
     substr = str[0] + str[len(str)//2] + str[-1]
     print(substr)

string('Florina')

#ex4
# Given 2 strings as arguments s1 and s2, write a function that appends s2 in the middle of s1
# e.g.:  append_middle('Legendary', 'wait')  => 'Legewaitndary'
#  append_middle('mama', 'MIA')  =>  'maMIAma'

def append_middle(s1, s2):
    middle_s1 = len(s1)//2
    result = s1[:middle_s1] + s2 + s1[middle_s1:]
    print(result)

append_middle('mama','RO')


# Write a function that takes any number of string arguments and will return the string formed
# from the arguments separated by -
# e.g.: coma_separated('one', 'two', 'three') => 'one-two-three'
# coma_separated('one', 'two', 'three', 'four', 'five') => 'one-two-three-four-five'

def coma_separated (*args):
    result = ''
    for arg in args:
        result +=  arg + '-'
    print(result[:-1])

coma_separated('one','two','three')
coma_separated('one', 'two', 'three', 'four', 'five')