num1 = int(input("Insira o numero 1 "))
num2 = int(input("Insira o numero 2 "))
operation = (input("Insira a operação "))

match operation:
    case "+":
        print("A soma é: ", num1 + num2)
    case "-":
        print("A subtração é: ", num1 - num2)
    case "*":
        print("A multiplicação é: ", num1 * num2)
    case "/":
        if num2 == 0:
            print("Divisão impossivel")
        else:
            print("A divisião é: ", num1 / num2)
    case "%":
        print("O módulo é: ",num1 % num2)
    case "//":
        print("A divisão inteira é: ",num1 // num2)
    case "**":
        print("A exponenciação é: ", num1 ** num2)