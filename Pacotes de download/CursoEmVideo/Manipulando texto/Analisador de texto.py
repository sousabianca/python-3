nome = str(input('Digite seu nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print('O seu nome tem um total de {} letras'.format(len(nome)-nome.count(' ')))