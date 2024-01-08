# Vitor Hugo Otto
# Calcular  o peso ideal de uma pessoa sabendo nome, sexo e altura.

nome = input("Digite seu nome: ")
sexo = input("Qual seu sexo M | F ")
altura = float(input("Qual sua altura? "))
sexo = sexo.upper()

if sexo == "M":
    peso = (72.2 * altura) - 58
else:
    peso = (61.2 * altura) - 44.7
    
print(nome, "seu peso ideal é %.2f" %peso)