print('Vamos analisar algumas informações\n')
continuar = 'S'
maior18 = 0
homens = 0
mulherjovem = 0

while continuar == 'S':

    idade = int(input('Digite a idade do participante: '))
    while idade < 0 or idade > 130:
        idade = int(input('Digite a idade do participante: '))
    if idade >= 18:
        maior18 += 1
    sexo = str(input('Digite o sexo do participante (M/F): ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo do participante (M/F): ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if idade < 20 and sexo == 'F':
        mulherjovem += 1
    continuar = str(input('\nQuer continuar? (S/N): ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('\nQuer continuar? (S/N): ')).strip().upper()
print('\nAnalisando as informações, temos o seguinte:\n')
print(f'    {maior18} pessoas são maior de idade.')
print(f'    {homens} homens foram cadastrados.')
print(f'    {mulherjovem} mulheres que participaram tem menos de 20 anos.')
print('\nFim do programa')
