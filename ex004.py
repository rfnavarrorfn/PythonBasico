# Exercício Python 4: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

nome = input("Digite o seu nome: ")
print(type(nome))
print(nome.isspace())
print(nome.isnumeric())
print(nome.isalpha())
