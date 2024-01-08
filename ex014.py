import math

a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))

if a == 0:
  print("Não é uma equação do segundo grau")
else:
  delta = b * b - 4 * a * c
  if delta < 0:
    print("Raizes imaginárias")
  else:
    r1 = (- b + math.sqrt(delta)) / (2 * a)
    r2 = (- b - math.sqrt(delta)) / (2 * a)
  print(" as raízes são %.2f e %.2f" %(r1, r2))
