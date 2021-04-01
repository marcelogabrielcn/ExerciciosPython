from time import sleep


def verificamaior(* num):
    print('Verificando os valores passados...')
    sleep(2)
    if len(num) > 0:
        for n in num:
            print(n, end=' ')
            sleep(0.5)
        print(f'\nForam informados {len(num)} valores.')
        print(f'Dentre eles, o maior valor é {max(num)}\n')
    else:
        print(f'\nForam informados 0 valores.')
        print(f'Dentre eles, o maior valor é 0\n')


print('Olá, bem vindo ao verificador do maior número\n')
verificamaior(1, 4, 6, 2, 9, 8, 4, 6, 743, 9)
verificamaior(9, 32, 236, 2236, 237, 270, 0)
verificamaior(0, 1, -414)
verificamaior()
