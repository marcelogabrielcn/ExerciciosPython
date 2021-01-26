print('Olá, seja bem vindo a 2021!!!')
# ok = 'm'
sexo = str(input('\nPor gentileza digite seu sexo (M/F): ')).lower().strip()[0]
# print(sexo)
while sexo not in 'mf':
    print('Oops, acho que você digitou algo inválido. Tente novamente')
    sexo = str(input('\nPor gentileza digite seu sexo (m/f): ')).lower().strip()[0]
print('Obrigado!')
