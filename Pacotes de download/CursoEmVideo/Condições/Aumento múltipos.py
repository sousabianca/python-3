salario = float(input('Qual seu salário? '))
if salario <= 1250:
    aumento = salario + (salario * 10 / 100)
else:
    aumento = salario + (salario * 15 / 100)

print('Quem ganhava R$ {} passará a ganhar R$ {}'.format(salario, aumento))