#Exercício 003 ##08/12/2024
#Descobrindo o tipo do Input:

palavra = input("Digite uma palavra:")
print("O tipo primitivo do que você digitou é ", type(palavra))
print('Tem espaços?',palavra.isspace())
print('Há letras?', palavra.isalpha())
print('O que você digitou é um número?', palavra.isnumeric())
print('Tem números no que você digitou?', palavra.isalnum()) #O AlPHANUMÉRICO NÃO FUNCIONA
print('Há letras Maiúsculas?', palavra.isupper())
print('Há letras minúsculas?', palavra.islower())
print('Está capitalizado?', palavra.istitle())