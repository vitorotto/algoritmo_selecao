# Vitor Hugo Otto

""" Escrever um programa que leia 3 valores inteiros e calcule a média
ponderada considerando os seguintes pesos: 5 para o maior valor, 3 para o
valor intermediário e 2 para o menor valor."""

n1 = int(input("digite o primeiro valor"))
n2 = int(input("digite o segundo valor"))
n3 = int(input("digite o terceiro valor"))

if n1 < n2 and n1 < n3:
    menor = n1
    if n2 < n3:
        meio = n2
        maior = n3
    else:
       meio = n3
       maior = n2
else:
    if n2 < n3:
        menor = n2
        if n1 < n3:
            meio = n1
            maior = n3
        else:
            meio = n3
            maior = n3
print(menor, meio, maior)