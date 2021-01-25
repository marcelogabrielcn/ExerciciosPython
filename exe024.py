cidade = input('Digite o nome de qualquer cidade: ')
lista = cidade.split()
print(lista)
if 'Santo' in lista[0]:
    print('Essa cidade começa com Santo.')
else:
    print('Essa cidade não começa com Santo.')
