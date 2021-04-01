n: int
produto: int

n = int(input("Deseja a tabuada para qual valor (até 20): "))

for i in range(1, 21):
   produto = n * i
   print(f"{n} * {i} = {produto}")