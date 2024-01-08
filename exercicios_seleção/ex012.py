salario = float(input("Seu salário? "))
sal_min = float(input("Salário mínimo atual? "))

if salario < 3 * sal_min:
    novo_sal = salario + salario * 0.5
    #novo_sal = salario * 1.5
    print("50%% de aumento")
else: 
  if salario >= 3 * sal_min and salario <= 10 * sal_min:
      print("20%% de aumento")
  else:
     print("15%% de aumento")
