print(10*'-=-')
print('    Anliasador de Triângulo    ')
print(10*'-=-')

r1 = float(input('Informe a reta r1: '))
r2 = float(input('Informe a reta r2: '))
r3 = float(input('Informe a reta r3: '))
if r1 < (r2+r3) and r2 < (r1+r3) and r3 < (r1+r2):
    print('As retas {},{} e {} PODEM formar um triângulo'.format(r1,r2,r3))
else:
    print('As retas {}, {} e {} NÃO podem formar um triângulo'.format(r1,r2,r3))