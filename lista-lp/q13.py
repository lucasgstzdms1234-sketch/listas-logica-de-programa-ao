nota = int(input("Digite uma nota de 1 a 10: "))
while nota < 1 or nota > 10:
    print("Nota inválida! Digite novamente.")
    nota = int(input("Digite uma nota de 1 a 10: "))
