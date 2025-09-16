input_salario = float(input("Insira seu salário: "))
input_faltas = int(input("Insira suas faltas: "))
salario_total = input_salario

if input_faltas == 0:
    salario_total = salario_total + 500

print("O salario final é: ", salario_total)
