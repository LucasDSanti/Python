n: int
soma: float = 0

n = int(input("Qual a ordem da matriz: "))

matriz: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
   for j in range(n):
      matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

for i in range(n):
   for j in range(n):
      soma = soma + matriz[i][j]

print(f"Soma dos valores da matriz: {soma:.2f}")