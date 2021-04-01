distancia = float(input('Qual a distância da viagem em KM? '))
if distancia <= 200:
    preco = distancia * 0.50
    print('O preço da passagem com a distância de {} km ficará R$ {:.2f}'.format(distancia, preco))
else:
   preco = distancia * 0.45
   print('O preço da passagem com a distância de {} km ficará R$ {:.2f}'.format(distancia,preco))
