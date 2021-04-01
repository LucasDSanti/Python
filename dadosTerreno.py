largura: float
comprimento: float
valorMetroQuadrado: float
area: float
preco: float

largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
valorMetroQuadrado = float(input("Digite o valor do metro quadrado: R$"))

area = largura * comprimento
print(f"Área do terreno: {area:.2f} metros quadrados")

preco = area * valorMetroQuadrado
print(f"Preço do terreno: R$ {preco:.2f}")