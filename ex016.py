# Vitor Hugo Otto

""" Escrever um programa que leia 3 valores inteiros e calcule a média
ponderada considerando os seguintes pesos: 5 para o maior valor, 3 para o
valor intermediário e 2 para o menor valor."""

v1 = float(input("digite o primeiro valor"))
v2 = float(input("digite o segundo valor"))
v3 = float(input("digite o terceiro valor"))

if v1 < v2 and v1 < v3: #Estrutura para saber qual o MENOR valor entre três valores distintos.
    menor = v1
else:
    if v2 < v3:
        menor = v2
    else:
        menor = v3

if v1 > v2 and v1 > v3: #Estrutura para saber qual o MAIOR valor entre três valores distintos.
    maior = v1
else:
    if v2 > v3:
        maior = v2
    else:
        maior = v3

# meio = v1 + v2 + v3 - maior - menor

if (v1 > v2 and v1 < v3) or (v1 >  v3 and v1 < v2):
    meio = v1

med_pond = (maior * 5 + meio * 3 + menor * 2) / (2 + 3 + 5)
print(med_pond)