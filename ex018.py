#Vitor Hugo Otto

""" 
Um posto está vendendo combustíveis conforme os critérios de descontos abaixo. 

a) Álcool:
• até 20 litros, desconto de 3% por litro
• a partir de 20 litros, desconto de 5% por litro

b) Gasolina:
• até 20 litros, desconto de 4% por litro
• a partir de 20 litros, desconto de 6% por litro

c) Diesel:
• até 20 litros, desconto de 5% por litro
• a partir de 20 litros, desconto de 7% por litro
 """

gas = input("Qual o tipo de combústivel desejado? (D - Diesel, G - Gasolina ou A - Alcool)") ; gas.upper()
l = float(input("Qunatos litros você deseja?"))

a = 5.87
d = 6.45
g = 6.89

if gas == "A":
    if l <= 20:
        custo = l * a * 0.97
    else:
        custo = a * l * 0.95
if gas == "D":
    if l <= 20:
        custo = d * l * 0.96
    else:
        custo = d * l * 0.94
if gas == "G":
    if l <= 20:
         custo = g * l * 0.95
    else:
        custo = g * l * 0.93        
print("O valor total a pagar é R$%.2f" %custo)