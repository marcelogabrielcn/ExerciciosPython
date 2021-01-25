from datetime import date
idade = (int(input('Digite o ano de nascimento do atleta: ')) - date.today().year) * -1
if idade <= 9:
    cat = "MIRIM"
elif idade <= 14:
    cat = 'INFANTIL'
elif idade <= 19:
    cat = 'JUNIOR'
elif idade <= 25:
    cat = 'SÊNIOR'
else:
    cat = 'MASTER'
print('O atleta tem {} anos e fará parte da categoria {}'.format(idade, cat))
