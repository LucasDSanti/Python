n: int

n = int(input("Qual a ordem da matriz: "))

matriz: [[float]] = [[0 for x in range(n)] for x in range(n)]

for i in range(n):
   for j in range(n):
      matriz[i][j] = float(input(f"Elemento [{i},{j}]: "))

print("Valores da diagonal principal: ")

for i in range(n):
   print(f"{matriz[i][i]}")