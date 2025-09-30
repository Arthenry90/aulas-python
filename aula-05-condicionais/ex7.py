nota1 = float(input("Digite a nota 1: "))


if nota1 >= 0 and nota1 <= 10:
    nota2 = float(input("Digite a nota 2: "))
    if nota2 >= 0 and nota2 <= 10:
        media = (nota1 + nota2) / 2
        if media < 5:
            print("Reprovado, média: ", media)
        else:
            print("Aprovado, média: ", media)
    else:
        print("Nota 2 invalida ", nota2)
else:
    print("Nota 1 invalida ", nota1)
    