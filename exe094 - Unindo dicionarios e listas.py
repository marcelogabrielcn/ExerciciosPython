pessoa = {}
pessoas = []
medIdade = 0

while True:
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoa['sexo'] = str(input('Sexo (M/F): ')).strip()[0].upper()
    pessoa['idade'] = int(input('Idade: '))
    medIdade += pessoa['idade']
    pessoas.append(pessoa.copy())
    pessoa.clear()
    continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    while continuar not in 'SN':
        print('Oops, não entendi. Digite SIM ou NÃO.')
        continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    if continuar == 'N':
        break

print('-=-' * 10)
print(f'Ao todo foram cadastradas {len(pessoas)} pessoas.')
print(f'A média de idade das pessoas é {medIdade/len(pessoas):.1f} anos.')
