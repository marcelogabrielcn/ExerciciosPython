from random import randint
from time import sleep


def sortear(lista):
    sleep(1)
    print("Sorteando valores...")
    for cont in range(0, 5):
        lista.append(randint(0, 100))


def somaPar(lista):
    sleep(1)
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma += n
    print(f"Somando os valores pares da lista temos: {soma}")


numeros = []
sortear(numeros)
print(numeros)
somaPar(numeros)
