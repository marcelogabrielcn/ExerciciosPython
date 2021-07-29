from time import sleep

def leiaInt(txt):
    ok = False
    num = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            num = int(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return num


def leiaFloat(txt):
    ok = False
    num = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():
            num = float(n)
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
        if ok:
            break
    return num


# Programa principal
nI = leiaInt('Digite um número Inteiro: ')
nR = leiaFloat('Digite um número Real: ')
sleep(1)
print(f'O número Inteiro digitado foi: {nI}')
print(f'O número Real digitado foi: {nR}')

