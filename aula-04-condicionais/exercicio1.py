input_venda = float(input("Insira o valor "))
valor_final = input_venda

if input_venda > 1000:
    valor_final = valor_final * 0.9

print("Venda:", valor_final)