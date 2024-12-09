#08/12/2024 Exercício 2:
#Sistema de calculo simples em python
#O sistema é capaz de realizar operações matemáticas simples

import math
valor1 = int(input("Escolha um número:"))
valor2 = int(input("Escolha outro número:"))
soma = valor1 + valor2
subtracao = valor1 - valor2
multiplicacao = valor1 * valor2
divisao = valor1/ valor2 
escolher_operacao = int(input("Escolha qual operação você deseja realizar: (Digite 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão)"))

def escolha_operação(escolher_operacao):
    if(escolher_operacao == 1):
        print("O valor da soma entre {} e {} é: {}" .format(valor1, valor2, soma))
    elif(escolher_operacao == 2):
        print("O valor da subtração entre {} e {} é: {}" .format(valor1, valor2, subtracao))
    elif(escolher_operacao == 3):
        print("O valor da multiplicação entre {} e {} é: {}" .format(valor1, valor2, multiplicacao))
    elif (escolher_operacao == 4):
        print("O valor da divisão entre {} e {} é: {}" .format(valor1, valor2, divisao))
    else:
        print("O dado informado não é válido.")

escolha_operação(escolher_operacao)