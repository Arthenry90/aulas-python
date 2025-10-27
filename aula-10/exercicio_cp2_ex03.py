# Artur Henrique Siqueira

input_num = int(input("Numero: "))
primo = True

for i in range(input_num):
    if i == 0 or i == 1:
        continue
    if input_num % i == 0:
        print(input_num,"não é primo")
        primo = False
        break

if primo:
    print(input_num,"é primo")
