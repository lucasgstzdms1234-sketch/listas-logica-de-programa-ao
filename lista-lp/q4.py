n = int(input("Digite um número inteiro de 1 a 10: "))
print("Tabuada do", n)
for i in range(1, 11):
     resultado = n * i
     print(n, "x", i, "=", resultado)
