# Vitor Hugo Otto

""" Escrever um programa em Python que informe a placa de um carro e a
    velocidade medida pelo radar da polícia rodoviária. Sabe-se que na rodovia o
    limite de velocidade é de 80 km/h.

    No final exibir uma mensagem informando a placa do carro e se ele foi multado
    ou não. Caso ele tenha sido multado, informar a velocidade medida e o valor da
    multa a ser paga (com duas casas decimais).

    A multa por excesso de velocidade é calculada da seguinte forma:
    • caso a velocidade do carro medida seja menor ou igual a 20% acima do
    limite permitido, então a multa é calculada cobrando um valor fixo de R$
    50,00 mais R$ 8,25 por cada km/h acima do limite.
    • caso a velocidade do carro medida seja superior a 20% do limite permitido,
    então a multa a ser cobrada é um valor fixo de R$ 100,00 mais R$ 12,50 por
    cada km/h acima do limite. """

placa = input("Qual a placa do veículo? ")
vel_medida = float(input("Qual a velocidade medida no radar? (apenas números) "))
limite = 80

if vel_medida < limite:
    print("velocidade medida:", vel_medida)
    print("O veículo de placa %s não foi multado" %placa)
else:
    if vel_medida <= limite * 1.2:
       multa = (vel_medida - limite) * 8.25 + 50
       print("velocidade medida:", vel_medida)
       print("O veículo de placa %s será multado em R$ %.2f" %(placa, multa))
    else: 
        vel_medida > limite * 1.2
        multa = (vel_medida - limite) * 12.5 + 100
        print("velocidade medida:", vel_medida)
        print("O veículo de placa %s será multado em R$ %.2f" %(placa, multa))

