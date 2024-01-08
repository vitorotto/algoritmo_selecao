#Vitor Hugo Otto

""" Escrever um programa que solicite o nome e a idade de uma pessoa e informe a sua classe eleitoral de acordo com os seguintes critérios: """

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

if idade < 16:
    print("Não eleitor")
else:
    if (idade >= 16 and idade <= 17) or idade > 65:
        print("Eleitor facultativo")
    else:
        print("Eleitor obrigatório")