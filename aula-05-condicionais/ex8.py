# Peça ao usuario que digite uma temperatura:
# Se ela for menor que 15, exibe: esta frio!  
# se ela for entre 15 e 25, exibe temperatura normal
# se ela estiver acima de 25 até 40, exbia esta muito quente!
# se ela estivar acima de 40, exbia torrei!

temp_input = int(input("Digite uma temperatura: "))

# Código resolvido com elif
# if temp_input < 15:
#     print("Está frio!")
# elif temp_input >= 15 and temp_input <= 25:
#     print("temperatura normal")
# elif temp_input > 25 and temp_input <= 40:
#     print("Está muito quente!")
# else:
#     print("Torrei!")

# codigo sem elif
if temp_input < 15:
    print("Está frio!")
if temp_input >= 15 and temp_input <= 25:
    print("temperatura normal")
if temp_input > 25 and temp_input <= 40:
    print("Está muito quente!")
if temp_input > 40:
    print("Torrei!")