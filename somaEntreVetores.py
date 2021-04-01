n: int

n = int(input("Qual será o tamanho dos vetores: "))

vetorA: [float] = [0 for x in range(n)]
vetorB: [float] = [0 for x in range(n)]
vetorResultante: [float] = [0 for x in range(n)]

print("Valores do vetor A: ")

for i in range(n):
   vetorA[i] = int(input())

print("Valores do vetor B: ")

for i in range(n):
   vetorB[i] = int(input())

for i in range(n):
   vetorResultante[i] = vetorA[i] + vetorB[i]
   
print("Valores do vetor resultante:")

for i in range(n):
   print(vetorResultante[i])