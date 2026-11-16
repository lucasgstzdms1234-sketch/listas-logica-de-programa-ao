par = 0
for contador in range(1, 6):
    numero = int(input(f"Digite o {contador} numero inteiro: "))
    if numero % 2 == 0:
        par += 1

print(f"Quantidade de números pares: {par}")