from time import sleep

def contar(a, b, c):
    inicio = a
    fim = b
    passo = c
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    while inicio != fim:
        if inicio < fim:
            print(inicio, end=' ')
            sleep(0.5)
            inicio += passo
        elif inicio > fim:
            print(inicio, end=' ')
            sleep(0.5)
            inicio -= passo
    print(f'{fim} FIM!')


print('Bem vindo ao progama contador!\n')
print('Contando de 0 a 10')
contar(0, 10, 1)
print()
print('Contando de 10 a 0')
contar(10, 0, -1)
print()
print('Agora digite qual contagem você quer ver: ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contar(ini, fim, pas)
print()
print('Fim do programa')
