distancia: float
gasto: float
consumo: float

distancia = float(input("Informe a distância percorrida (em KM): "))
gasto = float(input("Informe a quantidade combustível gasto (em litros): "))

consumo = distancia/gasto
print(f"Consumo médio: {consumo:.3f} litros/KM")