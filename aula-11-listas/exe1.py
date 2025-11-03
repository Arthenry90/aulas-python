v = [45,-89,32,-12,33]
import os

while True:
    os.system("cls")
    print("Escolha qual exercicio o programa irá rodar")
    opcao = input("Escolha: ")
    match opcao:
        case "0":
            break

        case "1":
            # Parte 1 exibir o primeiro
            print(v[0] , end=" ")
        
        case "2":
            # Parte 2 exibir os impares
            for i in range(0,5):
                if v[i] % 2 != 0:
                    print(v[i], end=" ")
        
        case "3":
            # Parte 3 Exibir os negativos
            for i in range(0,5):
                if v[i] < 0:
                    print(v[i], end=" ")

        case "4":
            # Parte 4 Somar os elementos do vetor
            sum = 0
            for i in range(0,5):
                sum += v[i]
            print(sum)

        case "5":
            # Parte 5 Calcular a média dos elementos
            sum = 0
            for i in range(0,5):
                sum += v[i]
            print(sum / len(v))

        case "6":
            # Parte 6 Exibir a soma dos números pares
            sum_par = 0
            for i in range(0,5):
                if v[i] % 2 == 0:
                    sum_par += v[i]
            print(sum_par)

        case "7":
            # Parte 7 pedir para o usuario preencher todos os elementos do vetor
            for i in range(5):
                input_vetor = input(f"Digite o número do indice {i}: ")
                v[i] = input_vetor
            print(v)

        case "8":
            # Parte 8 pedir para o usuario preencher um elemento especifico do vetor
            for i in range(5):
                input_indice = input(f"Digite o número do vetor que quer mudar: ")
                input_vetor = input(f"Digite o valor: ")
                v[input_indice] = input_vetor
            print(v)

    input("\nDigite algo para sair")

# print(sum_par)