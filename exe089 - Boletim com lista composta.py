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
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    med = (n1 + n2) / 2
    ltemp2.append(n1)
    ltemp2.append(n2)
    ltemp.append(med)
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
    print(f'{d[1]:.1f}')
print('-=-' * 10)
while True:
    expor = int(input('Quer mostrar a nota de qual aluno? (0 para sair) ')) - 1
    if expor == -1:
        print('Finalizando...')
        break
    if expor < 0 or expor > len(alunos) - 1:
        print('Digite um número válido, olhe na tabela o número correspondente ao aluno.')
        expor = int(input('Quer mostrar a nota de qual aluno? (0 para sair) ')) - 1
    print(f'Notas de {alunos[expor][0]}: {alunos[expor][2]}')
print('-=-' * 10)
print('PROGRAMA FINALIZADO')
