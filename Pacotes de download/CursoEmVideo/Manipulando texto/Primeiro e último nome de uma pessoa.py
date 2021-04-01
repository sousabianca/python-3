nome = input('Informe seu nome inteiro: ').strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
