# while(True):
#     nota = float(input("Digite uma nota: "))
#     if nota < 0 or nota > 10:
#         print("Digite uma nota valida.")
#         continue
#     print(f"Nota: {nota}")
#     break


nota = float(input("Digite uma nota: "))
while nota < 0 or nota > 10:
    print("Nota invalide, digite novamente")
    nota = float(input("Digite uma nota: "))
print(nota)