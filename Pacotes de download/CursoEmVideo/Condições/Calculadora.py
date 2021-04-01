print("Escolha a opção da calculadora:"
      "(+) - Adição"
      "(-) - Subtração"
      "(*) - Multiplicação"
      "(/) - Divisão")
opcao = (input("Opção: "))
n1 = int(input("Informe n1: "))
n2 = int(input("Informe n2: "))
calc = 0
if opcao == '+':
    calc = (n1 + n2)
elif opcao == '-':
    calc = (n1 - n2)
elif opcao == '*':
    calc = (n1 * n2)
elif opcao == '/':
    calc = (n1 / n2)
else:
    print("Opção inválida, tente novamente!")
print('{} {} {} = {}'.format(n1, opcao, n2, calc))
