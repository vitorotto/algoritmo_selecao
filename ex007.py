# Vitor Hugo Otto

""" Ler 3 valores e informar qual o menor dos três """

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))

""" if v1 < v2 and v1 < v3:
    print(v1, "é o menor")
if v2 < v1 and v2 < v3:
    print(v2, "é o menor")
if v3 < v1 and v3 < v2:
    print(v3, "é o menor") """

# ----------- forma mais eficiente: --------------- #

if v1 < v2 and v1 < v3:
    print ("menor =", v1)
else:
    if v2 < v3: # and v2 < v1:
        print("menor =", v2)
    else:
        # if v3 < v2 and v3 < v1:
            print("menor =", v3)


