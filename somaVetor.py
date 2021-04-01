n: int
soma: float = 0

n = int(input("Qual será o tamanho do vetor: "))

vetor: [float] = [0 for x in range(n)]

for i in range(n):
   vetor[i] = float(input("Digite os valores do vetor: "))
   soma = soma + vetor[i]

print(f"Soma dos valores do vetor: {soma:.2f}")