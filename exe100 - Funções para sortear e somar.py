from random import randint
from time import sleep


def sortear(lista):
    lista = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]
    print('Sorteando valores da lista:', end=' ')
    sleep(0.5)
    for n in lista:
        print(n, end=' ')
        sleep(0.5)
    return lista


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n


numeros = []
sortear(numeros)
