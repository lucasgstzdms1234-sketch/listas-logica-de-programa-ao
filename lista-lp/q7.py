zero= 0
positivo= 0
for contador in range(1, 7):
    numero = int(input(f"Digite o {contador} numero inteiro: "))
    if numero > 0:
        positivo += 1
    elif numero == 0:
        zero += 1

print(f"Quantidade de números positivos: {positivo}")
print(f"Quantidade de números zero: {zero}")