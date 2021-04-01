nota1: float
nota2: float
notaFinal: float

nota1 = float(input("Digite a 1a nota: "))
nota2 = float(input("Digite a 2a nota: "))

notaFinal = (nota1 + nota2) / 2.00

if notaFinal < 6.00:
   print("REPROVADO!")
   print(f"Nota final: {notaFinal:.2f}")
else:
   print("APROVADO!")
   print(f"Nota final: {notaFinal:.2f}")