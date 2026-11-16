codigo = int(input("Digite um codigo numérico: "))
while codigo != 2468:
    print("Código inválido! Digite novamente.")
    codigo = int(input("Digite um codigo numérico: "))
while codigo == 2468:
    print("Código correto! Acesso permitido.")
    break

