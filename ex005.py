# Exercício Python 5: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

numero = int(input("Escreva um, número inteiro: "))
sucessor = int(numero + 1)
antecessor = int(numero - 1)
print("O número digitado foi {}, o seu sucessor é {} e o seu antecessor é {}".format(numero, sucessor, antecessor))
