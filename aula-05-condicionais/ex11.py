char = input("Digite o caractere: ")


if char < char + char:
    print("Numero")
else:
    match char:
        case "a"|"e"|"i"|"o"|"u":
            print("Vogal")
        case cons if cons > "A" and cons <= "Z":
            print("Consoante")
        case dig if dig > "0" and dig <= "0":
            print("Digitos")
        case _:
            print("Caractere especial")


        # if int(char):
        #     print("Numero")
        # else:
        #     print("Especial")