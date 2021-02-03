lista = []
continuar = True
while continuar:
    num = int(input('Digite um valor: '))
    if num not in lista:
        lista.append(num)
        print('Valor adicionado a lista com sucesso...')
    else:
        print('Ops, esse valor já foi adicionado...')
    cont = str(input('Quer continuar? (S/N) ')).strip()[0].lower()
    if cont not in 'sn':
        print('Ops, não entendi, digite Sim ou Não. (S/N)')
        cont = str(input('Quer continuar? (S/N) ')).strip()[0].lower()
    if cont == 'n':
        continuar = False
print('-=-' * 20)
lista.sort()
print(f'\nVocê digitou os valores {lista}')
