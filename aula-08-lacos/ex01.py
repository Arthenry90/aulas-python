# while(True):
#     input_nota1 = float(input("Digite a nota 1: "))
#     input_nota2 = float(input("Digite a nota 2: "))

#     media = (input_nota1 + input_nota2) / 2
#     print(f"A média é {media:.2f}")
#     print("Deseja continuar? S(im) ou N(não)")
#     input_comando = input()
#     if input_comando.lower() == "n":
#         break

con = "s"
totalMedias = 0

while(con == "s"):
    input_nota1 = float(input("Digite a nota 1: "))
    input_nota2 = float(input("Digite a nota 2: "))

    media = (input_nota1 + input_nota2) / 2
    print(f"A média é {media:.2f}")
    totalMedias += 1
    print("Deseja continuar? S(im) ou N(não)")
    con = input().lower()

print(f"O total de médias foi: {totalMedias}")
