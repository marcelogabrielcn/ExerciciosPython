alunos = []
ltemp = []  # Lista temporária para armazenar nomes
ltemp2 = []  # Lista temporária para armazenar notas dentro de nomes
print('-=-' * 10)
logo = 'ESCOLA DE PYTHON'
print(f'{logo:^30}')
print('-=-' * 10)
print('Vamos cadastrar alguns alunos e suas notas.')
while True:
    ltemp.append(str(input('Digite o nome do aluno: ').capitalize()))
    ltemp2.append(float(input('Digite a primeira nota: ')))
    ltemp2.append(float(input('Digite a segunda nota: ')))
    ltemp.append(ltemp2[:])
    alunos.append(ltemp[:])
    ltemp.clear()
    ltemp2.clear()
    continuar = str(input('Quer continuar? (S/N) ')).strip()[0].upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? (S/N) '))
    if continuar == 'N':
        break
print('-=-' * 10)
print('No. NOME           MÉDIA')
for a, d in enumerate(alunos):  # a = numeros dos alunos d = dados dos alunos
    print(f'{a + 1:<4}', end='')
    print(f'{d[0]:<15}', end='')


    #for i, al in enumerate(d):  # i = índice al = dados dos alunos [0] = nome
        #print(al)
