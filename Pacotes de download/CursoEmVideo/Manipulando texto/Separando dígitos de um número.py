num = int(input('Digite um número: '))
n = str(num)
print('Analisando o número {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
#print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(n[3], n[2], n[1], n[0]))
