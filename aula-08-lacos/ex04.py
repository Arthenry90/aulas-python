import random

num_randon = random.randint(1,10)

num_tentativas = 0

# while(num_tentativas != 4):
#     print("Digite o número para tentar acertar")
#     input_num = int(input())
#     if input_num == num_randon:
#         print("Parabéns, você acertou em", num_tentativas, "tentativas")
#         break

#     elif input_num == 0:
#         break

#     else:
#         print("Errou! Tente novamente!")
#         num_tentativas += 1
#         print("Tentativas restantes: ",4 - num_tentativas)
        
# if num_tentativas == 3:
#     print("Suas tentativas acabaram, o número era: ",num_randon)

# for i in range(3):
#     input_num = int(input("Digite o número para tentar acertar"))

while num_tentativas < 3:
    input_num = int(input("Digite o número: "))

    # Sai do laço
    if input_num == 0:
        break
    
    if input_num == num_randon:
        print("Parabens, você acertou o número: ", input_num)
        break
    else:
        print("Errou, tente novamente!")
        num_tentativas += 1
        print("Tentativas restantes: ", 3 -  num_tentativas )
else:
    print("Você errou, o número era: ", input_num)
