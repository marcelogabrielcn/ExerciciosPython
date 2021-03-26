from datetime import date, datetime

trabalhador = {}

trabalhador['nome'] = str(input('Digite o nome do trabalhador: '))
nasc = int(input('Digite o ano de nascimento: '))
idade = datetime.now().year - nasc
trabalhador['idade'] = idade
trabalhador['carteira'] = int(input('Carteira de trabalho (0 se não tiver) '))
if trabalhador['carteira'] > 0:
    trabalhador['contratação'] = int(input('Ano de contratação: '))
    trabalhador['salario'] = float(input('Salário: R$'))
    trabalhador['aposentadoria'] = (trabalhador['contratação'] + 35) - datetime.now().year
for k, v in trabalhador.items():
    print(f'{k} tem valor {v}')
print('Fim')
