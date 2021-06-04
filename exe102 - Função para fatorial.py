def fatorial(num, show=False):
    '''
    fatorial(num, show=True)
        -> Calcula o fatorial de um número
        :param num: O número a ser calculado
        :param show: (Opcional), mostrar ou não a conta
        :return: O valor do fatorial de num
    '''
    if show:
        fat = 1
        i = 2
        print('1x2', end='')
        while i <= num:
            fat = fat * i
            i = i + 1
            print(f'x{i}', end='')
        return fat
    else:
        fat = 1
        i = 2
        while i <= num:
            fat = fat * i
            i = i + 1
        return fat


# Programa principal
print(f'Fatorial = {fatorial(5)}')
print(f' = {fatorial(5, True)}')
help(fatorial)