#Vitor Hugo Otto

""" Escrever um programa em Python que leia o nome, a idade, o peso e a altura de
uma pessoa e mostre sua condição de acordo com a tabela abaixo. Essa tabela
somente é válida para pessoas adultas (idade entre 18 e 65 anos). """

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

if idade >= 18 and idade <= 65:
    
    peso = float(input("Informe seu peso atualmente: ")) 
    altura = float(input("Informe sua altura: "))
    imc = peso / (altura * altura)

    if imc < 18.5:
        print("%s, seu IMC é %.2f, você está ABAIXO DO PESO." %(nome, imc))
    elif imc >= 18.5 and imc < 25:
        print("%s, seu IMC é %.2f, você está no PESO NORMAL." %(nome, imc))
    elif imc >= 25 and imc <= 30:
        print("%s, seu IMC é %.2f, você está ACIMA DO PESO." %(nome, imc))
    elif imc > 30:
        print("%s, seu IMC é %.2f, você está OBESO." %(nome, imc))
else:
    print("Só é possivel calcular em adultos (entre 18 e 65 anos).")