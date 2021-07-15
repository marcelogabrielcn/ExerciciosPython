def aumentar(valor, formatado=False, porcentagem=10):
    if formatado:
        valor = valor + ((valor / 100) * porcentagem)
        return moeda(valor)
    else:
        valor = valor + ((valor / 100) * porcentagem)
        return valor


def diminuir(valor, formatado=False, porcentagem=10):
    if formatado:
        valor = valor - ((valor / 100) * porcentagem)
        return moeda(valor)
    else:
        valor = valor - ((valor / 100) * porcentagem)
        return valor


def dobro(valor, formatado=False):
    if formatado:
        valor = valor * 2
        return moeda(valor)
    else:
        valor = valor * 2
        return valor


def metade(valor, formatado=False):
    if formatado:
        valor = valor / 2
        return moeda(valor)
    else:
        valor = valor / 2
        return valor


def moeda(n):
    formatado = f'R${float(n):.2f}'
    return formatado.replace('.', ',')


def resumo(num, aum: float, red: float):
    print('_' * 40)
    txt = 'RESUMO DO VALOR'
    print(f'{txt:>25}')
    print('_' * 40)
    print(f'Preço informado: {moeda(num):>25}')
    print(f'Metade do valor: {metade(num, True):>25}')
    print(f'Dobro do valor: {dobro(num, True):>25}')
    print(f'{aum}% de aumento: {aumentar(num, True, aum):>25}')
    print(f'{red}% de redução: {diminuir(num, True, red):>25}')

def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um valor inválido!\033[m')
        else:
            valido = True
            return float(entrada)
