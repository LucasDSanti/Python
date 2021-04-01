n: int
fatorial: int = 1

n = int(input("Digite um valor para descobrir seu fatorial: "))

for i in range (n, 0, -1):
   fatorial = fatorial * i

print(f"Fatorial: {fatorial}")