# Artur Henrique Siqueira

input_inicio = int(input("Inicio:" ))
input_fim = int(input("Fim:" ))
input_mult = int(input("Mult: "))
print("Multiplos: ")

for i in range(input_inicio, input_fim):
    if i % input_mult == 0:
        print(i)
