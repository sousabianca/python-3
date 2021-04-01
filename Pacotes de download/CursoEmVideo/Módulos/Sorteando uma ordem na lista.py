from random import shuffle
a = str(input('Aluno 1: '))
b = str(input('Aluno 2: '))
c = str(input('Aluno 3: '))
lista = [a, b, c]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)