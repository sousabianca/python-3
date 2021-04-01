vcasa = float(input('Qual o valor da casa? R$ '))
salario = float(input('Qual seu salário mensal? R$ '))
ano = int(input('Quantos de financiamento? '))
prestacao = vcasa / (ano * 12)
print('Para pagar uma casa de R$ (:.2f) em {} anos a prestação sera R$ {:.2f}'.format(vcasa,ano, prestacao))


