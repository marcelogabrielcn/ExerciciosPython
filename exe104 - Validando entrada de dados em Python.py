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


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
