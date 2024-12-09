#programa teste
#08/12/2024

#exercício001
mensagem = "Hello World"
print(mensagem)

#exercício002
nome = input("Digite o seu nome: ")
print("O seu nome é: {}.Seja bem vindo!".format(nome))

#exemplo001
oi = input('OOII tudo bem?')
if (oi == 'oi'):
    print('olá')

else:
    print('você é um masqueico')

#exercício003
n1 = int (input('Digite um número: '))
n2 = int(input ('Digite outro número:'))
soma = n1+n2
print('A soma de {} e {} vale {}' .format(n1, n2, soma)) #não conhecia essa forma de exibir. Show de bola.

#exercício004
num1 = float(input('Digite um número;'))
print(type(num1))

#type bool = True or False #Não sabia até ontem