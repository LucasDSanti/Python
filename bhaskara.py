import math

valorA: float
valorB: float
valorC: float
delta: float
valorX1: float
valorX2: float

valorA = float(input("Valor do coeficiente A: "))
valorB = float(input("Valor do coeficiente B: "))
valorC = float(input("Valor do coeficiente C: "))

delta = (valorB * valorB) - (4 * valorA * valorC)

if delta < 0:
   print("Esta equação não possuí raízes reais!")
else:
   valorX1 = ((-valorB) + math.sqrt(delta)) / (2 * valorA)
   valorX2 = ((-valorB) - math.sqrt(delta)) / (2 * valorA)

   print(f"Valor de X1: {valorX1:.2f}")
   print(f"Valor de X2: {valorX2:.2f}")