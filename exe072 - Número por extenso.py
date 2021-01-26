print('Programa número por extenso')
veroutro = True
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
           'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete',
           'dezoito', 'dezenove', 'vinte')
while veroutro:
    imprimir = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))
    while imprimir < 0 or imprimir > 20:
        print('\nOops, tente novamente.')
        imprimir = int(input('Digite um número de 0 a 20 para vê-lo por extenso: '))
    print(numeros[imprimir])
    continuar = str(input('Quer ver outro número? (S/N)')).strip()[0]
    while continuar not in 'SNsn':
        print('Oops, digite sim (S) ou não (N)')
        continuar = str(input('Quer ver outro número? (S/N)')).strip()[0]
    if continuar in 'Nn':
        veroutro = False
print('Até logo!')
