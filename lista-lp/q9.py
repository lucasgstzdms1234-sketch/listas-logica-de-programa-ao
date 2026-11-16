soma = 0

for contador in range(1, 5):
    nota = float(input(f"Digite a {contador}ª nota (0 a 10): "))
    soma += nota

media = soma / 4

print(f"A média das notas é: {media:.2f}")

