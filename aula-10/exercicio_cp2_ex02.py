# Artur Henrique Siqueira

input_num = int(input("Numero: "))
count = input_num
fatorial = 1

while count != 1:
    fatorial = fatorial * count
    count -= 1

print("Fatorial:", fatorial)

