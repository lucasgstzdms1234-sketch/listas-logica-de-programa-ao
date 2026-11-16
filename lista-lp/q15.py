n = int(input("Digite números inteiros (0 para sair): "))
soma = 0
while n != 0:
    soma = soma + n
    n = int(input("Digite números inteiros (0 para sair): "))
print(f"A soma de todos os números é: {soma}")