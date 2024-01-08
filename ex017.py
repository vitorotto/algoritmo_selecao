#Vitor Hugo Otto

""" Escrever um programa que leia 2 valores inteiros e um caractere e realize uma das quatro operações aritméticas básicas entre estes dois valores. A operação a ser realizada é dada pelo caractere (+, -, *, /). """
v1 = int(input("Insira o primeiro valor "))
v2 = int(input("Insira o segundo valor "))
oper = input("Qual operação deseja realizar? (+, -, *, /)")

if oper == "+":
    result = v1 + v2
elif oper == "-":
    result = v1 - v2
elif oper == "*":
    result = v1 * v2
    print("O resultado é: ", result)
elif oper == "/":
    if v2 == 0:
        print("Não é possivel dividir por zero.")
    else:
        result = v1 / v2
        print(" O resultado é:1 %.2f" %result)
else:
    print("Operação Invalida.")