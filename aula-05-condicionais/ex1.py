sorteado = 5
print("Duas tentativas")
tentativa1 = int(input(" Digite um número entre e a 5 " ))
if tentativa1 == sorteado:
    print("Acertou!!")
else:
    tentativa2 = int(input("Digite a tentativa 2: "))
    if tentativa2 == sorteado:
        print("Acertou!")
    else:
        print("Errou!")

if tentativa1 == 5 or tentativa2 == 5:
    print("Acertou!")
else:
    print("Errou, duas tentativas esgotadas")