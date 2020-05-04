#calculadora de dos términos
import sys, os
import math

def f():
    os.system('cls')
    print('-Raíz cuadrada-')
    dn1 = float(input('Digite el n: '))
    ans = math.sqrt(dn1)
    print(ans)
def e():
    os.system('cls')
    print('-Potenciar-')
    dn1 = float(input('Digite el n1: '))
    dn2 = float(input('Digite el n2: '))
    ans = dn1 ** dn2
    print(ans)
def d():
    os.system('cls')
    print('-División-')
    dn1 = float(input('Digite el n1: '))
    dn2 = float(input('Digite el n2: '))
    ans = dn1 / dn2
    print(ans)
def b():
    os.system('cls')
    print('-Resta-')
    dn1 = float(input('Digite el n1: '))
    dn2 = float(input('Digite el n2: '))
    ans = dn1 - dn2
    print(ans)
def c():
    #Multi
    os.system('cls')
    print('-Multiplicación-')
    dn1 = float(input('Digite el n1: '))
    dn2 = float(input('Digite el n2: '))
    ans = dn1 * dn2
    print(ans)

def a():
    #Sumar :P
    os.system('cls')
    print('-Suma-')
    dn1 = float(input('Digite el n1: '))
    dn2 = float(input('Digite el n2: ')) 
    ans = dn1 + dn2

    print(ans)

def menu():
    os.system('cls')
    print('Calculadora')
    print('')
    print('')
    print('1- Sumar')
    print('2- restar')
    print('3- Multiplicar')
    print('4- dividir')
    print('5- Potenciar')
    print('6- Raíz cuadrada')

    op = input('¿Que quieres hacer? ')

    if op == '1':
        a()
    if op == '2':
        b()
    if op == '3':
        c()
    if op == '4':
        d() 
    if op == '5':
        e()
    if op == '6':
        f()
menu()