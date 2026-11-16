exatamente_16 = 0
mais_de_16 = 0

for contador in range(1, 6):
    idade = int(input(f"Digite a idade da {contador}ª pessoa: "))
    
    if idade == 16:
        exatamente_16 += 1
    elif idade > 16:
        mais_de_16 += 1

print(f"Quantidade de pessoas com exatamente 16 anos: {exatamente_16}")
print(f"Quantidade de pessoas com mais de 16 anos: {mais_de_16}")
