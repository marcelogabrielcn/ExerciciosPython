def area(a, b):
    area = a * b
    print(f'\nA área desse do terreno {a} x {b} é igual a {area}m²')


print('Controle de terrenos')
print('-=-' * 7)
lar = float(input('Digite a largura do terreno (m): '))
comp = float(input('Digite o comprimento do terreno (m): '))
area(lar, comp)
