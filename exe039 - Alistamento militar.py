from datetime import date
print('Bem vindo ao programa de Alistamento Militar do Brasil.')
idade = int(input('Informe seu ano de nascimento: '))
print('''Qual seu sexo:
[M] - Masculino
[F] - Feminino''')
sexo = str(input('Digite seu sexo: ')).upper()
if sexo == 'F':
    print('Você não precisa participar do alistamento obrigatório')
else:
    anoatual = date.today().year
    if anoatual - idade == 18:
        print('Você completa 18 anos neste ano. Esta na hora de se alistar.')
    elif anoatual - idade > 18:
        passou = anoatual - idade - 18
        print('Ops, seu ano de alistamento foi a {} anos atrás'.format(passou))
    elif anoatual - idade < 18:
        falta = anoatual - idade - 18
        print('Bom, ainda faltam {} anos para seu alistamento.'.format(falta * -1))
print('O serviço militar agradece sua participação.')
