import random
for c in range(1,5):
    nome = str(input('Digite o nome {}:'.format(c)))
lista = [nome]
escolhido = random.choice(lista)
print('O nome do aluno escolhido é {}'.format(random.choice(nome)))