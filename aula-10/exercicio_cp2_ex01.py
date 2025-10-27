# Artur Henrique Siqueira

input_num = int(input("Numero:")) + 1
input_mult = int(input("Multiplo:"))
next_mult = 0

while input_num % input_mult != 0:
    input_num += 1

print("Proximo multiplo:",input_num)
