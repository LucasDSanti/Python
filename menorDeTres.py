valorA: int
valorB: int
valorC: int
menorValor: int

valorA = int(input("Informe o 1a valor: "))
valorB = int(input("Informe o 2a valor: "))
valorC = int(input("Informe o 3a valor: "))

if valorA < valorB and valorA < valorC:
   menorValor = valorA
elif valorB < valorC:
   menorValor = valorB
else:
   menorValor = valorC

print(f"Menor valor: {menorValor}")