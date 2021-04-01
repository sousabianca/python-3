from random import randint
print(20*'-=')
print('   Adivinhando um Número entre 0 e 5   ')
print(20*'-=')
pc = randint(0,5)
numero = int(input('Em que número pensei? '))
print('Processando ...')
if numero == pc:
    print('Você acertou!!')
else:
    print('Você errou, eu pensei no número {} e não no número {}'.format(pc, numero))