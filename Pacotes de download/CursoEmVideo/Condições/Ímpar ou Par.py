n = int(input('Digite um número inteiro: '))
resultado = n % 2
if resultado == 0:
    print('O número {} é par'.format(n))
else:
    print('O número {} é ímpar'.format(n))