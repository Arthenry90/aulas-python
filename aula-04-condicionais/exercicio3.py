input_num1 = int(input("Num1"))
input_num2 = int(input("Num2"))
input_num3 = int(input("Num3"))
maior_variavel = input_num1

if input_num2 > maior_variavel:
    maior_variavel = input_num2
if input_num3 > maior_variavel:
    maior_variavel = input_num3

print("Maior variavel é", maior_variavel)