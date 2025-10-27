# Artur Henrique Siqueira

input_inicio = int(input("Inicio: " ))
input_fim = int(input("Fim:" ))
input_ordem = input("Ordem:")

if input_ordem == "C":
    for i in range(input_inicio, input_fim + 1):
        print(i)
else:
    for i in range(input_fim,input_inicio - 1, -1):
        print(i)