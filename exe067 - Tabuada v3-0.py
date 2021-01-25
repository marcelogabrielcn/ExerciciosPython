print('-' * 40)
num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 40)
while num >= 0:
    for c in range(0, 11):
        print(f'{num} x {c:2} = {(num * c):2}')
    print('-' * 40)
    num = int(input('Digite um número para ver sua tabuada (valor negativo para sair): '))
    print('-' * 40)
print('Programa Tabuada V3 encerrado!')
