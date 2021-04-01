velocidade = float(input('Velocidade  do carro: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7 # o - 80 é pra considerar somente o que foi excedido
    print('Você ultrapassou a velocidade permitida e sofrerá uma multa de {:.2f}'.format(multa))
else:
    print('Você está dentro dos padrões da velocidade.')