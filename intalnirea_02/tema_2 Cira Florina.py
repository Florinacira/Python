#ex1
#Instructiunea if verifica valoarea de adevar si executa instructiunea daca aceasta valoare este adevarata,
# iar else executa cealalta instructiune in cazul in care prima nu e adevarata.

#ex2
x2 = int(input('Intoduceti un numar:'))
if x2>0:
    print('Numarul este pozitiv')
else:
    print('Numarul este negativ')

#ex3
x3 = int(input('Intoduceti un numar:'))
if x3==0:
    print('Numarul este neutru')
elif x3>0:
    print('Numarul este pozitiv')
else:
    print('Numarul este negativ')

#ex4
x4 = int(input('Intoduceti un numar:'))
if x4>-2 and x4<13:
    print('Numarul este cuprins intre-2 si 13')
else:
    print('Numarul nu este cuprins intre -2 si 13')

#ex5
x = 10
y = 8
n = x-y
print(n)
if n<5:
    print('Diferenta e mai mica decat 5')
else:
    print('Diferenta e mai mare decat 5')

#ex6
#Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

x = int(input('Introduceti un numar:'))
if not(x>5 and x<27):
    print(' x nu este intre 5 si 27')
else:
    print('x este intre 5 si 27')

#ex7
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

x = int(input('Introduceti un nr:'))
y = int(input('Introduceti un nr:'))
if x==y:
    print('x egal cu y')
elif x>y:
    print('x este mai mare')
else:
    print('y este mai mare')

#ex8
X, y, z - laturile unui triunghi
Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

x = float(input('latura 1:'))
y = float(input('latura 2:'))
z = float(input('latura 3:'))
if x==y and y==z:
    print('Triunghiul este echilateral')
elif x==y and y!=z:
    print('Triunghiul este isoscel')
else:
    print('Triunghiul este oarecare')

#ex9 Citeste o litera de la tastatura
#Verifica si afiseaza daca este vocala sau nu

n = str(input('Introduceti o litera:'))
n_vocale = 'a, e, i, o, u'
if n in n_vocale:
    print('Litera este o vocala')
else:
    print('Litera este o consoana')
    
#ex10
n = float(input('Introduceti nota: '))
if n>9:
    print('A')
elif n>8:
    print('B')
elif n>7:
    print('C')
elif n>6:
    print('D')
elif n>4:
    print('E')
else:
    print('F')



'''
#ex14  x, y, z (int)
#Afiseaza care este cel mai mare dintre ele?

x = int(input('x='))
y = int(input('y='))
z = int(input('z='))
if x>y and x>z:
    print('X este mai mare')
elif y>x>z:
    print('Y este mai mare')
else:
    print('Z este mai mare')

'''