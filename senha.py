senha: int
senhaCorreta: int = 2468

senha = int(input("DIgite sua senha: "))

while senha != senhaCorreta:   
   senha = int(input("SENHA INVÁLIDA! Digite sua senha novamente: "))

print("Acesso permitido")